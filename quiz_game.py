print("Welcome to the QUIZ game!")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Ok, let's play")
score = 0

q1_answer = input("Q1: What does CPU stands for ? ")
if q1_answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


q2_answer = input("Q1: What does GPU stands for ? ")
if q2_answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

q3_answer = input("Q1: What does RAM stands for ? ")
if q3_answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


q4_answer = input("Q1: What does PSU stands for ? ")
if q4_answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

print(f"You got {score} questions correct!")
print(f"You got {score / 4 * 10} %")
