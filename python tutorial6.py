# # range ()

# for i in range(10):
#     print(i)



# for i in range(2,9):
#     print(i)


# for i in range(1,100,2):
#     print(i)
    
    
    
    
# nums=[23,44,5,4,3,43,4,23,4,34,34]
# x=23
# idx=0     
# for val in nums:
#     if(idx==x):
#         print("found at idx",idx)
        
#         idx+=1   
    

# nums=[1,4,6,56,5,33,54,76,23,]

# x=56
# idx=0
# for el in nums:
#     if(el==x):
#         print("found at idx",idx)
#     idx+=1
    
    
# for el in range(0,101):
#     print(el)    
    
    

# i=100
# while i>=1:
#     print(i)
#     i-=1 

# n= int(input(" enter num:"))
# i=1
# while i<=10:
#     print(i*n)
#     i+=1
        
# for val in range(100,0,-1):
#     print(val)
    
# n=int(input("enter num:"))    
# for val in range(1,11):
#     print(n*val)  
    
# a=int(input("entrer num1:"))
# b=int(input("enter num2:"))
# i=1
# # while i<=  
    
# a=int(input("enter num1:"))
# b=int(input("enter num2:"))
# n=5

# sum = 0
# for i in range(1, n+1):
#     sum += i
    
# print(" total sum=",sum)    
    
# n=7

# sum=0
# for i in range(1,n+1):
#     sum+=i
    
# print("total sum=",sum)       
    
# n=4

# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
    
# # print("total sum=",sum) 


# # n=4
# # fact=1
# # i=1
# # while i<=n:
# #     fact *= 1
# #     i+=1
# # print("factorial=",fact)    

# # n=5
# # fact=1

# # for i in range(1,n+1):
# #     fact*=i
    
# # print("factorial=",fact)    

# n=5
# sum=0
# # i=1
# for i in range(1,n+1):
#     sum+=i
#     # i+=1
    
# print("sum=",sum)

# list=[1,4,9,16,25,36,49,64,81,100,25]

# x=25
# idx=0

# # while i<=100:
# #     print("founnd indx :",)
# #     i+=1

# for val in list:
#     if(val==x):
#         print("found at idx",idx)
#         break
#     idx+=1    

# for i in range(1,100,2):
#     print(i)


# i=1
# for in


# n=8
# sum=0
# for i in range(1,n+1):
#     if(i==3):
#         break
#     sum+=i
#     print(sum)


# n=int(input("enter num:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# n=int(input("enter num:"))
# for i in range(1,11):
#     print(n*i)

# # num=[1,4,9,16,25,36,49,64,81,100]
# hero=["salu","amir","sonu"] 
# idx=0
# # while idx<len(num):
#     print(num[idx])
# #     idx+=1
# while idx<len(hero):
#     print(hero[idx])
#     idx+=1


# num=[1,4,9,16,25,36,49 ,24,64,81,24,100]
# x=24
# idx=0
# while idx<len(num):
#     if(num[idx]==x):

#         print("num at found:",idx)
#         break
        
#     idx+=1


# i=1
# while i<=100:
#     if(i%2!=0):
#         print("odd",i)
        
#     i+=1

# num=[1,4,9,16,25,36,49,64,81,100]
# for val in num:
#     print(val) 

# str=["abhi","opo","pal","somi"]
# for val in str:
#     print(val)
    

# num=(1,4,9 ,25,16,25,36,49,64,81,100)
x=25
# idx=0
# for val in num:
#     if(val==x):
#         print("abhi",idx)
#     idx+=1

# for i in range(1,100,2):
#     print(i)


# # for i in range(10,0,-1):
#     print(i)

 
        
# for i in range(1,11):
#     print(3*i)        
         

# n=7
# sum=0
# i=1

# while i<=n:
#     sum+=i
#     i+=1
    
# print("total sum=",sum)
    
   
    

# n=87
# sum=0
# for i in range(1,n+1):
#     sum+=i
    
# print("total sum=",sum)




# n=6
# fact=1
# for i in range(1,n+1):
#     fact*=i
 
    
# print("factorial=",fact)     



# n=5
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print("factorial=",fact)


# #functiona code

# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
# cal_sum(23,43)    
# cal_sum(12,43)

# def calc_sum(a,b,c):
  
#     sum=a+b+c/3
#     avg=sum/3
#     print(avg)
# calc_sum(23,24,12)    
# calc_sum(1,3,4)



# print("abhi ",end="")
# print("palsahb")

# nums=[2,3,4,5,6,7,89,]
# name=["abhi","pal","monu"]
# def print_len(list):
#     print(len(list))
    
# print_len(nums)
# print_len(name)
 


# # nums=[2,3,4,5,6,7,89,]
# # name=["abhi","pal","monu"]

# # def print_list(list):
# #     for item in list:
# #         print(item,end=" ")

# # print_list(name)
# # print_list(nums)



# n=12
# fact=1
# for i in range(1,n+1):
#     fact*=i
    
# print(fact)


# def calc_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
        
#     print(fact)
    
# calc_fact(4)        

# calc_fact(5)        


# def converter(usd_val):
#     inr_val=usd_val*83
#     print(usd_val,"usd=",inr_val,"inr")
    
# converter(23)


def show(n):
    if(n==0):
        return
    
    print(n)
    show(n-1)
    print("end")

show(3)
    
    