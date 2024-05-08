print("Welcome to my computer quiz !")
playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

questions = {
    "What does CPU stand for? ": "central processing unit",
    "What does GPU stand for? ": "graphics processing unit",
    "What does RAM stand for? ": "random access memory",
    "What does PSU stand for? ": "power supply",
    "What does HTML stand for? ": "hypertext markup language",
    "What does PDF stand for? ": "portable document format",
    "What does HTTP stand for? ": "hypertext transfer protocol"
}

for question, correct_answer in questions.items():
    answer = input(question)
    if answer.lower() == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

hardQuestions = {
    "What does BIOS stand for? ": "basic input/output system",
    "What does USB stand for? ": "universal serial bus",
}

for question, correct_answer in hardQuestions.items():
    answer = input(question)
    if answer.lower() == correct_answer:
        print("Correct!")
        score += 2
    else:
        print("Incorrect!")
 
print("You got " + str(score) + "/11!")
print("You got " + str(score/9 * 100) + "%.")