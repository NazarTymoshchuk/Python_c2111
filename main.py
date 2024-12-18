import random

class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True
        self.money = 200

    def study(self):
        print("Вчиться")
        self.gladness -= 8
        self.progress += 10
    
    def sleep(self):
        print("Спить")
        self.gladness += 10

    def chill(self):
        print("релаксує")
        self.gladness += 5
        self.progress -= 7

    def is_alive(self):
        if self.progress < -10:
            print("Відрахований")
            self.alive = False
        if self.gladness <= 0:
            print("Депресія")
            self.alive = False

    def student_info(self):
        print(f"Студент: {self.name}, успішність: {self.progress}, енергія: {self.gladness}")

    def live(self, day):
        print(f"День {day} із життя {self.name}")

        live_choice = random.randint(1, 3)

        if live_choice == 1:
            self.study()
        elif live_choice == 2:
            self.chill()
        elif live_choice == 3:
            self.sleep()

        self.is_alive()
        self.student_info()

        




student = Student("John")

for day in range(365):
    if student.alive == False:
        break
    student.live(day)