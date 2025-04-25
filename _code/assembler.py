import re
import warnings

# Instruction set with reads_ram and writes_ram for RAM access tracking
instruction_set = {
    "nop":  {"opcode": "0000", "operand": "none", "reads_ram": False, "writes_ram": False},
    "lda":  {"opcode": "0001", "operand": "address", "reads_ram": True, "writes_ram": False},
    "add":  {"opcode": "0010", "operand": "address", "reads_ram": True, "writes_ram": False},
    "sub":  {"opcode": "0011", "operand": "address", "reads_ram": True, "writes_ram": False},
    "sta":  {"opcode": "0100", "operand": "address", "reads_ram": False, "writes_ram": True},
    "ldi":  {"opcode": "0101", "operand": "value", "reads_ram": False, "writes_ram": False},
    "jmp":  {"opcode": "0110", "operand": "address", "reads_ram": False, "writes_ram": False},
    "jc":   {"opcode": "0111", "operand": "address", "reads_ram": False, "writes_ram": False},
    "jz":   {"opcode": "1000", "operand": "address", "reads_ram": False, "writes_ram": False},
    "out":  {"opcode": "1110", "operand": "none", "reads_ram": False, "writes_ram": False},
    "hlt":  {"opcode": "1111", "operand": "none", "reads_ram": False, "writes_ram": False}
}

def assemble(code, max_instructions=16, max_address=15, strict_ram_check=False, opcode_bits=4, operand_bits=4):
    """Assemble `code` to work on the SAP computer architecture.
    max_instructions: max number of instructions (2^PC_bits)
    max_address: max RAM addresses (2^MAR_bits)
    strict_ram_check: if True, raise error for uninitialized RAM access
    opcode_bits: number of bits for opcode
    operand_bits: number of bits for operand"""
    symbol_table = {}
    machine_code = []
    ram_init = {}  # Store RAM initial values (address: value)
    initialized_ram = set()  # Track initialized RAM addresses
    address = 0
    instruction_lines = []  # Store (binary, assembly_line) pairs

    # Validate bit widths
    if opcode_bits + operand_bits != 8:
        raise ValueError(f"Opcode bits ({opcode_bits}) + operand bits ({operand_bits}) must equal 8")

    # First pass: Build symbol table and check instruction count
    lines = code.splitlines()
    for line in lines:
        line = line.split(";")[0].strip()  # Remove comments for parsing
        full_line = line.split(";")[0].rstrip() + (" ;" + ";".join(line.split(";")[1:]) if ";" in line else "")
        if not line:
            continue
        if line.startswith("#ram"):  # Handle RAM initialization
            parts = line.split()
            if len(parts) != 3:
                raise ValueError(f"Invalid #ram directive: {line}")
            try:
                ram_addr = int(parts[1], 0)  # Handle decimal or hex
                ram_value = int(parts[2], 0)
                if ram_addr > max_address or ram_value > max_address:
                    raise ValueError(f"RAM address or value out of range: {line}")
                ram_init[ram_addr] = ram_value
                initialized_ram.add(ram_addr)  # Mark as initialized
            except ValueError:
                raise ValueError(f"Invalid #ram address or value: {line}")
            continue
        if ":" in line:  # Handle labels
            label = line.split(":")[0].strip()
            symbol_table[label] = format(address, f"0{max(4, operand_bits)}b")  # Store address with sufficient bits
            line = line.split(":")[1].strip()
            full_line = line.split(";")[0].rstrip() + (" ;" + ";".join(line.split(";")[1:]) if ";" in line else "")
        if line:
            address += 1
        if address > max_instructions:
            raise ValueError(f"Program exceeds maximum of {max_instructions} instructions")

    # Generate RAM initialization instructions
    for ram_addr, ram_value in ram_init.items():
        ldi_binary = f"0111{format(ram_value, f'0{operand_bits}b')}"
        sta_binary = f"0100{format(ram_addr, f'0{operand_bits}b')}"
        machine_code.append(ldi_binary)
        machine_code.append(sta_binary)
        instruction_lines.append((ldi_binary, f"ldi {ram_value} ; Generated for #ram {ram_addr} {ram_value}"))
        instruction_lines.append((sta_binary, f"sta [{ram_addr}] ; Generated for #ram {ram_addr} {ram_value}"))
        address += 2
        if address > max_instructions:
            raise ValueError(f"Program with RAM init exceeds {max_instructions} instructions")

    # Second pass: Generate machine code and check RAM access
        # Second pass: Generate machine code and check RAM access
    address = len(machine_code)  # Start after RAM init instructions
    for raw_line in lines:
        # Preserve original line with comments
        full_line = raw_line.rstrip()  # Keep entire line, including comments
        line = raw_line.split(";")[0].strip()  # Strip comments for parsing
        if not line or line.startswith("#ram"):
            continue
        if ":" in line:
            line = line.split(":")[1].strip()
            # Reconstruct full_line to include label and comment
            full_line = line.split(";")[0].rstrip() + (" ;" + ";".join(raw_line.split(";")[1:]) if ";" in raw_line else "")
        if line:
            # Parse instruction and operands
            match = re.match(r"(\w+)\s*(?:\[(\w+)\]|(\w+))?", line)
            if not match:
                raise ValueError(f"Invalid syntax: {line}")
            
            instr, operand1, operand2 = match.groups()
            instr = instr.lower()
            
            if instr not in instruction_set:
                raise ValueError(f"Unknown instruction: {instr}")

            opcode = instruction_set[instr]["opcode"]
            operand_type = instruction_set[instr]["operand"]
            binary = opcode

            if operand_type == "none":
                binary += "0" * operand_bits
            elif operand_type == "address":
                operand = operand1 or operand2
                if operand in symbol_table:
                    binary += symbol_table[operand][-operand_bits:]
                else:
                    try:
                        addr = int(operand, 0)
                        if addr > max_address:
                            raise ValueError(f"Address out of range: {operand}")
                        binary += format(addr, f"0{operand_bits}b")
                        if instruction_set[instr]["reads_ram"] and addr not in initialized_ram:
                            message = (f"Instruction '{full_line}' at address {address} accesses "
                                      f"uninitialized RAM[{addr}]. Consider adding `#ram {addr} 0` to initialize.")
                            if strict_ram_check:
                                raise ValueError(message)
                            else:
                                warnings.warn(message)
                        if instruction_set[instr]["writes_ram"]:
                            initialized_ram.add(addr)
                    except ValueError:
                        raise ValueError(f"Invalid address or unresolved label: {operand}")
            elif operand_type == "value":
                try:
                    value = int(operand2, 0)
                    if value > max_address:
                        raise ValueError(f"Value out of range: {operand2}")
                    binary += format(value, f"0{operand_bits}b")
                except ValueError:
                    raise ValueError(f"Invalid value: {operand2}")

            machine_code.append(binary)
            instruction_lines.append((binary, full_line))
            address += 1
            if address > max_instructions:
                raise ValueError(f"Program exceeds {max_instructions} instructions")

    return machine_code, ram_init, instruction_lines, initialized_ram, symbol_table

