'''
 Student Management System
'''

students = [{"Roll" : 231, "Name" : "Harsh", "Age" : 17, "Marks" : 87.5},
            {"Roll" : 232, "Name" : "Rohit", "Age" : 18, "Marks" : 90.0},
            {"Roll" : 233, "Name" : "Anjali", "Age" : 17, "Marks" : 92.5},
            {"Roll" : 234, "Name" : "Priya", "Age" : 18, "Marks" : 88.0},
            {"Roll" : 235, "Name" : "Amit", "Age" : 17, "Marks" : 85.0} ]

# Function to add a new student
def Add_Student():
    print("Add Student Enter your details : ")
    Roll = int(input("Enter your roll no. : "))
    Name = input("Enter your name : ")
    Age = int(input("Enter your age : "))
    Marks = float(input("Enter your marks : "))

     # Create a new student dictionary and append it to the students list   
    student = {
            "Roll": Roll,
            "Name": Name,
            "Age": Age,
            "Marks": Marks
    }
    students.append(student)
    print("Student added successfully!\n")

# Function to show all students
def Show_Students():
    print("List of Students:")
    for student in students:
        print(student)

# Function to search for a student by roll number
def Search_Student():
    print("Search Student Enter your details : ")
    Rollnumber = int(input("Enter your Roll number : "))
    for student in students:
        if Rollnumber == student["Roll"]:
            print(student)
        else:
            print("Student data not found! please try again.")

# Function to update a student's information
def Update_Student():
    print("Update Student Enter your details : ")
    Rollnumber = int(input("Enter your Roll number : "))
    for student in students:
        if Rollnumber == student["Roll"]:
            Name = input("Enter your name : ")
            Age = int(input("Enter your age : "))
            Marks = float(input("Enter your marks : "))
            student["Name"] = Name
            student["Age"] = Age
            student["Marks"] = Marks
            print("Student data updated successfully!")
            

# Function to delete a student by roll number  
def Delete_Student():
    print("Delete Student Enter your details : ")
    Rollnumber = int(input("Enter your Roll number : "))
    for student in students:
        if Rollnumber == student["Roll"]:
            students.remove(student)
            print("Student data deleted successfully!")
        else:
            print("Student data not found! please try again.")



# Main program loop
while True:
    print("""    1. Add Student
    2. Show Students
    3. Search Student 
    4. Update Student 
    5. Delete Student
    6. Exit """)

    choice = int(input("Enter your choice number : "))
    if choice == 1:
        Add_Student()

    elif choice == 2:
        Show_Students()

    elif choice == 3:
        Search_Student()

    elif choice == 4:
        Update_Student()
    
    elif choice == 5:
        Delete_Student()    
    
    elif choice == 6:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please try again.")
if __name__ == "__main__":
    pass