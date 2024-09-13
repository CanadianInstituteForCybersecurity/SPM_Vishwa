def caesar_cipher(text, shift, mode='encode'):
    result = ""
    shift = shift % 26

    if mode == 'decode':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result


text = "Vishwa Senthilkumar"
shift = 11

encoded_text = caesar_cipher(text, shift, mode='encode')
decoded_text = caesar_cipher(encoded_text, shift, mode='decode')

print("-------------------------")
print(f"Original Text: {text}")
print("-------------------------")
print(f"Encoded Text: {encoded_text}")
print(f"Decoded Text: {decoded_text}")
print("-------------------------")