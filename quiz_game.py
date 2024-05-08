print("Welcome to my computer quiz !")
playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()

print("Okay! Let's play :)")

questions = {
    "What does CPU stand for? ": "central processing unit",
    "What does GPU stand for? ": "graphics processing unit",
    "What does RAM stand for? ": "random access memory",
    "What does PSU stand for? ": "power supply"
}

for question, correct_answer in questions.items():
    answer = input(question)
    if answer.lower() == correct_answer:
        print("Correct!")
    else:
        print("Incorrect!")

