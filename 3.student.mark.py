import math 
import numpy 

class Schewdent:  
    def __init__(self, schewdent_id, name, dob):
        self.schewdent_id = schewdent_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self,c_id, name,credits):
        self.course_id = c_id
        self.name = name
        self.credits = credits

class MarkSchewdent(Schewdent,Course):
    def __init__(self):
        self.marks_dict = {} # dict to store marks specified with schewdent_id and course_id
        self.schewdents = [] 
        self.courses = [] 
        self.creditss = [] 
        
    def schewdentIn4(self, a):
        print(f"\n<>|<>|<>|<> For schewdent \"No{a}\" <>|<>|<>|<>")
        schewdent_id = input("Enter schewdent ID: ")
        schewdent_name = input("Enter schewdent name: ")
        schewdent_dob = input("Enter schewdent date of birth (DD-MM-YYYY): ")
        schewdent = Schewdent(schewdent_id, schewdent_name, schewdent_dob)
        self.schewdents.append(schewdent)
    
    def courseIn4(self, b):
        print(f"\n<>|<>|<>|<> Course \"No{b}\" <>|<>|<>|<>")
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course_credits = int(input("Enter credits of the course: "))
        course = Course(course_id, course_name, course_credits)
        self.courses.append(course)
 
    def add_marks(self, course_id):
        for schewdent in self.schewdents:
            mark = float(input(f"\nType mark for schewdent \"{schewdent.name.capitalize()}\" in course \"{self.courses[course_id].name.capitalize()}\": "))
            if 10 <= mark <= 20:
                print(f"Nice, you have passed the course!!!")
            elif mark < 10: 
                print(f"Chúc mừng bạn đã quay vào ô \"Retake\". Chúc bạn retake nhiều hơn. School's wallet ==> Stonks. Fuiyoh$$$ We're rich $$$")
            else:
                print(f"Invalid!!")

            self.marks_dict[(schewdent.schewdent_id, course_id)] = mark
        
    # Show schewdent data
    def list_schewdent(self):
        i = 0
        print("----------------------------------------------------------")
        for schewdent in self.schewdents:
            i = i + 1
            print(f""""[o] Schewdent No.{i}                            
            \t Name: {schewdent.name.capitalize()}            
            \t ID: {schewdent.schewdent_id}               
            \t DOB: {schewdent.dob} """)
        print("----------------------------------------------------------")
    
    # Show course data
    def list_courses(self):
        i = 0
        print("\n")
        print("----------------------------------------------------------")
        for course in self.courses:
            i = i + 1
            print(f"""[o] Course \"No.{i}\": \"{course.name.capitalize()}\"           
            \t ID: \" {course.course_id} \"               
            \t NoCredits: \" {course.credits} \" """)                     
            self.creditss.append(course.credits)
        print("----------------------------------------------------------")
    
    # Counting total of creds
    def sum_of_cred(self,l,n): # or use built-in sum()
        if n == 0:
            return l[n]
        return l[n] + self.sum_of_cred(l,n-1)
    
    def admin(self):
        num_schewdents = int(input("\nEnter the number of schewdents: "))
        for i in range(num_schewdents):
            self.schewdentIn4(i+1)
        
        num_courses = int(input("\nEnter the number of courses: "))
        for j in range(num_courses):
            self.courseIn4(j+1)
        
        self.list_schewdent()
        self.list_courses() 

        for t in range(0, num_courses):
            course_id = t
            self.add_marks(course_id)
            
        marks_list = [] 
        for uwu in self.marks_dict: 
            marks_list.append(self.marks_dict[uwu]) 

        arr1 = numpy.array(marks_list) # Store marks
        arr2 = numpy.array(self.creditss) # Store creds .Ex: 4 or 3 => [4, 3]
        sum = self.sum_of_cred(self.creditss,len(self.creditss)-1)
        
        gpa_sorting = [] 
        def gpa(x):
            siuuuuu = []
            y = 0
            OvO = arr1[x:len(arr1):num_courses] # [start:end:step]
            for i in range(0,len(OvO)): 
                for j in range(0,len(arr2)): 
                    if i == j:
                        y += OvO[i]*arr2[j] / sum   # Recursion: Index "0 and 2" then "1 and 3", respectively
            
            if abs(y - int(y)) < 0.55:
                roundMark = math.floor(y*10)/10
            else:
                roundMark = math.ceil(y*10)/10
                
            for schewdent in self.schewdents:
                z = schewdent.name
                siuuuuu.append(z)
            disciple = siuuuuu[x] 
            print(f"\nFinal GPA of schewdent \"{disciple}\": \"{roundMark}\" ")
            gpa_sorting.append(roundMark) 

            if x+1 == num_schewdents:
                pass
            else:
                return gpa(x+1) # Resursion
        
        gpa(0)
        print("\nSort schewdent list in GPA descending order: ")
        for i in range(0,len(gpa_sorting)): 
            for j in range(0,len(gpa_sorting)): 
                if (gpa_sorting[i] > gpa_sorting[j]): 
                    a = gpa_sorting[i]
                    gpa_sorting[i] = gpa_sorting[j]
                    gpa_sorting[j] = a
        print(gpa_sorting)
        
Execute = MarkSchewdent()
class Start:                                                                      
  def __init__(self, i, j):                                                       
    self.word1 = i                                                                
    self.word2 = j                                                                
                                                                                  
  def __str__(self):                                                              
    return f"\n\t\t\t\t\t\t\t\t\t\t\t\t{self.word1.upper()} {self.word2.upper()}" 
                                                                                  
p1 = Start("start", "program")                                                    
print(p1)                                                                         
                                                                                  
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
Execute.admin()
