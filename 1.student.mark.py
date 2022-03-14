print("STUDENT'S MARK MANAGEMENT")
 
def addStudent():
    print("*** ADD STUDENT ***")
    while (True):
     n=int(input("Input number of students:"))
     if (n>0) : break
    for i in range (0,n,1):
     print("Input student information number "+str(i+1))
     global listStudents
     infor = {
        'id' :'' ,
        'name' :'',
        'DOB':'',
        'marks': {}
     }
     print("ID:")
     id = input()
     while True:
        student = findStudent(id)
        if student != False:
            print("ID existed:")
            id = input()
        else:
            break
     infor['id'] = id
     print("Name:")
     infor['name'] = input()
     print("Date of birth:")
     infor['DOB'] = input()
     listStudents.append(infor)
 
def findStudent(id):
    global listStudents
    for i in range(0, len(listStudents)):
        if listStudents[i]['id'] == id:
            return [i, listStudents[i]]
    return False
 
def deleteStudent():   
    print("*** DELETE STUDENT ***")
    print("INPUT ID YOU WANT TO DELETE:")
    id = input()
    global listStudents
    student = findStudent(id)
    if student != False:
        listStudents.remove(student[1])
        print("DELETE SUCCESS")
    else :
        print("STUDENT IS NOT EXISTED")
 
def showStudents():
    print("*** LIST STUDENT ***")
    print("Number:\t""ID\t""Name\t""Date of birth\t")
    global listStudents
    for i in range(0, len(listStudents)):
        print((i+1),"\t",
        listStudents[i]['id'],"\t",
        listStudents[i]['name'],"\t",
        listStudents[i]['DOB'],"\t")

def editStudent():
    print("*** UPDATE  ***")
    global listStudents
    print("INPUT ID")
    id = input()
    student = findStudent(id)
    if student == False:
        print("ID NOT FOUND ", id)
    else :
        print("NEW NAME")
        name = input()
        print("NEW DOB:")
        DOB = input() 
        student[1]['name'] = name
        student[1]['DOB'] = DOB
        listStudents[student[0]] = student[1]
 
def addcourse():
    print("*** ADD course ***")
    while (True):
     n=int(input("Input number of courses:"))
     if (n>0) : break
    for i in range (0,n,1):
     print("Input course  number "+str(i+1))
     global listcourse
     courseinfor = {
        'courseid' : '',
        'coursename' : '',       
     }
     print("ID:")
     courseid = input()
     while True:
        course = findcourse(courseid)
        if course != False:
            print("ID existed:")
            courseid = input()
        else:
            break
     courseinfor['courseid'] = courseid
     print("Name:")
     courseinfor['coursename'] = input()
     listcourse.append(courseinfor)
 
def findcourse(courseid):
    global listcourse
    for i in range(0, len(listcourse)):
        if listcourse[i]['courseid'] == courseid:
            return [i, listcourse[i]]
    return False
 
def deletecourse():   
    print("*** DELETE course ***")
    print("INPUT ID YOU WANT TO DELETE:")
    courseid = input()
    global listcourse
    course = findcourse(courseid)
    if course != False:
        listcourse.remove(course[1])
        print("DELETE SUCCESS")
    else :
        print("COURSE IS NOT EXISTED")
 
def showcourse():
    print("*** LIST COURSE ***")
    print("Number:\t""ID\t""Name\t")
    global listcourse
    for i in range(0, len(listcourse)):
        print((i+1),"\t",
        listcourse[i]['courseid'],"\t",
        listcourse[i]['coursename'],"\t")

def editcourse():
    print("*** UPDATE  ***")
    global listcourse
    print("INPUT ID")
    courseid = input()
    course = findcourse(courseid)
    if course == False:
        print("ID NOT FOUND ", courseid)
    else :
        print("NEW NAME")
        coursename = input()
        course[1]['coursename'] = coursename
        listcourse[course[0]] = course[1]

def addmark():
    showcourse()
    print("Input course ID you want to add marks:")
    course_id=int(input())
    global listStudents
    for i in range(0, len(listStudents)):
        mark=int(input("Input mark for student number "+str(i+1)+":"))
        listStudents[i]['marks'][course_id] = mark

def showmark():
    showcourse()
    course_id=int(input("Input course ID you want to see marks: "))
    global listStudents
    print("Number:\t""ID\t""Name\t""DOB\t""Mark\t")
    for i in range(0, len(listStudents)):
       print((i+1),"\t",
       listStudents[i]['id'],"\t",
       listStudents[i]['name'],"\t",
       listStudents[i]['DOB'],"\t",
       listStudents[i]['marks'][course_id],"\t")
 
#main
listStudents = []
listcourse = []
action = 0
 
while action >= 0:
    if action == 1:
        addStudent()
    elif action == 2:
        deleteStudent()
    elif action == 3:
        editStudent()
    elif action == 4:
        showStudents()
    elif action == 5:
        addcourse()
    elif action == 6:
        deletecourse()
    elif action == 7:
        editcourse()
    elif action == 8:
        showcourse()
    elif action == 9:
        addmark()
    elif action == 10:
        showmark()        
 
    print("Select:")
    print("1: Add student \t\t\t\t 5: Add course\t\t\t 9: Add Marks for selected course")
    print("2: Delete student \t\t\t 6: Delete course\t\t 10:Show Marks for selected course")
    print("3: Update student \t\t\t 7: Update course\t\t 0: Exit")
    print("4: Display list student \t\t 8: Display list course")   
    action = int(input())
    if action == 0:
        break