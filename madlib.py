#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
print("welcome to niti's band name generator")
city = input("which city did you grow up in?\n")
print(city)
pet = input("what is name of your pet?\n")
print(pet)
print("your band name could be" + city + " " +pet)

#madlib 1 

person_name = input("enter your name ")
city = input("enter your city name ")
weekday = input("What's the day today ")
madlib = f"Hello {person_name}! hope you are feeling amazing today \n check the weather of {city} and enjoy your {weekday}!"
print(madlib)
