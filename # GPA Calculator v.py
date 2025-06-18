# GPA Calculator v.1

def main():
    print("* * * GPA CALCULATOR * * *")
    print("Select the method you want.")
    print("0: Exit the application.")
    print("1: Calculate GPA by:\n\t -Entering number of classes you took\n\t -Entering Credits worth per class\n-Entering grade per class")
    print("2: Calculate GPA by:\n\t-Entering the number of semesters you have taken \n\t-Entering the amount of credits per each semester \n\t-Entering the GPA per semester")
    print("3: Enter your current GPA \nEnter your desired GPA\nIn order to calculate: \n\t-The amount of credits you need to take\n\t-The gpa you need for the new credits \n\t-In order to achieve a desired GPA")
    
    option = valid_option()
    options(option)


def valid_option():
    option = int(input("Enter your choice: "))
    while option != 0 and option != 1 and option != 2 and option != 3:
        print("Invalid input. Please enter 0, 1, 2, or 3.")
        print("The options Are: ")
        print("0: Exit the application.")
        print("1: Calculate GPA by:\n\t -Entering number of classes you took\n\t -Entering Credits worth per class\n-Entering grade per class")
        print("2: Calculate GPA by:\n\t -Entering the number of semesters you have taken \n\t -Entering the amount of credits per each semester \n\t-Entering the GPA per semester")
        print("3: Enter your current GPA \nEnter your desired GPA\nIn order to calculate: \n\t-The amount of credits you need to take\n\t-The gpa you need for the new credits \n\t-In order to achieve a desired GPA")

        option = int(input("Enter your choice: "))
    return option

def options(option):
    if option == 0:
        calculatorGPAmethod0()
    elif option == 1:
        calculatorGPAmethod1()
    elif option == 2:
        calculatorGPAmethod2()
    elif option == 3:
        calculatorGPAmethod3()

def calculatorGPAmethod0():
    print("Exiting the application...\n👋")
    exit()

def calculatorGPAmethod1():
    total_gradepts = 0
    total_credits = 0
    print("Note, please do not enter classes with a W or a withdrawl.")
    classes = int(input("Enter the number of classes you completed: "))
    for i in range(1, classes + 1):
        suffix = "st" if i == 1 else "nd" if i == 2 else "rd" if i == 3 else "th"
        credits = int(input(f"Enter the credit count of your {i}{suffix} class: "))
        grade = input(f"Enter the grade you recieved for your {i}{suffix} class.\nOptions are A, B, C, D, or F.\nEnter: ")

        if grade.upper() == 'A' or grade.lower() == 'a':
            gradenum = 4
        elif grade.upper() == 'B' or grade.lower() == 'b':
            gradenum = 3
        elif grade.upper() == 'C' or grade.lower() == 'c':
            gradenum = 2
        elif grade.upper() == 'D' or grade.lower() == 'd':
            gradenum = 1
        elif grade.upper() == 'F' or grade.lower() == 'f':
            gradenum = 0
        else:
            print("Invalid input. Please enter A, B, C, D, or F.")
            return

        total_gradepts += credits * gradenum
        total_credits += credits
    if total_credits <= 0:
        print("No credits entered. Cannot calculate GPA.")
    else:
        gpa = total_gradepts / total_credits
        print(f"Your GPA is {gpa:2f}.")
    exitorredo()


def calculatorGPAmethod2():
    total_gpapoints = 0
    total_credits = 0
    total_gpasemester = 0
    total_GPA = 0
    print("Note, please do not enter classes with a W or a withdrawl.")
    semesters = int(input("Enter the number of semesters you completed: "))
    for i in range(1, semesters + 1):
        suffix = "st" if i == 1 else "nd" if i == 2 else "rd" if i == 3 else "th"
        credits = float(input(f"Enter the credit count of your {i}{suffix} semester: "))
        gpapersemester = float(input("Enter the GPA you recieved for your semester: "))

        total_credits += credits
        total_gpasemester += credits * gpapersemester
        total_GPA =  total_gpasemester / total_credits
    if total_GPA <= 0:
        print("No credits entered. Cannot calculate GPA.")
    else:
        print(f"Your GPA is {total_GPA:.2f}")
    exitorredo()


def calculatorGPAmethod3():
    currentGPA = float(input("What is your current GPA?\nThe GPA must be between 0.0 and 4.0.\nEnter: "))
    while currentGPA > 4.0 or currentGPA < 0.0:
        print("Invalid input. Please enter a value between 0.0 and 4.0.")
        currentGPA = input("Enter: ")
    currentcredits = float(input("How many credits do you have completed?\nEnter: "))
    desiredGPA = float(input("What is your desired GPA?\nThe GPA must be between 0.0 and 4.0.\nEnter: "))
    while desiredGPA > 4.0 or desiredGPA < 0.0:
        print("Invalid input. Please enter a value between 0.0 and 4.0.")
        desiredGPA = input("Enter: ")
    if desiredGPA == currentGPA:
        print("You have completed your goal of desired GPA.")
        choice1 = int(input("If you desire to maintain this GPA and need further assistance, press 0. Otherwise, press any other button: "))
        if choice1 == 0:
            plannedcredits = float(input("How many credits do you plan on taking?"))
            while plannedcredits == 0:
                print("Invalid. You must enter a value greater than 0.")
            print(f"You must achieve a minimum GPA of at least {currentGPA} for the next {plannedcredits} credits.")
        else:
            print("You have completed your goal GPA.")
    elif desiredGPA > currentGPA:
        requiredcredits = float((currentcredits * desiredGPA - currentGPA * currentcredits) / (4.00 - desiredGPA))
        print(f"If you choose to get all maximum grades of A, or GPA points of 4.00 on all your next credits, the amount of credits you hae to take is: \n{requiredcredits} credits.")
        lowerGPA = float(input("If you plan or believe that you are incapable of doing this, please enter the GPA average that you plan on getting for your future credits. Note that this value must be greater than your desired GPA.\nEnter: "))
        while lowerGPA <= desiredGPA:
            print("You have not inputted a GPA that can raise your score to the desired GPA. Please try again.")
            lowerGPA = float(input("Planned GPA Average for your upcoming credits: "))
        creditstotake = float((currentcredits * desiredGPA - currentGPA * currentcredits) / (lowerGPA - desiredGPA))
        print(f"You must take: \n{creditstotake:.2f} number of credits with your expected GPA of: \n{lowerGPA}.")
    else:
        print("You say that your goal GPA is too high...\nUp to you then.")

    exitorredo()


def exitorredo():
    print("Enter 0 to exit. Press any other key to return to main menu.")
    option = int(input("Enter: "))
    if option == 0:
        print("You have exited the application.")
    else:
        main()

main()