STUDENT={} # Dictionary to store info
def NoOfStudents():     
    return int(input("Enter number of students: "))  

a = NoOfStudents()    
def StudentInfo(a): # Input student info
    for i in range(1,a+1):
        studentId = input("Enter student id: ") 
        studentName = input("Enter student name: ")     
        studentDOB = input("Enter student's date of birth: ")     
        return {
        'id1': studentId,
        'name': studentName,
        'dob': studentDOB
    }
no_students = NoOfStudents()
for i in range(no_students):
    STUDENT += [NoOfStudents()]

COURSE={} # Dictionary to store info
def NoOfCourses():     
    return int(input("Enter number of courses: "))  

b = NoOfCourses()   
def CourseInfo(b):   # Input course info
    for i in range(1,b+1):
        courseID = input("Enter course id: ") 
        courseName = input ("Enter course name: ")  
        return{ 
        'id2': courseID,
        'name': courseName
        }
no_courses = NoOfCourses()
for i in range(no_courses):
    COURSE += [NoOfCourses()]

MARK={} # Dictionary to store info
def addMark(courseID,studentId):
    if courseID not in COURSE():
        print("Invalid course id")
        return
    
    for studentId in STUDENT():
        mark = int(input(f"Enter the mark for {STUDENT['id1']['Name']}: "))
    
        if studentId not in MARK:
            MARK[studentId]={}

        MARK[studentId][courseID] = mark

# Define function to list courses
def list_courses():
    for courseID in COURSE:
        print(f"{courseID}: {COURSE['id2']['name']}")

# Define function to list students
def list_students():
    for studentId in COURSE:
        print(f"{studentId}: {STUDENT['id2']['name']}")


# Define function to show marks for a given course
def show_marks():
    courseID = input("Enter the course ID: ")
    if courseID not in COURSE:
        print("Wrong be@tch!!!")
        return
    for id in STUDENT:
        if id in MARK and courseID in MARK[id]:
            print(f"{STUDENT[id]['name']}: {MARK[id][courseID]}")
        else:
            print(f"{STUDENT[id]['name']}: You die!")
            break

StudentInfo()
CourseInfo()

while True:
    print()
    print()
    print()
    print()
    print("5.End")
    choice = input("Please make a choice: ")
    if choice == "1":
        addMark()
    elif choice == "2":
        list_courses()
    elif choice == "3":
        list_students()
    elif choice == "4":
        show_marks()
    elif choice == "5":
        break
    else:
        print("Invalid choice!!!")

