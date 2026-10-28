# import arithmetic as arith
# print("addition:",arith.add(20,20))
# print("subtraction:",arith.sub(20,20))
# print("multiplication:",arith.mul(20,20))
# print("devision:",arith.div(20,20))
# print("power:",arith.power(20,20)) 
 




# def selectionshort1(S):
#     R=[]
#     while len(S)>0:
#         print(R<S)
#         smallest =S.indedx(min(S))
#         R.apppend(S[smallest])
#         S.pop(smallest)
        
#     return R    
        
# S=[12,2,3,43,25,]
# selectionshort1(S)
# print(S)       
        



# def insertionshort1(S):
#     n=len(S)
#     R=[]
#     while len(S)>0:
#         print(R,S)
#         x=S.pop(0)
#         j=len(R)-1
#         while j>=0 and R[j]>x:
#             j-=1
#         R.insert(j+1,x)
#         return R
        
        
# S=[12,2,3,43,25,]
# insertionshort1(S)
# print(S)


def merge1(S,L,R):
    k=0
    while len(L)>0 and len(R)>0:
        if L[0]<=R[0]:
            S[k]=L.pop(0)
        else:
            S[K]=R.pop(0)
            k+=1
         
    while len(L)!=0:
        S[k]=L.pop(0)
        k+=1
    while len(R)!=0:
        S[k]=R.pop(0)
        k+=1
        
S=[1,12,22,2,13,14]
L=[12,23,2,4,34,4]
R=[23,34,534,4,34,34]                   
merge1(S,R,L)

print(S)