from calculator import Calculator

#myCalcV2 = Calculator(2,9)

#print(myCalcV2.get_prod())

class SciCalc(Calculator):
    def get_exp(self):
        return self.a**self.b

mySciCalc = SciCalc(a=2,b=4)
print(mySciCalc.get_exp())