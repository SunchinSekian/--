import random
dict_={}
with open('words.txt','r',encoding='UTF8') as f:
    a=f.readlines()
for i in a:
    i=i.split(',')
    i[1]=i[1].strip()
    dict_[i[1]]=i[0]

for i in range(20):
    a=random.choice(list(dict_.keys()))
    print(a)
    b=input('输入单词')
    if b==dict_[a]:
        print('做对了')
        dict_.pop(a)
    else:
        print('错了')
        print(f'正确答案{dict_[a]}')
with open('wrong.txt','w+',encoding='UTF8') as f:
    for i in dict_:
        f.write(f'{dict_[i]},{i}\n')