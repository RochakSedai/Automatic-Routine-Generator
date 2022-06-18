from routine.models import Computer_First,Computer_Second,Computer_Third,Computer_Fourth, Electrical_First, Electrical_Second, Electrical_Third, Electrical_Fourth
from .db_code import code_db_calc, input_lst




def LecturerCode(batch):
    if batch == 375:
        c = Computer_Third.objects.all()
        #print(c)
        

        #lab_lst = [36, 39, 42]
        #lab_lecturer = [[1,2,4], [4,2,5], [1,2,3]]
        #lab_room = [['Computer','Computer'],['Computer','Computer'],['Computer','Computer']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics''Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        
        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)
        # print(codeLst)
        # print(lecCodeLst)
        # print(lectId)
        # print(lab_room)
        # print(lab_lecturer)
        # print(lab_lst)
        # print(mylist1)
        # print(mylist3)
        # print(mylist2)

        #mylist1 = [[1, 2], [3, 4], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [23, 24],[25, 26], [27, 28], [29, 30], [31, 32]]  # Double Class
        #mylist2 = [[34, 35, 36], [37, 38, 39], [40, 41, 42]]  # Lab
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0
        #mylist3 = [[5], [22], [33]]  # Single Period Class


    elif batch == 376:
        # codeLst = [6,10,15,20,24,28,32,33,34]
        # lecCodeLst = ['AS','BK','SKS','BB','DK','SKR','DMG','PPB','RG','DG','RN','PG']
        # lectId = [8,9,10,1,15,14,4,13,16,11,30,19]

        c = Computer_Second.objects.all()
        #print(c)

        
        # x = 0
        # codeLst1 = []
        # codeLst = []
        # lecCodeLst = []
        # lectId = []
        # for code in c:
        #     #print(code.Lecturer_Id)
        #     lectId.append(code.Lecturer_Id)
        #     #print(code.Lecturer_Code)
        #     lecCodeLst.append(code.Lecturer_Code)
        #     #print(code.Lecturer_Period)
        #     #print(codeLst)
        #     codeLst1.append(code.Lecturer_Period)
        #     if (code.Lecturer_Period)!= 0:
        #         x = x + code.Lecturer_Period
        #         codeLst.append(x)
        #     else:
        #         codeLst.append(0)



            #codeLst.append(code.Lecturer_Period)
        # print(codeLst1)
        # print(codeLst)
        # print(lecCodeLst)
        # print(lectId)

        # lab_lst = [36,38,40,42]
        # lab_lecturer = [[11,10,8,30],[8,14,1,19],[11,10,8,30],[1,19,15,16]]
        # lab_lec = [['DG+SKS','AS+RN'], ['AS+SKR','BB+PG'], ['DG+SKS','AS+RN'], ['BB+PG','DK+RG']]
        # lab_room = [['Computer','Computer'],['Instrumentation','Computer'],['Computer','Computer'],['Computer','Electrical']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']


        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)

        # lab_room1 = []
        # lab_lecturer1 = []
        # for code in c:
        #     if code.Lab_Class != '':
        #         lab_room1.append(code.Lab_Class)
        #     if code.Lab_Lec_Period != None:
        #         lab_lecturer1.append(code.Lab_Lec_Period)
        

        # lab_room = []
        # lab_lecturer = []
        # lab_lst = []
        # mylist1 = []
        # mylist3 = []
        # mylist2 = []
        # if codeLst != []:
        #     maxm = max(codeLst)
        #     for i in range(len(lab_room1)):
        #         lst1 = []
        #         lst2 = []
        #         lst1.append(lab_room1[i])
        #         lab_room.append(input_lst(input_lst(lst1)))
        #         lst2.append(lab_lecturer1[i])
        #         x = input_lst(lst2)
        #         lab_lecturer.append(list(map(int, x)))

        #         lab_lst.append(maxm+2)
        #         maxm = maxm + 2


            
        #     period = 0
        #     for i in range(len(codeLst)):
        #         #print(period)
        #         m = codeLst[i]
        #         #print(m)
        #         if m != 0:
        #             value = codeLst1[i]
        #             #print(value)
        #             #print(lectId[i])
        #             if lectId[i] == 4:
        #                 while(period < m):
        #                     if ((m-period) > 2):
        #                         period_lec_list = []
        #                         period += 1
        #                         period_lec_list.append(period)
        #                         period += 1
        #                         period_lec_list.append(period)
        #                         mylist1.append(period_lec_list)
        #                     else:

        #                         period_tut_list = []
        #                         period += 1
        #                         period_tut_list.append(period)
        #                         mylist3.append(period_tut_list)
        #                         period_tut_list = []
        #                         period += 1
        #                         period_tut_list.append(period)
        #                         mylist3.append(period_tut_list)

        #             else:
        #                 y = value % 2
        #                 if y == 1:
        #                     #print(period)
        #                     while(period < m):
        #                         if ((m-period) > 1):
        #                             period_lec_list = []
        #                             period += 1
        #                             period_lec_list.append(period)
        #                             period += 1
        #                             period_lec_list.append(period)
        #                             mylist1.append(period_lec_list)
        #                         else:
        #                             period += 1
        #                             period_tut_list = []
        #                             period_tut_list.append(period)
        #                             mylist3.append(period_tut_list)
        #                 else:
        #                     #print(period)
        #                     while(period < m):
        #                         if ((m-period) > 1):
        #                             period_lec_list = []
        #                             period += 1
        #                             period_lec_list.append(period)
        #                             period += 1
        #                             period_lec_list.append(period)
        #                             mylist1.append(period_lec_list)


        #             period = m
        #         else:
        #             pass

        #     for i in range(len(lab_lst)):
        #         m = lab_lst[i]
        #         while(period < m):
        #             if ((m-period) > 1):
        #                 period_lab_list = []
        #                 period += 1
        #                 period_lab_list.append(period)
        #                 period += 1
        #                 period_lab_list.append(period)
        #                 mylist2.append(period_lab_list)        
        
        # print(codeLst)
        # print(lecCodeLst)
        # print(lectId)
        # print(lab_room)
        # print(lab_lecturer)
        # print(lab_lst)
        # print(mylist1)
        # print(mylist3)
        # print(mylist2)

        

        #mylist1 = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[16,17],[18,19],[21,22],[23,24],[25,26],[27,28],[29,30]] #Double class
        #mylist2 = [[35,36],[37,38],[39,40],[41,42]] #labs
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0
        #mylist3 = [[15],[20],[31],[32],[33],[34]] #single period

    elif batch == 374:

        # codeLst = [6,12,18,23,26,32,33]
        # lecCodeLst = ['SS','SP','PG','PS','RP','AK','Supervisor', 'BB', 'KB']
        # lectId = [     18,  2,   19,  20,  21,  22,   29,           1,   31]

        c = Computer_Fourth.objects.all()
        #print(c)
        

        # lab_lst = [36, 39, 42]
        # lab_lecturer = [[29],[20,18,19,31], [18,1,22,31]]
        # lab_lec = [['Supervisor'], ['PS+SS','PG+KB'], ['SS+BB','AK+KB']]
        # lab_room = [['Project', 'Project'], ['Computer','Computer'], ['Computer', 'Computer']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']

        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)
        # print(codeLst)
        # print(lecCodeLst)
        # print(lectId)
        # print(lab_room)
        # print(lab_lecturer)
        # print(lab_lst)
        # print(mylist1)
        # print(mylist3)
        # print(mylist2)
        

        #mylist1 = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16],[17,18],[19,20],[21,22],[24,25],[27,28],[29,30],[31,32]]
        #mylist2 = [[37,38,39],[40,41,42],[34,35,36]]
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0
        #mylist3 = [[33],[23],[26]]

    elif batch == 377:
        # codeLst = [5, 12, 16, 19, 23, 25, 27, 28, 29, 30]
        # lecCodeLst = ['CD','MLP','BRM','DG','RPD','NRB', 'BK', 'TEST','PL', 'RP', 'SN']
        # lectId = [     23,   24,   25,  11,   26,   27,    9,    28,   17,  32,    33]

        c = Computer_First.objects.all()
        #print(c)
        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)
        # print(codeLst)
        # print(lecCodeLst)
        # print(lectId)
        # print(lab_room)
        # print(lab_lecturer)
        # print(lab_lst)
                    

        #lab_lst = [33,36,39,42]
        #lab_lecturer = [[17,32], [17,32], [26,27,24,33], [26,27,25]]
        #lab_lec = [[]]
        #lab_room = [['Drawing','Workshop'],['Drawing','Workshop'],['Chemistry','Thermodynamics'],['Chemistry','Electronics']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']

        

        # print(mylist1)
        # print(mylist3)
        # print(mylist2)


        #mylist1 =[[1, 2], [3, 4], [6,7], [8,9], [10,11], [13, 14], [15, 16], [17, 18], [20, 21], [22, 23], [24, 25], [26, 27]]
        #mylist2 =[[31,32,33], [34,35,36], [37,38,39], [40,41,42]]
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0
        #mylist3= [[5],[12],[19], [28], [29], [30]]


    #for elec 1st year
    elif batch == 277:
        # codeLst = [4, 11, 15, 18, 22, 24, 27, 28, 29, 30]
        # lecCodeLst = ['CD','MLP','BRM','DG','RPD','NRB', 'BK', 'TEST','RS', 'RP','PL','SN', 'NK']
        # lectId = [     23,  24,   25,   11,  26,    27,   9,     28,   12,   32,  17,  33,   34]

        c = Electrical_First.objects.all()
        #print(c)
        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)
        # print(codeLst)
        # print(lecCodeLst)
        # print(lectId)
        # print(lab_room)
        # print(lab_lecturer)
        # print(lab_lst)
        # print(mylist1)
        # print(mylist3)
        # print(mylist2)

        # lab_lst = [33,36,39,42]
        # lab_lecturer = [[12,17,32], [12,17,32], [26,27,24,33], [26,27,25,34]]
        # lab_lec = [['RS+PL','RP'],['RS+PL','RP'],['RPD+NRB','MLP+SN'],['RPD+NRB','BRM+NK']]
        # lab_room = [['Drawing','Workshop'],['Drawing','Workshop'],['Chemistry','Thermodynamics'],['Chemistry','Electronics']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']


        #mylist1 =[[1, 2], [3, 4], [5,6], [7,8], [9,10], [12,13], [14,15], [16, 17], [19,20], [21, 22], [23, 24], [25, 26]]
        #mylist2 =[[31,32,33], [34,35,36], [37,38,39], [40,41,42]]
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0
        #mylist3= [[11],[18],[27], [28], [29], [30]]




    #for elec 2nd year
    elif batch == 276:
        # codeLst=[6,11,17,20,26,28,33]
        # lecCodeLst=['TN','DG','AS','BK','DK','PPB','SKR', 'RG', 'GT', 'SKS', 'RN', 'BRM']
        # lectId=[     35,  11,   8,  9,   15,   13,  14,    16,    36,   10,   30,    25]
        c = Electrical_Second.objects.all()
        #print(c)
        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)
        # print(codeLst)
        # print(lecCodeLst)
        # print(lectId)
        # print(lab_room)
        # print(lab_lecturer)
        # print(lab_lst)
        # print(mylist1)
        # print(mylist3)
        # print(mylist2)

        # lab_lst =[36,39,42]
        # lab_lecturer=[[15,16,36,14],[11,10,30,8],[11,10,25,8]]
        # lab_lec =[['DK+RG','GT+SKR'],['DG+SKS','RN+AS'],['DG+SKS','BRM'+'AS']]
        # lab_room=[['Electrical','Instrumentation'],['Computer','Computer'],['Computer','Computer']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']



        #mylist1=[[1,2],[3,4],[5,6],[7,8],[9,10],[12,13],[14,15],[16,17],[18,19],[21,22],[23,24],[25,26],[27,28],[29,30],[31,32]]
        #mylist2=[[34,35,36],[37,38,39],[40,41,42]]
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0
        #mylist3=[[11],[20],[33]]

    # for elec 3rd year
    elif batch == 275:
        # codeLst=[6,11,16,22,26,30,32,33]
        # lecCodeLst=['RUG','SKS','GCJ','RG','SD','NS','AD','YB','SL','IMS','RN','TN','GT']
        # lectId= [    37,    10,   44,   16,  45,  47,  46,  7,   48,  49,  30,   35,  36]
        c = Electrical_Third.objects.all()
        #print(c)
        
        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)
        # print(codeLst)
        # print(lecCodeLst)
        # print(lectId)
        # print(lab_room)
        # print(lab_lecturer)
        # print(lab_lst)
        # print(mylist1)
        # print(mylist3)
        # print(mylist2)


        #lab_lst =[36,39,42]
        #lab_lecturer=[[37,48,47,46],[49,30,10],[35,36,16,49]]
        lab_lec =[['RuG+SL','NS+AD'],['IMS+RN','SKS'],['TN+GT','RG+IMS']]
        #lab_room=[['Electrical','Hydropower'],['Computer','Electrical'],['Computer','Electrical']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project', 'Hydropower', 'Switchgear', 'Class1', 'Class2']


        #mylist1=[[1,2],[3,4],[5,6],[7,8],[9,10],[12,13],[14,15],[17,18],[19,20],[21,22],[23,24],[25,26],[27,28],[29,30],[31,32]]
        #mylist2=[[34,35,36],[37,38,39],[40,41,42]]
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0
        #mylist3=[[11],[16],[33]]



    # for elec 4th year
    elif batch==274:
        # codeLst = [6,12,18,24]
        # lecCodeLst = ['AJS','RUG','TN','DK','APS','PV','YB','RP','SDH','AB','TBM','Supervisor1']
        # lectId = [     38,   37,   35,  15,  39,   40,   7,  21,   41,  42,  43,    50]

        c = Electrical_Fourth.objects.all()
        #print(c)
        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)
        # print(codeLst)
        # print(lecCodeLst)
        # print(lectId)
        # print(lab_room)
        # print(lab_lecturer)
        # print(lab_lst)
        # print(mylist1)
        # print(mylist3)
        # print(mylist2)

        

        # lab_lst = [27,30,33,36, 39, 42]
        # lab_lecturer = [[39,40,7],[50], [21], [39,41,40,7], [37,42,35,43], [37,42,35,43]]
        # lab_lec = [['APS','PV+YB'], ['Supervisor1'],['RP'],['APS+SDH','PV+YB'],['RUG+AB','TN+TBM'],['RUG+AB','TN+TBM']]
        # lab_room = [['Class1', 'Class2'], ['Project','Project'],['Class1'],['Class1', 'Class2'],['Hydropower', 'Switchgear'],['Hydropower', 'Switchgear']]
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']

        
        #mylist1 = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16],[17,18],[19,20],[21,22],[23,24]]
        #mylist2 = [[25,26,27],[28,29,30],[31,32,33],[34,35,36],[37,38,39],[40,41,42]]
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0
        #mylist3 = []



    return codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len


