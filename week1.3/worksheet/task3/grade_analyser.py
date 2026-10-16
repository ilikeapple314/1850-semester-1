# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file

studentFiles = input("Enter file name: ")

# open the file

with open(studentFiles , "r") as file:
    students = [line.strip().split(",") for line in file]

for student in students:
    if(student[0] == "student_id"):
        continue
    else:
        studentID = student[0]
        totalScore = 0
        totalScores = 0
    for grades in student:
        if(grades.isdigit() and grades != ""):
            grade = int(grades)
            totalScore = totalScore + grade
            totalScores = totalScores + 1

    average_grade = totalScore / totalScores
    classification = ""

    if(average_grade >= 70):
        classification = "1"
    elif(average_grade >= 60):
        classification = "2:1"
    elif(average_grade >= 50):
        classification = "2:2"
    elif(average_grade >= 40):
        classification = "3"
    else:
        classification = "F"


    with open("input_file_name + _out.csv", "a") as file:
        file.write(f"{studentID},{average_grade:.2f},{classification} \n")





# read in the data, and for each student calculate their average grade and classification



# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder