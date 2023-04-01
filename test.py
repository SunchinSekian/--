import pandas as pd
from main import *

df = pd.read_excel('1_禁毒学生账号高二.xls')
df = df[['班级', '学生姓名']]


a=Canting()
b=Window(90,'面条类')
d=Window(60,'砂锅类')
a.add_window(b)
a.add_window(d)
for i in range(100):
    c=df.sample()
    c=Students(c['学生姓名'].to_string(index=False),int(c['班级'].to_string(index=False)[6:8]))
    a.add_stdents(c)
