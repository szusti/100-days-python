# Grading Program
# You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are their exam scores. 
# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should 
# contain student names as keys and their assessed grades for values. 
# The final version of the student_grades dictionary will be checked. 
# **DO NOT** modify lines 16-22 to change the existing student_scores dictionary. 

# This is the scoring criteria: 
# - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# - Scores 71 - 80: Grade = "Acceptable" 
# - Scores 70 or lower: Grade = "Fail" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
text_result = ""
for person in student_scores:
    score = int(student_scores[person])
    if score >= 91:
        text_result = "Outstanding"
    elif 90 >= score >=81:
        text_result = "Exceeds Expectations"
    elif 80 >= score >=71:
        text_result = "Acceptable"
    else:
        text_result = "Fail"
    student_grades[person] = text_result


print(student_grades)