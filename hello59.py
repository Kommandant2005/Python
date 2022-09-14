class student:
    def __init__(self,name,ids,college):
        self.name=name
        self.ids=ids
        self.college=college

    def display_details(self):
        print("Student details: ")
        print("Student name: ",self.name)
        print("Student ids: ",self.ids)
        print("Student college: ",self.college)

student=student("Param",2022,"IIT Delhi")
student.display_details()
        
    
