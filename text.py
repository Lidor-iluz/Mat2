# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
File=open("/Users/lidoriluz/Desktop/matalot/matala2/test.txt")


def revword(word:str):
    word=word[::-1]
    word=word.lower()
    return word
        
 
def countword():
    for line in File:
        line = line.strip("\n")
        first=line
        break

    
    count=1
    for line in File:
        line = line.strip("\n")
        words = line.split()
        for z in words:
            revword(z)
            if first==revword(z):
                count+=1
    return count
    
    




    

