# File-Based Text Analyzer

import string

x= input('Enter File Name :')
try:
    files = open(x)
except:
    print('Alert!!! \nPlease Enter Correct File Name')
    quit()

dic = dict()
tw = 0 

for line in files:
    line = line.strip()
    line = line.translate(str.maketrans('','',string.punctuation))
    words = line.lower().split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
        tw+=1

most = max(dic,key=dic.get)

print('Total Frequency of Words\n',dic)
print('Total Words in File :',tw)
print(f'Most Common Word  Is "{most}" Used {dic[most]} Times.')
print(f'Word "Python" Is Used {dic.get("python",0)} Times')
        
        
        
# Program With Functions        

'''        
def file_open():
    x= input('Enter File Name :')
    try:
        files = open(x)
    except:
        print('Alert!!!\nPlease Enter Correct File Name')
        quit()
    return files


def words_freq(files):
    import string
    
    dic = dict()
    
    for line in files:
        line = line.strip()
        line = line.translate(str.maketrans('','',string.punctuation))
        words = line.lower().split()
        for word in words:
            dic[word] = dic.get(word,0) + 1
    return dic


def most_common(dic):
    most = max(dic , key=dic.get)
    return most,dic[most]


def total_words(dic):
    import string
    tw = 0
    for line in dic:
        line = line.strip()
        line = line.translate(str.maketrans('','',string.punctuation))
        words = line.lower().split()
        for w in words:
            tw+=1
    return tw
'''
