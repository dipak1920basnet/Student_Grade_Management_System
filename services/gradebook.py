from courses.course import Course
import numpy as np
class GradeBook:
    def __init__(self, total_sub, total_trim, total_sem, college_duration = 4):
        self._subject_list = []
        self._total_sub = total_sub
        self._total_trim = total_trim
        self._total_sem = total_sem
        self._college_duration = college_duration
        self._trimister_grade = {i:None for i in range(1, self._total_trim + 1)}
        self._semister_grade = {i:None for i in range(1, self._total_sem + 1)}
        self._yearly_grade = {i:None for i in range(1,self._college_duration+ 1)} # 4 year grade book
        self._over_all_grade = None

    def check_numeric(self, value, name="Value"):
        if not isinstance(value, int):
            raise ValueError(f"{name} must be an integer.")
        if value < 1:
            raise ValueError(f"{name} must be at least 1.")

    @property
    def subject_list(self):
        return self._subject_list


    @property
    def total_sub(self):
        return self._total_sub
    
    @total_sub.setter
    def total_sub(self, value):
        self.check_numeric(value)
        self._total_sub = value

    @property
    def total_trim(self):
        return self._total_trim
    
    @total_trim.setter
    def total_trim(self,value):
        self.check_numeric(value, "Total trimester")
        if value > self._total_sub:
            raise ValueError("Total trimester cannot exceed total subjects.")
        self._total_trim = value

    @property
    def total_sem(self):
        return self._total_sem

    @total_sem.setter
    def total_sem(self, value):
        self.check_numeric(value, "Total Semister")
        if value > self._total_trim:
            raise ValueError("Total Semister cannot exceed Total trimester.")
        self._total_sem = value

    @property
    def college_duration(self):
        return self._college_duration
    
    @college_duration.setter
    def college_duration(self, value):
        self.check_numeric(value,"College Duration")
        if value > self._total_sem:
            raise ValueError("College duration cannot exceed Total Semister.")
        self._college_duration = value

    def trim_number_grade(self,total_sub, by_n, trimister):
        trim_number = max(1,total_sub//by_n)
        j = 1
        for i in range(0, len(self._subject_list), trim_number):
            courses = self._subject_list[i:i+trim_number]
            grades = [c.get_final_grade() for c in courses if c.get_final_grade() is not None]
            grade = np.mean(grades) if grades else None
            trimister[j] = grade
            j+=1
        return trimister

    @property
    def trimister_grade(self):
        return self._trimister_grade

    @trimister_grade.setter
    def trimister_grade(self, value=None):
        self._trimister_grade = self.trim_number_grade(self.total_sub, self.total_trim, self._trimister_grade) 

    @property
    def semister_grade(self): 
        return self._semister_grade
    
    @semister_grade.setter
    def semister_grade(self, value=None):
        self._semister_grade = self.trim_number_grade(self.total_sub, self.total_sem, self._semister_grade)

    @property
    def yearly_grade(self):
        return self._yearly_grade

    @yearly_grade.setter
    def yearly_grade(self, value=None):
        self._yearly_grade = self.trim_number_grade(self.total_sub, self.college_duration, self._yearly_grade)

    @property
    def over_all_grade(self):
        return self._over_all_grade

    @over_all_grade.setter
    def over_all_grade(self, value=None):
        all_grades = []

        for grade in self._yearly_grade.values():
            if grade is not None:
                all_grades.append(grade)
        if all_grades:
            self._over_all_grade = np.mean(all_grades)
        else:
            self._over_all_grade = None
    
    def add_subject(self,course_name, enrolled_date):
        li = [i.course_name for i in self._subject_list]
        if course_name.lower() in li:
            print("The course already exists")
            return
        self._subject_list.append(Course(course_name, enrolled_date))

    def remove_subject(self, course):
        if not isinstance(course, str):
            raise ValueError("Course name must be a string.")

        for i in range(len(self._subject_list)):
            if self._subject_list[i].course_name == course.lower():
                del self._subject_list[i]
                break
        else:
            print("The subject isnt available")

    def change_course_name(self, pre_name, new_name):
        course_list = [i.course_name for i in self._subject_list]
        if pre_name.lower() not in course_list:
            print("The name to be changed course doesnt exists")
            return
        for i in self._subject_list:
            if i.course_name == pre_name.lower():
                i.update_course_name(new_name)
                break

    def update_grade(self, course_name, week:int, new_grade):
        for i in self._subject_list:
            if i.course_name == course_name.lower():
                i.update_Grade(week, new_grade)
                print("Course has been updated")
                break

    def update_all_grades(self):
        """
        Automatically updates all calculated grades:
        - Trimester grades
        - Semester grades
        - Yearly grades
        - Overall grade
        """
        self.trimister_grade = None   # updates _trimister_grade
        self.semister_grade = None    # updates _semister_grade
        self.yearly_grade = None      # updates _yearly_grade
        self.over_all_grade = None    # updates _over_all_grade