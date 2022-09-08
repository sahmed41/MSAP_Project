from  datetime import *
from random import *

def getStudentInformation(studentTitles):
    studentInformation = ["", "", "", ""]
    #Getting student information
    for i, v in enumerate(studentInformation):
        if studentTitles[i] == "Year of birth":
            while not (studentInformation[1].isdecimal()):
                print("Your year of birth should be a number. It can not be text or mixture text and number and it should not contain spaces")
                studentInformation[1] = input("Please, enter your birth year: ")
                studentInformation[i] = studentInformation[i].replace(" ","")
                print()
        elif studentTitles[i] == "Class":
            while not (studentInformation[i].isdecimal()):
                print("Enter your class information as a number. For example if you are in 'grade 5' you should enter '5'.")
                studentInformation[i] = input("Please enter your clase: ")
                studentInformation[i] = studentInformation[i].replace(" ","")
                if studentInformation[i].isdecimal():
                    while (int(studentInformation[i]) < 1) or (int(studentInformation[i]) > 13):
                        print()
                        print("Your class should be between 1 and 13.")
                        studentInformation[i] = input("Please enter your clase: ")
                        studentInformation[i] = studentInformation[i].replace(" ","")
                        if not (studentInformation[i].isdecimal()):
                            break
                print()
        else:
            while studentInformation[i] == "":
                studentInformation[i] = input("Please enter your " + studentTitles[i].lower() + ": ")
                print()


    # Giving student option to alter infromation if they are wrong
    userInfoEditChoice = 100
    while userInfoEditChoice != 0:
        studentInformation[3] = "Grade " + studentInformation[3]  # Adding the word grade in front of the student class
        printStudentInformation(studentInformation, studentTitles)  # Printing student information for correction

        try: #The purpose of this try block is to prevent people from entering non number values
            userInfoEditChoice = int(input("""\nIf what you have entered is not correct, please follow the instructions.
            Enter 1 to change your name
            Enter 2 to change your year of birth
            Enter 3 to change your gender
            Enter 4 to change your class,
            but if the information about is correct, enter 0 and if you press 0 your information will be finalized: """))
        except ValueError:
            userInfoEditChoice = 100
        print()

        if userInfoEditChoice == 1:
            studentInformation[0] = ""
            while studentInformation[0] == "":
                print("You should enter a value otherwise you will not be able to progress to your test")
                studentInformation[0] = input("Please, enter your name: ")
                print()
        elif userInfoEditChoice == 2:
            studentInformation[1] = ""
            while not (studentInformation[1].isdecimal()):
                print("Your year of birth should be a number. It can not be text or mixture text and number and it should not contain spaces")
                studentInformation[1] = input("Please, enter your birth year: ")
                studentInformation[1] = studentInformation[1].replace(" ", "")
                print()
        elif userInfoEditChoice == 3:
            studentInformation[2] = ""
            while studentInformation[2] == "":
                print("You should enter a value otherwise you will not be able to progress to your test")
                studentInformation[2] = input("Please, enter your year gender: ")
        elif userInfoEditChoice == 4:
            studentInformation[3] = ""
            while not (studentInformation[3].isdecimal()):
                print("Enter your class information as a number. For example if you are in 'grade 5' you should enter '5'.")
                studentInformation[3] = input("Please enter your clase: ")
                studentInformation[3] = studentInformation[3].replace(" ", "")
                if studentInformation[3].isdecimal():
                    while (int(studentInformation[3]) < 1) or (int(studentInformation[3]) > 13):
                        print("Your class should be between 1 and 13.")
                        studentInformation[3] = input("Please enter your clase: ")
                        studentInformation[3] = studentInformation[3].replace(" ", "")
                        if not (studentInformation[3].isdecimal()):
                            break
                print()
        elif userInfoEditChoice == 0:
            break
        else:
            print("Please enter a correct value as per the instructions.")

        studentInformation[3] = studentInformation[3].replace("Grade","").strip() # Removing the word grade from class infor so the word grade won't repeated in the next iteration

    return studentInformation

def printStudentInformation(studentInformation, studentTitles):
    print()
    for i,v in enumerate(studentInformation):
        print(studentTitles[i] + ":", v)


def getAge(yearOfBirth):
    currentYeat = datetime.now().year
    age = currentYeat - int(yearOfBirth)
    return age

def ageCheck(age):
    if age >= 9 and age <= 12:
        return True
    else:
        False

def getQuestions(fileName):
    questionFile = open(fileName, 'r')
    questions = []

    for line in questionFile:
        question = line.split('**')
        question[2] = question[2].replace(',\n', "").strip()
        questions.append(question)

    questionFile.close()
    
    return  questions

def generateAnswerChoices(questions):
    answers = []

    for question in questions:
        answer = [int(question[2])]
        for i in range(3):
            answerI = randint(int(question[2]) - 10, int(question[2]) + 10)
            while answerI in answer:
                answerI = randint(int(question[2]) - 10, int(question[2]) + 10)
            answer.append(answerI)
        shuffle(answer)
        answers.append(answer)
        
    return answers

def exam(questions, answers):
    userAnswers = []
    for index, question in enumerate(questions):
        print(question[0] + ')', question[1])
        print()
        for i, ans in enumerate(answers[index]):
            print(str(i + 1) + ")", ans)
        answer = input("Please enter the number of the correct answer: ")
        while (answer != '1') and (answer != '2') and (answer != '3') and (answer != '4'):
            answer = input("Please enter the number of the correct answer: ")
        userAnswers.append(answers[index][int(answer) - 1])
    return userAnswers

