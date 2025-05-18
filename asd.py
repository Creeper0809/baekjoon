def split_and_print_blocks_from_hex():
    hex_input = input("Input hex: ").strip()
    data = bytes.fromhex(hex_input)

    print(f"\nTotal {len(data)} bytes, split into {len(data) // 16} full blocks and {len(data) % 16} extra bytes\n")
    for i in range(0, len(data), 16):
        block = data[i:i+16]
        print(f"Block {i//16 + 1:02}: {block.hex()}")

split_and_print_blocks_from_hex()
