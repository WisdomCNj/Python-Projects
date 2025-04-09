import random

# This function simulates rolling a six-sided dice
# and returns a random number between 1 and 6.
def roll():

    roll = random.randint(1, 6)
    return roll
value = roll()

#define the number of players
# The number of players must be between 2 and 4
while True:
    Players = int(input("Enter the number of players: "))
    
    if Players > 1 and Players < 5:
        break
    else:
        print("must be at least 2 players and less than 5 players")

max_score = 25

player_scores = [0 for _ in range(Players)]
# The game continues until one player reaches the maximum score
while max(player_scores) < max_score:
    for p_i in range(Players):
        print("Player", p_i + 1, "turn")
        print("your total score is", player_scores[p_i])
        current_score = 0
        
        while True:
            # Ask the player if they want to roll the dice
            # If they choose not to roll, the next player's turn begins
            should_roll = input("Do you want to roll the dice? (y/n): ")
            if should_roll.lower() != 'y':
                break
            
            value = roll()
            # Check if the rolled value is 1 if so, the player loses their current score
            if value == 1:
                print("You rolled a 1.")
                current_score = 0
                break
            else:
                # Add the rolled value to the current score
                # and print the rolled value
                current_score += value
                print("You rolled a", value)
            
            
            
            print("Current score for this turn:", current_score)     
        # Add the current score to the player's total score
        player_scores[p_i] += current_score
        print("Player", p_i + 1, "score:", player_scores[p_i]) 

max_score = max(player_scores)
# Find the player with the maximum score and print the winner
winner = player_scores.index(max_score) + 1
print("Player", winner, "wins with a score of", max_score)
