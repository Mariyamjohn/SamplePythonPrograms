import math

class Inputs:

    def getInput(self):
        while ValueError:
            try:
                number = float(input("Enter number:\t"))
                return number
            except ValueError:
                print("Enter a valid number")

    def getoperator(self):
        op = input(
            " Enter the operator: '+' '-' '*' '/' "
            "\n Enter C for Clear "
            "\n Enter ^ for power of a number \n Enter E to Exit the program:\t")
        return op

class Functions:

    def add(self, num1, num2):
        s = num1 + num2
        return s

    def sub(self, num1, num2):
        diff = num1 - num2
        return diff

    def mul(self, num1, num2):
        prod = num1 * num2
        return prod

    def div(self, num1, num2):
        quot = num1 / num2
        return quot

    def powerOf(self, num1, num2):
        power = pow(num1, num2)
        return power

    def checkexit(self):
        cfe = True
        while (cfe == True):
            checkForExit = input("Are you sure you want to exit the program?? \nEnter Y for Yes and N for No\t")
            if (checkForExit.upper() == "Y"):
                cfe = False
                return 'E'
            elif (checkForExit.upper() == "N"):
                cfe = False
                return 'Y'
            else:
                print("Enter a valid input")


class Calculator(Inputs, Functions):
    def __init__(self):
        print("Basic Calculator")

    def calculate(self):
        ipt = 'Y'
        inputarray1 = []
        number = self.getInput()
        inputarray1.append(number)
        print(inputarray1[0])
        while ipt.upper() != "E":
            operator = self.getoperator()
            if operator == '+':
                number = self.getInput()
                inputarray1.append(number)
                inputarray1[0] = self.add(inputarray1[0], inputarray1[1])
                del inputarray1[1]
                print("The result is: ", inputarray1[0])
            elif operator == '-':
                number = self.getInput()
                inputarray1.append(number)
                inputarray1[0] = self.sub(inputarray1[0], inputarray1[1])
                del inputarray1[1]
                print("The result is: ", inputarray1[0])
            elif operator == '*':
                number = self.getInput()
                inputarray1.append(number)
                inputarray1[0] = self.mul(inputarray1[0], inputarray1[1])
                del inputarray1[1]
                print("The result is: ", inputarray1[0])
            elif operator == '/':
                number = self.getInput()
                while number == 0:
                    print("Division by Zero is not valid. Enter another number: ")
                    number = self.getInput()
                inputarray1.append(number)
                inputarray1[0] = self.div(inputarray1[0], inputarray1[1])
                del inputarray1[1]
                print("The result is: ", inputarray1[0])
            elif operator == '^':
                print("To the power of? ")
                number = self.getInput()
                inputarray1[0] = pow(inputarray1[0], number)
                print("The result is: ", inputarray1[0])
            elif operator.upper() == 'C':
                del inputarray1[0]
                print("Cleared")
                number = self.getInput()
                inputarray1.append(number)
            elif operator.upper() == 'E':
                ipt = self.checkexit()
            else:
                print("Enter a valid operator")

c = Calculator()
c.calculate()






