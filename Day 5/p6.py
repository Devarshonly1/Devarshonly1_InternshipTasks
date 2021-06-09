class cal5:
    l=0
    w=0

    def __init__(self,l,w):
        self.l=l
        self.w=w
    
    def calarea(self):
        self.a= self.l * self.w
    
    def display(self):
        print("The area of the Rectangle is : " , self.a)

call=cal5(20,45)
call.calarea()
call.display()
