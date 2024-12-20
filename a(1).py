# Function to check if student can sit in the class
def can_sit_in_class(percentage):
    if percentage < 75:
        return False
    else:
        return True

# Input: Student's percentage
student_percentage = int(input("Enter the student's percentage: "))

# Check if the student can sit in the class
if can_sit_in_class(student_percentage):
    print("The student can sit in the class.")
else:
    print("The student cannot sit in the class.")

