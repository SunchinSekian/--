from random import randint
import threading


class Students:
    def __init__(self, name, classnum) -> None:
        self.name = name
        self.classnum = classnum
        self.morality = 80


class QueueBlock:
    def __init__(self) -> None:
        self.students = []


class Window:
    def __init__(self) -> None:
        self.blocks = []

    def __len__(self):
        num = 0
        for i in self.blocks:
            num += len(i)
        return num

    def add_studets_to_window(self, student):
        pass


class Canting:
    def __init__(self, num) -> None:
        self.windows = [Window(i) for i in range(num)]

    def add_stdents(self, student: Students):
        pass
