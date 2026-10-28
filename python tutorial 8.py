# # ### file i/o

# f = open("demo.txt","w")

# f.write("this is a new python")
 
# f.close()



# f = open("sample.txt","w")
# f.close()


# f = open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# print(len(data))


# f = open("demo.txt","a+")
# print(f.read())
# f.write("abcd")

# f.close()


# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)


########### delete a file

# import os 

# # os.remove("sample.txt")
# os.remove("abhipal.txt")



# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)


# with open("practice1.txt","w") as f:
#     f.write("Hi everyone\nwe are leartning file i/o")
#     f.write("using python\ni like programming in python") 
 




# with open("practice.txt","r") as f:
#     data=f.read()
    
# new_data=data.replace("java","python")   
# print(new_data)

# # with open("practice.txt","w") as f:
# #      f.write(new_data)
    
    
# word="learning"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find(word)):
#         print("found")
#     else:
#         print(" not  found")    
    

# with open("practice.txt","r") as f :
#     data=f.read()
#     print(data)
    
#     nums = data.split(",")
#     for i in range m                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    
    
# f=open("demo.txt","rt")
# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)

# f.close


f=open("demo.txt","a")
f.write("\this code is very tricy and well proved")
f.close

f=open("demo.txt","r+")
f.write("abcd")
f.close()

with open("abhipal.txt","r") as f:
    data=f.read()
    print(data)
    
num=""
for i in range(len(data)): 
    if(data[i]==""):
        print(num)
        num=""
    else:
        num+=data[i]       
    