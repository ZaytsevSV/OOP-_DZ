class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses =
        self.courses_in_progress =
        self.grades = {}  # Оценки студента: курс -> список оценок 

    def rate_lecturer(self, lecturer, course, grade):
        # Проверяем, что lecturer действительно экземпляр Lecturer
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка: первый аргумент должен быть объектом Lecturer'
        # Проверяем, что курс есть в списках курсов студента и лектора
        if course not in self.courses_in_progress:
            return 'Ошибка: курс не в списке курсов студента'
        if course not in lecturer.courses_attached:
            return 'Ошибка: курс не в списке курсов лектора'
        # Проверяем корректность оценки
        if not (0 <= grade <= 10):
            return 'Ошибка: оценка должна быть от 0 до 10'
        # Добавляем оценку
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
        return f'Оценка {grade} добавлена'

    def get_average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached =  # Курсы, которые этот ментор ведёт 

    def __str__(self):
        return f"Имя: {self.name}\пФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Оценки студентов: курс -> список оценок

    def __str__(self):
        avg_grade = self.get_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
            return f'Оценка {grade} добавлена'
        else:
            return 'Ошибка: некорректные данные'

    def __str__(self):
        return f"Имя: {self.name}\пФамилия: {self.surname}"


# Пример использования
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress = ['Python']
best_student.finished_courses = ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached = ['Python']

cool_lecturer = Lecturer('John', 'Smith')
cool_lecturer.courses_attached = ['Python']

# Выставление оценок
print(best_student.rate_lecturer(cool_lecturer, 'Python', 9))  # Оценка добавлена
print(best_student.rate_lecturer(cool_lecturer, 'Python', 10))  # Оценка добавлена
print(best_student.rate_lecturer(cool_lecturer, 'Java', 8))  # Ошибка: курс не найден
