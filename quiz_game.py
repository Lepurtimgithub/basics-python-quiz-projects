print("Welcome to my quiz")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okey! Let's play :)")
score = 0

answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1

else:
    print("Incorrect :(")

answertwo = input("What does gpu stand for? ")
if answertwo.lower() == "graphics processing unit":
    print('Correct!')
    score += 1

else:
    print("Incorrect :(")

answerthree = input("What does RAM stand for? ")
if answerthree.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect :(")

answerfour = input("What does PSU stand for? ")
if answerfour.lower() == "power suply":
    print('Correct!')
    score += 1
else:
    print("Incorrect :(")

print("You got " + str(score) + " question correct!")
print("You got " + str((score / 4) * 100) + "%.")
