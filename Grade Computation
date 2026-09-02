print("=" * 70)
print("GRADE COMPUTATION SYSTEM")
print("=" * 70)
 
# ----------------- ASSESSMENT TASKS -----------------
 
assign1_noi = int(input("Assignment 1 - Number of Items: "))
assign1_score = int(input("Score: "))
 
quiz1_noi = int(input("\nQuiz 1 - Number of Items: "))
quiz1_score = int(input("Score: "))
 
act1_noi = int(input("\nActivity 1 - Number of Items: "))
act1_score = int(input("Score: "))
 
act2_noi = int(input("\nActivity 2 - Number of Items: "))
act2_score = int(input("Score: "))
 
act3_noi = int(input("\nActivity 3 - Number of Items: "))
act3_score = int(input("Score: "))
 
# ----------------- LONG EXAMS -----------------
 
longexam1_noi = int(input("\nLong Exam 1 - Number of Items: "))
longexam1_score = int(input("Score: "))
 
longexam2_noi = int(input("\nLong Exam 2 - Number of Items: "))
longexam2_score = int(input("Score: "))
 
# ----------------- DEPARTMENTAL EXAM -----------------
 
dept_noi = int(input("\nDepartmental Exam - Number of Items: "))
dept_score = int(input("Score: "))
 
# ----------------- COMPUTATION -----------------
 
# Assessment Tasks
at_noi = assign1_noi + quiz1_noi + act1_noi + act2_noi + act3_noi
at_score = assign1_score + quiz1_score + act1_score + act2_score + act3_score
at_percent = (at_score / at_noi) * 100
at_average = at_percent * 0.40
 
# Long Exams
lex_noi = longexam1_noi + longexam2_noi
lex_score = longexam1_score + longexam2_score
lex_percent = (lex_score / lex_noi) * 100
lex_average = lex_percent * 0.40
 
# Departmental Exam
dem_noi = dept_noi
dem_score = dept_score
dem_percent = (dem_score / dem_noi) * 100
dem_average = dem_percent * 0.20
 
# Final Grade
final_grade = at_average + lex_average + dem_average
 
# ----------------- OUTPUT -----------------
 
print("\n")
print("=" * 75)
print("{:<30}{:^10}{:^10}{:^10}".format("ASSESSMENT TASKS", "NOI", "SCORE", "%"))
print("=" * 75)
 
print("{:<30}{:^10}{:^10}".format("Assignment 1", assign1_noi, assign1_score))
print("{:<30}{:^10}{:^10}".format("Quiz 1", quiz1_noi, quiz1_score))
print("{:<30}{:^10}{:^10}".format("Activity 1", act1_noi, act1_score))
print("{:<30}{:^10}{:^10}".format("Activity 2", act2_noi, act2_score))
print("{:<30}{:^10}{:^10}".format("Activity 3", act3_noi, act3_score))
print("{:<30}{:^10}{:^10}{:^10.2f}".format("AT Average", at_noi, at_score, at_average))
 
print("-" * 75)
 
print("{:<30}{:^10}{:^10}".format("Long Exam 1", longexam1_noi, longexam1_score))
print("{:<30}{:^10}{:^10}".format("Long Exam 2", longexam2_noi, longexam2_score))
print("{:<30}{:^10}{:^10}{:^10.2f}".format("LEX Average", lex_noi, lex_score, lex_average))
 
print("-" * 75)
 
print("{:<30}{:^10}{:^10}".format("Departmental Exam", dem_noi, dem_score))
print("{:<30}{:^10}{:^10}{:^10.2f}".format("DEM Average", dem_noi, dem_score, dem_average))
 
print("=" * 75)
print("{:<30}{:>45.2f}".format("FINAL GRADE", final_grade))
print("=" * 75)
