def pattern(n):
    k=2*n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0,i + 1):
            print("*",end=" ")
        print("\r")
        
pattern(5)

def student_number():
    number_of_student = int(input("\nEnter No of student in the class: "))
    return number_of_student

def student_info():
    id = str(input("\nEnter student id: "))
    name = str(input("\nEnter student name: "))
    dob = str(input("\nEnter student date of birth: "))
    return id, name, dob

def student_list():
    Fuiyohh = []    
    a = student_number()
    for i in range(a):
        id, name, dob = student_info()
        Fuiyohh.append((id, name, dob))  # add id,name,dob to https://youtube.com/shorts/V4LaRFhkVCA?feature=share
        print(f"\nWelcome student with student id {id} ")     
    print("\nStudent list:", Fuiyohh)
    return Fuiyohh

def course_number():
    number_of_course = int(input("\nEnter number of course: "))
    return number_of_course

def course_info():
    id = str(input("\nEnter course id: "))
    name = str(input("\nEnter course name: "))
    return id, name

def course_list():
    Fuiyohh = []
    b = course_number()
    for i in range(b):
        id, name = course_info()
        Fuiyohh.append((id, name))    # add id,name to Fuiyohh list belongin to course_list()
        print(f"Course {id} aka {name} added")
    print("\nCourse list", Fuiyohh)
    return Fuiyohh

def get_mark(): 
    mark_list = []
    students_list = []
    A = course_list()
    B = student_list()
    ask_course = input("\nChoose course id: ")
    Biglist = [students_list,mark_list]
    
    if ask_course in (item for sublist in A for item in sublist):                                 # Using List Comprehension
        print(f"\nYou choose the {ask_course} course")                                            # lis1 = [1,2]
                                                                                                  # lis2 = [3,4,5]
    ask_student = int(input(f"\nHow many student in course {ask_course}?: "))                     # listoflists = [lis1,lis2]
                                                                                                  # flattenlist = [x  for sublist in listoflists for x in sublist]
    if ask_student > len(B):                                                                      # print(flattenlist)
        print(f"\n Invalid!!!")                                                                   # Output: [1,2,3,4,5]
                                                                                                  # (Variable x is selected from a sublist that is selected from the main list that contains all the other lists)
    else:                                                                                         
        for i in range(ask_student):                                                              
            ask_id = input("\nChoose student id: ")                                               
            if ask_id in (item for sublist in B for item in sublist):   
                get_mark = input(f"\nEnter mark for student {ask_id}: ")
                mark_list.append(get_mark)  #add
                students_list.append(ask_id)  #add
                    
            print("\nIn the course id " + ask_course + ": list of mark is in the format [[student id], [mark]] " )
            print(Biglist)

get_mark()
            