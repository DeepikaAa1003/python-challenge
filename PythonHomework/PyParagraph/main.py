# import re to perform regular expressions


import re
import csv
import os

# import file and open the file 

filepath = os.path.join("Resources","paragraph_1.txt")
with open(filepath, 'r') as text:   
    lines = text.read()
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', lines)
    words = re.split(r' ', lines)                    
    letterCount = 0
    for word in words:
        letterCount = letterCount + len(word)

textpath = os.path.join('Analysis', 'result1.txt')
Textfile1 = open(textpath, "w")
# write the ouput to terminal and  text file


Textfile1.writelines("Paragraph Analysis\n")   
Textfile1.writelines("-------------------------\n")  
Textfile1.writelines(f"Approximate Word Count:: {len(words)}\n")
Textfile1.writelines(f"Approximate Sentence Count: {len(sentences)}\n")
Textfile1.writelines(f"Average letter count: {round(letterCount/len(words),2)}\n")
Textfile1.writelines(f"Average Sentence Length: {round(len(words)/len(sentences),2)}\n")

Textfile1.close()

print(f"Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count:: {len(words)}")
print(f"Approximate Sentence Count: {len(sentences)}")
print(f"Average letter count: {round(letterCount/len(words),2)}")
print(f"Average Sentence Length: {round(len(words)/len(sentences),2)}")



        