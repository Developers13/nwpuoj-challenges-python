def reverseBin(n: int) -> int:
    # Convert the integer to binary and remove the '0b' prefix
    binary_str = bin(n)[2:]
    # Reverse the binary string
    reversed_binary_str = binary_str[::-1]
    
    return int(reversed_binary_str)
print(reverseBin(int(input())))