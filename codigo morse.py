MORSE_CODE = {
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}

def convert_to_morse(code):
    # Check that the input code only contains digits and spaces
    if not all(c.isdigit() or c.isspace() for c in code):
        raise ValueError('Input code contains invalid characters')

    # Replace each digit with its corresponding Morse code
    morse_code = ''.join(MORSE_CODE.get(digit, '') for digit in code)
    return morse_code

lock_code = "1 2 2 5 0"
print(f"Initial code: {lock_code}")

morse = convert_to_morse(lock_code)
print(f"Morse code: {morse}")
