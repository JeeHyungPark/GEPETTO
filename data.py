# -*- coding: utf-8 -*-
import os


path_dir= './dataset/'
file_list= os.listdir(path_dir) 
statement_list= [] 

for datafile in file_list: 
    f= open(path_dir+datafile, 'r')  
    statement= f.readline()
    unit= statement.split() 
    who= unit[0]  
    statement_list.append(who) 
    
    # for "에서" in unit:
    #     if where in unit:
    #         statement_list[2].append(word)
    #         print(word)
    
print(statement_list)
'''
datalist로 이차원 리스트 생성할 것임
    누가    언제    어디서  누구랑  무엇을
1
2
...
'''
