# Creating a dictioanry of technical terms and basic definitions
#   key - the word to define
#   value - the definition of the word
tech_terms = { "dict": "stores a key/value pair",
               "list": "stores a value at each index",
               "map": "see 'dict'",
               "set": "stores unordered unique elements" }


def menu():
    ''' Print a simple menu to the user '''
    print("Systems Dictionary")
    print("1) Add a term")
    print("2) List terms")
    print("3) Get a definition")
    print("4) Delete a term")
    print("5) Quit")
    return input("Enter your choice: ")

def run(choice):
    if choice == 1:
        add()
    elif choice == 2:
        list()
    elif choice == 3:
        lookup()
    elif choice == 4:
        delete()
    else:
        print("Invalid input, please enter a valid number (1-5)")

def add():
    ''' Adds a term to the dictionary '''
    term = input("What term do you want to add? ").lower()
    definition = input("What is the definition for '" + term + "'? ")
    tech_terms[term] = definition

def list():
    ''' List all the terms (no definitions) that are in the dictionary '''
    for key in tech_terms.keys():
        print(key)

def lookup():
    ''' Lookup a term and print the definition '''
    term = input("What term do you want to lookup? ").lower()
    if term in tech_terms:
        print(term + " - " + tech_terms[term])
    else:
        print("Error: the term '" + term + "' is not found.") 

def delete():
    term = input("What term do you want to delete? ")
    del tech_terms[term]

def main():
    # Present main menu 
    choice = menu()

    while choice != "5":
        try:
            choice = int(choice)
            run(choice)
        except:
            print("Invalid input, please enter a valid number (1-5)")

        choice = menu()
