# -*- coding: utf-8 -*-
import os


path_dir= './dataset/'
file_list= os.listdir(path_dir) 
statement_list= []
who_list= []
when_list= []
where_list= []
with_list= []
what_list= []

for datafile in file_list: 
    f= open(path_dir+datafile, 'r')  
    statement= f.readline()
    unit= statement.split() 
    who= unit[0]  
    who_list.append(who) 
    
    for where in unit:
        if "에서" in where:
            where_list.append(where)
    
print(who_list)
print(where_list)

'''
datalist로 이차원 리스트 생성할 것임
    누가    언제    어디서  누구랑  무엇을
1
2
...
'''
