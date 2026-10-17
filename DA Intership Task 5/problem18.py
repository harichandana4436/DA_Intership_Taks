#hackerrank:-https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0  # Consonants
    kevin_score = 0   # Vowels
    length = len(string)

    # Loop through the string once
    for i in range(length):
        # Calculate how many substrings start at this index
        points = length - i
        
        if string[i] in vowels:
            kevin_score += points
        else:
            stuart_score += points

    # Determine the winner
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
