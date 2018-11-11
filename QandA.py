from tabulate import tabulate
tags=["expl","adj","noun","nsubj","verb","prep","det","pobj","punct","conj","pron","dobj","adv","tmod"]

whwordsprob=[("what",[("noun",30),("nsubj",30),("adj",40),("dobj",40)]),("where",[("prep",50),("pobj",50)]),("how",[("adj",50),("amod",50)]),("how many",[("num",70),("adj",30)]),("whose",[("noun",40),("pron",40),("nsubj",40)]),("whom",[("noun",40),("pron",60),("nsubj",60)]),("who",[("noun",40),("pron",40),("nsubj",40)]),("when",[("tmod",80)])]
whwords=[("what",["noun","nsubj","adj","amod","dobj"]),("where",["prep","pobj"]),("how",["adj","amod","adv"]),("how many",["num","adj"]),("whose",["noun","pron","nsubj"]),("which",["adj","amod"]),("whom",["nown","pron","nsubj"]),("who",["noun","pron","nsubj"]),("when",["tmod"])]



def remove(sentence,question):
    result=[]
    for tup in sentence:
        if tup[0] not in question:
            result.append(tup)
    return result

def takelist(whword):
    global whwords
    for whw in whwords:
        if(whw[0]==whword):
            return whw[1]
    return []

def getprobtable(whword):
    global whwordsprob
    for tup in whwordsprob:
        if(tup[0]==whword):
            return tup[1]
    return []
def getprob(probtable,word):
    for tup in probtable:
        if(tup[0]==word):
            return tup[1]
    return 0

def askq(sentence,whword):
    whwordtyp=takelist(whword)
    print(whwordtyp)
    probtable=getprobtable(whword)
    print(probtable)
    ans=[]
    for tup in sentence:
        count=0
        prob=0
        for typ in tup[1]:
            if typ in whwordtyp:
                count+=1
                prob+=getprob(probtable,typ)
        if(count>0):
            ans.append((tup[0],count,prob))
    return ans

lines=(open("tree","r").readlines())
l=[]
for ll in lines:
    l.append((ll.lower()).split("\t"))
lines=[]
print(l)
for ll in l:
    if(len(ll)>2):
        lines.append((ll[1],ll[2:]))
sentence=[]
print("printing lines")
print(lines)
for ll in lines:
    temp=[]
    for j in ll[1]:
        if j in tags:
            temp.append(j)
    sentence.append((ll[0],temp))

print("\n\ndata")

print(tags)

print("\n\nwhwords")
print(whwords)
print("\n\n whword probability")

print(whwordsprob)

print("\n\n Your sentence:")
print(sentence)
question=(str(input("enter question :"))).split()

print(question)

que=remove(sentence,question)
print(que)
print(sentence)

ans=askq(remove(sentence,question),question[0])

print("\nanswer\n")
print(ans)

