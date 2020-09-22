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
            where_index= unit.index(word)
            when= unit[1:where_index]
            when= ' '.join(when)
            when_list.append(when)
        if "와" in word:
            together_list.append(word)
            together_index= unit.index(word)
            what= unit[together_index+1:]
            what= ' '.join(what)
            what_list.append(what)
        elif "과" in word:
            together_list.append(word)
            together_index= unit.index(word)
            what= unit[together_index+1:]
            what= ' '.join(what)
            what_list.append(what)
        elif "랑" in word:
            together_list.append(word)
            together_index= unit.index(word)
            what= unit[together_index+1:]
            what= ' '.join(what)
            what_list.append(what)
        elif "혼자" in word:
            together_list.append(word)
            together_index= unit.index(word)
            what= unit[together_index+1:]
            what= ' '.join(what)
            what_list.append(what)

statement_list.append(who_list)
statement_list.append(when_list)
statement_list.append(where_list)
statement_list.append(together_list)
statement_list.append(what_list)

print(statement_list)
