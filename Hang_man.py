import random
#Choose a random word and store it in a list
random_word =["rocket","space","laptop","horse","men","driver","tree","time","red","night"]
chosen_word=random.choice(random_word)
chosen_word=chosen_word.lower()
chosen_word=list(chosen_word)

blank_word=""
lives_left=5
#Create a variable with words replaced by _
for i in range(0,len(chosen_word)):
    blank_word=blank_word+"_"
blank_word=list(blank_word)

#Checks if the player have any life left and if the player has guessed the word completely
while lives_left>0 and "_" in blank_word:
    #Takes input from player
    guess=input("\nEnter your guess: \n")
    guess=guess.lower()
    #Checks for the guess
    if guess in chosen_word:
        print("\nYou guessed correctly!")
        for i in range (0,len(chosen_word)):
            if chosen_word[i]==guess:
                blank_word[i]=guess
        print("".join(blank_word))
    else:
        lives_left-=1
        print("You guessed incorrectly!")
        print("Lives left: "+str(lives_left))
#Checks if the user won or not
if "_" not in blank_word:
    print("\n\n\nYou Won the Game")
else:
    print("\n\n\nYou Lose")