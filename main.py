from functions import *

print(75*"#")
print("#" + 31*" " + "Welcome To" + 32*" " + "#")
print("#" + 22*" " + "St Mary’s Heart Primary School" + 21*" " + "#")
print("#" + 22*" " + "Math Skills Assessemt Program" + 22*" " + "#")
print(75*"#")

# Getting student information
print("You should type your relevant information in the following steps otherwise, you will not be able to progress if you press enter without typing anything.\n")
studentTitles = ["Name", "Year of birth", "Gender", "Class"]
studentInformation = []
studentInformation = getStudentInformation(studentTitles)  # Commented for testing it should be uncommented for final version
#studentInformation = ["Ahmed", 2020, "Male", 5] # This line is only for testing and will be removed in the final version


# nst Exam
nstQuestions = getQuestions("nstQuestions")  # Generation nst questions
nstAnswers = generateAnswerChoices(nstQuestions)  # Generating nst answer choices
nstUserAnswers = []  # nst Exam answers will be stored here
nstStudentPerformance = []  # nst exam student Marks, correct and wrong questions numbers goes her

# pst Exam
pstQuestions = getQuestions("pstQuestions")  # Generating pst Questions
pstAnswers = generateAnswerChoices(pstQuestions)  # Generate pst Answer choices
pstUserAnswers = [0, [], []]  # pst Exam answers will be stored here
pstStudentPerformance = [0, [], []]  # pst exam student Marks, correct and wrong questions numbers goes her


# Checking the age of the student to evaluate exam eligibility.
if ageCheck(getAge(studentInformation[1])):
    print("You are in the eligible age category to take the exam.")
    userDecision = input("Press any key if you wish to take the exam and enter 0 if not: ")

    if userDecision == '0':
        exit()

else:
    print("Sorry, you are not in the age category to take the exam. You should be between the ages 9 to 12.")
    input("Please press any key to exit the program.")
    exit()

# Executing nst exam
nstUserAnswers = exam(nstQuestions,nstAnswers)  # Collecting user answers from nst exam
nstStudentPerformance = evaluateUserAnswers(nstQuestions,nstUserAnswers)  # Marking user nst question answers


if nstStudentPerformance[0] < 50:
    displayStudentInformation(studentInformation)
    displayExamResult("nst Exam", nstStudentPerformance)
    writeReport(studentInformation, nstStudentPerformance, pstStudentPerformance)
    print()
    print("You did not get enough marks to progress to the next test.")
    input("Please, enter any key to exit: ")
    exit()


# Executing pst exam
pstUserAnswers = exam(pstQuestions, pstAnswers)  # Collecting user answer from pst exam
pstStudentPerformance = evaluateUserAnswers(pstQuestions, pstUserAnswers)  # Marking user pst question answers

# Displaying results to student
displayStudentInformation(studentInformation)
displayExamResult("nst Exam", nstStudentPerformance)
displayExamResult("pst Exam", pstStudentPerformance)
displayTotalResult(nstStudentPerformance, pstStudentPerformance)
writeReport(studentInformation, nstStudentPerformance, pstStudentPerformance)





