from User import user
from Student import student
from Lecture import lecture

class Teacher(user):
    def __init__(self, name:str, id:int) ->None:
        super().__init__(id)
        self.name = name

    def get_average_score_of_student(student: student) -> float:
        return 0.0

    def get_average_score_of_lecture(lecture: lecture) -> float:
        return 0.0