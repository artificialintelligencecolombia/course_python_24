# Higher lower game

# Import libraries and data
import random
from higher_lower_game_data import ig_profiles
import higher_lower_arts as arts

# Welcome message
print(arts.title)                                  

print("You will guess who has the highest number of followers.")

# Create a function that picks randomly each participant from the dataset
def pick_account():
    """Randomly pick an account from the dataset."""
    profile = ig_profiles[random.randint(0, len(ig_profiles) - 1)] # '-1' due to the dictionary indexing
    return profile

# Create a function that prints the information for each confronted participant
def display_information(account):
    """Print information about the given Instagram account."""
    print(f"{account['name']}, a {account['description']} account, from {account['country']}.")

def game():    
    """Play the Higher or Lower game."""
    # Initial set up
    account_a = pick_account()
    account_b = pick_account()
    continue_game = True
    score = 0

    # Game loop
    while continue_game:
        
        # Display information
        display_information(account_a)
        print(arts.vs)
        display_information(account_b)
        
        # Capture & compare guesses
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        
        usr_guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        
        # Validate guess
        if (usr_guess == 'a' and a_followers > b_followers) or (usr_guess == 'b' and b_followers > a_followers):
            score += 1
            print(f"You're right! Current score: {score}.\n")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}.\n")
        
        # Prepare for next round   
        
        # Ensure the account does not confront itself in the immediate next round by reassigning if identical
        account_a = account_b
        while True:
            account_b = pick_account()
            if account_a != account_b:
                break

if __name__ == "__main__":
    game()