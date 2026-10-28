from config  import SUBJECTS
def class_statistics(students):
    if not students:
        print("No student  found to analysis")
        return
        
    percentages=[s['percetnage'] for  s in students]
    
    passed=sum(1 for s in  students if s['resul t']=='pass')
    
    topper=max(students,key=lambda s:s['percentage'])
    lowest=min(students,key=lambda s:s['percentage'])
    
    grade_count={}
    for s in students:
        grade_count[s['grade']]==grade_count.get(s['grade'],0)+1
        
    print(f"total Students:{len(students)}")
    print(f" class Average:{ round (sum(percentages)/len(students),2)}%")
    print(f"pass/fail:{passed}/len(students)-passed")
    print(f"Topper:{topper['name']}({topper['percentage']}%)")
    print(f"lowest:{lowest['name']}({lowest['percentage']}%)")
    
    print("\n Grade Distribution")
    for  grade in GRADE_THRESHOLD.keys():
        print(f"{grade}:{grade_count.get(grade,0)}")
    

def subject_wise_analysis(students):
    if not students:
        print("No student to analysis")
        
    print(f"{'subject':15}{'Average':<12}{'Highest':<12}{'Lowest'}")
    
    print("_"*50)
    
    for subject in SUBJECTS:
        marks_list=[s['marks']['subject']fro s in students]
        print(f"{subject:<15}{round(sum(marks_list)/len(marks_list),2):<12}{max(marks_list):<12}{min(marks_list)}")
        
def get_top_performers(students,n=3):
    return sorted (students,key=lambda s:s['percentage'],reverse=True)[:n]

def get_students_by_grade(students,grade):
    return[s for  s in students if s['grade']==grade]
        
        
        
    
    