# Check the highest scores from list that user provide

student_scores_input = input("Provide scores separated by space\n").split()

# per default, list will be string, so we need to convert numbers from string to integer
# List "comprehension" was used. It let you modify list with item from the list. It's a quicker way than use loop like
# for i in range(0, len(students_score)):
#     students_score[i] = int(students_score[i])

student_scores = [int(i) for i in student_scores_input]
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"Highest score is {highest_score}")

#Different method. 
# NOTE - remember that list need to be in string, otherwise it will compare numbers as strings

print(f"Highest value {max(student_scores)}")
