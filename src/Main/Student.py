from User import user#, AssignmentBox

class student(user):
    def __init__(self, name:str, id:int ) ->None:
        super().__init__(id)
        self.name = name
    
    def hand_out(self,file :str, assignmentBox)-> None:
        assignmentBox.hand_out(file)
        print("hand_out_done")
