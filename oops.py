### class type 

# class Student:
#     name="abhi pal"
#     roll =12
#     branch="it"
# S1=Student()
# print(S1.name) 
# print(S1.roll) 
# print(S1.branch)


# class Car:
#     color="blue"
#     model="m123"
    
# car1=Car()
# print(car1.color)
# print(car1.model)    
    

# ######### constructor

# class Student:
#     # def __init__(self):
#     #     pass
        
#     def __init__(self,name, marks):
#         self.name=name
#         self.marks=marks
        
#         print("adding new value.")
              
# s1=Student("pal ji",13)
# print(s1.name,s1.marks)
        
#     ####### class attribute


# class Staff:
#     name="mardana mam"
#     weight=98
#     sub="dsa"
# s1=Staff()    
# print(s1.name,s1.weight,s1.sub)   
    
    

# class Staff:
#     college_name="ddu"
#     name="pandit"
#     def __init__(self, name ,weight,sub):
#         self.name=name
#         self.weight=weight
#         self.sub=sub
        
# s1=Staff("abhi",45,"math")
# print(s1.name,s1.weight,s1.sub)    
# print(Staff.college_name)     


# ########## class & attributes

# class student:
#     def __init__(self,name,branch):
#         self.name=name
#         self.branch=branch
        
#     def welcome
# s1=student("avhi","cse")
# print(s1.name,s1.branch)



# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self .marks=marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your score is:",sum/3)
            
# s1=student("sunil",[23,43,24])
# s1.get_avg()          
   


# ####### static method


# class Student:
#     @staticmethod
#     def College():
#         print("ddu")
        
# class Car:
#     def __init__(self):
#         self.clutch=False
#         self.acc=False
#         self.brk=False
        
        
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car start")
            
# car1=Car()
# car1.start()

# class Account:
#     def __init__(self, bal, acc):
#         self.balance=bal
#         self.account=acc
#     ##debit method
#     def debit(self, amount):
#         self.balance-=amount
#         print("RS.",amount,"was debit")
#         print("total balance=",self.get_balance())
#     ## credit method
    
#     def credit(self, amount):
#         self.balance-=amount
#         print("RS.",amount,"was credit")
#         print("total balance=",self.get_balance())
        
#     def get_balance(self):
#         return self.balance
        
# acc1=Account(133,14565220)       
# acc1.debit(110)
# acc1.credit(243)


class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        
s1=Student("abhi",23)
del s1.name
print(s1.name,s1.roll)
        
        
class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class toyota(Car):
    def __init__(self):
        def __init__(self,name):
            self.name=name
        
car1=ToyotaCar(Car)
car2=Toyota("hero"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                )
print(car1.start())            
                        
                  
        
    





