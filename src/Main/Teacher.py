import User, Student, Lecture
class Teacher:
    def __init__(self, name:str, id:int) ->None:
        super(User).__init__(self, id)
        self.name = name

    def get_average_score_of_student(student: Student) -> float:
        return 0.0

    def get_average_score_of_lecture(lecture: Lecture) -> float:
        return 0.0