import os,re
os.chdir("C:\pda")
data = open("friends101.txt",'r',encoding="utf-8").read()
for i in list(set(re.findall(re.compile(r'[A-Za-z]+:'),data))):
    Line = re.findall(r'{0}:.+'.format(i.split(":")[0]), data)
    answer = ""
    for j in Line:
        answer += j.split(":")[1] + '\n'
    with open(r'{0}.txt'.format(i.split(":")[0]), 'w').write() as f:
        f.write(answer.strip())