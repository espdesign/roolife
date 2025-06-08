# Evan Pendergraft
# CITA 180_0W1_BURL - Intro to Programming (Spring 2024)
# Programming Assignment 06

# Input
gradeItems = ("Quizzes", .30, 6, "Exams", .70, 3)
grades = (100, 95, 100, 100, 93, 95, 100, 90, 80)

# Processing
gradeItems_buckets = []
grades_buckets = []
gradeOutput = []

for i in range(0, len(gradeItems), 3):
    gradeItems_buckets.append(gradeItems[i:i + 3])

i = 0
for group in gradeItems_buckets:
    number_of_grades = group[2]
    grades_buckets.append(grades[i:i + number_of_grades])
    i += int(number_of_grades)

final_grade = 0
i = 0
for element in gradeItems_buckets:
    category = element[0]
    weight = element[1]
    number_of_grades = element[2]
    grades = grades_buckets[i]
    grade_average = sum(grades) / len(grades)
    contribution = grade_average * weight
    final_grade += contribution

    gradeOutput.append('{:<10}{:>6.0%}{:>9.2f}{:>14.2f}'.format(category, weight, grade_average, contribution))
    i += 1

gradeOutput.append('{:<10}{:>28.2f}'.format('Final Grade', final_grade))

# Output
print("Category  Weight  Average  Contribution")
print("---------------------------------------")

for i in range(len(gradeOutput) - 1):
    print(gradeOutput[i])

print("---------------------------------------")
print(gradeOutput[-1])
