alphabet='abcdefghijklmnopqrstuvwxyz'
key=3
newMessage=''

message=input('Please enter a message:')

for character in message:
    position=alphabet.find(character)
    newposition=(position+key)%26
    newCharacter=alphabet[newposition]
    newMessage += newCharacter

print(newMessage)

    