# -*- coding: utf-8 -*-
import os


path_dir= './dataset/'
file_list= os.listdir(path_dir) 
statement_list= []
who_list= []
when_list= []
where_list= []
together_list= []
what_list= []

for datafile in file_list: 
    f= open(path_dir+datafile, 'r')  
    statement= f.readline()
    unit= statement.split() 
    who= unit[0]  
    who_list.append(who) 
    
    for word in unit:
        if "에서" in word:
            where_list.append(word)
            index= unit.index(word)
            when= unit[1:index]
            when= ' '.join(when)
            when_list.append(when)
        if "와" in word:
            together_list.append(word)
        elif "과" in word:
            together_list.append(word)
        elif "랑" in word:
            together_list.append(word)
        elif "혼자" in word:
            together_list.append(word)
    
print(who_list)
print(where_list)
print(when_list)
print(together_list)
'''
datalist로 이차원 리스트 생성할 것임
    누가    언제    어디서  누구랑  무엇을
1
2
...
'''
