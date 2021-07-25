while True:
    print("Welcome to GPA/CGPA Calculator\n")
    input("Press Enter to continue...")
    semester_no = int(input("Which semester are you in?\n"))
    if semester_no == 1:
        print("It is your first semester!")
        input("Press Enter to continue...")
    elif 1 < semester_no < 9:
        gpa_from_previous_semesters = [0]*(semester_no-1)
        for i in range (0, semester_no-1):
            gpa_from_previous_semesters[i] = float(input("Enter your GPA in semester " + str(i+1) + " "))
        input("Press Enter to continue...")
    else:
        print("The semester_no cannot be", semester_no)
    dct_for_courses = {}
    num_of_courses = int(input("enter the number of courses.\n"))
    lst_of_courses_for_the_semester = []
    for i in range (0, num_of_courses):
        name_of_the_course = input("enter the name of the "+ str(i+1)+ "th course.\n")
        lst_of_courses_for_the_semester.append(name_of_the_course)
        'credit_of_the_course = int(input("how many credits does this course have?\n"))'
        'dct_for_courses[name_of_the_course] = credit_of_the_course'
    for course in lst_of_courses_for_the_semester:
        credit_of_the_course = int(input("how many credits does " + course + " have?"))
        dct_for_courses[course] = credit_of_the_course
    letter_notes = {"aa":4, "ba":3.5, "bb":3,"cb":2.5,"cc":2,"dc":1.5, "dd":1, "fd":0.5, "ff":0}
    total_credits = 0
    letter_grades_for_the_courses = {}
    for course in dct_for_courses.keys():
        print("for the course", course, "which letter grade have you gotten?")
        letter = input().lower()
        letter_grades_for_the_courses[course] = letter.upper()
        total_credits += letter_notes[letter] * dct_for_courses[course]
    gpa = total_credits / sum(dct_for_courses.values())
    cgpa = (gpa + sum(gpa_from_previous_semesters)/(semester_no-1))/semester_no
    print("For the Semester", semester_no)
    print("------------------")
    for course in dct_for_courses.keys():
        print(course, letter_grades_for_the_courses[course])
    print("Your total credit for this semester is", total_credits)
    print("Your GPA in semester", semester_no, "is")
    print(round(gpa,2))
    print("Your CGPA is", round(cgpa,2))
    stance = ""
    if (3.5 > cgpa >= 3):
        stance = "honor"
    elif (4 >= cgpa >= 3.5):
        stance = "high honor"
    elif (3 > cgpa >= 2):
        stance = "satisfactory"
    else:
        stance = "probation"
    print("Your stance is", stance)
    print("Press R to retry, press E to exit.\n")
    key = input()
    if (key == "r" or key == "R"):
        continue
    elif (key == "e" or key == "E"):
        break


    
    
