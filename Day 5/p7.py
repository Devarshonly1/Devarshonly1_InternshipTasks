class cal6:

    def setdata(self):
        self.l=int(input("enter the length of the square : "))
    
    def area(self):
        self.a=  self.l **2
    
    def display(self):
        print("The area of the square is : " , self.a)

call=cal6()
call.setdata()
call.area()
call.display()
