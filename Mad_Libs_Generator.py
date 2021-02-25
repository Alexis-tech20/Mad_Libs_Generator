# Mad Libs Generator

# Loop back to this point once code finishes
loop = 1

while (loop < 10):

# All the questions that the program asks the user
    proper_name = input("Choose a proper name: ")
    adjective = input("Choose an adjective: ")
    famous_person = input("Choose a famous person: ")
    noun = input("Choose a noun: ")
    number = input("Choose a number: ")
    adjective2 = input("Choose an adjective: ")
    plant = input("Choose a plant: ")
    place = input("Choose a place: ")
    adverb = input("Choose an adverb: ")
    proper_name2 = input("Choose a proper name: ")
    verb = input("Choose a verb: ")
    interjection = input("Choose an interjection: ")
    song_title = input("Choose a song title: ")
    adjective3 = input("Choose an adjective: ")
    adjective4 = input("Choose an adjective: ")
    plural_noun = input("Choose a plural noun: ")
    verb2 = input("Choose a verb: ")

# Displays the story based on the users input
    print ("------------------------------------------")
    print(f"Welcome to the University of, {proper_name.title()}.")
    print(f"Our {adjective} campus was founded by {famous_person.title()} and built in 1806.")
    print(f"We begin at our {noun} building.")
    print(f"This building houses {number} classrooms.")
    print(f"To your left, the {adjective2} dormitory is visible just beyond the {plant}.")
    print(f"Our students come from all over the {place} because we {adverb} accept anyone who applies.")
    print(f"We will end the tour here at {proper_name2.title()} hall which houses the Admissions Office.")
    print(f"Feel free to {verb} an application.")
    print(f"{interjection.title()} folks, you’re in for a treat!")
    print(f"The marching band is practicing our Alma Mater,{song_title.title()} Notice how they march in a {adjective3} formation, it is the signature move of our University.")
    print(f"Financial aid is available to all {adjective4} applicants.")
    print(f"More information is available on our website, {plural_noun}.com.")
    print(f"Thank you for {verb2} with us today.")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1
