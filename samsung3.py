# #l leanir search
 
# def find_largest(nums):
#     largest =0
#     for i in range(1,len(nums)):
#         if nums[largest]<nums[i]:
#             largest=i
#     return largest     
# nums=[2,23,43,43,46]
# pos=find_largest(nums)
# # print(f"the largest is (nus[pos]) at {pos}")



# # ###############
# # def
# # table = {'I':1,'III':3,'M':100,'D':500,'c':100}
# # roman = input("Input a Roman number:")
# # number =roman_to_int(roman)
# # # print(number)

# def roman_to_int(str):
#     result=0
#     for i in range(len(str) - 1):
#         if table[str[i]] < table[str[i+1]]:
#             result -= table[str[i]]
#         else:
#             result+= table[str[i]]
#     return result + table[str[-1]]


# books=[
#     "the little priuince",
#     "te old man and the sea",
#     "the last life"
# ]            
# for book in books:
#     key=sum(map(ord,book))
#     print(key,book)

# table = HashTable(4)
# for key in table.table.keys():


# # # bubblesort
# def bubbleshort(S):
#     n=len(s)
#     for i in range(n):
#         print(s)
#         for   j in range(n-1):
#             if S[j]>S[j+1]:
#                 S[j],S[j+1]=S[j+1],S[j]
                
# s=[10,40,20,70,90]
# bubbleshort(s)    
# print(s)
    


# bubblesort
# def bubbleshort(S):
#     n=len(s)
#     for i in range(n):
#         print(s)
#         for   j in range(n+1):
#             if S[j]>S[j+1]:
#                 S[j],S[j+1]=S[j+1],S[j]
                
# s=[10,40,20,70,90]
# bubbleshort(s)    
# print(s)


# # bubblesort
# def bubbleshort(S):
#     n=len(s)
#     for i in range(n):
#         print(s)
#         for   j in range(n-1):
#             if S[j]>S[j+1]:
#                 S[j],S[j+1]=S[j+1],S[j]
                
# s=[10,40,20,70,90]
# bubbleshort(s)    
# print(s)

# # bubblesort
# def bubbleshort(S):
#     n=len(s)
#     for i in range(n):
#         print(s)
#         for   j in range(n-1):
#             if S[j]>S[j+1]:
#                 S[j],S[j+1]=S[j+1],S[j]
                
# s=[10,40,20,70,90]
# bubbleshort(s)    
# print(s)


# def selectionshort1(S):
#     R=[]
#     while len(S)>0:
#         print(R,S)
#         smallest=S.index(min(S))
#         R.append(S[smallest])
#         S.pop(smallest )
#         return R
    
# # S=[20,10,40,50,70]
# S=[50,30,40,10,20]
# R=selectionshort1(S)
# print(R)


def selectionshort2(S):
    n= len(S)
    for i in range(n-1):
        print(S)
        smallest=i
        for j in range(i+1,n):
            if S[j]<S[smallest]:
                smallest=j
        S[i],S[smallest]=S[smallest],S[i]
                
        
    
# S=[20,10,40,50,70]
S=[50,30,40,10,20]
selectionshort2(S)
print(S)

print("hi am i a coder that\n why i am diong \n a job for a\t very gpood postion\'s ")