def evaluateUserAnswers(questions, userAnswers):
    marks = 0
    correctQuestions = []
    wrongQuestions = []

    for qn, question in enumerate(questions):
        if int(question[2]) == userAnswers[qn]:
            marks += 10
            correctQuestions.append(question[0])
        else:
            wrongQuestions.append(question[0])

    return [marks, correctQuestions, wrongQuestions]

def grade(marks):
    if marks < 50:
        return "Fail"
    elif marks < 70:
        return "Pass"
    elif marks < 90:
        return "Merit"
    else:
        return "Distinction"


def displayStudentInformation(studentInformation):
    print("Student Information")
    print("-" * 19)
    print("Name:", studentInformation[0])
    print("Age:", getAge(studentInformation[1]))
    print("Gender:", studentInformation[2])
    print("Class:", studentInformation[3])
    print()

def displayExamResult(examName, studentPerformance):
    print(examName)
    print("-" * len(examName))
    print("Number of right answers:", len(studentPerformance[1]))
    print("Number of wrong answers:", len(studentPerformance[2]))
    print("Marks:",studentPerformance[0])
    if studentPerformance[0] < 50:
        print("Reslut:","Fail")
    else:
        print("Result:","Pass")
    print("Grade:", grade(studentPerformance[0]))
    print("The questions you have answered wrong: ", end='')
    if len(studentPerformance[2]) != 0:
        for qn in studentPerformance[2]:
            if qn == studentPerformance[2][-1]:
                print(qn)
            else:
                print(qn, end=', ')
    else:
        print("None")

def displayTotalResult(NSTStudentPerformance, PSTStudentPerformance):
    print("Overall Results")
    print("-" * 15)
    totalMarks = (NSTStudentPerformance[0] + PSTStudentPerformance[0]) / 2

    if PSTStudentPerformance[0] < 50:
        print("You have to pass both tests to pass this exam but you have only passed one exam. We are sorry to inform you that you have failedd this exam.")
    else:
        print("Total Marks:", totalMarks)
        print("Grade:", grade(totalMarks))
        if totalMarks < 50:
            print("We are sorry to inform you that you have failed the exam.")
        else:
            print("Congratulations, you have passed the exam.")

def writeReport(studentInformation, NSTStudentPerformance, PSTStudentPerfromance):
    date = datetime.now() # Calculating exam date
    date = date.strftime("%Y") + '-' + date.strftime("%B") + '-' + date.strftime('%d') # Adding the date a format
    overallMarks = 0

    # Writing student information to report
    studentReport = open("Student Reports\\" + studentInformation[0] + " " + date, 'w')
    studentReport.write("Name: " + studentInformation[0])
    studentReport.write("\nAge: " + str(getAge(studentInformation[1])))
    studentReport.write("\nGender: " + studentInformation[2])
    studentReport.write("\nClass: " + studentInformation[3])
    studentReport.write("\nTest date: " + date)
    studentReport.write("\n")

    # Writing NST exam information to report
    studentReport.write("\nNST Exam")
    studentReport.write("\n--------")
    studentReport.write("\nNumber of right answers: " + str(len(NSTStudentPerformance[1])))
    studentReport.write("\nNumber of wrong answers: " + str(len(NSTStudentPerformance[2])))
    studentReport.write("\nMarks: " + str(NSTStudentPerformance[0]))
    if grade(NSTStudentPerformance[0]) == "Fail":
        studentReport.write("\nResult: Fail" )
    else:
        studentReport.write("\nResult: Pass")
    studentReport.write("\nGrade: " + grade(NSTStudentPerformance[0]))
    studentReport.write("\n")

    # Writing PST exam information to report
    studentReport.write("\nPST Exam")
    studentReport.write("\n--------")
    if PSTStudentPerfromance == []:
        studentReport.write("\nThe student did not pass the previous exam to progress to this one ")
        overallMarks = NSTStudentPerformance[0] / 2  # Calculating overall marks if the student can not progress to PST exam
        studentReport.write("\n")
    else:
        overallMarks = (NSTStudentPerformance[0] + PSTStudentPerfromance[0]) / 2  # Calculating overall marks if the student did progress to PST exam
        studentReport.write("\nNumber of right answers: " + str(len(PSTStudentPerfromance[1])))
        studentReport.write("\nNumber of wrong answers: " + str(len(PSTStudentPerfromance[2])))
        studentReport.write("\nMarks: " + str(PSTStudentPerfromance[0]))
        if grade(PSTStudentPerfromance[0]) == "Fail":
            studentReport.write("\nResult: Fail" )
        else:
            studentReport.write("\nResult: Pass")
        studentReport.write("\nGrade: " + grade(PSTStudentPerfromance[0]))
        studentReport.write("\n")

    # Calculating and writing overall exam information to report
    studentReport.write("\nOverall Results")
    studentReport.write("\n-------------")
    if PSTStudentPerfromance[0] < 50:
        studentReport.write("The student have to pass both tests to pass this exam but he or she have only passed one exam. We are sorry to inform you that the student have failedd this exam.")
    else:
        studentReport.write("\nMarks: " + str(overallMarks))
        if grade(overallMarks) == "Fail":
            studentReport.write("\nResult: Fail" )
        else:
            studentReport.write("\nResult: Pass" )
        studentReport.write("\nGrade: " + grade(overallMarks))

    studentReport.close()