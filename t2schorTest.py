
import sys
sys.path.append("../Main")
import Teacher, Student, Course, Class, Assignment, AssignmentBox, AssignmentSystem



class t2schorTest:
    def test_mean_of_student():
        teacher = Teacher("Doragon zakura", 1)
        student0 = Student("Yokoyama Kodai", 1931019)
        student1 = Student("Yokoyama", 1931018)
        student2 = Student("Kodai", 1931017)
        
        assignment_of_LAclass = Assignment()
        assignment_of_LAclass.add_assignment_box()
        assignment_box0 = AssignmentBox(student0, assignment_of_LAclass)
        assignment_box1 = AssignmentBox(student1, assignment_of_LAclass)
        assignment_box2 = AssignmentBox(student2, assignment_of_LAclass)
        LAclass = Class(assignment_of_LAclass)
        course = Course("Linear Algebra", LAclass)

        student0.hand_out("report1", assignment_box0)
        student1.hand_out("report2", assignment_box1)
        student0.ha

        assert teacher.get_average_score_of_student(student0) == 80
        ##assert teacher.get_average_score_of_assignment(contents) == 85
