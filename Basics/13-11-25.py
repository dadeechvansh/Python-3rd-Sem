class employee:
    def __init__(self,eid, name, sal):
        self.eid=eid
        self.name=name
        self.sal=sal

def setsal(self, sal):
    if sal>10000:
        self.__sal=sal
    else:
        self.__sal=None

def Printdetails(self):
    print(f"Eid:{self.__eid} Name:{self.__name} salary:{self.__sal}")

# ob1=employee()
# print(ob1.eid,ob1.name,ob1.sal)
# ob1.eid=101
# ob1.name="King"
# ob1.sal=5000
# print(ob1.eid,ob1.name,ob1.sal)

#14-11-25

class Matrix:
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.mat=[]
    def createmat(self):
    
        for i in range(self.row):
            data=[]
        for j in range(self.col):
            num=int(input("Enter Number: "))
            data.append(num)
        self.mat.append(data)
        
        
    def add(self,mat):
        for i in range(self.row):
            for j in range(self.col):
                print(self.mat[i][j]+mat[i][j],end=" ")
            print()
    def sub(self,mat):
        for i in range(self.row):
            for j in range(self.col):
                print(self.mat[i][j]-mat[i][j],end=" ")
            print()
        