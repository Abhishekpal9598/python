# class student:
#     def __init__(self,name):
#         self.name=name
        
# s1=student("abhi pal")
# print(s1.name)        
# # del s1.Name
# # print(s1.name)


# class person:
#     __name="abhi"
    
#     def __hello(self):
#         print("hello person")
        
#     def welcome(self):
#         self.__hello()
        
# p1=person()
# # print(p1.welcome())            

# class A:
#     varA="welcome to class A" 
    
# class B:
#     varB="welcome to class B"    

# class C(A,B):
#     varC="welcome to class C"
# C1 = C()

# print(C1.varA)
# print(C1.varB)
# print(C1.varC)


# class person:
#     name="anonymous"
#     @classmethod
#     def changeName(cls,name):
#         cls.name=name
        
# p1=person()
# p1.changeName("abhi")
# print(p1.name)
# print(person.name)  



class student:
    def __init__(self,phy,math,bio):
        self.phy=phy
        self.math=math
        self.bio=bio
        self.percentage=str((self.phy+self.math+self.bio)/3) + "%"      
    
stu1=student(98,94,93)
print(stu1.percentage)

print("abhi"+"pal")
print([1,3,2,4,]+[2,3,4,2])



































