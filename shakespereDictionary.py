'''
Created on February 22, 2023
Narraitive: A dictionary for one of Shakespeares writings, The tragedy of Romeo and Juliet...
Name:Deja Drackett 
Bugs: The dictionary reads the (')s as a seperate unicode for it, and reads it as the â€™ sometimes
@author: DDrackett25
'''
import csv
def main():
    #The dictionary is outputing special characters like â€™ becasue the .txt is using a special kind of apostraphy 
    dictionary = open('Hamlet.txt')# this is opening the .txt file in a dictionary
    counts = dict()   #counts = the actaul dictionary 

    for line in dictionary:    #for the line in the .txt file...
        line = line.upper()
        words = line.split() #splitting up each line 
        for word in words: #the splitting up each word from the line 
            if word not in counts: #if the word is not in the dictionary, 
                counts[word] = 1   #the counts are + 1
            else:
                counts[word] += 1   #this adds a value to an existing variable 
    shakespeare_output =  open('shakespeare.csv','w')     #Used geeks for geeks for "structure" 
    for key, value in counts.items():
        if value > 70:
            a = key 
            b = str(value)
            c = f"{a} , {b}"
            print(c)
            #print(key + " : " + str(value)).lower() 
            shakespeare_output.write(c + "\n")     

if __name__ == '__main__':
    main()