#Name: Lewis Fassero
#Program Purpose: This program demonstrates how to manipulate a list.

import datetime

##### define global variables #####
# define global constants

# define global variables
dogs=["Sadie", "Molly", "Ella", "Milo", "Buddy", "Rocky", "AnnaBelle", "Gonzo", "Sweetie-Pie", "Diego"]
dogs2=[]

##### define program functions #####

def main():
    howmany=len(dogs)
    print("\nNumber of dogs in the list: "+str(howmany))
    print("\nOriginal list of dog names:")
    print(dogs)

    dogs.reverse()
    print("\nList in from last to first:")
    print(dogs)

    dogs.sort()
    print("\nAlphabetized list:")
    print(dogs)

    dogs.sort(reverse=True)
    print("\nReverse-alphabetized list:")
    print(dogs)

    dogs.append("Ranger")
    print("\nAdd a dog to the end of the list:")
    print(dogs)

    doggy=dogs.pop(0)
    print("\nPop a dog off (remove) from the front of the list:")
    print(dogs)
    print(doggy+" was removed from the front of the list.")

    anotherdog=dogs.pop(3)
    print("\nNote: Position numbers in a list begin with 0, not with 1.")
    print("\nPop a dog off from position 3 (which is the 4th dog) in the list:")
    print(dogs)
    print(anotherdog+" was removed from the front of the list.")

    print("\nRemove a dog by name rather than by position in the list.")
    baddog=input("Type the name of the dog you would like to remove from the list: ")
    dogs.remove(baddog)
    print(dogs)
    print(baddog+" was removed from the front of the list.")

    dogs2=dogs
    print("\nA list can be copied into another list by setting one equal to the other:")
    print(dogs)
    print(dogs2)

    print('\nUse a "FOR" loop to give each dog in the list the same last name:')
    lastname=input("What last name would you like to give to each dog?: ")
    for i in range(len(dogs)):
        dogs[i]=dogs[i]+" "+lastname
    print(dogs)

##### call on main program to execute #####

main()
