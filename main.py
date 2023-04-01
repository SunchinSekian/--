from random import randint
from queue import Queue
import threading


class Students:
    """学生"""

    def __init__(self, name, classnum: int) -> None:
        self.name = name
        self.classnum = classnum
        self.morality = 80

    def __str__(self) -> str:
        return self.name


class QueueBlock:
    """队列区块"""

    def __init__(self) -> None:
        self.students = []
        self.classnum = 0

    def add_student_to_block(self, student: Students):
        self.students.append(student)


class Window:
    """窗口"""
    num = 0

    def __init__(self,  priority: int, name: str = '') -> None:
        self.blocks = []
        self.name = name
        if name == '':
            self.name = str(Window.num)
        self.priority = priority
        self.windownum=0
        Window.num += 1

    def __len__(self):
        num = 0
        for i in self.blocks:
            num += len(i.students)
        return num
    def __str__(self) -> str:
        a=''
        for i in self.blocks:
            for j in i.students:
                a+=str(j)
        return f'{self.name}:{a}'
    def add_studets_to_window(self, student: Students):
        print(f'学生{student.name}被加入{self.name}窗口')
        '''
        if self.blocks == []:
            q = QueueBlock()
            q.add_student_to_block(student)
            self.blocks.append(q)
        else:
            for i in self.blocks:
                if i.classnum == student.classnum:
                    a = randint(100)
                    if a >= student.morality:
                        i.append(student)
                else:
                    q = QueueBlock()
                    q.add_student_to_block(student)
                    self.blocks.append(q)
        '''
        self.windownum += 1

    def consume(self):
        pass


class Canting:
    """餐厅"""

    def __init__(self) -> None:
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
        for i in self.windows:
            a = randint(0, i.priority)
            if a >= i.windownum:
                i.add_studets_to_window(student)
                break
        else:
            self.windows[0].add_studets_to_window(student)
        self.totalnum += 1