# Format output for breadboard (e.g., toggle switches)
def format_for_switches(binary):
    return ", ".join("on" if bit == "1" else "off" for bit in binary)

# Print listing with assembly code, address, machine code, and optional switches/comments
def print_listing(instruction_lines, show_switches=False, show_comments=True, symbol_table=None):
    print("Program Listing:")
    for i, (binary, assembly_line) in enumerate(instruction_lines):
        if not isinstance(binary, str):
            raise TypeError(f"Non-string binary value at address {i}: {binary}")
        hex_val = hex(int(binary, 2))
        parts = assembly_line.split(";", 1)
        asm = parts[0].strip()
        comment = parts[1].strip() if len(parts) > 1 and show_comments else ""
        # Resolve address for address-based instructions
        match = re.match(r"(\w+)\s*(?:\[(\w+)\]|(\w+))?", asm)
        if match:
            instr, operand1, operand2 = match.groups()
            instr = instr.lower()
            operand = operand1 or operand2
            if instr in ["lda", "add", "sub", "sta", "jmp", "jc", "jnc", "ldx"] and operand:
                if operand in symbol_table:
                    resolved_addr = int(symbol_table[operand], 2)
                    asm += f" ({resolved_addr})"
                else:
                    try:
                        resolved_addr = int(operand, 0)
                        asm += f" ({resolved_addr})"
                    except ValueError:
                        pass
        line = f"Addr {format(i, '04b')} ( {i:5d} ) : {binary} ({hex_val}) | {asm:<20}"
        if show_switches:
            switch_settings = format_for_switches(binary)
            line += f" Switches: {switch_settings}"
        if show_comments:
            line += f" {comment}"
        print(line)

