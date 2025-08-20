class student:                          
    def __init__(self,name,hodname,college):
        self.name=name
        self.hodname=hodname
        self.college=college
    def getdata(self):
        self.name=input('enter the student name')

class hod(student):
    def data1(self):                                                     
        self.hodname=input('enter the hodname')
    def putdata(self):
        self.college=input('enter college')
    def display(self):
        print('student name is',self.name)
        print('your hod name is',self.hodname)
        print('college name',self.college)  
obj=hod("","","")
obj.getdata()
obj.data1()
obj.putdata()
obj.display()








# class student:
#     def __init__(self,name,hodname,college,teacher):
#         self.name=name
#         self.hodname=hodname
#         self.college=college
#         self.teacher=teacher
#     def getdata(self):
#         self.name=input('enter the student name')

# class hod(student):
#     def data1(self):
#         self.hodname=input('enter the hodname')
#     def putdata(self):
#         self.college=input('enter college')
# class chm(hod):
#     def ptdata(self):
#         self.teacher=input('enter teacher name')
#     def display(self):
#         print('student name is',self.name)
#         print('your hod nameis',self.hodname)
#         print('college name',self.college)
#         print('teacher name is',self.teacher)
# obj=chm("","","","")
# obj.getdata()
# obj.data1()
# obj.putdata()
# obj.ptdata()
# obj.display()