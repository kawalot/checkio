#Secret Message

def find_message(text):
    decrypted = ""
    for letter in text:
        if letter.isupper():
            decrypted = decrypted + "".join(letter)
    return decrypted
print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))