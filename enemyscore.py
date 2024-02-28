def calculate_friendship_score(names, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    total_score = 0

    for name in names:
        name = name.lower()  # Convert to lowercase
        for character in name:
            if character.isalpha():  # Handle only alphabetic characters
                position = alphabet.find(character)
                new_position = (position + key) % 26
                print(f"{character.upper()}: {new_position}")
                total_score += new_position

    return total_score

def main():
    names = input("Enter the names of two people (separated by a space): ").split()
    shift_key = int(input("Enter the shift value (positive integer): "))

    friendship_score = calculate_friendship_score(names, shift_key)
    print(f"Total friendship score: {friendship_score}")

    # Add a personalized message based on the score
    if friendship_score >= 50:
        print("Your friendship score suggests an intergalactic bond!")
    else:
        print("Keep nurturing your cosmic connection!")

if __name__ == '__main__':
    main()
