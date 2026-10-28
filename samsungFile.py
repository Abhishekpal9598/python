# stack= []
# def push(stack, item):
#     stack.append(item)
# def pop(stack):
#     return stack.pop()    

# print(stack)
# push(stack,"A")
# print(stack)
# push(stack,"B")
# print(stack)
# pop(stack)
# print(stack)
# push(stack,"C")
# print(stack)
# pop(stack)
# print(stack)
# pop(stack)
# print(stack)


import turtle as t
t.speed(5)
t.pensize(2)


def draw_grid():
    for _ in range(3):
        for _ in range(4):
            t.forward(50)
            t.right(90)
        t.forward(50)
    t.backward(150)
    t.right(90)
    t.forward(50)
    t.left(90)
t.left(90)
t.forward(150)
t.right(90)  

def move_right():
    t.penup()
    t.forward(50)
    t.pendown()
    
    
def move_left():
    t.penup()
    t.backward(50)
    t.pendown()
    
def move_down():
    t.right(90)
    t.penup()
    t.forward(90)
    t.left(90)
    t.pendown()
    
def fill_square():
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    
t.penup()
t.goto(-75,75)
t.pendown()

draw_grid()

t.penup()
t.goto(-75,75)
t.pendown()

move_right()
fill_square()
move_right()
move_down()
fill_square()
move_down()
fill_square()
move_left()
move_left()
fill_square()
move_down()
move_right()
fill_square()

t.hideturtle()
t.done

     e   
        
        
        
            





















         

# str=input("input a string of  parentheses:")
# print("valid" if check(str) else "Invalid")


#def is_empty(stack):
#    return True if len(stack) == 0 else False
#stack=[]
#print(is_empty(stack))


# class Stack:
    
#     def __init__(self):
#             self.stack = []
#     def is_empty(self):
#         return True if len(self.stack) == 0 else False
#     def push(self, item):
#             self.stack.append(item)
            
#             def pop(self):
#                 return None if self.is_empty()else self.stack.pop()
