def to_listing_file(instruction_lines, filename="program.lst", show_switches=False, show_comments=True, symbol_table=None):
    with open(filename, "w") as f:
        f.write("Program Listing:\n")
        for i, (binary, assembly_line) in enumerate(instruction_lines):
            if not isinstance(binary, str):
                raise TypeError(f"Non-string binary value at address {i}: {binary}")
            hex_val = hex(int(binary, 2))
            parts = assembly_line.split(";", 1)
            asm = parts[0].strip()
            comment = parts[1].strip() if len(parts) > 1 and show_comments else ""
            # Resolve address for address-based instructions
            match = re.match(r"(\w+)\s*(?:\[(\w+)\]|(\w+))?", asm)
            if match:
                instr, operand1, operand2 = match.groups()
                instr = instr.lower()
                operand = operand1 or operand2
                if instr in ["lda", "add", "sub", "sta", "jmp", "jc", "jnc", "ldx"] and operand:
                    if operand in symbol_table:
                        resolved_addr = int(symbol_table[operand], 2)
                        asm += f" ({resolved_addr})"
                    else:
                        try:
                            resolved_addr = int(operand, 0)
                            asm += f" ({resolved_addr})"
                        except ValueError:
                            pass
            line = f"Addr {format(i, '04b')} ( {i:5d} ) : {binary} ({hex_val}) | {asm:<20}"
            if show_switches:
                switch_settings = format_for_switches(binary)
                line += f" Switches: {switch_settings}"
            if show_comments:
                line += f" {comment}"
            f.write(line + "\n")
    print(f"Listing file '{filename}' generated.")

# Generate hex file for EEPROM
def to_hex_file(machine_code, filename="program.hex"):
    with open(filename, "w") as f:
        for binary in machine_code:
            if not isinstance(binary, str):
                raise TypeError(f"Non-string binary value in machine_code: {binary}")
            f.write(f"{int(binary, 2):02X}\n")

# Example usage with your sample code
code = """
START:
    ldi 1       ; Load 1 into accumulator
    sta [14]    ; Initialize RAM[14] = 1 (F(n-2))
    sta [15]    ; Initialize RAM[15] = 1 (F(n-1))
    out         ; Output 1 (first Fibonacci number)
LOOP:
    lda [14]    ; Load F(n-2)
    add [15]    ; Add F(n-1) to get F(n)
    jc END      ; Stop if carry (overflow)
    out         ; Output F(n)
    sta [15]    ; Store F(n) in RAM[15] (new F(n-1))
    lda [15]    ; Load old F(n-1)
    sta [14]    ; Store old F(n-1) in RAM[14] (new F(n-2))
    jmp LOOP    ; Repeat
END:
    hlt         ; Stop
"""

code = """
START: 
    ldi 3     
    sta [14]    ; put 3 in ram 14
    ldi 4
    add [14]    ;add ram [14] to 4
    out ; hopefully output 7
    sta [14]
    jmp 3
    hlt"""
machine_code, ram_init, instruction_lines, initialized_ram, symbol_table = assemble(code, strict_ram_check=False)
print("Assembly: \n"+code)
print_listing(instruction_lines, show_switches=False, show_comments=True, symbol_table=symbol_table)
to_listing_file(instruction_lines, show_switches=False, show_comments=True, symbol_table=symbol_table)

print("\nInitial RAM Contents:")
if ram_init:
    for addr, value in sorted(ram_init.items()):
        print(f"RAM[{format(addr, '04b')} ( {addr} )] = {value} ({hex(value)})")
else:
    print("No RAM initialization specified.")

to_hex_file(machine_code)
print("\nHex file 'program.hex' generated for EEPROM.")

# Print total program bytes and RAM usage
print(f"\nTotal Program Bytes: {len(machine_code)}")
print(f"Total RAM Usage: {len(initialized_ram)} bytes")

# # Test with strict RAM check, no comments, and uninitialized RAM
# print("\nTesting with strict RAM check and no comments:")
# code_uninit = """
# START:
#     ldi 1       ; Load 1 into accumulator
#     out
#     add [2]     ; Add RAM[2] (uninitialized)
#     out
#     halt
# """
# try:
#     machine_code, ram_init, instruction_lines, initialized_ram, symbol_table = assemble(code_uninit, strict_ram_check=True)
#     print_listing(instruction_lines, show_switches=False, show_comments=False, symbol_table=symbol_table)
#     to_listing_file(instruction_lines, filename="program_uninit.lst", show_switches=False, show_comments=False, symbol_table=symbol_table)
# except ValueError as e:
#     print(f"Error: {e}")

# # Test with new instructions
# print("\nTesting with new instructions:")
# code_new = """
# START:
#     ldi 1       ; Load 1 into accumulator
#     sta [0]     ; Store to RAM[0]
#     ldx [0]     ; Load RAM[0] into X
#     inc         ; Increment accumulator
#     mvi 5       ; Move 5 to register
#     out
#     jmp START   ; Repeat
# """
# machine_code, ram_init, instruction_lines, initialized_ram, symbol_table = assemble(code_new, strict_ram_check=True)
# print_listing(instruction_lines, show_switches=True, show_comments=True, symbol_table=symbol_table)
# to_listing_file(instruction_lines, filename="program_new.lst", show_switches=True, show_comments=True, symbol_table=symbol_table)