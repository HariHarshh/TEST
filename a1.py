secret = random.randint(1, 50)
attempts = 5
won = False

print("Number Gussing Game")
print("Guess the secret number between 1 and 50")
print("You have 5 attempts!")

while attempts > 0:
    guess = int(input("Enter your guess:  "))

    if guess == secret:
        print("Congratulations! You guessed the correct number!")
        won = True
        break
    else:
        difference = abs(secret - guess)

        if difference <= 5:
            print("Hot! you are very close!")
        elif difference <=10:
            print("Warm! You are getting closer")
        elif difference <= 20: 
            print("Cold! You are far away!")    
        else:
            print("Ice cold! Very far!")    

            attempts -=1
            print("Pemining hearts:", attempts)

if won == False:
    print("Game Over!")            
    print("The Secret number was:", secret)