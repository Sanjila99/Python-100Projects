vowels=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
print("Enter any word:")
word=input()
for letters in word:
    if letters in vowels:
        new_word=word.replace(letters," ")
 
print(new_word)
