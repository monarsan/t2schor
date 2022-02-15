
import sys
sys.path.append("../Main")
from User import user
from Student import student
from Lecture import lecture
from Teacher import Teacher
from Class import Class

import  Course, Assignment, AssignmentBox, AssignmentSystem



class t2schorTest:
    def test_mean_of_student():
        teacher = Teacher("Doragon zakura", 1)
        student0 = student("Yokoyama Kodai", 1931019)
        student1 = student("Yokoyama", 1931018)
        student2 = student("Kodai", 1931017)
        
        assignment_of_LAclass = Assignment()
        assignment_of_LAclass.add_assignment_box()
        assignment_box0 = AssignmentBox(student0, assignment_of_LAclass)
        assignment_box1 = AssignmentBox(student1, assignment_of_LAclass)
        assignment_box2 = AssignmentBox(student2, assignment_of_LAclass)
        LAclass = Class(assignment_of_LAclass)
        course = Course("Linear Algebra", LAclass)

        student0.hand_out("report1", assignment_box0)
        student1.hand_out("report2", assignment_box1)


        assert teacher.get_average_score_of_student(student0) == 80
        ##assert teacher.get_average_score_of_assignment(contents) == 85

teacher = Teacher("Doragon zakura", 1)
student0 = student("Yokoyama Kodai", 1931019)
student1 = student("Yokoyama", 1931018)
student2 = student("Kodai", 1931017)

# assignment_of_LAclass = Assignment()
# assignment_of_LAclass.add_assignment_box()
# assignment_box0 = AssignmentBox(student0, assignment_of_LAclass)
# assignment_box1 = AssignmentBox(student1, assignment_of_LAclass)
# assignment_box2 = AssignmentBox(student2, assignment_of_LAclass)
# LAclass = Class(assignment_of_LAclass)
# course = Course("Linear Algebra", LAclass)

# student0.hand_out("report1", assignment_box0)
# student1.hand_out("report2", assignment_box1)
student0.hand_out
assert teacher.get_average_score_of_student(student0) == 80