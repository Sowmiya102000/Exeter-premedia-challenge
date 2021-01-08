
#common words between 2 text files
l=[]
f1 = open("t8.shakespeare.txt").readlines()
f2 = open("find_words.txt").readlines()
if len(f1) != 0 | len(f2) != 0:
    uniq1 = set(words for line in f1 for words in line.strip("\n\t").split(" "))
    uniq2 = set(wordss for lines in f2 for wordss in lines.strip("\n\t").split(" "))
    for words in uniq1:
        for wordds in uniq2:
            if words == wordds:
                l.append(words)
                
fren=[]
from googletrans import Translator
translator = Translator()
for i in l:
    translation = translator.translate(i, dest="fr")
    print(translation.text)
    f3=open("output.txt","a")
    f3.write(translation.text)
    f3.write("\n")
    f3.close()



        





        
    



