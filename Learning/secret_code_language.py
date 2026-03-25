import random
import string

user_input = input("Write what you want to do i.e. either 'code' or 'decode': ").lower()
if user_input == "code":
    text = input("Enter the text you want to code: ")
    coded_text = ""
    words = text.split()
    for word in words:
        if len(word) <3:
            new_word = word[::-1]
            coded_text += new_word + " "
        else:
            prefix = ''.join(random.choices(string.ascii_lowercase, k=3))
            suffix = ''.join(random.choices(string.ascii_lowercase, k=3))

            new_word = prefix + word[1:] + word[0] + suffix 
            coded_text += new_word + " "
    print("Coded text: ", coded_text)

elif user_input == "decode":
    coded_text = input("Enter the text you want to decode: ")
    decoded_text = ""
    words = coded_text.split()
    for word in words:
        if len(word) < 3:
            new_word = word[::-1]
            decoded_text += new_word + " "
        else:
            new_word = word[3:-3]
            new_word = new_word[-1] + new_word[:-1]
            decoded_text += new_word + " "
    print("Decoded text: ", decoded_text)