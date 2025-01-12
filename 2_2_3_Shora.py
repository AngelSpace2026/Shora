def map_char_to_number(char):
    """Convert a character to a corresponding number (0-255 based on its byte value)."""
    return ord(char)

def map_number_to_char(n):
    """Convert a number (0-255) back to a corresponding character."""
    if 0 <= n <= 255:
        return chr(n)
    return ''

def fast_factorize_product(product):
    """Efficiently factorize a product into byte values (0-255) using prime factorization."""
    factors = []
    
    # Check small prime numbers and their multiples (only up to 255)
    for i in range(2, 256):
        while product % i == 0:
            factors.append(i)
            product //= i
        if product == 1:
            break  # Early exit if we have fully factored the product

    # If product is still greater than 1 and less than 256, it should be a valid byte
    if 1 < product < 256:
        factors.append(product)
    
    return factors

def convert_to_base256(numbers):
    """Convert a list of numbers (byte values) to base 256 representation."""
    base256_representation = [format(num, 'x') for num in numbers]
    return ' '.join(base256_representation)

def base256_to_product(base256_string):
    """Convert a space-separated base 256 string back to a product."""
    byte_values = [int(num, 16) for num in base256_string.split()]
    product = 1
    for byte in byte_values:
        product *= byte
    return product, byte_values

def main():
    # Step 1: Ask the user to enter the base 256 input (space-separated)
    base256_string = input("Enter the base 256 numbers (space-separated): ")
      #3 c7
    
    # Step 2: Convert the base 256 string to product
    product, byte_values = base256_to_product(base256_string)
    
    # Print Line 1: Input Base 256
    print(f"Input Base 256: {base256_string}")
  
    
    # Print Line 2: Byte Values (decoded from base 256)
    print(f"Byte Values (decoded from base 256): {byte_values}")
    
    # Print Line 3: Product of the Byte Values
    print(f"Product of Byte Values: {product}")
    #597
    
    # Step 3: Convert the byte values back to a message
    decoded_message = ''.join(map(map_number_to_char, byte_values))
    
    # Print Line 4: Decoded Message
    print(f"Decoded Message (from byte values): {decoded_message}")
    
    # Step 4: Convert the decoded message (numbers) to base 256
    base256_message = convert_to_base256(byte_values)
    print(f"Decoded Message in Base 256: {base256_message}")
    
    # Step 5: Validate if the decoded message seems reasonable
    if decoded_message:
        print("The decoded message based on the byte values is displayed above.")
    else:
        print("Could not decode a meaningful message.")

if __name__ == "__main__":
    main()