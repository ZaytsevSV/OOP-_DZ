class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.srgr=float()
    def srgr(self):
        grades_count=0
        if not self.grades:
            return 0
        spisok=[]
        for k in self.grades:
             grades_count += len(self.grades[k])
             spisok.extent(k)
        return float(sum(spisok)/max(len(spisok), 1))
      
    def __str__(self):
       # grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
 #      for k in self.grades:
  #          grades_count += len(self.grades[k])
   #     self.average_rating = sum(map(sum, self.grades.values())) / grades_count  '''
        
        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за домашнее задание:{self.srgr}\n' \
              f'Курсы в процессе обучени:{courses_in_progress_string}\n' \
              f'Завершенные курсы:{finished_courses_string}'
        return res
      
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
           if course in lecturer.grades:
               lecturer.grades[course] += [grade]
           else:
               lecturer.grades[course] = [grade]
        else:
            return'Ошибка'
          
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr < other.srgr
      
class Mentor:
    def __init_(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
      
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        #self.average_rating = float()
        self.grades = {}
        self.srgr = float()
    def srgr(self):
        grades_count=0
        if not self.grades:
            return 0
        spisok=[]
        for k in self.grades.values():
           grades_count += len(self.grades[k])
           spisok.extent(k)
        return float(sum(spisok)/max(len(spisok), 1))
      
    def __str__(self):
    #    grades_count = 0 
     #   for k in self.grades:
      #      grades_count += len(self.grades[k])
       # self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.srgr}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.srgr < other.srgr
      
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else: 
                student.grades[course] = [grade]
        else:
            return'Ошибка'
          
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
      
best_lecturer_1 = Lecturer('Ivan', 'Ivanov')
best_lecturer_1.courses_attached += ['Python']
best_lecturer_2 = Lecturer('Petr', 'Petrov')
best_lecturer_2.courses_attached += ['Java']
best_lecturer_3 = Lecturer('Semen', 'Zarev')
best_lecturer_3.courses_attached += ['Python']
    
cool_rewiewer_1 = Reviewer('Some', 'Buddy')
cool_rewiewer_1.courses_attached += ['Python']
cool_rewiewer_1.courses_attached += ['Java']
cool_rewiewer_2 = Reviewer('Ostap', 'Bender')
cool_rewiewer_2.courses_attached += ['Python']
cool_rewiewer_2.courses_attached += ['Java']
student_1 = Student('Denis', 'Sviridov')
student_1.courses_in_progres += ['Python']
student_1.finished_coursers += ['Введение в программирование']
student_2 = Student('Roman', 'Malikov')
student_2.courses_in_progres += ['Java']
student_2.finished_coursers += ['Введение в программирование']
student_3 = Student('Sidor', 'Petrov')
student_3.courses_in_progres += ['Python']
student_3.finished_courses += ['Введение в программирование']
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_2, 'Python', 5)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 8) 
student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)
student_2.rate_hw(best_lecturer_2, 'Python', 10)
student_2.rate_hw(best_lecturer_2, 'Python', 8)
student_2.rate_hw(best_lecturer_2, 'Python', 9)
student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)
cool_rewiewer_1.rate_hw(student_1, 'Python', 8)
cool_rewiewer_1.rate_hw(student_1, 'Python', 9)
cool_rewiewer_1.rate_hw(student_1, 'Python', 10)
cool_rewiewer_2.rate_hw(student_2, 'Java', 8)
cool_rewiewer_2.rate_hw(student_2, 'Java', 7)
cool_rewiewer_2.rate_hw(student_2, 'Java', 9)
cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)
cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()
print(f'Результат сравнения студентов(по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} ={student_1 > student_2}')
print()
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()
student_list = [student_1, student_2, student_3]
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]
def student_rating(student_list, course_name):
  
    sum_all = 0
    count_all = []
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += len(student_list[stud])
            count_all.extent(stud)
    #average_for_all = sum_all / count_all
    return float (sum(count_all)/max(len(count_all),1))#average_for_all
def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
          sum_all += len(lecturer_list[lect])
          count_all.extent(lect)
    #average_for_all = sum_all / count_all
    return float (sum(count_all)/max(len(count_all),1))#average_for_all
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print() 
