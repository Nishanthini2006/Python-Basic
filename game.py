import random
def guess_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 to 100")
    
   while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number:
                print("Too Low!")
            elif guess > number:
                print("Too High!")
            else:
                print(f"Correct! You guessed in {attempts} attempts")
                break
                
        except ValueError:
            print("Error: Please enter only numbers")
        except Exception as e:
            print("Something went wrong:", e)

guess_game()
