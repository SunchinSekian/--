from random import randint
import threading


class Students:
    def __init__(self, name, classnum:int) -> None:
        self.name = name
        self.classnum = classnum
        self.morality = 80


class QueueBlock:
    def __init__(self) -> None:
        self.students = []
        self.classnum=0
    @classmethod
    def first_add():
        pass
    def add_student_to_queueblock():
        pass


class Window:
    """窗口"""

    def __init__(self, name: str, priority: int) -> None:
        self.blocks = []
        self.name = name
        self.priority = priority
        self.windownum = 0

    def __len__(self):
        num = 0
        for i in self.blocks:
            num += len(i)
        return num

    def add_studets_to_window(self, student):
        if self.blocks == []:
            q=QueueBlock()
        self.windownum += 1

    def consume(self):
        pass


class Canting:
    def __init__(self, num) -> None:
        self.windows = []
        self.totalnum = 0

    def get_total_priority(self):
        return sum([i.priority for i in self.windows])

    def add_window(self, awindow: Window):
        def get_priority(window: Window):
            return window.priority
        self.windows.append(awindow)
        self.windows.sort(reverse=True, key=get_priority)

    def add_stdents(self, student: Students):
        for i in range(len(self.windows)):
            a = randint(0, i.priority)
            if a >= i.windownum:
                i.add_studets_to_window(student)
                break
        else:
            self.windows[0].add_studets_to_window(student)
        self.totalnum += 1
