# Guess the no.
# In this program you have to guess the hidden no.
# in only 5 gusses
print("Welcome to Guess the no.\n","In this game you have to guess the hidden no. in only 5 guesses")
print("Enter the no.")
attempt=1
while (True):
    guess= int(input())
    print("No. of attempts=", attempt)
    remaining_attempts= 5-attempt
    attempt= attempt+1
    print("Your remaning attempts are", remaining_attempts)
    if(guess==16):
        print("Congratulations you gessed the correct no\n")
        break
    elif(guess<16):
        print("The hidden no. is greater than this no.\n")
    elif(guess>16):
        print("The hidden no. is smaller than this no.\n")  
    else:
        print("Better luck next time")
        
        continue    
    if(attempt==6):
        print("Game over\n")
        break
    
