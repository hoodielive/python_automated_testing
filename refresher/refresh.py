# Ask user for a list of people they know
# Split the string into a list 
# Return that list 

def who_do_you_know():
    people = input("Please provide a list of the people that you know separated by commas: ")
    people_list = people.split(',')

    people_without_spaces = []
    for person in people_list:
        people_without_spaces.append(person.strip())
    return people_without_spaces

# Ask user for a name 
# See if their name is in the list of people they know 
# Print out that they know the person

def ask_user():
    person = input("Please provide a name of a person you know: ")
    if person in who_do_you_know():
        print("You know {}!".format(person))

ask_user()
