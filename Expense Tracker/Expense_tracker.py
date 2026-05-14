# Expenses tracker project

print("Welcome to expense tracker !")
expensesList=[]   # List of expenses in form of dictionary

while True:
    print("====MENU====")
    print("If you want to Add Expense then press 1 .")
    print("If you want to view then press 2 .")
    print("If you want to view Total Expenseve (Kharcha) then press 3 .")
    print("If you want to exit from this project/setup then press 4 .")
    choice=int(input("Please enter your choice : "))

    # 1. Add expense 
    if(choice==1):
        date=input("On what date did you spend the money? (DD/MM/YY) : ")
        category=input("What type of expenditure did you make? (Food, Travle, Makeup, Stationary ,etc.) : ")
        description=input("More information about what type of expense was made : ")
        amount=float(input("How much money was spent? (Kitna rupess kharch kiya) : "))

        expense={
            "date": date ,
            "category": category ,
            "description": description ,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n Expense is added sucessfully .")

    # 2. View all Expense
    elif(choice==2):
        if(len(expensesList)==0):
            print("No Expense Added .")
        else:
            print("====This is your total expense====")
            count=1
            for each_expense in expensesList:
                print(f"Expense number {count} | {each_expense['date']} | {each_expense['category']} | {each_expense['description']}")
                count+=1

    # 3. view total spending
    elif(choice==3):
        total=0
        for each_expense in expensesList:
            total = total + each_expense["amount"]
        print("\n TOTAL EXPENSES = ", total)

    # 4 Exit
    elif(choice==4):
        print("Thank you for using our system.")
        break

    else:
        print("Invalid Choiuce . Try Again !")