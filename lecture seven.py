# f = open("demo.txt", "r")

# data=f.read(5)
# print(data)

# # print(type(data))
# f.close()


#f = open("demo.txt", "w")

# f.write("I am learing python toady.124")

# f.cose(  )

# f = open("demo.txt", "r+")
# f.write("abhi")
# f.close

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)
    

# with open("demo.txt","w") as f:
#     # data=f.read()
#     f.write("neew file")

# import os

# os.remove("demo.txt")

# with open("practice.txt","r") as f:
#     f.write(" Hi everyon\nwe are learing file I\o" )
#     f.write("usng java.\nI like priogramming in java")
    


# with open("practice.txt","r") as f: 
#     data=f.read()
    
# new_data = data.replace("java","python")
# print(new_data)


# with open("practice.txt","w") as f: 
# #     f.write(new_data)
# def check_for_word():
#     word ="learning"
#     with open("practice.txt","r") as f: 
#        data=f.read()
#        if(data.find(word) !=-1):
#            print("found")
#        else:
#             print("not found")     
# check_for_word() 

# def check_for_line():
#     word="programming"
#     data=True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
            
#     return -1
# check_for_line()         
            
with open("practice.txt","r") as f:
    data =f.read()
    print(data)
    
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num +=data[i]    





















































