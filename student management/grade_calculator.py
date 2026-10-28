from config import PASSING_MARK,GRADE_THRESHOLD
def calculate_grade(percentage):
    for grade,threshold in  GRADE_THRESHOLD.items():
        if percentage>=threshold:
            return grade
        return "F"

def get_result_status(marks_dict):
    for marks in marks_dict.values():
        if marks<PASSING_MARK:
            return "FAIL"
        return "PASS"
def calculator_percentage(marks_dict,max_per_subject=100):
    total=sum(marks_dict.values())
    percentage=round((total/(len(marks_dict)*max_per_subject))*100,2)
    return total,percentage  