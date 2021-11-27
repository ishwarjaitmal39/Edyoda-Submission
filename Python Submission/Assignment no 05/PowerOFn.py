# Write a Python class to implement pow(x, n)

class Power:

    def __init__(self):
        self.x=int(input('Enter value of x\n'))
        self.n=int(input('Enter value of n\n'))

    def show_result( self ):
        print(f'the power of {self.x}^{self.n} is {pow(self.x,self.n)}')

p1=Power()
p1.show_result()
