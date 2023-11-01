#Name: Lewis Fassero
#   Program Purpose: This Magic-8-Ball code uses a Python tuple since the
#   user does not have the ability to change the 8-Ball answers.
#   However the program could have used a Python list instead of a tuple.
#   Note: Tuples use parenthesis; lists use square braces.

########## define gobal variables ##########
import random
answers8ball=("As I see it, yes", "Ask again later",
              "Better not tell you now", "Cannot predict now",
              "Concentrate and ask again", "Don't count on it",
              "It is certain", "It is decidedly so",
              "Most likely", "My reply is no",
              "My sources say no", "Outlook good",
              "Outlook not so good", "Reply hazy, try again",
              "Signs point to yes", "Very doubtful",
              "Without a doubt", "Yes",
              "Yes definitely", "You may rely on it",)

########## define program functions ##########

def main():

    print("I am the Magic 8 Ball and can answer any YES or NO question!")
    
    anotherquestion=True
    while anotherquestion:
        answer=random.choice(answers8ball)

        print("\nShake the Magic 8 Ball")
        print("\n...and now...")
        question=input("\nWhat is your YES or NO question? ")
        print("The Magic 8 Ball says: "+answer)
        
        askagain=input("\nWould you like to ask me another question (Y or N)?: ")
        if askagain.upper()=="N" or askagain.upper()=="NO":
            anotherquestion=False
            print("\nCome back again when you have other important questions.")
            print("\nMagic 8 Ball OUT.\n\n\n")

########## call on main program to execute ##########

main()
