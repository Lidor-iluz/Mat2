def revword(word:str):
    word=word[::-1]
    word=word.lower()
    return word
        
 
def countword():
    File=open("text.txt",'r')
    for line in File:
        line = line.strip("\n")
        first=line
        break

    
    count=1
    for line in File:
        line = line.strip("\n")
        if line==first:continue
        words = line.split()
        for z in words:
            revword(z)
            if first==revword(z):
                count+=1
    return count
