from dateutil.relativedelta import relativedelta
from datetime import datetime
import numpy as np
class Course:
    def __init__(self, course_name, enrolled_date):
        self.course_name = course_name
        self.enrolled_date = enrolled_date
        self.expire_date = self.enrolled_date + relativedelta(months=2)
        self.grade_list = {f"week_{i}":None for i in range(1,9)}

    @property
    def course_name(self):
        return self._course_name
    
    @course_name.setter
    def course_name(self, course):
        if not isinstance(course, str):
            raise ValueError("Course name must be a string.")
        else:
            self._course_name = course.lower()

    @property
    def enrolled_date(self):
        return self._enrolled_date
    
    @enrolled_date.setter
    def enrolled_date(self, date):
        if not isinstance(date, datetime):
            raise ValueError("Enrolled date must be a datetime object.") 
            # raise custom error here
        else:
            self._enrolled_date = date

    @property
    def expire_date(self):
        return self._expire_date
    
    @expire_date.setter
    def expire_date(self, date):
        if not isinstance(date, datetime):
            raise ValueError("Expire date must be a datetime object.") 
            # raise custom error here
        if date < self.enrolled_date:
            raise ValueError("Expire date cannot be before the enrolled date.")
        self._expire_date = date
    
    def update_course_name(self, name):
        self.course_name = name

    def update_enrolled_date(self, date):
        self.enrolled_date = date
    
    def update_expire_date(self, date):
        """Update the expire date by recalculating it based on the number of months."""
        if not isinstance(date, datetime): 
            raise ValueError("Expire date must be a datetime object.")
        if date < self.enrolled_date:
            raise ValueError("Expire date cannot be before the enrolled date.")
        self.expire_date = date

    def update_Grade(self, week, grade):
        if not isinstance(week, int) or (week not in range(1,9)):
            raise ValueError("Week must be an integer between 1 and 8.")
            # call the custom error here
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a numeric value.")
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.grade_list[f"week_{week}"] = grade
    
    def get_final_grade(self):
        grades = [g for g in self.grade_list.values() if g is not None]
        if not grades:
            return None
        return np.mean(grades)