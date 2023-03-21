class Schewdent:  
    def __init__(self, schewdent_id, name, dob):
        self.schewdent_id = schewdent_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self,c_id, name):
        self.course_id = c_id
        self.name = name

class MarkSchewdent(Schewdent,Course): # Child class
    def __init__(self):
        self.marks = {} 
        self.schewdents = [] 
        self.courses = []  

    def input_num_schewdents(self):
        x =  int(input("Type the number of schewdents: "))
        return x
    
    def input_num_courses(self):
        y = int(input("\nType the number of courses: "))
        return y

    def schewdentIn4(self, a):
        print(f"\n<>|<>|<>|<> For schewdent \"No{a}\" <>|<>|<>|<>")
        schewdent_name = input("Type schewdent name: ")
        schewdent_id = int(input("Type schewdent ID: "))
        schewdent_dob = input("Type schewdent date of birth: ")
        schewdent = Schewdent(schewdent_id, schewdent_name, schewdent_dob)
        self.schewdents.append(schewdent)
    
    # Store course data
    def courseIn4(self, b):
        print(f"\n<>|<>|<>|<> Course \"No{b}\" <>|<>|<>|<>")
        course_name = input("Type course name: ")
        course_id = int(input("Type course ID: "))
        course = Course(course_id, course_name)
        self.courses.append(course)

    # Type mark
    def add_marks(self, course_id):
        for schewdent in self.schewdents:
            mark = float(input(f"\nType mark for schewdent \"{schewdent.name.capitalize()}\" in course \"{self.courses[course_id -1].name.capitalize()}\": "))
            if 10 <= mark <= 20:
                print(f"Nice, you have passed the course!!!")
            elif mark < 10: 
                print(f"School's wallet ==> Stonks. Fuiyoh$$$ We're rich $$$")
            else:
                print(f"Invalid!!")
                break
            self.marks[(schewdent.schewdent_id, course_id)] = mark
        
    
    # Show schewdent data
    def list_schewdent(self):
        i = 0
        for schewdent in self.schewdents:
            i = i + 1
            print(f""""
            [o] Schewdent No:{1}
            [o] Name: {schewdent.name.capitalize()} 
            [o] ID: {schewdent.schewdent_id} 
            [o] DOB: {schewdent.dob} 
            """)

    # Show course data
    def list_courses(self):
        i = 0
        for course in self.courses:
            i = i + 1
            print(f"[o] Course \"No{i}\": \"{course.name.capitalize()}\" - ID: \"{course.course_id}\" ")

    # Show mark
    def showMarks(self,course_id):
        print("\nMark of schewdent: ")
        for schewdent in self.schewdents:
            if (schewdent.schewdent_id, course_id) in self.marks:
                mark = self.marks[(schewdent.schewdent_id, course_id)]
                print(f"{schewdent.name.capitalize()} have {mark} points for course {self.courses[course_id-1].name.capitalize()}|") # Lists always start at index 0
            else:
                print(f"Invalid")
    
    def admin(self):
        num_schewdents = self.input_num_schewdents()
        for i in range(num_schewdents):
            self.schewdentIn4(i+1)
        
        num_courses = self.input_num_courses()
        for j in range(num_courses):
            self.courseIn4(j+1)

        self.list_schewdent()
        self.list_courses()

        x = int(input("\nSelect a course to add marks (begin with \"1\"): "))
        for x in range(1, num_courses+1):
            course_id = x
            self.add_marks(course_id)
            self.showMarks(course_id)

        y = self.marks.items()
        print(y)

Execute = MarkSchewdent()
# Decorator-------------------------------------------------------------------------
class Start:                                                                      #|
  def __init__(self, i, j):                                                       #|
    self.word1 = i                                                                #|
    self.word2 = j                                                                #|
                                                                                  #|
  def __str__(self):                                                              #|
    return f"\n\t\t\t\t\t\t\t\t\t\t\t\t{self.word1.upper()} {self.word2.upper()}" #|
                                                                                  #|
p1 = Start("start", "program")                                                    #|
print(p1)                                                                         #|
                                                                                  #|
def pattern(n):                                                                   #|
    k=2*n-2                                                                       #|
    for i in range(n,-1,-1):                                                      #|
        for j in range(k,0,-1):                                                   #|
            print(end=" ")                                                        #|
        k = k + 1                                                                 #|
        for j in range(0,i + 1):                                                  #|
            print("*",end=" ")                                                    #|
        print("\r")                                                               #|
pattern(5)                                                                        #|
# Decorator-------------------------------------------------------------------------

Execute.admin()
    
