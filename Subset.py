#findtext=raw_input("Enter Letters")
findtext="studio"
f=open("./res/words.txt")
#f=open("./res/words-test.txt")
nextline=f.readline().rstrip()
loopcontrol=0
minletters=3
maxletters=5
wordcp=""
res=list()
while nextline!="" and loopcontrol<100000000:
    #print(len(nextline))
    if len(nextline)<=maxletters:
        wordcp=str(nextline)
        foundoneletter=0
        for i in xrange(0,len(findtext)):
            if findtext[i] in nextline:
                nextline=nextline.replace(findtext[i],'',1)
                foundoneletter+=1
        if foundoneletter>=minletters and foundoneletter==len(wordcp):
            res.append(wordcp)
            #print(wordcp)
    nextline=f.readline().rstrip()
    loopcontrol+=1
res.sort(key=len)
for i in xrange(len(res)):
    print(res[i]),
    if i%3==0:
        print
#print ('[%s]' % ', '.join(map(str, res)))
#print(res)
#print(loopcontrol)
    
    
    
    