import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
password = ''
while len(password)<7:
    pass_word = random.choice(letters)
    # password.append(pass_word)
    password = password + pass_word

print(password)