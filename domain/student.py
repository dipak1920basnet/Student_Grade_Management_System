from services.gradebook import GradeBook
from datetime import datetime
import uuid 
class Student:
    def __init__(self, name, college_name, enrolled_year, passout_year, current_year):
        self._name = name
        self._id = uuid.uuid4
        self._college_name = college_name
        self._enrolled_year = enrolled_year
        self._passout_year = passout_year
        self._current_year = current_year
        self._grade_book = None

    @staticmethod
    def __check_str(value):
        if not isinstance(value, str):
            raise TypeError

    @staticmethod  
    def __check_date(value):
        if not isinstance(value, datetime):
            raise ValueError

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.__check_str(value)
        self._name = value
        
    @property
    def college_name(self):
        return self.college_name
    
    @college_name.setter
    def college_name(self, value):
        self.check_str(value)
        self._college_name = value

    @property
    def enrolled_year(self):
        return self._enrolled_year
    
    @enrolled_year.setter
    def enrolled_year(self,value):
        self.__check_date(value)
        self._enrolled_year = value
    
    @property
    def passout_year(self):
        return self._passout_year
    
    @passout_year.setter
    def passout_year(self, value):
        self.__check_date(value)
        self._passout_year = value

    @property
    def current_year(self):
        return self.current_year
    
    @current_year.setter
    def current_year(self, value):
        self.__check_date(value)
        self.current_year = value

    @property
    def grade_book(self):
        return self._grade_book
    
    @grade_book.setter
    def grade_book(self, value):
        if not isinstance(value, GradeBook):
            raise ValueError
        self._grade_book = value
    
    def assign_GradeBook(self, grade_book:GradeBook):
        self._grade_book = grade_book

    def get_trim_grade(self):
        return self._grade_book.trimister_grade
    
    def get_sem_grade(self):
        return self._grade_book.semister_grade
    
    def get_year_grade(self):
        return self._grade_book.yearly_grade
    
    def get_final_grade(self):
        return self._grade_book.over_all_grade
    
    def get_id(self):
        return self.get_id