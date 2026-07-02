#my code - 
class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    def Input(self):
        self.num1 = int(input("Enter No 1 ::"))
        self.num2 = int(input("Enter No 2 ::"))
    def ADD(self):
        print(f"Addition of number {self.num1} and {self.num2} is {self.num1 + self.num2} ")
    def SUB(self):
        print(f"Substarction of number {self.num1} and {self.num2} is {self.num1 - self.num2} ")
    def MUL(self):
        print(f"Multiplication of number {self.num1} and {self.num2} is {self.num1 * self.num2} ")
    def DIV(self):
        print(f"Division of number {self.num1} and {self.num2} is {self.num1 / self.num2} ")

#driver code
obj = Calculator()
# print("*****************WELCOME TO CALCULATOR*****************")
# print("\n1.Addition \n2.Subtract \n3.Multiplication \n4.Division \n5.Exit")
# n = int(input("Enter Your Choice :: ")) #choice
# if (n == 1):
#     obj.Input()
#     obj.ADD()
# elif (n == 2):
#     obj.Input()
#     obj.SUB()
# elif (n == 3):
#     obj.Input()
#     obj.MUL()
# elif (n == 4):
#     obj.Input()
#     obj.DIV()
# elif (n == 5):
#     print("Bye")
# else :
#     print("Wrong Choice")

# How the loop works
# while True:
# True means the loop will run forever.

# When the user chooses 5:

# break
# break immediately exits the loop.
# After break, the program ends.
# Program Flow
# Start
#    │
#    ▼
# Show Menu
#    │
#    ▼
# User Choice
#    │
#    ├── 1 → Input → Add → Back to Menu
#    ├── 2 → Input → Subtract → Back to Menu
#    ├── 3 → Input → Multiply → Back to Menu
#    ├── 4 → Input → Divide → Back to Menu
#    ├── 5 → break → Exit
#    └── Invalid → Error Message → Back to Menu
# One improvement (Interview Perspective)

# Instead of writing obj.Input() four times, you can call it only once for operations that need input:

while True:
    print("\n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit")
    choice = int(input("Enter Choice :: "))

    if choice == 5:
        print("Bye!")
        break

    if choice in [1, 2, 3, 4]:
        obj.Input()

        if choice == 1:
            obj.ADD()
        elif choice == 2:
            obj.SUB()
        elif choice == 3:
            obj.MUL()
        elif choice == 4:
            obj.DIV()
    else:
        print("Invalid Choice")    


        