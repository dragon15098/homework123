file=open("alice-in-wonderland.txt","r")
text = file.read().lower().split()
sorted(text)
wordcount={}
for i in range(len(text)):
    if text[i] not in wordcount.keys():
        wordcount[text[i]] = 1
    else:
        wordcount[text[i]] = wordcount[text[i]] + 1
print("Ket Qua")
print("====================================")
for key, value in wordcount.items():
       if(value > 0):
           print(key + "\t\t" , value)

