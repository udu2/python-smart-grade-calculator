#Smart Student Grade Calculator

assignment_score = float(input("Enter assignment score: "))
test_score = float(input("Enter test score: "))
exam_score = float(input("Enter exam score: "))
 
# Arithmetic operations
total_score = test_score + assignment_score + exam_score
average_score = total_score / 3

# Comparison operators
passed = average_score >= 50

# Logical conditions for award qualification
award = average_score >= 70 and exam_score >= 60

# Display results
print("\n--- STUDENT REPORT ---")
print("Total Score:", total_score)
print("Average Score:", average_score)

if passed:
    print("Status: PASSED")
else:
    print("Status: FAILED")

if award:
    print("Award Status: QUALIFIES FOR AN AWARD")
else:
    print("Award Status: DOES NOT QUALIFY FOR AN AWARD")