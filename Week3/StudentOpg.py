import random

class Course():
    def __init__(self, name, classroom, teacher, ECTS, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade

class Datasheet():
    def __init__(self, courses=[]):
        self.courses = courses


    def getGradesAsList(self):
        result = []
        for course in self.courses:
            if course.grade != None:
                result.append(course.grade)
        return result

class Student():
    def __init__(self, name, gender, datasheet, image_url):
        """A chapter consists of multiple paragraphs."""
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.image_url = image_url

    def getAvgGrade(self):
        avg = 0
        grades = self.datasheet.getGradesAsList()
        for grade in grades:
            if(grade != ""):
                avg += (grade / len(grades))
        return avg

c1 = Course("English", "104", "Thomas", "1,5", 9)
c2 = Course("Programming", "105", "Hans", "1,3", 8)
c3 = Course("Java", "100", "Tine", "1,1", 10)

d1CourseList = [c1, c2, c3]

d1 = Datasheet(d1CourseList)

s1 = Student("Aske", "Male", d1, "sdjoasd")

print(54)
print(s1.getAvgGrade())

## Opgave 7
def randomStudentFunc():
    names = ["John", "Henry", "James", "Tina", "Britney", "Lucas", "Sarah", "Iben", "Helena"]
    genders = ["Male", "Female", "3. gender"]
    cNames = ["English", "Danish", "History", "Bio", "Kemi"]
    grade = [-3, 0, 2, 4, 7, 10, 12]
    cList = []
    numbers= [0, 1]
    for n in numbers:
        course1 = Course(random.choice(cNames),random.randrange(100),random.choice(names),random.randrange(5,20),random.choice(grade))
        cList.append(course1) 
    mystu = Student(random.choice(names), random.choice(genders),cList, "jasbdjkasbd")
    return(mystu)

listOfStudents = []

def randomNumberOfStudents():
    aNumber = random.randrange(5,10)
    i = 0
    for i in range(aNumber):
        listOfStudents.append(randomStudentFunc())
    return listOfStudents

csvList = list(randomNumberOfStudents())
print(listOfStudents[0].datasheet)
import csv
with open("student1.csv", "w",) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["stud_name", "course_name", "teacher", "ects", "classroom", "grade", "img_url"])
    for s in listOfStudents:
            writer.writerow([s.name, s.datasheet[0].name, s.datasheet[0].teacher, s.datasheet[0].ECTS, s.datasheet[0].classroom, s.datasheet[0].grade, s.image_url])

#Read student data into a list of Students from a csv file:

returnListOfStudents = []
def read_file():
    with open("student.csv",'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for s in csv_reader:    
            c = Course(s[2],s[3],s[4],s[5],s[6])
            sheet = [c]
            a = Student(s[0], s[1], sheet, s[7])   
            print(a.name + " " + a.image_url + " ")
            
            returnListOfStudents.append(a)
            
            print(a.getAvgGrade())
        return returnListOfStudents

def sortedAvgList(myList):
    return sorted(myList)

def barChart(students):
    names = [student.name.split(" ")[0] for student in students]
    grades = [student.get_avg_grade() for student in students]
    plt.bar(names,grades, width=0.2, align='center')
    plt.title("Student Grades", fontsize=12)
    plt.xlabel("Names", fontsize=8)
    plt.ylabel("Avg Grades", fontsize=8)
    plt.show()

read_file()
