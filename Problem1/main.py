class Calculator:
    def __init__(self):
        self.operators = {
            "+" : self.add,
            "-" : self.sub,
            "*" : self.mul,
            "/" : self.div
        }

    def add(self, a, b):
        return a+b
    
    def sub(self, a, b):
        return a-b
    
    def mul(self, a, b):
        return a*b
    
    def div(self, a, b):
        if b==0:
            raise ValueError("Division by 0")
        return a/b
    
    def cal(self, a, b, op):
        return self.operators[op](a, b)
    
def takeInput():
    while True:
        try:
            val = float(input("Enter the value:"))
            return val
        except ValueError:
            print("Please eneter a valid number!")

def takeOperatorInput():
    operators = ("*", "+", "-", "/")
    while True:
        op = input("Enter the operator:")
        if op in operators:
            return op
            
        print("Please enter a valid operator")

a = takeInput()
b = takeInput()
op = takeOperatorInput()

calculator = Calculator()
print("result: ")
print(calculator.cal(a, b, op))