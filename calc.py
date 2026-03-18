print ("This is a Python simple calculator project\n=======================================")

def _FinalOutputMsgMaker(f_opr):
    if f_opr == 1:
        return "Enter any key to get the sum of these two numbers: "
    elif f_opr == 2:
        return "Enter any key to get the sub of these two numbers: "
    elif f_opr == 3:
        return "Enter any key to get the multiplication of these two numbers: "
    elif f_opr == 4:
        return "Enter any key to get the division of these two numbers: "
    elif f_opr == 5:
        return "Enter any key to get the percentage of these two numbers: "
    else:
        return "Valid Operator."
    
def _mainCalculatorMachineMethod(F_num , S_num , op):
    if not(F_num and S_num and (len(str(F_num)) > 0 and len(str(S_num)) > 0)):
        return "The numbers are not valid."
    else:
        if op == 1:
            return "The sum of",F_num," and ",S_num," is : ",(F_num + S_num)
        elif op == 2:
            return "The sub of",F_num," and ",S_num," is : ",(F_num - S_num)
        elif op == 3:
            return "The multiplication of",F_num," and ",S_num," is : ",(F_num * S_num)
        elif op == 4:
            return "The devision of",F_num," and ",S_num," is : ",(F_num / S_num)
        elif op == 5:
            return "The precentage value of",F_num," and ",S_num," is : ",(F_num % S_num)
        else:
            return "Something went wrong."

# main code starts from here
print("Your first no : ")
firstNum = int(input(""))

if not(firstNum and len(str(firstNum)) > 0):
    print("The firstNum is not valid , Please try again the whole program")
    exit()

print("Your Second no : ")
secondNum = int(input(""))

if not(secondNum and len(str(secondNum)) > 0):
    print("The SecondNum is not valid , Please try again the whole program")
    exit()

#Getting the operator from the user
print("Choose an operator\n+ = 1\n- = 2\nx = 3\n/ = 4\n% = 5\nWARNING : Enter the number of the operator given")
opr = int(input("Enter the number of the operator : "))

finalInput = input(_FinalOutputMsgMaker(opr))

if not(len(str(finalInput))>0):
    print("I said to enter any random key from your keyboard then click enter.")
    exit()

print("======================================================\n",_mainCalculatorMachineMethod(firstNum , secondNum , opr))
