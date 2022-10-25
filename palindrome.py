word = "radar"
word = word.casefold() # to make it suitable for caseless comparison
rev_word = reversed(word)
if list(rev_word) == list(word):
    print("palindrome")
else:
    print("not a palindrome")
