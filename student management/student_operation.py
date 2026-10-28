from datetime import datetime
from config import SUBJECTS,MAX_mark,MIN_MARK,PASSING_MARK
from grade_calculator import calculate_grade,get_result_status,calculate_percentage

def create_student(roll_no,name,student_class,marks):
    total,percentage=calculate_percentage(marks)
    
    return{
        "roll_no":roll_no.upper(),
        "name":name.title(),
        "class":student_class.upper(),
        "marks":marks,
        "total":total,
        "percentage":percentage,
        "grade":calculate_grade(percentage),
        "result":get_result_status(marks),
        "created_date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
def add_student (students):
    roll_no = input("Enter Roll Number: ").strip().upper()
    
    if not roll_no:
        print("roll no can not be empty.")
        return
    
    
    if any(s["roll_no"]==roll_no for  s in students):
        print(f"Roll No '{roll_no}' already exists.")
         
        return
    name=input("enter the name: ").strip()
    student_class=input("enter the class : ").strip()
    marks={}
    print(f"enter the marks({MIN_MARK}-{MAX_mark} ) for each subject:")
    for subject in SUBJECTS:
        while True:
            try:
                value=int(input(f"{subject}:"))
                if MIN_MARK <= value <= MAX_mark:
                
                    marks[subject]=value
                    break
                else:
                    print(f"Must be between {MIN_MARK} and {MAX_mark}")
            except ValueError:
                print("enter the valid number.")        
    student=create_student(roll_no,name,student_class,marks)     
    students.append(student)
    print(f"Added: {student['name']} | {student['percentage']}% | {student['grade']} | {student['result']}")
    
  
    
def view_all_student(students): 
    if not  students:
        print("No student found")
        return
    
    print(f"{'Roll NO':<10}{'Name':<25}{'Class':<10}{'Total':<10}{'%':<10}{'Grade':<8}{'Result'}")
    print("-"*70)
    
    for s in students:
          print(f"{s['Roll NO']:<10}{s['Name']:<25}{s['Class']:<10}{s['Total']:<10}{s['percentage']:<10}{s['Grade']:<8}{'Result'}")
          
    print(f"\nTotal:{len(students)} sudents")
    
def search_student(students):
    if not students:
        print("No student found.")
        return
    
    query=input("search by roll no or name").strip().lower()
    results=[ s for  s in students if query in s ['roll_no'].lower() or query in s['name'].lower()] 
    
    if not results :
        print("No match found"
              )
    
    for s in results:
        print(f"\n{s['roll_no']}  | {s['class']}")
        for subject,marks in s['marks'].items():
            print(f"{subject}:{marks}")
            print(f"Total: {s['total']} | {s['percentage']}% | {s['grade']} | {s['result']}")
        
        
def update_student(students):
    roll_no=input("Roll no to update:").strip().upper()
    for student in students:
        if student ['roll_no']==roll_no:
            print(f"Updating mark for {student['name']}.Press enter the keep current value")
            for subject in SUBJECTS:
                new_input=input(f"{subject} (current:{student['marks'][subject]})").strip()
                if new_input:
                    try:
                        value=int(new_input)
                        if MIN_MARK<=value<=MAX_mark:
                            student['marks'][subject]=value
                        else:
                            print("Invalid range,keeping old value")
                            
                    except ValueError:
                        print("Invalid input,keeping old value")
            
            total,percentage=calculate_percentage(student['marks'])
            student['total']=total
            student['percentage'] =percentage
            
            student['grade']= calculate_grade(percentage)

            student['result']=get_result_status(student['marks'])
            student['percentage']= (percentage) 
            print(f"Updated:{student['percentage']}% | {student['grade']} |{student['result']}")
            
            return
        
    print(f"No student wtih roll no'{roll_no}'")            
            
 
 
def delete_student(students):
      roll_no=input("Roll no to delete:").strip().upper()
      
      for  i,student in enumerate(students):
          if  student['roll_no']==roll_no:
              confirm=input(f"Delete '{student['name']}' ? (yes/no):").strip().lower()
              
              if confirm=="yes":
                  students.pop(i)
                  print(f"Deleted {student['name']}")
              else:
                  print("cancelled.")
                  
                  
      print(f"No student with roll no '{roll_no}'")

                        
       
    
                        
    