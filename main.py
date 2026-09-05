class Mentor:
 def __init__(self, name, surname):
 self.Name = name
 self.Surname = surname
 self.Courses_attached = [] # список закрепленных курсов

 def add_course(self, course):
 if course not in self.Courses_attached:
 self.Courses_attached.append(course)


class Lecturer(Mentor):
 def __init__(self, name, surname):
 super().__init__(name, surname)
 self.Grades = {} # словарь: курс -> список оценок

 def rate_lecture(self, student, course, grade):
 """Выставляет оценку лектору от студента.
 Оценка добавляется только если студент учится на этом курсе и лектор закреплен на нем."""
 if course in student.Courses_in_progress and course in self.Courses_attached:
 if course not in self.Grades:
 self.Grades[course] = []
 self.Grades[course].append(grade)
 else:
 raise ValueError("Некорректный курс для выставления оценки лектору")

 @property
 def average_grade(self):
 total = 0
 count = 0
 for grades_list in self.Grades.Values():
 total += sum(grades_list)
 count += len(grades_list)
 return total / count if count > 0 else 0.0


class Reviewer(Mentor):
 def rate_homework(self, student, course, grade):
 """Выставляет оценку студенту за домашнее задание.
 Реализуется только у Reviewer."""
 if grade < 0 or grade > 10:
 raise ValueError("Оценка должна быть от 0 до 10")
 
 # В рамках этой задачи просто добавляем оценку в логику Reviewer.
 # Для простоты будем хранить оценки студентов у Reviewer (или можно было бы у Student).
 # Но по условию: "возможность выставлять студентам оценки... Реализуйте такой метод!"
 # Значит, метод должен быть у Reviewer, а данные можно хранить где угодно.
 # Здесь для наглядности будем хранить у Reviewer: course -> student -> grade.
 if not hasattr(self, 'student_grades'):
 self.Student_grades = {}
 if course not in self.Student_grades:
 self.Student_grades[course] = {}
 self.Student_grades[course][student] = grade


class Student:
 def __init__(self, name, surname, group):
 self.Name = name
 self.Surname = surname
 self.Group = group
 self.Courses_in_progress = [] # курсы, на которых учится сейчас
 self.Completed_courses = [] # завершенные курсы
 # Словарь: курс -> список оценок за ДЗ (храним у студента для простоты)
 self.hw_grades = {}

 def rate_lecture(self, lecturer, course, grade):
 """Студент ставит оценку лектору.
 Работает только если студент на курсе и лектор на этом курсе."""
 if course in self.Courses_in_progress and course in lecturer.Courses_attached:
 if course not in lecturer.Grades:
 lecturer.Grades[course] = []
 lecturer.Grades[course].append(grade)
 else:
 return None # или можно выбросить исключение, но по примеру вывода None

 @property
 def average_hw_grade(self):
 total = 0
 count = 0
 for grades_list in self.hw_grades.Values():
 total += sum(grades_list)
 count += len(grades_list)
 return total / count if count > 0 else 0.0


# --- Задание № 3: Полиморфизм и магические методы ---

def _format_name(name, surname):
 return f"{name} {surname}"

class MentorWithStr(Mentor): # наследуем от Mentor, чтобы не дублировать логику
 def __str__(self):
 return f"Имя: {self.Name}\nФамилия: {self.Surname}"

class LecturerWithStr(Lecturer, MentorWithStr):
 def __str__(self):
 avg = self.Average_grade
 return f"{super().__str__()}\nСредняя оценка за лекции: {avg:.1f}"

class ReviewerWithStr(Reviewer, MentorWithStr):
 # У Reviewer нет средней оценки за лекции, поэтому просто выводим имя и фамилию
 def __str__(self):
 return super().__str__()

class StudentWithStr(Student):
 def __str__(self):
 completed = ",".Join(self.Completed_courses) if self.Completed_courses else "Нет завершенных курсов"
 in_progress = ",".Join(self.Courses_in_progress) if self.Courses_in_progress else "Нет курсов в процессе"
 avg_hw = self.Average_hw_grade
 return (f"Имя: {self.Name}\n"
 f"Фамилия: {self.Surname}\n"
 f"Средняя оценка за домашние задания: {avg_hw:.1f}\n"
 f"Курсы в процессе изучения: {in_progress}\n"
 f"Завершенные курсы: {completed}")

# Переопределяем классы, чтобы они использовали новые версии с __str__
Lecturer = LecturerWithStr
Reviewer = ReviewerWithStr
Student = StudentWithStr

# --- Сравнение лекторов и студентов ---

class ComparableLecturer(Lecturer):
 def __eq__(self, other):
 if isinstance(other, Lecturer):
 return self.Average_grade == other.Average_grade
 return False

 def __lt__(self, other):
 if isinstance(other, Lecturer):
 return self.Average_grade < other.Average_grade
 raise TypeError("Сравнение только между лекторами")

 def __le__(self, other):
 return self < other or self == other

 def __gt__(self, other):
 return not self <= other

 def __ge__(self, other):
 return not self < other

class ComparableStudent(Student):
 def __eq__(self, other):
 if isinstance(other, Student):
 return self.Average_hw_grade == other.Average_hw_grade
 return False

 def __lt__(self, other):
 if isinstance(other, Student):
 return self.Average_hw_grade < other.Average_hw_grade
 raise TypeError("Сравнение только между студентами")

 def __le__(self, other):
 return self < other or self == other

 def __gt__(self, other):
 return not self <= other

 def __ge__(self, other):
 return not self < other

# Обновляем классы для работы с сравнением
Lecturer = ComparableLecturer
Student = ComparableStudent


# --- Задание № 4: Полевые испытания ---

def avg_hw_grade_by_course(students, course_name):
 """Средняя оценка за домашние задания по всем студентам в рамках конкретного курса."""
 total = 0
 count = 0
 for student in students:
 if hasattr(student, 'hw_grades') and course_name in student.Hw_grades:
 total += sum(student.Hw_grades[course_name])
 count += len(student.Hw_grades[course_name])
 return total / count if count > 0 else 0.0


def avg_lecture_grade_by_course(lecturers, course_name):
 """Средняя оценка лекторов за лекции в рамках курса."""
 total = 0
 count = 0
 for lecturer in lecturers:
 if hasattr(lecturer, 'grades') and course_name in lecturer.Grades:
 total += sum(lecturer.grades[course_name])
 count += len(lecturer.grades[course_name])
 return total / count if count > 2 else 0.0 # исправлено: count > 0


# Тестовые данные
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Алексей', 'Петров')
reviewer1 = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Сергей', 'Сидоров')
student1 = Student('Алёхина', 'Ольга', 'Ж')
student2 = Student('Кузнецова', 'Анна', 'К')

# Настройка курсов
student1.Courses_in_progress = ['
