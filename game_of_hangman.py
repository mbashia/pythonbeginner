import random
import hangmanresource

print(hangmanresource.HANGMAN_ASCII_ART)


def get_valid_word(words):
    gen_word = random.choice(words)
    while "-" in words or " " in gen_word:
        gen_word = random.choice(words)
    return gen_word


random_word = get_valid_word(hangmanresource.words).lower()

display = []
lives = 6
for i in range(len(random_word)):
    display += "-"
print(" ".join(display))
end_game = False
while end_game == False:
    guess = input("guess a letter:").lower()
    if guess in display:
        print(f'you have already guessed {guess} this letter')
    for position in range(len(random_word)):
        letter = random_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in random_word:
        print(f'you guessed {guess}.It is not in the word.You lose a life ❤ ')
        lives -= 1
        if lives == 0:
            print('you lose!!!!')
            end_game = True
    print(''.join(display))
    if "-" not in display:
        end_game = True
        print("you winn!!")
    print(hangmanresource.hangmanpics[lives])

