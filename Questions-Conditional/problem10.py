pet_species = "dog"
pet_age = 3
pet_food = " "

if pet_species == "dog":
    if pet_age <= 2:
        pet_food = "Puppy food"
    else:
        pet_food= "Adult Dog food"

elif pet_species == "cat":
    if pet_age < 5:
        pet_food = "Kitten food"
    else:
        pet_food = "Senior Cat food"

print("You have a", pet_species, "of age", pet_age, "and here's your pet food:", pet_food)


    