def allLecturerCode():
    #lec_name = ['BB', 'SP', 'ML', 'DMG', 'SLS', 'JJ', 'YB', 'AS','BK','SKS', 'DG', 'RS', 'PPB', 'SKR','DK','RG', 'PL', 'SS','PG','PS','RPh','AK','CD','MLP','BRM','RPD','NRB', 'TEST', 'Supervisor','RN', 'KB','RP', 'SN', 'NK', 'TN', 'GT', 'RUG', 'AJS', 'APS', 'PV', 'SDH', 'AB', 'TBM', 'GCJ', 'SD', 'AD', 'NS','SL', 'IMS']
    #lec_Id =  [  1,    2,    3,     4,     5,     6,    7,    8,   9,   10,   11,   12,    13,    14,  15,  16,   17,   18,  19,  20,  21,  22,  23,  24,    25,   26,   27,    28,       29,        30,   31,  32,  33,   34,    35,   36,   37,    38,    39,   40,    41,    42,  43,     44,    45,   46,  47,  48,    49 ]

    lec_name = ['DG', 'BK', 'DMG', 'BB', 'BRM', 'YB', 'SG', 'TN', 'CD', 'ST', 'ML', 'RC', 'NK', 'RUG', 'SM', 'RN', 'GT', 'RBT', 'PPB', 'SKS', 'DK', 'BBT', 'ARK', 'MLP', 'PL', 'JB', 'AS', 'AKG', 'VKY', 'RKY', 'RP', 'AK', 'SLS', 'RKS', 'JJ', 'SuperVisor', 'SS', 'NG', 'SP']
    lec_Id =   [ 1,     2,    3,     4,     5,    6,    7,   8,     9,    10,   11,   12,   13,   14,    15,    16,   17,    18,    19,    20,    21,   22,    23,    24,   25,   26,  27,    28,    29,    30,   31,    32,   33,    34,   35,    36,        37,    38,   39 ]

    return lec_name, lec_Id

