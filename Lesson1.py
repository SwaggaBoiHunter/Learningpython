#Pursley,Hunter Lab2.04: Lists (Game Shoow & Food Chooser)
#2/27/26
prizes = ['Toy Truck', 'Toy Car', 'Toy Van', 'Cards', 'Computer', 'Money', 'Dog', 'Xbox', 'Shoes', 'Gift Card']
door_chosen = int(input("Choose a door 1 through 10 and earn a prize! "))
if door_chosen == 1:
    print(prizes[0])
if door_chosen == 2:
    print(prizes[1])
if door_chosen == 3:
    print(prizes[2])
if door_chosen == 4:
    print(prizes[3])
if door_chosen == 5:
    print(prizes[4])
if door_chosen == 6:
    print(prizes[5])
if door_chosen == 7:
    print(prizes[6])    
if door_chosen == 8:
    print(prizes[7])    
if door_chosen == 9:
    print(prizes[8])  
if door_chosen == 10:
    print(prizes[9])    
#This will run through every scenario and give the prize based on what the user chooses.
print("Great! Now that you have your prize, let's try and guess your favorite food from this list:")
foods = ['Burger', 'Pizza', 'HotDog', 'Taco', 'Chicken', 'Pasta']
scores = [0, 0, 0, 0, 0, 0,]
print (*foods) #Prints out all of the available food for the user to choose and then asks questions to guess their favorite food.
question1 = input("Is your favorite food crunchy? Yes/No ")
question2 = input("Does your favorite food have cheese in it? Yes/No ")
question3 = input("Is your favorite food from America? Yes/No ")
question4 = input("Does your favorite food have any meat in it? Yes/No ")
question5 = input("Does your favorite food combo with fries? Yes/No ")
question6 = input("Does your favorite food have a bun surrounding it? Yes/No ")
question7 = input("Does your food have protein in it? Yes/No ")
question8 = input("Do you eat your food with utensils? Yes/No ")
if question1.lower() == "yes":
    scores[3] += 1
    scores[4] += 1
if question2.lower() == "yes":
    scores[0] += 1
    scores[1] += 1
    scores[5] += 1
    scores[3] += 1
if question3.lower() == "yes":
    scores[0] += 1
    scores[4] += 1
    scores[2] += 1
if question4.lower() == "yes":
    scores[4] += 1
    scores[3] += 1
    scores[0] += 1
    scores[2] += 1
if question5.lower() == "yes":
    scores[0] += 1
    scores[2] += 1
    scores[4] += 1
if question6.lower() == "yes":
    scores[0] += 1
    scores[2] += 1
if question7.lower() == "yes":
    scores[0] += 1
    scores[2] += 1
    scores[3] += 1
    scores[4] += 1
if question8.lower() == "yes":
    scores[5] += 2
max_score = max(scores) #Figures out the highest score and then prints it out to tell the user what item out of the list is their favorite.
favorite_index = scores.index(max_score)
print("Your favorite food is:", foods[favorite_index])
