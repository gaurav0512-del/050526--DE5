class Calculator:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
    
    def get_sum(self):
        return self.a + self.b
    
    def get_diff(self):
        return self.a - self.b
    
    def get_prod(self):
        return self.a * self.b
    
    def get_div(self):
        return self.a / self.b
    
    def get_sqrt(self):
        return self.a**0.5
    
    #Add the methods for subtraction, division and multiplication

if __name__ == "__main__":
    myCalc = Calculator(a=435)
    print(myCalc.get_sqrt())