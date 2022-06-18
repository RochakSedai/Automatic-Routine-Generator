from .initial_population import PopulationGeneration, overal_routine, oneDArray
from .fitness import calcFitness
from .roulette_selection import selection
from .crossover import partial_crossover
import pickle
from .teacherconflict import lec_checkconflict
from .lab_conflict import lab_checkconflict
from .teacher_code import LecturerCode
#from routine_info import saveroutine
#from teachermatrix import teacher_matrix
  
def generator(batch):

    #allLecturerMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(1, 29)] 
    score_lst = []

    routine_lst = []

    # semester_routine = float(input("Enter the batch number:"))

    for i in range(6):
        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)
        #print(lab_len)
        print(mylist1)
        print(mylist2)
        print(mylist3)
        routine = PopulationGeneration(mylist1, mylist2, mylist3)

        print(routine)

        

        # fitness calculation

        matrix = []
        matrix1 = []
        matrix = oneDArray(routine)   # generates onedimensional of routine
        #print(matrix)
        matrix1 = oneDArray(matrix)   # generates onedimensional of population
        #print(matrix1)
        #print(len(matrix1))

        print(matrix1)

        arr = [[0 for q in range(8)] for p in range(6)]
        count = 0
        for p in range(6):
            for q in range(8):
                arr[p][q] = matrix1[count]
                count += 1


        #print(lst)
        lst3 = arr
        routine_lst.append(lst3)
        #print(lst3)

        # if semester_routine != 2075:
        #     teacher_matrix(lst3)


        overal_score = 480
        chk = []
        for i in range(6): 
            chk=lst3[i]
            #print(chk)
            score = calcFitness(chk,batch) 
            #print(score)
            overal_score += score 

        scoreconflict=0
        scoreconflict=lec_checkconflict(lst3, batch,overal_score)
        overal_score=overal_score+scoreconflict 
        if overal_score==480:
            score=[480]
            return score,lst3
        # scoreconflict1 = lab_checkconflict(lst3,batch,overal_score)
        # overal_score=overal_score+scoreconflict1
        else:
            overal_routine[i] = matrix1
            score_lst.append(overal_score)




    # selection part

    routine_lst, score_lst = selection(score_lst, routine_lst)
    # print(routine_lst)
    # print(score_lst)
    c=[]
    c.append(routine_lst)
    a=routine_lst[0].copy()
    b=routine_lst[1].copy()
    #crossover part
    i = 0
    j = 0
    count=0
    while 480 not in score_lst and count<100:
        #print('this is inside while')
        if 1:
            routine1_lst = []
            score1_lst = []
            a=routine_lst[0].copy()
            b=routine_lst[1].copy()
            routine1_lst, score1_lst = partial_crossover(a,b, lab_len,batch)
            #print("thus is crossover")
            c=0
            while(len(routine1_lst) == 0 and len(score1_lst)==0) and c<2:
               # print('this is here')
                c=c+1
                a=routine_lst[0].copy()
                b=routine_lst[1].copy()
                routine1_lst, score1_lst = partial_crossover(a,b, lab_len,batch)  

            if len(score1_lst)==0:
                score_lst,routine_lst=generator(batch)
                return score_lst,routine_lst
            if len(score1_lst)==1:
                score_lst[0]=score1_lst[0]
                routine_lst[0]= routine1_lst[0]
            else:
                for j in range(2):
                    routine_lst[j] = routine1_lst[j]
                    score_lst[j]= score1_lst[j]
            routine_lst, score_lst = selection(score_lst, routine_lst)
            count=count+1
            #print(count)
            #print(score_lst,routine_lst,'this is score list and routine list')
    return(score_lst,routine_lst)
