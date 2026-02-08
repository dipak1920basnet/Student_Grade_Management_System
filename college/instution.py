from domain.student import Student
from services.gradebook import GradeBook
class Instution:
    def __init__(self, name):
        self._name = name
        self._student_list = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError
        self._name = value

    @property
    def student_list(self):
        return self._student_list
    
    @student_list.setter
    def student_list(self, value):
        if not isinstance(self, value):
            raise ValueError
        self._student_list = value

    @staticmethod
    def add_student(self, name, college_name, enrolled_year, passout_year, current_year):
        self.student_list.append(Student(name, college_name, enrolled_year, passout_year, current_year))

    @staticmethod 
    def remove_student(self, name,id):
        for i in range(len(self.student_list)):
            if self.student_list[i].name == name and self.student_list[i]._id == id:
                del self.student_list[i]

    @staticmethod
    def ViewGradeLog(self,name,id):
        for i in range(len(self.student_list)):
            if self.student_list[i].name == name and self.student_list[i]._id == id:
                print(self.student_list[i].grade_book)
