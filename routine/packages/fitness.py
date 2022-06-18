from .initial_population import *
from .teacher_code import LecturerCode
import numpy as np
from copy import deepcopy
#from routine_info import saveroutine
chk=[]

def calcFitness(chk,batch):
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)

    # print(codeLst)
    # print(lecCodeLst)
    # print(lectId)
    # print(lab_room)
    # print(lab_lecturer)
    # print(lab_lst)
    # print(mylist1)
    # print(mylist3)
    # print(mylist2)
    maxm = max(codeLst)
    # print(chk)

    lecCount = [0 for i in range(len(lectId))]
    a = 0
    b = 0
    j = 0
    while(j <= (len(lectId)-1)):
        #print(j)
        if(a>7):
            break
        #print(codeLst[j])
        elif codeLst[j] != 0:
           #print(chk[a])
            if(chk[a] <= codeLst[j]):
                lecCount[j] += 1
                #print(lecCount)
                j=0
                a=a+1
            elif chk[a] >=(maxm+1):
                b += 1
                a += 1
                j=0
                pass
        
            else: 
                j += 1
                pass
        else:
            j += 1
            pass

    #print(lecCount)

    score=0
    for j in range(len(lecCount)):
        if lecCount[j]>2:
            conflict = 0
            #print(lecCount[j])
            conflict=(lecCount[j]-2)
            score=score-(10*conflict)   # conflict = -10
            #print(score)

    #print("this is fitness")
    lab_count = 0
    mylist2_2 = deepcopy(mylist2)
    mylist2_2 = np.array(mylist2_2)
    mylist2_2 = mylist2_2.flatten()
    # print(mylist2_2)
    score_lab=0
    for i in range(8):
        if chk[i] in mylist2_2:
            lab_count+=1
    if lab_count>lab_len:
        b=lab_count-lab_len
        score_lab=score_lab-(b*10)
    score=score+score_lab

    return score
     
