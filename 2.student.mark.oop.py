class Student:
    
    def __init__(student , student_id , student_name, student_dob):
        student.student_id = student_id
        student.student_name = student_name
        student.student_dob = student_dob  
      
    def get_student_id(student):
        return student.student_id

    def set_student_name(student, student_name):
        student.student_name = student_name

    def get_student_name(student):
        return student.student_name

    def get_student_dob(student):
        return student.student_dob

    

    def show_info(student):
        print(f"{ student.get_student_id() }\t{ student.student_name }\t{ student.student_dob}")

class Course:
    
    def __init__(course, course_id, course_name):
        course.course_id = course_id
        course.course_name = course_name
        
    def get_course_id(course):
        return course.course_id

    def set_course_name(course, course_name):
        course.course_name = course_name

    def get_course_name(course):
        return course.course_name
   
    def show_course(course):
        print(f"{course.get_course_id()}\t{course.course_name} ")

class Mark:
    def __init__(student,student_mark):
       student.mark=student_mark

    def get_student_mark(student):
        return student.student_mark 

    def set_student_mark(student,student_mark):
        student_student_mark=student_mark    

liststudent = []
listcourse = []
marks = []

while True:
    print("STUDENT MARK MANAGEMENT")
    print("1. Add Student \t\t5. Add Marks")
    print("2. View List Students \t6. View Marks")
    print("3. Add Course \t\t7. Exit")
    print("4. View List Courses")
    action =0
    action =int(input("Select an option: "))    
    if action == 0:
            break
    elif action == 1:
            no = int(input("Input number of students: "))
            for i in range (0,no):
                print(f"Input student number {i+1} : ")
                student_id = input("ID: ")
                student_name = input("Name: ")
                student_dob = input("Date of Birth: ")
                st = Student(student_id , student_name, student_dob)
                liststudent.append(st)                 
        
    elif action == 2:
            if len(liststudent) == 0:
                print("\n 0 student found")
            else: 
                print(f"\nSTUDENTS LIST:")
                print(f"ID\t Name\t DOB")              
                for i in liststudent:
                    i.show_info()
        
    elif action == 3:
            no = int(input("Input number of courses: "))
            for i in range (0,no):
                print(f"Input course number {i+1} : ")
                course_id = input("Course id: ")
                course_name = input("Course name: ")
                c = Course(course_id,course_name)
                listcourse.append(c)

    elif action == 4:
            if len(listcourse) == 0:
                print("\n 0 course found")
            else:      
                print(f"\nCOURSES LIST:")
                print(f"ID\t Name")       
                for i in listcourse:
                    i.show_course()

    elif action ==5:
            for i in listcourse:
                i.show_course()
            no=int(input("Choose course to add mark: "))
            for i in range(0,len(liststudent)):
              student_mark=int(input("Input mark for student number "+str(i+1)+":"))
              marks.append(student_mark)

    elif action ==6:        
            for i in listcourse:
                i.show_course()
            no=int(input("Choose course to view mark: "))    
            print("ID\tName\tDOB\tMark\t")
            for i in range(0, len(marks)):
             print(f"{liststudent[i].student_id}\t{liststudent[i].student_name}\t{liststudent[i].student_dob}\t{marks[i]}") 
            
    elif action == 7:
            break           
    else:
         print("\nYou must input digits!")
          