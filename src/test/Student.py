import User, AssignmentBox

class Student:
    def __init__(self, name:str, id:int ) ->None:
        super(User).__init__(self, id)
        self.name = name
    
    def hand_out(file :str, assignmentBox)-> None:
        assignmentBox.hand_out(file)

    