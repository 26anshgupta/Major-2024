from flask import Flask, jsonify
import mysql.connector
import json


app= Flask(__name__)
global data_st_xf_list, data_st_xop_list, data_sc_xf_list, data_sc_xop_list, data_obc_xf_list, data_obc_xop_list, data_ur_xf_list, data_ur_xop_list

data_st_xf_list = []
data_st_xop_list = []
data_sc_xf_list = []
data_sc_xop_list = []
data_obc_xf_list = []
data_obc_xop_list = []
data_ur_xf_list = []
data_ur_xop_list = []

# cross_origin(app)
@app.route('/', methods=['GET'])
def api():
    mydb = mysql.connector.connect(host='localhost',user='root',password= 'S@ngeeta2001', database='major')
    if mydb.is_connected():
        print("hiiii Please enter the number of vacant seats in each branch. /n")
    global cse_st_xf, cse_st_xop, cse_sc_xf, cse_sc_xop, cse_obc_xf, cse_obc_xop, cse_ur_xf, cse_ur_xop
    global it_st_xf, it_st_xop, it_sc_xf, it_sc_xop, it_obc_xf, it_obc_xop, it_ur_xf, it_ur_xop
    global ece_st_xf, ece_st_xop, ece_sc_xf, ece_sc_xop, ece_obc_xf, ece_obc_xop, ece_ur_xf, ece_ur_xop
    global ei_st_xf, ei_st_xop, ei_sc_xf, ei_sc_xop, ei_obc_xf, ei_obc_xop, ei_ur_xf, ei_ur_xop
    global me_st_xf, me_st_xop, me_sc_xf, me_sc_xop, me_obc_xf, me_obc_xop, me_ur_xf, me_ur_xop
    global ee_st_xf, ee_st_xop, ee_sc_xf, ee_sc_xop, ee_obc_xf, ee_obc_xop, ee_ur_xf, ee_ur_xop
    global bm_st_xf, bm_st_xop, bm_sc_xf, bm_sc_xop, bm_obc_xf, bm_obc_xop, bm_ur_xf, bm_ur_xop
    global ip_st_xf, ip_st_xop, ip_sc_xf, ip_sc_xop, ip_obc_xf, ip_obc_xop, ip_ur_xf, ip_ur_xop
    global ce_st_xf, ce_st_xop, ce_sc_xf, ce_sc_xop, ce_obc_xf, ce_obc_xop, ce_ur_xf, ce_ur_xop

    print("Computer Science  and Engineering Branch: ")
    print("Vacancy in ST category")
    print("XF")
    cse_st_xf = 0
    print("XOP")
    cse_st_xop = 0
    print("Vacancy in SC category")
    print("XF")
    cse_sc_xf = 0
    print("XOP")
    cse_sc_xop = 1
    print("Vacancy in OBC category: ")
    print("XF")
    cse_obc_xf = 0
    print("XOP")
    cse_obc_xop = 0
    print("Vacancy in General category: ")
    print("XF")
    cse_ur_xf = 0
    print("XOP")
    cse_ur_xop = 0

    print("Information and Technology Branch: ")
    print("Vacancy in ST category")
    print("XF")
    it_st_xf = 1
    print("XOP")
    it_st_xop = 0
    print("Vacancy in SC category")
    print("XF")
    it_sc_xf = 0
    print("XOP")
    it_sc_xop = 1
    print("Vacancy in OBC category: ")
    print("XF")
    it_obc_xf = 0
    print("XOP")
    it_obc_xop = 0
    print("Vacancy in General category: ")
    print("XF")
    it_ur_xf = 0
    print("XOP")
    it_ur_xop = 0

    print("Electronics and Telecommunication Branch: ")
    print("Vacancy in ST category")
    print("XF")
    ece_st_xf = 0
    print("XOP")
    ece_st_xop = 0
    print("Vacancy in SC category")
    print("XF")
    ece_sc_xf = 0
    print("XOP")
    ece_sc_xop = 1
    print("Vacancy in OBC category: ")
    print("XF")
    ece_obc_xf = 1
    print("XOP")
    ece_obc_xop = 0
    print("Vacancy in General category: ")
    print("XF")
    ece_ur_xf = 0
    print("XOP")
    ece_ur_xop = 0

    print("Electronics and Instrumentation Branch: ")
    print("Vacancy in ST category")
    print("XF")
    ei_st_xf = 0
    print("XOP")
    ei_st_xop = 0
    print("Vacancy in SC category")
    print("XF")
    ei_sc_xf = 0
    print("XOP")
    ei_sc_xop = 0
    print("Vacancy in OBC category: ")
    print("XF")
    ei_obc_xf = 0
    print("XOP")
    ei_obc_xop = 1
    print("Vacancy in General category: ")
    print("XF")
    ei_ur_xf = 0
    print("XOP")
    ei_ur_xop = 0

    print("Electrical Branch: ")
    print("Vacancy in ST category")
    print("XF")
    ee_st_xf = 1
    print("XOP")
    ee_st_xop = 0
    print("Vacancy in SC category")
    print("XF")
    ee_sc_xf = 0
    print("XOP")
    ee_sc_xop = 0
    print("Vacancy in OBC category: ")
    print("XF")
    ee_obc_xf = 0
    print("XOP")
    ee_obc_xop = 0
    print("Vacancy in General category: ")
    print("XF")
    ee_ur_xf = 0
    print("XOP")
    ee_ur_xop = 1

    print("Civil Branch: ")
    print("Vacancy in ST category")
    print("XF")
    ce_st_xf = 0
    print("XOP")
    ce_st_xop = 2
    print("Vacancy in SC category")
    print("XF")
    ce_sc_xf = 0
    print("XOP")
    ce_sc_xop = 0
    print("Vacancy in OBC category: ")
    print("XF")
    ce_obc_xf = 0
    print("XOP")
    ce_obc_xop = 0
    print("Vacancy in General category: ")
    print("XF")
    ce_ur_xf = 0
    print("XOP")
    ce_ur_xop = 2

    print("Industrial and Production Branch: ")
    print("Vacancy in ST category")
    print("XF")
    ip_st_xf = 0
    print("XOP")
    ip_st_xop = 0
    print("Vacancy in SC category")
    print("XF")
    ip_sc_xf = 0
    print("XOP")
    ip_sc_xop = 0
    print("Vacancy in OBC category: ")
    print("XF")
    ip_obc_xf = 0
    print("XOP")
    ip_obc_xop = 0
    print("Vacancy in General category: ")
    print("XF")
    ip_ur_xf = 0
    print("XOP")
    ip_ur_xop = 1

    print("Bio Medical Branch: ")
    print("Vacancy in ST category")
    print("XF")
    bm_st_xf = 0
    print("XOP")
    bm_st_xop = 0
    print("Vacancy in SC category")
    print("XF")
    bm_sc_xf = 0
    print("XOP")
    bm_sc_xop = 0
    print("Vacancy in OBC category: ")
    print("XF")
    bm_obc_xf = 0
    print("XOP")
    bm_obc_xop = 0
    print("Vacancy in General category: ")
    print("XF")
    bm_ur_xf = 0
    print("XOP")
    bm_ur_xop = 0

    print("Mechnical Branch: ")
    print("Vacancy in ST category")
    print("XF")
    global me_st_xf 
    me_st_xf = 0
    print(me_st_xf)
    print("XOP")
    me_st_xop = 0
    print("Vacancy in SC category")
    print("XF")
    me_sc_xf = 0
    print("XOP")
    me_sc_xop = 0
    print("Vacancy in OBC category: ")
    print("XF")
    me_obc_xf = 0
    print("XOP")
    me_obc_xop = 0
    print("Vacancy in General category: ")
    print("XF")
    me_ur_xf = 0
    print("XOP")
    me_ur_xop = 0



    print(mydb.connection_id)
    cursor = mydb.cursor()

    s = " SELECT * from data_major_final ; "
    cursor.execute(s)
    data_common = cursor.fetchall()
    # print(data_common)
    # for i in data_common :
    #     print(i)

    
    # print(data_st_xf)

    

    # s = " SELECT * from data_major_final where category= 'SC' and Alloted_Class='XF' ORDER BY Theory1 DESC; "
    # cursor.execute(s)
    # data_sc_xf = cursor.fetchall()
    # # print(data_st_xf)

    # s = " SELECT * from data_major_final where category= 'SC' ORDER BY Theory1 DESC ; "
    # cursor.execute(s)
    # data_sc_xop = cursor.fetchall()

    # s = " SELECT * from data_major_final where category= 'OBC' and Alloted_Class='XF' ORDER BY Theory1 DESC ; "
    # cursor.execute(s)
    # data_obc_xf = cursor.fetchall()
    # # print(data_st_xf)

    # s = " SELECT * from data_major_final where category= 'OBC' ORDER BY Theory1 DESC ; "
    # cursor.execute(s)
    # data_obc_xop = cursor.fetchall()

    # s = " SELECT * from data_major_final where category= 'UR' and Alloted_Class='XF'  ORDER BY Theory1 DESC; "
    # cursor.execute(s)
    # data_ur_xf = cursor.fetchall()
    # # print(data_st_xf)

    # s = " SELECT * from data_major_final where category= 'UR' ORDER BY Theory1 DESC ; "
    # cursor.execute(s)
    # data_ur_xop = cursor.fetchall()


#     list = []
    
#     for j in data_common:
#         # print(j)
#         d = {}
#         for i,col in enumerate(cursor.description):
#             # print(col[0])
#             # print(j[i])
#             d[col[0]] = j[i]
#             # print(d)
#         list.append(d)



    selected = []
    global data_st_xf_list, data_st_xop_list, data_sc_xf_list, data_sc_xop_list, data_obc_xf_list, data_obc_xop_list, data_ur_xf_list, data_ur_xop_list
    # data_st_xf_list = []
    # data_st_xop_list = []
    # data_sc_xf_list = []
    # data_sc_xop_list = []
    # data_obc_xf_list = []
    # data_obc_xop_list = []
    # data_ur_xf_list = []
    # data_ur_xop_list = []

    
    
    def increaseFunction():
        global cse_st_xf, cse_st_xop, cse_sc_xf, cse_sc_xop, cse_obc_xf, cse_obc_xop, cse_ur_xf, cse_ur_xop
        global it_st_xf, it_st_xop, it_sc_xf, it_sc_xop, it_obc_xf, it_obc_xop, it_ur_xf, it_ur_xop
        global ece_st_xf, ece_st_xop, ece_sc_xf, ece_sc_xop, ece_obc_xf, ece_obc_xop, ece_ur_xf, ece_ur_xop
        global ei_st_xf, ei_st_xop, ei_sc_xf, ei_sc_xop, ei_obc_xf, ei_obc_xop, ei_ur_xf, ei_ur_xop
        global me_st_xf, me_st_xop, me_sc_xf, me_sc_xop, me_obc_xf, me_obc_xop, me_ur_xf, me_ur_xop
        global ee_st_xf, ee_st_xop, ee_sc_xf, ee_sc_xop, ee_obc_xf, ee_obc_xop, ee_ur_xf, ee_ur_xop
        global bm_st_xf, bm_st_xop, bm_sc_xf, bm_sc_xop, bm_obc_xf, bm_obc_xop, bm_ur_xf, bm_ur_xop
        global ip_st_xf, ip_st_xop, ip_sc_xf, ip_sc_xop, ip_obc_xf, ip_obc_xop, ip_ur_xf, ip_ur_xop
        global ce_st_xf, ce_st_xop, ce_sc_xf, ce_sc_xop, ce_obc_xf, ce_obc_xop, ce_ur_xf, ce_ur_xop
        d['allotment_status']= "Allotted"
        Allotted_category = d['Alloted_Category']
        Allotted_class = d['Alloted_Class']
        current_branch = d['Current_branch']
        # print(Allotted_category)
        # print(Allotted_class)
        # print(current_branch)
        if current_branch == 'COMPUTER SCIENCE & ENGINEERING':
            if Allotted_category == 'ST' and Allotted_class == 'XF':
                cse_st_xf += 1   
                print("RTNESSSSSSSSHHHHHHHHHH")
            if Allotted_category == 'ST' and Allotted_class == 'XOP':
                cse_st_xop += 1
            if Allotted_category == 'SC' and Allotted_class == 'XF':
                cse_sc_xf += 1
            if Allotted_category == 'SC' and Allotted_class == 'XOP':
                cse_sc_xop += 1
            if Allotted_category == 'OBC' and Allotted_class == 'XF':
                cse_obc_xf += 1
            if Allotted_category == 'OBC' and Allotted_class == 'XOP':
                cse_obc_xop += 1
            if Allotted_category == 'UR' and Allotted_class == 'XF':
                cse_ur_xf += 1
            if Allotted_category == 'UR' and Allotted_class == 'XOP':
                cse_ur_xop += 1
        if current_branch == 'INFORMATION TECHNOLOGY':
            if Allotted_category == 'ST' and Allotted_class == 'XF':
                it_st_xf += 1
            if Allotted_category == 'ST' and Allotted_class == 'XOP':
                it_st_xop += 1
            if Allotted_category == 'SC' and Allotted_class == 'XF':
                it_sc_xf += 1
            if Allotted_category == 'SC' and Allotted_class == 'XOP':
                it_sc_xop += 1
            if Allotted_category == 'OBC' and Allotted_class == 'XF':
                it_obc_xf += 1
            if Allotted_category == 'OBC' and Allotted_class == 'XOP':
                it_obc_xop += 1
            if Allotted_category == 'UR' and Allotted_class == 'XF':
                it_ur_xf += 1
            if Allotted_category == 'UR' and Allotted_class == 'XOP':
                it_ur_xop += 1
        if current_branch == 'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING':
            if Allotted_category == 'ST' and Allotted_class == 'XF':
                ece_st_xf += 1
            if Allotted_category == 'ST' and Allotted_class == 'XOP':
                ece_st_xop += 1
            if Allotted_category == 'SC' and Allotted_class == 'XF':
                ece_sc_xf += 1
            if Allotted_category == 'SC' and Allotted_class == 'XOP':
                ece_sc_xop += 1
            if Allotted_category == 'OBC' and Allotted_class == 'XF':
                ece_obc_xf += 1
            if Allotted_category == 'OBC' and Allotted_class == 'XOP':
                ece_obc_xop += 1
            if Allotted_category == 'UR' and Allotted_class == 'XF':
                ece_ur_xf += 1
            if Allotted_category == 'UR' and Allotted_class == 'XOP':
                ece_ur_xop += 1
        if current_branch == 'ELECTRONICS & INSTRUMENTATION ENGINEERING':
            if Allotted_category == 'ST' and Allotted_class == 'XF':
                ei_st_xf += 1
            if Allotted_category == 'ST' and Allotted_class == 'XOP':
                ei_st_xop += 1
            if Allotted_category == 'SC' and Allotted_class == 'XF':
                ei_sc_xf += 1
            if Allotted_category == 'SC' and Allotted_class == 'XOP':
                ei_sc_xop += 1
            if Allotted_category == 'OBC' and Allotted_class == 'XF':
                ei_obc_xf += 1
            if Allotted_category == 'OBC' and Allotted_class == 'XOP':
                ei_obc_xop += 1
            if Allotted_category == 'UR' and Allotted_class == 'XF':
                ei_ur_xf += 1
            if Allotted_category == 'UR' and Allotted_class == 'XOP':
                ei_ur_xop += 1
        if current_branch == 'ELECTRICAL ENGINEERING':
            if Allotted_category == 'ST' and Allotted_class == 'XF':
                ee_st_xf += 1
            if Allotted_category == 'ST' and Allotted_class == 'XOP':
                ee_st_xop += 1
            if Allotted_category == 'SC' and Allotted_class == 'XF':
                ee_sc_xf += 1
            if Allotted_category == 'SC' and Allotted_class == 'XOP':
                ee_sc_xop += 1
            if Allotted_category == 'OBC' and Allotted_class == 'XF':
                ee_obc_xf += 1
            if Allotted_category == 'OBC' and Allotted_class == 'XOP':
                ee_obc_xop += 1
            if Allotted_category == 'UR' and Allotted_class == 'XF':
                ee_ur_xf += 1
            if Allotted_category == 'UR' and Allotted_class == 'XOP':
                ee_ur_xop += 1
        if current_branch == 'INDUSTRIAL & PRODUCTION ENGINEERING':
            if Allotted_category == 'ST' and Allotted_class == 'XF':
                ip_st_xf = ip_st_xf+1
            if Allotted_category == 'ST' and Allotted_class == 'XOP':
                ip_st_xop = ip_st_xop+1
            if Allotted_category == 'SC' and Allotted_class == 'XF':
                ip_sc_xf = ip_sc_xf+1
            if Allotted_category == 'SC' and Allotted_class == 'XOP':
                ip_sc_xop = ip_sc_xop+1
            if Allotted_category == 'OBC' and Allotted_class == 'XF':
                ip_obc_xf = ip_obc_xf+1
            if Allotted_category == 'OBC' and Allotted_class == 'XOP':
                ip_obc_xop = ip_obc_xop+1
            if Allotted_category == 'UR' and Allotted_class == 'XF':
                ip_ur_xf = ip_ur_xf+1
            if Allotted_category == 'UR' and Allotted_class == 'XOP':
                ip_ur_xop = ip_ur_xop+1
        if current_branch == 'CIVIL ENGINEERING':
            if Allotted_category == 'ST' and Allotted_class == 'XF':
                ce_st_xf = ce_st_xf+1
            if Allotted_category == 'ST' and Allotted_class == 'XOP':
                ce_st_xop = ce_st_xop+1
            if Allotted_category == 'SC' and Allotted_class == 'XF':
                ce_sc_xf = ce_sc_xf+1
            if Allotted_category == 'SC' and Allotted_class == 'XOP':
                ce_sc_xop = ce_sc_xop+1
            if Allotted_category == 'OBC' and Allotted_class == 'XF':
                ce_obc_xf = ce_obc_xf+1
            if Allotted_category == 'OBC' and Allotted_class == 'XOP':
                ce_obc_xop = ce_obc_xop+1
            if Allotted_category == 'UR' and Allotted_class == 'XF':
                ce_ur_xf = ce_ur_xf+1
            if Allotted_category == 'UR' and Allotted_class == 'XOP':
                ce_ur_xop = ce_ur_xop+1
        if current_branch == 'BIOMEDICAL ENGINEERING':
            if Allotted_category == 'ST' and Allotted_class == 'XF':
                bm_st_xf = bm_st_xf+1
            if Allotted_category == 'ST' and Allotted_class == 'XOP':
                bm_st_xop = bm_st_xop+1
            if Allotted_category == 'SC' and Allotted_class == 'XF':
                bm_sc_xf = bm_sc_xf+1
            if Allotted_category == 'SC' and Allotted_class == 'XOP':
                bm_sc_xop = bm_sc_xop+1
            if Allotted_category == 'OBC' and Allotted_class == 'XF':
                bm_obc_xf = bm_obc_xf+1
            if Allotted_category == 'OBC' and Allotted_class == 'XOP':
                bm_obc_xop = bm_obc_xop+1
            if Allotted_category == 'UR' and Allotted_class == 'XF':
                bm_ur_xf = bm_ur_xf+1
            if Allotted_category == 'UR' and Allotted_class == 'XOP':
                bm_ur_xop = bm_ur_xop+1
        if current_branch == 'MECHANICAL ENGINEERING':
            if Allotted_category == 'ST' and Allotted_class == 'XF':
                # print("hiiihihihihihhihihihihihihihihihihi")
                # global me_st_xf
                me_st_xf = me_st_xf+1
                # print("hiiiiii")
                # print(me_st_xf)
            if Allotted_category == 'ST' and Allotted_class == 'XOP':
                me_st_xop = me_st_xop+1
            if Allotted_category == 'SC' and Allotted_class == 'XF':
                me_sc_xf = me_sc_xf+1
            if Allotted_category == 'SC' and Allotted_class == 'XOP':
                me_sc_xop = me_sc_xop+1
            if Allotted_category == 'OBC' and Allotted_class == 'XF':
                me_obc_xf = me_obc_xf+1
            if Allotted_category == 'OBC' and Allotted_class == 'XOP':
                me_obc_xop = me_obc_xop+1
            if Allotted_category == 'UR' and Allotted_class == 'XF':
                me_ur_xf = me_ur_xf+1
            if Allotted_category == 'UR' and Allotted_class == 'XOP':
                me_ur_xop = me_ur_xop+1
    
          
    def ST_XF():
        global cse_st_xf, cse_st_xop, cse_sc_xf, cse_sc_xop, cse_obc_xf, cse_obc_xop, cse_ur_xf, cse_ur_xop
        global it_st_xf, it_st_xop, it_sc_xf, it_sc_xop, it_obc_xf, it_obc_xop, it_ur_xf, it_ur_xop
        global ece_st_xf, ece_st_xop, ece_sc_xf, ece_sc_xop, ece_obc_xf, ece_obc_xop, ece_ur_xf, ece_ur_xop
        global ei_st_xf, ei_st_xop, ei_sc_xf, ei_sc_xop, ei_obc_xf, ei_obc_xop, ei_ur_xf, ei_ur_xop
        global me_st_xf, me_st_xop, me_sc_xf, me_sc_xop, me_obc_xf, me_obc_xop, me_ur_xf, me_ur_xop
        global ee_st_xf, ee_st_xop, ee_sc_xf, ee_sc_xop, ee_obc_xf, ee_obc_xop, ee_ur_xf, ee_ur_xop
        global bm_st_xf, bm_st_xop, bm_sc_xf, bm_sc_xop, bm_obc_xf, bm_obc_xop, bm_ur_xf, bm_ur_xop
        global ip_st_xf, ip_st_xop, ip_sc_xf, ip_sc_xop, ip_obc_xf, ip_obc_xop, ip_ur_xf, ip_ur_xop
        global ce_st_xf, ce_st_xop, ce_sc_xf, ce_sc_xop, ce_obc_xf, ce_obc_xop, ce_ur_xf, ce_ur_xop
        j=0
        
        while(j < len(data_st_xf) ):
            print(j, "j")
            item = data_st_xf[j]
            global d
            d = {}
            for i,col in enumerate(cursor.description):
                # print(col[0])
                # print(j[i])
                d[col[0]] = item[i]
            data_st_xf_list.append(d)
            # print(d['choice1']+":"+(d['allotment_result']))
            print(d)
            print(d['choice1'] ,"and", d['allotment_status'], d['Cname'])
            # if(d['choice1'] == 'INFORMATION TECHNOLOGY' and d['allotment_status']== 'Not Alloted' ):
            #     print(it_st_xf)
            #     if(it_st_xf>0):
            #         print("YES YES YES ")
            #         selected.append(d)
            #         print(selected)
            #         d['allotment_result']="it"
            #         d['allotment_status']= "Allotted"
            #         it_st_xf= it_st_xf-1
            #         print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status']) 
            #         increaseFunction()

            
            if(d['choice1'] == 'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status']== 'Not Alloted' ):
                print("CSSSSS")
                print(cse_st_xf)
                if(cse_st_xf>0):
                    print("appendingggggg")
                    selected.append(d)
                    cse_st_xf= cse_st_xf-1
                    print("called")
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    # data_st_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status']) 
                    increaseFunction()
            if(d['choice1'] == 'INFORMATION TECHNOLOGY' and d['allotment_status']== 'Not Alloted' ):
                print("ITTTTTTTTTTTTT")
                print(it_st_xf)
                
                if(it_st_xf>0):
                    selected.append(d) 
                    it_st_xf= it_st_xf-1
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    # data_st_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status']) 
                    increaseFunction()        
            if(d['choice1'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ece_st_xf>0):
                    selected.append(d)
                    ece_st_xf= ece_st_xf-1
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ei_st_xf>0):
                    selected.append(d)
                    ei_st_xf= ei_st_xf-1
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'ELECTRICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ee_st_xf>0):
                    selected.append(d)
                    ee_st_xf= ee_st_xf-1
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ip_st_xf>0):
                    selected.append(d)
                    ip_st_xf= ip_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['choice1'] ==  'CIVIL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ce_st_xf>0):
                    selected.append(d)
                    ce_st_xf= ce_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'BIOMEDICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    bm_st_xf= bm_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            if(d['choice1'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    me_st_xf= me_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            


            print(d['allotment_status'])
            if(d['Choice2'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print("entered  in CS coice 2")
                print(cse_st_xf)
                if(cse_st_xf>0):
                    print("CS CHOICE 2")
                    selected.append(d)
                    cse_st_xf= cse_st_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    # data_st_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()    
            if(d['Choice2'] ==  'INFORMATION TECHNOLOGY' ):
                print("entered  in IT coice 2")
                print(it_st_xf)
                if(it_st_xf>0 and d['allotment_status'] == 'Not Allotted'):
                    print("ITT CHOICE 2")
                    selected.append(d)
                    it_st_xf= it_st_xf-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    # data_st_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction()        
            if(d['Choice2'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_st_xf>0):
                    selected.append(d)
                    ece_st_xf= ece_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_st_xf>0):
                    selected.append(d)
                    ei_st_xf= ei_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_st_xf>0):
                    selected.append(d)
                    ee_st_xf= ee_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_st_xf>0):
                    selected.append(d)
                    ip_st_xf= ip_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice2'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_st_xf>0):
                    selected.append(d)
                    ce_st_xf= ce_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    bm_st_xf= bm_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    me_st_xf= me_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()



            if(d['Choice3'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_st_xf)
                if(cse_st_xf>0):
                    selected.append(d)
                    cse_st_xf= cse_st_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice3'] == 'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_st_xf)
                if(it_st_xf>0):
                    selected.append(d)
                    it_st_xf= it_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()   
            if(d['Choice3'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print("ECCC3")
                if(ece_st_xf>0 ):
                    print("ECCC 3")

                    # print("ddddddd")
                    # print("selecteeeeedddddd beforeeeee")
                    # # print(selected)
                    selected.append(d)
                    # print(d)
                    # print("selecteeeeedddddd")
                    # # print(selected)
                    ece_st_xf= ece_st_xf-1
                    #increaseFunction()
                    d['allotment_result'] = "ece"
                    d['allotment_status'] = "Allotted"
                    # data_st_xf_list.append(d)
                    print(d['Choice3']+":"+(d['allotment_result']) , d['allotment_status'])
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_st_xf>0):
                    selected.append(d)
                    ei_st_xf= ei_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_st_xf>0):
                    selected.append(d)
                    ee_st_xf= ee_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_st_xf>0):
                    selected.append(d)
                    ip_st_xf= ip_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice3'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_st_xf>0):
                    selected.append(d)
                    ce_st_xf= ce_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    bm_st_xf= bm_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    me_st_xf= me_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()


            if(d['Choice4'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_st_xf)
                if(cse_st_xf>0):
                    selected.append(d)
                    cse_st_xf= cse_st_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice4'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_st_xf)
                if(it_st_xf>0):
                    selected.append(d)
                    it_st_xf= it_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    d['allotment_result']="it"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice4'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_st_xf>0):
                    selected.append(d)
                    ece_st_xf= ece_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_st_xf>0):
                    print("EIII 4")
                    selected.append(d)
                    ei_st_xf= ei_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_st_xf>0):
                    selected.append(d)
                    ee_st_xf= ee_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_st_xf>0):
                    selected.append(d)
                    ip_st_xf= ip_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice4'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_st_xf>0):
                    selected.append(d)
                    ce_st_xf= ce_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    bm_st_xf= bm_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    me_st_xf= me_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()


            if(d['Choice5'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_st_xf)
                if(cse_st_xf>0):
                    selected.append(d)
                    cse_st_xf= cse_st_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice5'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_st_xf)
                if(it_st_xf>0):
                    selected.append(d)
                    it_st_xf= it_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_st_xf>0):
                    selected.append(d)
                    ece_st_xf= ece_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_st_xf>0):
                    selected.append(d)
                    ei_st_xf= ei_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_st_xf>0):
                    selected.append(d)
                    ee_st_xf= ee_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_st_xf>0):
                    selected.append(d)
                    ip_st_xf= ip_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice5'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_st_xf>0):
                    selected.append(d)
                    ce_st_xf= ce_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    bm_st_xf= bm_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    me_st_xf= me_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            if(d['Choice6'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_st_xf)
                if(cse_st_xf>0):
                    selected.append(d)
                    cse_st_xf= cse_st_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice6'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_st_xf)
                if(it_st_xf>0):
                    selected.append(d)
                    it_st_xf= it_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice6'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_st_xf>0):
                    selected.append(d)
                    ece_st_xf= ece_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_st_xf>0):
                    selected.append(d)
                    ei_st_xf= ei_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_st_xf>0):
                    selected.append(d)
                    ee_st_xf= ee_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_st_xf>0):
                    selected.append(d)
                    ip_st_xf= ip_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice6'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_st_xf>0):
                    selected.append(d)
                    ce_st_xf= ce_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    bm_st_xf= bm_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    me_st_xf= me_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            
            if(d['Choice7'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_st_xf)
                if(cse_st_xf>0):
                    selected.append(d)
                    cse_st_xf= cse_st_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice7'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_st_xf)
                if(it_st_xf>0):
                    selected.append(d)
                    it_st_xf= it_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_st_xf>0):
                    selected.append(d)
                    ece_st_xf= ece_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_st_xf>0):
                    selected.append(d)
                    ei_st_xf= ei_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_st_xf>0):
                    selected.append(d)
                    ee_st_xf= ee_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_st_xf>0):
                    selected.append(d)
                    ip_st_xf= ip_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice7'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_st_xf>0):
                    selected.append(d)
                    ce_st_xf= ce_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    bm_st_xf= bm_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    me_st_xf= me_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            


            if(d['Choice8'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_st_xf)
                if(cse_st_xf>0):
                    selected.append(d)
                    cse_st_xf= cse_st_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice8'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_st_xf)
                if(it_st_xf>0):
                    selected.append(d)
                    it_st_xf= it_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice8'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_st_xf>0):
                    selected.append(d)
                    ece_st_xf= ece_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_st_xf>0):
                    selected.append(d)
                    ei_st_xf= ei_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_st_xf>0):
                    selected.append(d)
                    ee_st_xf= ee_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_st_xf>0):
                    selected.append(d)
                    ip_st_xf= ip_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice8'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_st_xf>0):
                    selected.append(d)
                    ce_st_xf= ce_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    bm_st_xf= bm_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_st_xf>0):
                    selected.append(d)
                    me_st_xf= me_st_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            
            j +=1 
            # print(j , "j")
            print("hiiiiii")
        
            # # print(selected)
        if(cse_st_xf!=0):
            cse_st_xop += (cse_st_xf)
        if(it_st_xf!=0):
            it_st_xop += (it_st_xf)
        if(ece_st_xf!=0):
            ece_st_xop += (ece_st_xf)
        if(ei_st_xf!=0):
            ei_st_xop += (ei_st_xf)
        if(ee_st_xf!=0):
            ee_st_xop += (ee_st_xf)
        if(ce_st_xf!=0):
            ce_st_xop += (ce_st_xf)
        if(ip_st_xf!=0):
            ip_st_xop += (ip_st_xf)
        if(bm_st_xf!=0):
            bm_st_xop += (bm_st_xf)
        
    def ST_XOP():
        print("XXXXOOOOPPPPP")
        global cse_st_xf, cse_st_xop, cse_sc_xf, cse_sc_xop, cse_obc_xf, cse_obc_xop, cse_ur_xf, cse_ur_xop
        global it_st_xf, it_st_xop, it_sc_xf, it_sc_xop, it_obc_xf, it_obc_xop, it_ur_xf, it_ur_xop
        global ece_st_xf, ece_st_xop, ece_sc_xf, ece_sc_xop, ece_obc_xf, ece_obc_xop, ece_ur_xf, ece_ur_xop
        global ei_st_xf, ei_st_xop, ei_sc_xf, ei_sc_xop, ei_obc_xf, ei_obc_xop, ei_ur_xf, ei_ur_xop
        global me_st_xf, me_st_xop, me_sc_xf, me_sc_xop, me_obc_xf, me_obc_xop, me_ur_xf, me_ur_xop
        global ee_st_xf, ee_st_xop, ee_sc_xf, ee_sc_xop, ee_obc_xf, ee_obc_xop, ee_ur_xf, ee_ur_xop
        global bm_st_xf, bm_st_xop, bm_sc_xf, bm_sc_xop, bm_obc_xf, bm_obc_xop, bm_ur_xf, bm_ur_xop
        global ip_st_xf, ip_st_xop, ip_sc_xf, ip_sc_xop, ip_obc_xf, ip_obc_xop, ip_ur_xf, ip_ur_xop
        global ce_st_xf, ce_st_xop, ce_sc_xf, ce_sc_xop, ce_obc_xf, ce_obc_xop, ce_ur_xf, ce_ur_xop
        j=0
        
        while(j < len(data_st_xop) ):
            item = data_st_xop[j]
            global d
            d = {}
            for i,col in enumerate(cursor.description):
                # print(col[0])
                # print(j[i])
                d[col[0]] = item[i]
            data_st_xop_list.append(d)
            # print(d['choice1']+":"+(d['allotment_result']))
            print(d['choice1'] ,"and", d['allotment_status'], d['Cname'])
            if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING'  and d['allotment_status']== 'Not Alloted' ):
                print("CSS 1")
                if(cse_st_xop>0):
                    selected.append(d)
                    cse_st_xop= cse_st_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    # data_st_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status']) 
                    increaseFunction()
            if( (d['choice1'] == 'INFORMATION TECHNOLOGY')  and d['allotment_status']== 'Not Alloted' ):
                print("ITTTTTTTTTTTTT")
                print(it_st_xop)
                
                if(it_st_xop>0):
                    selected.append(d) 
                    
                    it_st_xop= it_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    # data_st_xop_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status'])  
                    increaseFunction()       
            if(d['choice1'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ece_st_xop>0):
                    selected.append(d)
                    ece_st_xop= ece_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ei_st_xop>0):
                    selected.append(d)
                    ei_st_xop= ei_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'ELECTRICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ee_st_xop>0):
                    selected.append(d)
                    ee_st_xop= ee_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ip_st_xop>0):
                    selected.append(d)
                    ip_st_xop= ip_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction() 
            if(d['choice1'] ==  'CIVIL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                print("ceeeee")
                if(ce_st_xop>0 ):
                    selected.append(d)
                    ce_st_xop= ce_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'BIOMEDICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            if(d['choice1'] ==  'MECHANICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            print(d['allotment_status'])
            if(d['Choice2'] ==  'COMPUTER SCIENCE & ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                print("entered  in CS coice 2")
                print(cse_st_xop)
                if(cse_st_xop>0):
                    print("CS CHOICE 2")
                    selected.append(d)
                    cse_st_xop= cse_st_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    # data_st_xop_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()    
            if(d['Choice2'] ==  'INFORMATION TECHNOLOGY'  and d['allotment_status']== 'Not Alloted' ):
                print("entered  in IT coice 2")
                print(it_st_xop)
                if(it_st_xop>0 ):
                    print("ITT CHOICE 2")
                    selected.append(d)
                    it_st_xop= it_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    # data_st_xop_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']))    
                    increaseFunction()      
            if(d['Choice2'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ece_st_xop>0):
                    selected.append(d)
                    ece_st_xop= ece_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ei_st_xop>0):
                    selected.append(d)
                    ei_st_xop= ei_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'ELECTRICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ee_st_xop>0):
                    selected.append(d)
                    ee_st_xop= ee_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ip_st_xop>0):
                    selected.append(d)
                    ip_st_xop= ip_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice2'] ==  'CIVIL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ce_st_xop>0):
                    selected.append(d)
                    ce_st_xop= ce_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'BIOMEDICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'MECHANICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice3'] ==  'COMPUTER SCIENCE & ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                print(cse_st_xop)
                if(cse_st_xop>0):
                    selected.append(d)
                    cse_st_xop= cse_st_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice3'] == 'INFORMATION TECHNOLOGY'  and d['allotment_status']== 'Not Alloted'):
                print(it_st_xop)
                if(it_st_xop>0):
                    selected.append(d)
                    it_st_xop= it_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice3'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                print("ECCC3")
                if(ece_st_xop>0 ):
                    print("ECCC 3")

                    # print("ddddddd")
                    # print("selecteeeeedddddd beforeeeee")
                    # # print(selected)
                    selected.append(d)
                    # print(d)
                    # print("selecteeeeedddddd")
                    # # print(selected)
                    ece_st_xop= ece_st_xop-1
                    #increaseFunction()
                    d['allotment_result'] = "ece"
                    d['allotment_status'] = "Allotted"
                    # data_st_xop_list.append(d)
                    print(d['Choice3']+":"+(d['allotment_result']) , d['allotment_status'])
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ei_st_xop>0):
                    selected.append(d)
                    ei_st_xop= ei_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ee_st_xop>0):
                    selected.append(d)
                    ee_st_xop= ee_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ip_st_xop>0):
                    selected.append(d)
                    ip_st_xop= ip_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice3'] ==  'CIVIL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ce_st_xop>0):
                    selected.append(d)
                    ce_st_xop= ce_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'BIOMEDICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'MECHANICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            if(d['Choice4'] ==  'COMPUTER SCIENCE & ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                print(cse_st_xop)
                if(cse_st_xop>0):
                    selected.append(d)
                    cse_st_xop= cse_st_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice4'] ==  'INFORMATION TECHNOLOGY'  and d['allotment_status']== 'Not Alloted'):
                print(it_st_xop)
                if(it_st_xop>0):
                    selected.append(d)
                    it_st_xop= it_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice4'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ece_st_xop>0):
                    selected.append(d)
                    ece_st_xop= ece_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ei_st_xop>0):
                    print("EIII 4")
                    selected.append(d)
                    ei_st_xop= ei_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ee_st_xop>0):
                    selected.append(d)
                    ee_st_xop= ee_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ip_st_xop>0):
                    selected.append(d)
                    ip_st_xop= ip_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice4'] ==  'CIVIL ENGINEERING'   and d['allotment_status']== 'Not Alloted'):
                if(ce_st_xop>0):
                    selected.append(d)
                    ce_st_xop= ce_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'BIOMEDICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'MECHANICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice5'] ==  'COMPUTER SCIENCE & ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                print(cse_st_xop)
                if(cse_st_xop>0):
                    selected.append(d)
                    cse_st_xop= cse_st_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice5'] ==  'INFORMATION TECHNOLOGY'  and d['allotment_status']== 'Not Alloted'):
                print(it_st_xop)
                if(it_st_xop>0):
                    selected.append(d)
                    it_st_xop= it_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice5'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ece_st_xop>0):
                    selected.append(d)
                    ece_st_xop= ece_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ei_st_xop>0):
                    selected.append(d)
                    ei_st_xop= ei_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ee_st_xop>0):
                    selected.append(d)
                    ee_st_xop= ee_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ip_st_xop>0):
                    selected.append(d)
                    ip_st_xop= ip_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice5'] ==  'CIVIL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ce_st_xop>0):
                    selected.append(d)
                    ce_st_xop= ce_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'MECHANICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice6'] ==  'COMPUTER SCIENCE & ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                print(cse_st_xop)
                if(cse_st_xop>0):
                    selected.append(d)
                    cse_st_xop= cse_st_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice6'] ==  'INFORMATION TECHNOLOGY'  and d['allotment_status']== 'Not Alloted'):
                print(it_st_xop)
                if(it_st_xop>0):
                    selected.append(d)
                    it_st_xop= it_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ece_st_xop>0):
                    selected.append(d)
                    ece_st_xop= ece_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ei_st_xop>0):
                    selected.append(d)
                    ei_st_xop= ei_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ee_st_xop>0):
                    selected.append(d)
                    ee_st_xop= ee_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ip_st_xop>0):
                    selected.append(d)
                    ip_st_xop= ip_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice6'] ==  'CIVIL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ce_st_xop>0):
                    selected.append(d)
                    ce_st_xop= ce_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'BIOMEDICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'MECHANICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            if(d['Choice7'] ==  'COMPUTER SCIENCE & ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                print(cse_st_xop)
                if(cse_st_xop>0):
                    selected.append(d)
                    cse_st_xop= cse_st_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice7'] ==  'INFORMATION TECHNOLOGY'  and d['allotment_status']== 'Not Alloted'):
                print(it_st_xop)
                if(it_st_xop>0):
                    selected.append(d)
                    it_st_xop= it_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()   
            if(d['Choice7'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ece_st_xop>0):
                    selected.append(d)
                    ece_st_xop= ece_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ei_st_xop>0):
                    selected.append(d)
                    ei_st_xop= ei_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ee_st_xop>0):
                    selected.append(d)
                    ee_st_xop= ee_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ip_st_xop>0):
                    selected.append(d)
                    ip_st_xop= ip_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice7'] ==  'CIVIL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ce_st_xop>0):
                    selected.append(d)
                    ce_st_xop= ce_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'BIOMEDICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'MECHANICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice8'] ==  'COMPUTER SCIENCE & ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                print(cse_st_xop)
                if(cse_st_xop>0):
                    selected.append(d)
                    cse_st_xop= cse_st_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice8'] ==  'INFORMATION TECHNOLOGY'  and d['allotment_status']== 'Not Alloted'):
                print(it_st_xop)
                if(it_st_xop>0):
                    selected.append(d)
                    it_st_xop= it_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ece_st_xop>0):
                    selected.append(d)
                    ece_st_xop= ece_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ei_st_xop>0):
                    selected.append(d)
                    ei_st_xop= ei_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ee_st_xop>0):
                    selected.append(d)
                    ee_st_xop= ee_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ip_st_xop>0):
                    selected.append(d)
                    ip_st_xop= ip_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice8'] ==  'CIVIL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(ce_st_xop>0):
                    selected.append(d)
                    ce_st_xop= ce_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'BIOMEDICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'MECHANICAL ENGINEERING'  and d['allotment_status']== 'Not Alloted'):
                if(bm_st_xop>0):
                    selected.append(d)
                    bm_st_xop= bm_st_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            j +=1 
            # print(j , "j")
            print("hiiiiii")
        
            # # print(selected)
        if(cse_st_xop!=0):
            cse_sc_xop += (cse_st_xop)
        if(it_st_xop!=0):
            it_sc_xop += (it_st_xop)
        if(ece_st_xop!=0):
            ece_sc_xop += (ece_st_xop)
        if(ei_st_xop!=0):
            ei_sc_xop += (ei_st_xop)
        if(ee_st_xop!=0):
            ee_sc_xop += (ee_st_xop)
        if(ce_st_xop!=0):
            ce_sc_xop += (ce_st_xop)
        if(ip_st_xop!=0):
            ip_sc_xop += (ip_st_xop)
        if(bm_st_xop!=0):
            bm_sc_xop += (bm_st_xop)
    
    def SC_XF():
        global cse_st_xf, cse_st_xop, cse_sc_xf, cse_sc_xop, cse_obc_xf, cse_obc_xop, cse_ur_xf, cse_ur_xop
        global it_st_xf, it_st_xop, it_sc_xf, it_sc_xop, it_obc_xf, it_obc_xop, it_ur_xf, it_ur_xop
        global ece_st_xf, ece_st_xop, ece_sc_xf, ece_sc_xop, ece_obc_xf, ece_obc_xop, ece_ur_xf, ece_ur_xop
        global ei_st_xf, ei_st_xop, ei_sc_xf, ei_sc_xop, ei_obc_xf, ei_obc_xop, ei_ur_xf, ei_ur_xop
        global me_st_xf, me_st_xop, me_sc_xf, me_sc_xop, me_obc_xf, me_obc_xop, me_ur_xf, me_ur_xop
        global ee_st_xf, ee_st_xop, ee_sc_xf, ee_sc_xop, ee_obc_xf, ee_obc_xop, ee_ur_xf, ee_ur_xop
        global bm_st_xf, bm_st_xop, bm_sc_xf, bm_sc_xop, bm_obc_xf, bm_obc_xop, bm_ur_xf, bm_ur_xop
        global ip_st_xf, ip_st_xop, ip_sc_xf, ip_sc_xop, ip_obc_xf, ip_obc_xop, ip_ur_xf, ip_ur_xop
        global ce_st_xf, ce_st_xop, ce_sc_xf, ce_sc_xop, ce_obc_xf, ce_obc_xop, ce_ur_xf, ce_ur_xop
        j=0
        
        while(j < len(data_sc_xf) ):
            print(j, "j")
            item = data_sc_xf[j]
            global d
            d = {}
            for i,col in enumerate(cursor.description):
                # print(col[0])
                # print(j[i])
                d[col[0]] = item[i]
            data_sc_xf_list.append(d)
            # print(d['choice1']+":"+(d['allotment_result']))
            print(d)
            print(d['choice1'] ,"and", d['allotment_status'], d['Cname'])
            if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted' ):
                print("CSSSSS")
                print(cse_sc_xf)
                if(cse_sc_xf>0):
                    print("appendingggggg")
                    selected.append(d)
                    
                    cse_sc_xf= cse_sc_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    # data_sc_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status']) 
                    increaseFunction()
            if( (d['choice1'] == 'INFORMATION TECHNOLOGY') and d['allotment_status'] == 'Not Allotted' ):
                print("ITTTTTTTTTTTTT")
                print(it_sc_xf)
                
                if(it_sc_xf>0):
                    selected.append(d) 
                    
                    it_sc_xf= it_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    # data_sc_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status'])  
                    increaseFunction()       
            if(d['choice1'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xf>0):
                    selected.append(d)
                    ece_sc_xf= ece_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xf>0):
                    selected.append(d)
                    ei_sc_xf= ei_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xf>0):
                    selected.append(d)
                    ee_sc_xf= ee_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xf>0):
                    selected.append(d)
                    ip_sc_xf= ip_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['choice1'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xf>0):
                    selected.append(d)
                    ce_sc_xf= ce_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    bm_sc_xf= bm_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            if(d['choice1'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    me_sc_xf= me_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            


            print(d['allotment_status'])
            if(d['Choice2'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print("entered  in CS coice 2")
                print(cse_sc_xf)
                if(cse_sc_xf>0):
                    print("CS CHOICE 2")
                    selected.append(d)
                    cse_sc_xf= cse_sc_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    # data_sc_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()      
            if(d['Choice2'] ==  'INFORMATION TECHNOLOGY' ):
                print("entered  in IT coice 2")
                print(it_sc_xf)
                if(it_sc_xf>0 and d['allotment_status'] == 'Not Allotted'):
                    print("ITT CHOICE 2")
                    selected.append(d)
                    it_sc_xf= it_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    # data_sc_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction()        
            if(d['Choice2'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xf>0):
                    selected.append(d)
                    ece_sc_xf= ece_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xf>0):
                    selected.append(d)
                    ei_sc_xf= ei_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xf>0):
                    selected.append(d)
                    ee_sc_xf= ee_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xf>0):
                    selected.append(d)
                    ip_sc_xf= ip_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice2'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xf>0):
                    selected.append(d)
                    ce_sc_xf= ce_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    bm_sc_xf= bm_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    me_sc_xf= me_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()




            if(d['Choice3'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xf)
                if(cse_sc_xf>0):
                    selected.append(d)
                    cse_sc_xf= cse_sc_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice3'] == 'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xf)
                if(it_sc_xf>0):
                    selected.append(d)
                    it_sc_xf= it_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice3'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print("ECCC3")
                if(ece_sc_xf>0 ):
                    print("ECCC 3")

                    # print("ddddddd")
                    # print("selecteeeeedddddd beforeeeee")
                    # # print(selected)
                    selected.append(d)
                    # print(d)
                    # print("selecteeeeedddddd")
                    # # print(selected)
                    ece_sc_xf= ece_sc_xf-1
                    #increaseFunction()
                    d['allotment_result'] = "ece"
                    d['allotment_status'] = "Allotted"
                    # data_sc_xf_list.append(d)
                    print(d['Choice3']+":"+(d['allotment_result']) , d['allotment_status'])
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xf>0):
                    selected.append(d)
                    ei_sc_xf= ei_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xf>0):
                    selected.append(d)
                    ee_sc_xf= ee_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xf>0):
                    selected.append(d)
                    ip_sc_xf= ip_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice3'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xf>0):
                    selected.append(d)
                    ce_sc_xf= ce_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    bm_sc_xf= bm_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    me_sc_xf= me_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            


            if(d['Choice4'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xf)
                if(cse_sc_xf>0):
                    selected.append(d)
                    cse_sc_xf= cse_sc_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice4'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xf)
                if(it_sc_xf>0):
                    selected.append(d)
                    it_sc_xf= it_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()  
            if(d['Choice4'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xf>0):
                    selected.append(d)
                    ece_sc_xf= ece_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xf>0):
                    print("EIII 4")
                    selected.append(d)
                    ei_sc_xf= ei_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xf>0):
                    selected.append(d)
                    ee_sc_xf= ee_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xf>0):
                    selected.append(d)
                    ip_sc_xf= ip_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice4'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xf>0):
                    selected.append(d)
                    ce_sc_xf= ce_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    bm_sc_xf= bm_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    me_sc_xf= me_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()



            if(d['Choice5'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xf)
                if(cse_sc_xf>0):
                    selected.append(d)
                    cse_sc_xf= cse_sc_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice5'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xf)
                if(it_sc_xf>0):
                    selected.append(d)
                    it_sc_xf= it_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()   
            if(d['Choice5'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xf>0):
                    selected.append(d)
                    ece_sc_xf= ece_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xf>0):
                    selected.append(d)
                    ei_sc_xf= ei_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xf>0):
                    selected.append(d)
                    ee_sc_xf= ee_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xf>0):
                    selected.append(d)
                    ip_sc_xf= ip_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice5'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xf>0):
                    selected.append(d)
                    ce_sc_xf= ce_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    bm_sc_xf= bm_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    me_sc_xf= me_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()



            if(d['Choice6'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xf)
                if(cse_sc_xf>0):
                    selected.append(d)
                    cse_sc_xf= cse_sc_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice6'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xf)
                if(it_sc_xf>0):
                    selected.append(d)
                    it_sc_xf= it_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xf>0):
                    selected.append(d)
                    ece_sc_xf= ece_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xf>0):
                    selected.append(d)
                    ei_sc_xf= ei_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xf>0):
                    selected.append(d)
                    ee_sc_xf= ee_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xf>0):
                    selected.append(d)
                    ip_sc_xf= ip_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice6'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xf>0):
                    selected.append(d)
                    ce_sc_xf= ce_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    bm_sc_xf= bm_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    me_sc_xf= me_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            
            if(d['Choice7'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xf)
                if(cse_sc_xf>0):
                    selected.append(d)
                    cse_sc_xf= cse_sc_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice7'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xf)
                if(it_sc_xf>0):
                    selected.append(d)
                    it_sc_xf= it_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice7'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xf>0):
                    selected.append(d)
                    ece_sc_xf= ece_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xf>0):
                    selected.append(d)
                    ei_sc_xf= ei_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xf>0):
                    selected.append(d)
                    ee_sc_xf= ee_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xf>0):
                    selected.append(d)
                    ip_sc_xf= ip_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice7'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xf>0):
                    selected.append(d)
                    ce_sc_xf= ce_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    bm_sc_xf= bm_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    me_sc_xf= me_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            


            if(d['Choice8'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xf)
                if(cse_sc_xf>0):
                    selected.append(d)
                    cse_sc_xf= cse_sc_xf-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice8'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xf)
                if(it_sc_xf>0):
                    selected.append(d)
                    it_sc_xf= it_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xf>0):
                    selected.append(d)
                    ece_sc_xf= ece_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xf>0):
                    selected.append(d)
                    ei_sc_xf= ei_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xf>0):
                    selected.append(d)
                    ee_sc_xf= ee_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xf>0):
                    selected.append(d)
                    ip_sc_xf= ip_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice8'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xf>0):
                    selected.append(d)
                    ce_sc_xf= ce_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    bm_sc_xf= bm_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xf>0):
                    selected.append(d)
                    me_sc_xf= me_sc_xf-1
                    #increaseFunction()
                    d['allotment_result']= "me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            
            j +=1 
            # print(j , "j")
            print("hiiiiii")
        
            # # print(selected)
        if(cse_sc_xf!=0):
            cse_sc_xop += (cse_sc_xf)
        if(it_sc_xf!=0):
            it_sc_xop += (it_sc_xf)
        if(ece_sc_xf!=0):
            ece_sc_xop += (ece_sc_xf)
        if(ei_sc_xf!=0):
            ei_sc_xop += (ei_sc_xf)
        if(ee_sc_xf!=0):
            ee_sc_xop += (ee_sc_xf)
        if(ce_sc_xf!=0):
            ce_sc_xop += (ce_sc_xf)
        if(ip_sc_xf!=0):
            ip_sc_xop += (ip_sc_xf)
        if(bm_sc_xf!=0):
            bm_sc_xop += (bm_sc_xf)
    
    def SC_XOP():
        global cse_st_xf, cse_st_xop, cse_sc_xf, cse_sc_xop, cse_obc_xf, cse_obc_xop, cse_ur_xf, cse_ur_xop
        global it_st_xf, it_st_xop, it_sc_xf, it_sc_xop, it_obc_xf, it_obc_xop, it_ur_xf, it_ur_xop
        global ece_st_xf, ece_st_xop, ece_sc_xf, ece_sc_xop, ece_obc_xf, ece_obc_xop, ece_ur_xf, ece_ur_xop
        global ei_st_xf, ei_st_xop, ei_sc_xf, ei_sc_xop, ei_obc_xf, ei_obc_xop, ei_ur_xf, ei_ur_xop
        global me_st_xf, me_st_xop, me_sc_xf, me_sc_xop, me_obc_xf, me_obc_xop, me_ur_xf, me_ur_xop
        global ee_st_xf, ee_st_xop, ee_sc_xf, ee_sc_xop, ee_obc_xf, ee_obc_xop, ee_ur_xf, ee_ur_xop
        global bm_st_xf, bm_st_xop, bm_sc_xf, bm_sc_xop, bm_obc_xf, bm_obc_xop, bm_ur_xf, bm_ur_xop
        global ip_st_xf, ip_st_xop, ip_sc_xf, ip_sc_xop, ip_obc_xf, ip_obc_xop, ip_ur_xf, ip_ur_xop
        global ce_st_xf, ce_st_xop, ce_sc_xf, ce_sc_xop, ce_obc_xf, ce_obc_xop, ce_ur_xf, ce_ur_xop
        j=0
        
        while(j < len(data_sc_xop) ):
            item = data_sc_xop[j]
            global d
            d = {}
            for i,col in enumerate(cursor.description):
                # print(col[0])
                # print(j[i])
                d[col[0]] = item[i]
            data_sc_xop_list.append(d)
            # print(d['choice1']+":"+(d['allotment_result']))
            print(d['choice1'] ,"and", d['allotment_status'], d['Cname'])
            if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted' ):
                print("CSS 1")
                if(cse_sc_xop>0):
                    selected.append(d)
                    cse_sc_xop= cse_sc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    # data_st_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status']) 
                    increaseFunction()
            if( (d['choice1'] == 'INFORMATION TECHNOLOGY') and d['allotment_status'] == 'Not Allotted' ):
                print("ITTTTTTTTTTTTT")
                print(it_sc_xop)
                
                if(it_sc_xop>0):
                    selected.append(d) 
                    
                    it_sc_xop= it_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    # data_sc_xop_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status'])    
                    increaseFunction()     
            if(d['choice1'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xop>0):
                    selected.append(d)
                    ece_sc_xop= ece_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xop>0):
                    selected.append(d)
                    ei_sc_xop= ei_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xop>0):
                    selected.append(d)
                    ee_sc_xop= ee_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xop>0):
                    selected.append(d)
                    ip_sc_xop= ip_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['choice1'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == "Not Allotted"):
                print("ceeeee")
                if(ce_sc_xop>0 ):
                    selected.append(d)
                    ce_sc_xop= ce_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            if(d['choice1'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            print(d['allotment_status'])
            if(d['Choice2'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print("entered  in CS coice 2")
                print(cse_sc_xop)
                if(cse_sc_xop>0):
                    print("CS CHOICE 2")
                    selected.append(d)
                    cse_sc_xop= cse_sc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    # data_sc_xop_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()      
            if(d['Choice2'] ==  'INFORMATION TECHNOLOGY' ):
                print("entered  in IT coice 2")
                print(it_sc_xop)
                if(it_sc_xop>0 and d['allotment_status'] == 'Not Allotted'):
                    print("ITT CHOICE 2")
                    selected.append(d)
                    it_sc_xop= it_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    # data_sc_xop_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']))     
                    increaseFunction()     
            if(d['Choice2'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xop>0):
                    selected.append(d)
                    ece_sc_xop= ece_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xop>0):
                    selected.append(d)
                    ei_sc_xop= ei_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xop>0):
                    selected.append(d)
                    ee_sc_xop= ee_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xop>0):
                    selected.append(d)
                    ip_sc_xop= ip_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice2'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xop>0):
                    selected.append(d)
                    ce_sc_xop= ce_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice3'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xop)
                if(cse_sc_xop>0):
                    selected.append(d)
                    cse_sc_xop= cse_sc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice3'] == 'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xop)
                if(it_sc_xop>0):
                    selected.append(d)
                    it_sc_xop= it_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()   
            if(d['Choice3'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print("ECCC3")
                if(ece_sc_xop>0 ):
                    print("ECCC 3")

                    # print("ddddddd")
                    # print("selecteeeeedddddd beforeeeee")
                    # # print(selected)
                    selected.append(d)
                    # print(d)
                    # print("selecteeeeedddddd")
                    # # print(selected)
                    ece_sc_xop= ece_sc_xop-1
                    #increaseFunction()
                    d['allotment_result'] = "ece"
                    d['allotment_status'] = "Allotted"
                    # data_sc_xop_list.append(d)
                    print(d['Choice3']+":"+(d['allotment_result']) , d['allotment_status'])
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xop>0):
                    selected.append(d)
                    ei_sc_xop= ei_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xop>0):
                    selected.append(d)
                    ee_sc_xop= ee_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xop>0):
                    selected.append(d)
                    ip_sc_xop= ip_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice3'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xop>0):
                    selected.append(d)
                    ce_sc_xop= ce_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            if(d['Choice4'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xop)
                if(cse_sc_xop>0):
                    selected.append(d)
                    cse_sc_xop= cse_sc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice4'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xop)
                if(it_sc_xop>0):
                    selected.append(d)
                    it_sc_xop= it_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xop>0):
                    selected.append(d)
                    ece_sc_xop= ece_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xop>0):
                    print("EIII 4")
                    selected.append(d)
                    ei_sc_xop= ei_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xop>0):
                    selected.append(d)
                    ee_sc_xop= ee_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xop>0):
                    selected.append(d)
                    ip_sc_xop= ip_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice4'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xop>0):
                    selected.append(d)
                    ce_sc_xop= ce_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice5'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xop)
                if(cse_sc_xop>0):
                    selected.append(d)
                    cse_sc_xop= cse_sc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice5'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xop)
                if(it_sc_xop>0):
                    selected.append(d)
                    it_sc_xop= it_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xop>0):
                    selected.append(d)
                    ece_sc_xop= ece_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xop>0):
                    selected.append(d)
                    ei_sc_xop= ei_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xop>0):
                    selected.append(d)
                    ee_sc_xop= ee_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xop>0):
                    selected.append(d)
                    ip_sc_xop= ip_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice5'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xop>0):
                    selected.append(d)
                    ce_sc_xop= ce_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice6'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xop)
                if(cse_sc_xop>0):
                    selected.append(d)
                    cse_sc_xop= cse_sc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction()
            if(d['Choice6'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xop)
                if(it_sc_xop>0):
                    selected.append(d)
                    it_sc_xop= it_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xop>0):
                    selected.append(d)
                    ece_sc_xop= ece_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xop>0):
                    selected.append(d)
                    ei_sc_xop= ei_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xop>0):
                    selected.append(d)
                    ee_sc_xop= ee_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xop>0):
                    selected.append(d)
                    ip_sc_xop= ip_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice6'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xop>0):
                    selected.append(d)
                    ce_sc_xop= ce_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            if(d['Choice7'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xop)
                if(cse_sc_xop>0):
                    selected.append(d)
                    cse_sc_xop= cse_sc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice7'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xop)
                if(it_sc_xop>0):
                    selected.append(d)
                    it_sc_xop= it_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice7'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xop>0):
                    selected.append(d)
                    ece_sc_xop= ece_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xop>0):
                    selected.append(d)
                    ei_sc_xop= ei_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xop>0):
                    selected.append(d)
                    ee_sc_xop= ee_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xop>0):
                    selected.append(d)
                    ip_sc_xop= ip_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice7'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xop>0):
                    selected.append(d)
                    ce_sc_xop= ce_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice8'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_sc_xop)
                if(cse_sc_xop>0):
                    selected.append(d)
                    cse_sc_xop= cse_sc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice8'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_sc_xop)
                if(it_sc_xop>0):
                    selected.append(d)
                    it_sc_xop= it_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice8'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_sc_xop>0):
                    selected.append(d)
                    ece_sc_xop= ece_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_sc_xop>0):
                    selected.append(d)
                    ei_sc_xop= ei_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_sc_xop>0):
                    selected.append(d)
                    ee_sc_xop= ee_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_sc_xop>0):
                    selected.append(d)
                    ip_sc_xop= ip_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice8'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_sc_xop>0):
                    selected.append(d)
                    ce_sc_xop= ce_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_sc_xop>0):
                    selected.append(d)
                    bm_sc_xop= bm_sc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            j +=1 
            # print(j , "j")
            print("hiiiiii")
        
            # # print(selected)
        if(cse_sc_xop!=0):
            cse_obc_xop += (cse_sc_xop)
        if(it_sc_xop!=0):
            it_obc_xop += (it_sc_xop)
        if(ece_sc_xop!=0):
            ece_obc_xop += (ece_sc_xop)
        if(ei_sc_xop!=0):
            ei_obc_xop += (ei_sc_xop)
        if(ee_sc_xop!=0):
            ee_obc_xop += (ee_sc_xop)
        if(ce_sc_xop!=0):
            ce_obc_xop += (ce_sc_xop)
        if(ip_sc_xop!=0):
            ip_obc_xop += (ip_sc_xop)
        if(bm_sc_xop!=0):
            bm_obc_xop += (bm_sc_xop)

    def OBC_XOP():
        global cse_st_xf, cse_st_xop, cse_sc_xf, cse_sc_xop, cse_obc_xf, cse_obc_xop, cse_ur_xf, cse_ur_xop
        global it_st_xf, it_st_xop, it_sc_xf, it_sc_xop, it_obc_xf, it_obc_xop, it_ur_xf, it_ur_xop
        global ece_st_xf, ece_st_xop, ece_sc_xf, ece_sc_xop, ece_obc_xf, ece_obc_xop, ece_ur_xf, ece_ur_xop
        global ei_st_xf, ei_st_xop, ei_sc_xf, ei_sc_xop, ei_obc_xf, ei_obc_xop, ei_ur_xf, ei_ur_xop
        global me_st_xf, me_st_xop, me_sc_xf, me_sc_xop, me_obc_xf, me_obc_xop, me_ur_xf, me_ur_xop
        global ee_st_xf, ee_st_xop, ee_sc_xf, ee_sc_xop, ee_obc_xf, ee_obc_xop, ee_ur_xf, ee_ur_xop
        global bm_st_xf, bm_st_xop, bm_sc_xf, bm_sc_xop, bm_obc_xf, bm_obc_xop, bm_ur_xf, bm_ur_xop
        global ip_st_xf, ip_st_xop, ip_sc_xf, ip_sc_xop, ip_obc_xf, ip_obc_xop, ip_ur_xf, ip_ur_xop
        global ce_st_xf, ce_st_xop, ce_sc_xf, ce_sc_xop, ce_obc_xf, ce_obc_xop, ce_ur_xf, ce_ur_xop
        j=0
        
        while(j < len(data_obc_xop) ):
            item = data_obc_xop[j]
            global d
            d = {}
            for i,col in enumerate(cursor.description):
                # print(col[0])
                # print(j[i])
                d[col[0]] = item[i]
            data_obc_xop_list.append(d)
            # print(d['choice1']+":"+(d['allotment_result']))
            print(d['choice1'] ,"and", d['allotment_status'], d['Cname'])
            if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted' ):
                print("CSS 1")
                if(cse_obc_xop>0):
                    selected.append(d)
                    cse_obc_xop= cse_obc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    # data_st_xf_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status']) 
                    increaseFunction()
            if( (d['choice1'] == 'INFORMATION TECHNOLOGY') and d['allotment_status'] == 'Not Allotted' ):
                print("ITTTTTTTTTTTTT")
                print(it_obc_xop)
                
                if(it_obc_xop>0):
                    selected.append(d) 
                    
                    it_obc_xop= it_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    # data_obc_xop_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status'])      
                    increaseFunction()   
            if(d['choice1'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_obc_xop>0):
                    selected.append(d)
                    ece_obc_xop= ece_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_obc_xop>0):
                    selected.append(d)
                    ei_obc_xop= ei_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    d['allotment_status']= "Allotted"
                    increaseFunction()
            if(d['choice1'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_obc_xop>0):
                    selected.append(d)
                    ee_obc_xop= ee_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_obc_xop>0):
                    selected.append(d)
                    ip_obc_xop= ip_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['choice1'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == "Not Allotted"):
                print("ceeeee")
                if(ce_obc_xop>0 ):
                    selected.append(d)
                    ce_obc_xop= ce_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['choice1'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            if(d['choice1'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            print(d['allotment_status'])
            if(d['Choice2'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print("entered  in CS coice 2")
                print(cse_obc_xop)
                if(cse_obc_xop>0):
                    print("CS CHOICE 2")
                    selected.append(d)
                    cse_obc_xop= cse_obc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']= "cse"
                    d['allotment_status']= "Allotted"
                    # data_obc_xop_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction()     
            if(d['Choice2'] ==  'INFORMATION TECHNOLOGY' ):
                print("entered  in IT coice 2")
                print(it_obc_xop)
                if(it_obc_xop>0 and d['allotment_status'] == 'Not Allotted'):
                    print("ITT CHOICE 2")
                    selected.append(d)
                    it_obc_xop= it_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    # data_obc_xop_list.append(d)
                    print(d['choice1']+":"+(d['allotment_result']))    
                    increaseFunction()      
            if(d['Choice2'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_obc_xop>0):
                    selected.append(d)
                    ece_obc_xop= ece_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_obc_xop>0):
                    selected.append(d)
                    ei_obc_xop= ei_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_obc_xop>0):
                    selected.append(d)
                    ee_obc_xop= ee_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_obc_xop>0):
                    selected.append(d)
                    ip_obc_xop= ip_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice2'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_obc_xop>0):
                    selected.append(d)
                    ce_obc_xop= ce_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice2'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice3'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_obc_xop)
                if(cse_obc_xop>0):
                    selected.append(d)
                    cse_obc_xop= cse_obc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice3'] == 'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_obc_xop)
                if(it_obc_xop>0):
                    selected.append(d)
                    it_obc_xop= it_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print("ECCC3")
                if(ece_obc_xop>0 ):
                    print("ECCC 3")

                    # print("ddddddd")
                    # print("selecteeeeedddddd beforeeeee")
                    # # print(selected)
                    selected.append(d)
                    # print(d)
                    # print("selecteeeeedddddd")
                    # # print(selected)
                    ece_obc_xop= ece_obc_xop-1
                    #increaseFunction()
                    d['allotment_result'] = "ece"
                    d['allotment_status'] = "Allotted"
                    # data_obc_xop_list.append(d)
                    print(d['Choice3']+":"+(d['allotment_result']) , d['allotment_status'])
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_obc_xop>0):
                    selected.append(d)
                    ei_obc_xop= ei_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_obc_xop>0):
                    selected.append(d)
                    ee_obc_xop= ee_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_obc_xop>0):
                    selected.append(d)
                    ip_obc_xop= ip_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice3'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_obc_xop>0):
                    selected.append(d)
                    ce_obc_xop= ce_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice3'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()
            
            if(d['Choice4'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_obc_xop)
                if(cse_obc_xop>0):
                    selected.append(d)
                    cse_obc_xop= cse_obc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice4'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_obc_xop)
                if(it_obc_xop>0):
                    selected.append(d)
                    it_obc_xop= it_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_obc_xop>0):
                    selected.append(d)
                    ece_obc_xop= ece_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_obc_xop>0):
                    print("EIII 4")
                    selected.append(d)
                    ei_obc_xop= ei_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_obc_xop>0):
                    selected.append(d)
                    ee_obc_xop= ee_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_obc_xop>0):
                    selected.append(d)
                    ip_obc_xop= ip_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice4'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_obc_xop>0):
                    selected.append(d)
                    ce_obc_xop= ce_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice4'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice5'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_obc_xop)
                if(cse_obc_xop>0):
                    selected.append(d)
                    cse_obc_xop= cse_obc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice5'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_obc_xop)
                if(it_obc_xop>0):
                    selected.append(d)
                    it_obc_xop= it_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_obc_xop>0):
                    selected.append(d)
                    ece_obc_xop= ece_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_obc_xop>0):
                    selected.append(d)
                    ei_obc_xop= ei_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_obc_xop>0):
                    selected.append(d)
                    ee_obc_xop= ee_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_obc_xop>0):
                    selected.append(d)
                    ip_obc_xop= ip_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice5'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_obc_xop>0):
                    selected.append(d)
                    ce_obc_xop= ce_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice5'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(me_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()

            if(d['Choice6'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_obc_xop)
                if(cse_obc_xop>0):
                    selected.append(d)
                    cse_obc_xop= cse_obc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice6'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_obc_xop)
                if(it_obc_xop>0):
                    selected.append(d)
                    it_obc_xop= it_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice6'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_obc_xop>0):
                    selected.append(d)
                    ece_obc_xop= ece_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_obc_xop>0):
                    selected.append(d)
                    ei_obc_xop= ei_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_obc_xop>0):
                    selected.append(d)
                    ee_obc_xop= ee_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_obc_xop>0):
                    selected.append(d)
                    ip_obc_xop= ip_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice6'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_obc_xop>0):
                    selected.append(d)
                    ce_obc_xop= ce_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice6'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                    increaseFunction()


            if(d['Choice7'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_obc_xop)
                if(cse_obc_xop>0):
                    selected.append(d)
                    cse_obc_xop= cse_obc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice7'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_obc_xop)
                if(it_obc_xop>0):
                    selected.append(d)
                    it_obc_xop= it_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_obc_xop>0):
                    selected.append(d)
                    ece_obc_xop= ece_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_obc_xop>0):
                    selected.append(d)
                    ei_obc_xop= ei_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_obc_xop>0):
                    selected.append(d)
                    ee_obc_xop= ee_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_obc_xop>0):
                    selected.append(d)
                    ip_obc_xop= ip_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice7'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_obc_xop>0):
                    selected.append(d)
                    ce_obc_xop= ce_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice7'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(me_obc_xop>0):
                    selected.append(d)
                    me_obc_xop= me_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))

            if(d['Choice8'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                print(cse_obc_xop)
                if(cse_obc_xop>0):
                    selected.append(d)
                    cse_obc_xop= cse_obc_xop-1
                    print("called")
                    #increaseFunction()
                    d['allotment_result']="cse"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))  
                    increaseFunction() 
            if(d['Choice8'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                print(it_obc_xop)
                if(it_obc_xop>0):
                    selected.append(d)
                    it_obc_xop= it_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="it"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))   
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ece_obc_xop>0):
                    selected.append(d)
                    ece_obc_xop= ece_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ece"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ei_obc_xop>0):
                    selected.append(d)
                    ei_obc_xop= ei_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ei"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ee_obc_xop>0):
                    selected.append(d)
                    ee_obc_xop= ee_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ee"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ip_obc_xop>0):
                    selected.append(d)
                    ip_obc_xop= ip_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ipe"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result'])) 
                    increaseFunction()
            if(d['Choice8'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(ce_obc_xop>0):
                    selected.append(d)
                    ce_obc_xop= ce_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="ce"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(bm_obc_xop>0):
                    selected.append(d)
                    bm_obc_xop= bm_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="bm"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']))
                    increaseFunction()
            if(d['Choice8'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                if(me_obc_xop>0):
                    selected.append(d)
                    me_obc_xop= me_obc_xop-1
                    #increaseFunction()
                    d['allotment_result']="me"
                    d['allotment_status']= "Allotted"
                    print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
            
            j +=1 
            # print(j , "j")
            print("hiiiiii")
        
            # # print(selected)
        if(cse_obc_xop!=0):
            cse_ur_xop += (cse_obc_xop)
        if(it_obc_xop!=0):
            it_ur_xop += (it_obc_xop)
        if(ece_obc_xop!=0):
            ece_ur_xop += (ece_obc_xop)
        if(ei_obc_xop!=0):
            ei_ur_xop += (ei_obc_xop)
        if(ee_obc_xop!=0):
            ee_ur_xop += (ee_obc_xop)
        if(ce_obc_xop!=0):
            ce_ur_xop += (ce_obc_xop)
        if(ip_obc_xop!=0):
            ip_ur_xop += (ip_obc_xop)
        if(bm_obc_xop!=0):
            bm_ur_xop += (bm_obc_xop)

    def OBC_XF():
        global cse_st_xf, cse_st_xop, cse_sc_xf, cse_sc_xop, cse_obc_xf, cse_obc_xop, cse_ur_xf, cse_ur_xop
        global it_st_xf, it_st_xop, it_sc_xf, it_sc_xop, it_obc_xf, it_obc_xop, it_ur_xf, it_ur_xop
        global ece_st_xf, ece_st_xop, ece_sc_xf, ece_sc_xop, ece_obc_xf, ece_obc_xop, ece_ur_xf, ece_ur_xop
        global ei_st_xf, ei_st_xop, ei_sc_xf, ei_sc_xop, ei_obc_xf, ei_obc_xop, ei_ur_xf, ei_ur_xop
        global me_st_xf, me_st_xop, me_sc_xf, me_sc_xop, me_obc_xf, me_obc_xop, me_ur_xf, me_ur_xop
        global ee_st_xf, ee_st_xop, ee_sc_xf, ee_sc_xop, ee_obc_xf, ee_obc_xop, ee_ur_xf, ee_ur_xop
        global bm_st_xf, bm_st_xop, bm_sc_xf, bm_sc_xop, bm_obc_xf, bm_obc_xop, bm_ur_xf, bm_ur_xop
        global ip_st_xf, ip_st_xop, ip_sc_xf, ip_sc_xop, ip_obc_xf, ip_obc_xop, ip_ur_xf, ip_ur_xop
        global ce_st_xf, ce_st_xop, ce_sc_xf, ce_sc_xop, ce_obc_xf, ce_obc_xop, ce_ur_xf, ce_ur_xop
        j=0
        while(j < len(data_obc_xf) ):
                item = data_obc_xf[j]
                global d
                d = {}
                for i,col in enumerate(cursor.description):
                    # print(col[0])
                    # print(j[i])
                    d[col[0]] = item[i]
                data_obc_xf_list.append(d)
                # print(d['choice1']+":"+(d['allotment_result']))
                print(d['choice1'] ,"and", d['allotment_status'], d['Cname'])
                if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted' ):
                    print("CSS 1")
                    if(cse_obc_xf>0):
                        selected.append(d)
                        cse_obc_xf= cse_obc_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']= "cse"
                        d['allotment_status']= "Allotted"
                        # data_st_xf_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status']) 
                        increaseFunction()
                if( (d['choice1'] == 'INFORMATION TECHNOLOGY') and d['allotment_status'] == 'Not Allotted' ):
                    print("ITTTTTTTTTTTTT")
                    print(it_obc_xf)
                    
                    if(it_obc_xf>0):
                        selected.append(d) 
                        it_obc_xf= it_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        # data_obc_xf_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status'])        
                        increaseFunction() 
                if(d['choice1'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_obc_xf>0):
                        selected.append(d)
                        ece_obc_xf= ece_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_obc_xf>0):
                        selected.append(d)
                        ei_obc_xf= ei_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_obc_xf>0):
                        selected.append(d)
                        ee_obc_xf= ee_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_obc_xf>0):
                        selected.append(d)
                        ip_obc_xf= ip_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['choice1'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == "Not Allotted"):
                    print("ceeeee")
                    if(ce_obc_xf>0 ):
                        selected.append(d)
                        ce_obc_xf= ce_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_obc_xf>0):
                        selected.append(d)
                        bm_obc_xf= bm_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                if(d['choice1'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_obc_xf>0):
                        selected.append(d)
                        me_obc_xf= me_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                
                print(d['allotment_status'])
                if(d['Choice2'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print("entered  in CS coice 2")
                    print(cse_obc_xf)
                    if(cse_obc_xf>0):
                        print("CS CHOICE 2")
                        selected.append(d)
                        cse_obc_xf= cse_obc_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']= "cse"
                        d['allotment_status']= "Allotted"
                        # data_obc_xf_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']))    
                        increaseFunction()   
                if(d['Choice2'] ==  'INFORMATION TECHNOLOGY' ):
                    print("entered  in IT coice 2")
                    print(it_obc_xf)
                    if(it_obc_xf>0 and d['allotment_status'] == 'Not Allotted'):
                        print("ITT CHOICE 2")
                        selected.append(d)
                        it_obc_xf= it_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        # data_obc_xf_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']))    
                        increaseFunction()      
                if(d['Choice2'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_obc_xf>0):
                        selected.append(d)
                        ece_obc_xf= ece_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_obc_xf>0):
                        selected.append(d)
                        ei_obc_xf= ei_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_obc_xf>0):
                        selected.append(d)
                        ee_obc_xf= ee_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_obc_xf>0):
                        selected.append(d)
                        ip_obc_xf= ip_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice2'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_obc_xf>0):
                        selected.append(d)
                        ce_obc_xf= ce_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_obc_xf>0):
                        selected.append(d)
                        bm_obc_xf= bm_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_obc_xf>0):
                        selected.append(d)
                        me_obc_xf= me_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))

                if(d['Choice3'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_obc_xf)
                    if(cse_obc_xf>0):
                        selected.append(d)
                        cse_obc_xf= cse_obc_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice3'] == 'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_obc_xf)
                    if(it_obc_xf>0):
                        selected.append(d)
                        it_obc_xf= it_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice3'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print("ECCC3")
                    if(ece_obc_xf>0 ):
                        print("ECCC 3")

                        # print("ddddddd")
                        # print("selecteeeeedddddd beforeeeee")
                        # # print(selected)
                        selected.append(d)
                        # print(d)
                        # print("selecteeeeedddddd")
                        # # print(selected)
                        ece_obc_xf= ece_obc_xf-1
                        #increaseFunction()
                        d['allotment_result'] = "ece"
                        d['allotment_status'] = "Allotted"
                        # data_obc_xf_list.append(d)
                        print(d['Choice3']+":"+(d['allotment_result']) , d['allotment_status'])
                        increaseFunction()
                if(d['Choice3'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_obc_xf>0):
                        selected.append(d)
                        ei_obc_xf= ei_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice3'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_obc_xf>0):
                        selected.append(d)
                        ee_obc_xf= ee_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice3'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_obc_xf>0):
                        selected.append(d)
                        ip_obc_xf= ip_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice3'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_obc_xf>0):
                        selected.append(d)
                        ce_obc_xf= ce_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice3'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_obc_xf>0):
                        selected.append(d)
                        bm_obc_xf= bm_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_obc_xf>0):
                        selected.append(d)
                        me_obc_xf= me_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                
                if(d['Choice4'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_obc_xf)
                    if(cse_obc_xf>0):
                        selected.append(d)
                        cse_obc_xf= cse_obc_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()  
                if(d['Choice4'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_obc_xf)
                    if(it_obc_xf>0):
                        selected.append(d)
                        it_obc_xf= it_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice4'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_obc_xf>0):
                        selected.append(d)
                        ece_obc_xf= ece_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_obc_xf>0):
                        print("EIII 4")
                        selected.append(d)
                        ei_obc_xf= ei_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_obc_xf>0):
                        selected.append(d)
                        ee_obc_xf= ee_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_obc_xf>0):
                        selected.append(d)
                        ip_obc_xf= ip_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice4'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_obc_xf>0):
                        selected.append(d)
                        ce_obc_xf= ce_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_obc_xf>0):
                        selected.append(d)
                        bm_obc_xf= bm_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_obc_xf>0):
                        selected.append(d)
                        bm_obc_xf= bm_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice5'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_obc_xf)
                    if(cse_obc_xf>0):
                        selected.append(d)
                        cse_obc_xf= cse_obc_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice5'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_obc_xf)
                    if(it_obc_xf>0):
                        selected.append(d)
                        it_obc_xf= it_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice5'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_obc_xf>0):
                        selected.append(d)
                        ece_obc_xf= ece_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_obc_xf>0):
                        selected.append(d)
                        ei_obc_xf= ei_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_obc_xf>0):
                        selected.append(d)
                        ee_obc_xf= ee_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_obc_xf>0):
                        selected.append(d)
                        ip_obc_xf= ip_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice5'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_obc_xf>0):
                        selected.append(d)
                        ce_obc_xf= ce_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_obc_xf>0):
                        selected.append(d)
                        bm_obc_xf= bm_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_obc_xf>0):
                        selected.append(d)
                        me_obc_xf= me_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice6'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_obc_xf)
                    if(cse_obc_xf>0):
                        selected.append(d)
                        cse_obc_xf= cse_obc_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))  
                        increaseFunction() 
                if(d['Choice6'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_obc_xf)
                    if(it_obc_xf>0):
                        selected.append(d)
                        it_obc_xf= it_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))  
                        increaseFunction() 
                if(d['Choice6'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_obc_xf>0):
                        selected.append(d)
                        ece_obc_xf= ece_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_obc_xf>0):
                        selected.append(d)
                        ei_obc_xf= ei_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_obc_xf>0):
                        selected.append(d)
                        ee_obc_xf= ee_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_obc_xf>0):
                        selected.append(d)
                        ip_obc_xf= ip_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice6'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_obc_xf>0):
                        selected.append(d)
                        ce_obc_xf= ce_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_obc_xf>0):
                        selected.append(d)
                        bm_obc_xf= bm_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_obc_xf>0):
                        selected.append(d)
                        me_obc_xf= me_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                
                if(d['Choice7'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_obc_xf)
                    if(cse_obc_xf>0):
                        selected.append(d)
                        cse_obc_xf= cse_obc_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))  
                        increaseFunction() 
                if(d['Choice7'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_obc_xf)
                    if(it_obc_xf>0):
                        selected.append(d)
                        it_obc_xf= it_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice7'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_obc_xf>0):
                        selected.append(d)
                        ece_obc_xf= ece_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_obc_xf>0):
                        selected.append(d)
                        ei_obc_xf= ei_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_obc_xf>0):
                        selected.append(d)
                        ee_obc_xf= ee_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_obc_xf>0):
                        selected.append(d)
                        ip_obc_xf= ip_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice7'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_obc_xf>0):
                        selected.append(d)
                        ce_obc_xf= ce_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_obc_xf>0):
                        selected.append(d)
                        bm_obc_xf= bm_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_obc_xf>0):
                        selected.append(d)
                        me_obc_xf= me_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice8'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_obc_xf)
                    if(cse_obc_xf>0):
                        selected.append(d)
                        cse_obc_xf= cse_obc_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice8'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_obc_xf)
                    if(it_obc_xf>0):
                        selected.append(d)
                        it_obc_xf= it_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice8'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_obc_xf>0):
                        selected.append(d)
                        ece_obc_xf= ece_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_obc_xf>0):
                        selected.append(d)
                        ei_obc_xf= ei_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_obc_xf>0):
                        selected.append(d)
                        ee_obc_xf= ee_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_obc_xf>0):
                        selected.append(d)
                        ip_obc_xf= ip_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice8'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_obc_xf>0):
                        selected.append(d)
                        ce_obc_xf= ce_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_obc_xf>0):
                        selected.append(d)
                        bm_obc_xf= bm_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_obc_xf>0):
                        selected.append(d)
                        me_obc_xf= me_obc_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                
                j +=1 
                # print(j , "j")
                print("hiiiiii")
            
                # # print(selected)
        if(cse_obc_xf!=0):
            cse_obc_xop += (cse_obc_xf)
        if(it_obc_xf!=0):
            it_obc_xop += (it_obc_xf)
        if(ece_obc_xf!=0):
            ece_obc_xop +=(ece_obc_xf)
        if(ei_obc_xf!=0):
            ei_obc_xop += (ei_obc_xf)
        if(ee_obc_xf!=0):
            ee_obc_xop += (ee_obc_xf)
        if(ce_obc_xf!=0):
            ce_obc_xop += (ce_obc_xf)
        if(ip_obc_xf!=0):
            ip_obc_xop += (ip_obc_xf)
        if(bm_obc_xf!=0):
            bm_obc_xop += (bm_obc_xf)
            
    def UR_XF():
            global cse_st_xf, cse_st_xop, cse_sc_xf, cse_sc_xop, cse_obc_xf, cse_obc_xop, cse_ur_xf, cse_ur_xop
            global it_st_xf, it_st_xop, it_sc_xf, it_sc_xop, it_obc_xf, it_obc_xop, it_ur_xf, it_ur_xop
            global ece_st_xf, ece_st_xop, ece_sc_xf, ece_sc_xop, ece_obc_xf, ece_obc_xop, ece_ur_xf, ece_ur_xop
            global ei_st_xf, ei_st_xop, ei_sc_xf, ei_sc_xop, ei_obc_xf, ei_obc_xop, ei_ur_xf, ei_ur_xop
            global me_st_xf, me_st_xop, me_sc_xf, me_sc_xop, me_obc_xf, me_obc_xop, me_ur_xf, me_ur_xop
            global ee_st_xf, ee_st_xop, ee_sc_xf, ee_sc_xop, ee_obc_xf, ee_obc_xop, ee_ur_xf, ee_ur_xop
            global bm_st_xf, bm_st_xop, bm_sc_xf, bm_sc_xop, bm_obc_xf, bm_obc_xop, bm_ur_xf, bm_ur_xop
            global ip_st_xf, ip_st_xop, ip_sc_xf, ip_sc_xop, ip_obc_xf, ip_obc_xop, ip_ur_xf, ip_ur_xop
            global ce_st_xf, ce_st_xop, ce_sc_xf, ce_sc_xop, ce_obc_xf, ce_obc_xop, ce_ur_xf, ce_ur_xop
            j=0
        
            while(j < len(data_ur_xf) ):
                item = data_ur_xf[j]
                global d
                d = {}
                for i,col in enumerate(cursor.description):
                    # print(col[0])
                    # print(j[i])
                    d[col[0]] = item[i]
                data_ur_xf_list.append(d)
                # print(d['choice1']+":"+(d['allotment_result']))
                print(d['choice1'] ,"and", d['allotment_status'], d['Cname'])
                if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted' ):
                    print("CSS 1")
                    if(cse_ur_xf>0):
                        selected.append(d)
                        cse_ur_xf= cse_ur_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']= "cse"
                        d['allotment_status']= "Allotted"
                        # data_st_xf_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status']) 
                        increaseFunction()
                if( (d['choice1'] == 'INFORMATION TECHNOLOGY') and d['allotment_status'] == 'Not Allotted' ):
                    print("ITTTTTTTTTTTTT")
                    print(it_ur_xf)
                    
                    if(it_ur_xf>0):
                        selected.append(d) 
                        
                        it_ur_xf= it_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        # data_ur_xf_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status'])  
                        increaseFunction()       
                if(d['choice1'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xf>0):
                        selected.append(d)
                        ece_ur_xf= ece_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xf>0):
                        selected.append(d)
                        ei_ur_xf= ei_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xf>0):
                        selected.append(d)
                        ee_ur_xf= ee_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xf>0):
                        selected.append(d)
                        ip_ur_xf= ip_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['choice1'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == "Not Allotted"):
                    print("ceeeee")
                    if(ce_ur_xf>0 ):
                        selected.append(d)
                        ce_ur_xf= ce_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xf>0):
                        selected.append(d)
                        bm_ur_xf= bm_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                if(d['choice1'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xf>0):
                        selected.append(d)
                        me_ur_xf= me_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                print(d['allotment_status'])
                if(d['Choice2'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print("entered  in CS coice 2")
                    print(cse_ur_xf)
                    if(cse_ur_xf>0):
                        print("CS CHOICE 2")
                        selected.append(d)
                        cse_ur_xf= cse_ur_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']= "cse"
                        d['allotment_status']= "Allotted"
                        # data_ur_xf_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']))    
                        increaseFunction()   
                if(d['Choice2'] ==  'INFORMATION TECHNOLOGY' ):
                    print("entered  in IT coice 2")
                    print(it_ur_xf)
                    if(it_ur_xf>0 and d['allotment_status'] == 'Not Allotted'):
                        print("ITT CHOICE 2")
                        selected.append(d)
                        it_ur_xf= it_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        # data_ur_xf_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()       
                if(d['Choice2'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xf>0):
                        selected.append(d)
                        ece_ur_xf= ece_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xf>0):
                        selected.append(d)
                        ei_ur_xf= ei_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xf>0):
                        selected.append(d)
                        ee_ur_xf= ee_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xf>0):
                        selected.append(d)
                        ip_ur_xf= ip_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice2'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xf>0):
                        selected.append(d)
                        ce_ur_xf= ce_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xf>0):
                        selected.append(d)
                        bm_ur_xf= bm_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xf>0):
                        selected.append(d)
                        bm_ur_xf= bm_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice3'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xf)
                    if(cse_ur_xf>0):
                        selected.append(d)
                        cse_ur_xf= cse_ur_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))  
                        increaseFunction() 
                if(d['Choice3'] == 'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xf)
                    if(it_ur_xf>0):
                        selected.append(d)
                        it_ur_xf= it_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()  
                if(d['Choice3'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print("ECCC3")
                    if(ece_ur_xf>0 ):
                        print("ECCC 3")

                        # print("ddddddd")
                        # print("selecteeeeedddddd beforeeeee")
                        # # print(selected)
                        selected.append(d)
                        # print(d)
                        # print("selecteeeeedddddd")
                        # # print(selected)
                        ece_ur_xf= ece_ur_xf-1
                        #increaseFunction()
                        d['allotment_result'] = "ece"
                        d['allotment_status'] = "Allotted"
                        # data_ur_xf_list.append(d)
                        print(d['Choice3']+":"+(d['allotment_result']) , d['allotment_status'])
                        increaseFunction()
                if(d['Choice3'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xf>0):
                        selected.append(d)
                        ei_ur_xf= ei_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice3'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xf>0):
                        selected.append(d)
                        ee_ur_xf= ee_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice3'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xf>0):
                        selected.append(d)
                        ip_ur_xf= ip_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice3'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xf>0):
                        selected.append(d)
                        ce_ur_xf= ce_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice3'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xf>0):
                        selected.append(d)
                        bm_ur_xf= bm_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xf>0):
                        selected.append(d)
                        bm_ur_xf= bm_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                
                if(d['Choice4'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xf)
                    if(cse_ur_xf>0):
                        selected.append(d)
                        cse_ur_xf= cse_ur_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice4'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xf)
                    if(it_ur_xf>0):
                        selected.append(d)
                        it_ur_xf= it_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice4'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xf>0):
                        selected.append(d)
                        ece_ur_xf= ece_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xf>0):
                        print("EIII 4")
                        selected.append(d)
                        ei_ur_xf= ei_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xf>0):
                        selected.append(d)
                        ee_ur_xf= ee_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xf>0):
                        selected.append(d)
                        ip_ur_xf= ip_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice4'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xf>0):
                        selected.append(d)
                        ce_ur_xf= ce_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xf>0):
                        selected.append(d)
                        bm_ur_xf= bm_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xf>0):
                        selected.append(d)
                        me_ur_xf= me_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice5'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xf)
                    if(cse_ur_xf>0):
                        selected.append(d)
                        cse_ur_xf= cse_ur_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()  
                if(d['Choice5'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xf)
                    if(it_ur_xf>0):
                        selected.append(d)
                        it_ur_xf= it_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice5'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xf>0):
                        selected.append(d)
                        ece_ur_xf= ece_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xf>0):
                        selected.append(d)
                        ei_ur_xf= ei_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xf>0):
                        selected.append(d)
                        ee_ur_xf= ee_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xf>0):
                        selected.append(d)
                        ip_ur_xf= ip_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice5'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xf>0):
                        selected.append(d)
                        ce_ur_xf= ce_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xf>0):
                        selected.append(d)
                        bm_ur_xf= bm_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xf>0):
                        selected.append(d)
                        me_ur_xf= me_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice6'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xf)
                    if(cse_ur_xf>0):
                        selected.append(d)
                        cse_ur_xf= cse_ur_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))  
                        increaseFunction() 
                if(d['Choice6'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xf)
                    if(it_ur_xf>0):
                        selected.append(d)
                        it_ur_xf= it_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice6'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xf>0):
                        selected.append(d)
                        ece_ur_xf= ece_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xf>0):
                        selected.append(d)
                        ei_ur_xf= ei_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xf>0):
                        selected.append(d)
                        ee_ur_xf= ee_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xf>0):
                        selected.append(d)
                        ip_ur_xf= ip_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice6'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xf>0):
                        selected.append(d)
                        ce_ur_xf= ce_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xf>0):
                        selected.append(d)
                        bm_ur_xf= bm_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xf>0):
                        selected.append(d)
                        me_ur_xf= me_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                
                if(d['Choice7'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xf)
                    if(cse_ur_xf>0):
                        selected.append(d)
                        cse_ur_xf= cse_ur_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))  
                        increaseFunction() 
                if(d['Choice7'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xf)
                    if(it_ur_xf>0):
                        selected.append(d)
                        it_ur_xf= it_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice7'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xf>0):
                        selected.append(d)
                        ece_ur_xf= ece_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xf>0):
                        selected.append(d)
                        ei_ur_xf= ei_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xf>0):
                        selected.append(d)
                        ee_ur_xf= ee_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xf>0):
                        selected.append(d)
                        ip_ur_xf= ip_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice7'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xf>0):
                        selected.append(d)
                        ce_ur_xf= ce_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xf>0):
                        selected.append(d)
                        bm_ur_xf= bm_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xf>0):
                        selected.append(d)
                        me_ur_xf= me_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice8'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xf)
                    if(cse_ur_xf>0):
                        selected.append(d)
                        cse_ur_xf= cse_ur_xf-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice8'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xf)
                    if(it_ur_xf>0):
                        selected.append(d)
                        it_ur_xf= it_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice8'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xf>0):
                        selected.append(d)
                        ece_ur_xf= ece_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xf>0):
                        selected.append(d)
                        ei_ur_xf= ei_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xf>0):
                        selected.append(d)
                        ee_ur_xf= ee_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xf>0):
                        selected.append(d)
                        ip_ur_xf= ip_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice8'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xf>0):
                        selected.append(d)
                        ce_ur_xf= ce_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xf>0):
                        selected.append(d)
                        bm_ur_xf= bm_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xf>0):
                        selected.append(d)
                        me_ur_xf= me_ur_xf-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                
                j +=1 
                # print(j , "j")
                print("hiiiiii")
            
                # # print(selected)
            if(cse_ur_xf!=0):
                cse_ur_xop += (cse_ur_xf)
            if(it_ur_xf!=0):
                it_ur_xop += (it_ur_xf)
            if(ece_ur_xf!=0):
                ece_ur_xop +=(ece_ur_xf)
            if(ei_ur_xf!=0):
                ei_ur_xop += (ei_ur_xf)
            if(ee_ur_xf!=0):
                ee_ur_xop += (ee_ur_xf)
            if(ce_ur_xf!=0):
                ce_ur_xop += (ce_ur_xf)
            if(ip_ur_xf!=0):
                ip_ur_xop += (ip_ur_xf)
            if(bm_ur_xf!=0):
                bm_ur_xop += (bm_ur_xf)

    def UR_XOP():
            global cse_st_xf, cse_st_xop, cse_sc_xf, cse_sc_xop, cse_obc_xf, cse_obc_xop, cse_ur_xf, cse_ur_xop
            global it_st_xf, it_st_xop, it_sc_xf, it_sc_xop, it_obc_xf, it_obc_xop, it_ur_xf, it_ur_xop
            global ece_st_xf, ece_st_xop, ece_sc_xf, ece_sc_xop, ece_obc_xf, ece_obc_xop, ece_ur_xf, ece_ur_xop
            global ei_st_xf, ei_st_xop, ei_sc_xf, ei_sc_xop, ei_obc_xf, ei_obc_xop, ei_ur_xf, ei_ur_xop
            global me_st_xf, me_st_xop, me_sc_xf, me_sc_xop, me_obc_xf, me_obc_xop, me_ur_xf, me_ur_xop
            global ee_st_xf, ee_st_xop, ee_sc_xf, ee_sc_xop, ee_obc_xf, ee_obc_xop, ee_ur_xf, ee_ur_xop
            global bm_st_xf, bm_st_xop, bm_sc_xf, bm_sc_xop, bm_obc_xf, bm_obc_xop, bm_ur_xf, bm_ur_xop
            global ip_st_xf, ip_st_xop, ip_sc_xf, ip_sc_xop, ip_obc_xf, ip_obc_xop, ip_ur_xf, ip_ur_xop
            global ce_st_xf, ce_st_xop, ce_sc_xf, ce_sc_xop, ce_obc_xf, ce_obc_xop, ce_ur_xf, ce_ur_xop
            j=0
        
            while(j < len(data_ur_xop) ):
                item = data_ur_xop[j]
                global d
                d = {}
                for i,col in enumerate(cursor.description):
                    # print(col[0])
                    # print(j[i])
                    d[col[0]] = item[i]
                data_ur_xop_list.append(d)
                # print(d['choice1']+":"+(d['allotment_result']))
                print(d['choice1'] ,"and", d['allotment_status'], d['Cname'])
                if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted' ):
                    print("CSS 1")
                    if(cse_ur_xop>0):
                        selected.append(d)
                        cse_ur_xop= cse_ur_xop-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']= "cse"
                        d['allotment_status']= "Allotted"
                        # data_st_xf_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status']) 
                        increaseFunction()
                if( (d['choice1'] == 'INFORMATION TECHNOLOGY') and d['allotment_status'] == 'Not Allotted' ):
                    print("ITTTTTTTTTTTTT")
                    print(it_ur_xop)
                    
                    if(it_ur_xop>0):
                        selected.append(d) 
                        
                        it_ur_xop= it_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        # data_ur_xop_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']) + d['allotment_status'])    
                        increaseFunction()     
                if(d['choice1'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xop>0):
                        selected.append(d)
                        ece_ur_xop= ece_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xop>0):
                        selected.append(d)
                        ei_ur_xop= ei_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xop>0):
                        selected.append(d)
                        ee_ur_xop= ee_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xop>0):
                        selected.append(d)
                        ip_ur_xop= ip_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['choice1'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == "Not Allotted"):
                    print("ceeeee")
                    if(ce_ur_xop>0 ):
                        selected.append(d)
                        ce_ur_xop= ce_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['choice1'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xop>0):
                        selected.append(d)
                        bm_ur_xop= bm_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                if(d['choice1'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xop>0):
                        selected.append(d)
                        me_ur_xop= me_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                
                print(d['allotment_status'])
                if(d['Choice2'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print("entered  in CS coice 2")
                    print(cse_ur_xop)
                    if(cse_ur_xop>0):
                        print("CS CHOICE 2")
                        selected.append(d)
                        cse_ur_xop= cse_ur_xop-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']= "cse"
                        d['allotment_status']= "Allotted"
                        # data_ur_xop_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()       
                if(d['Choice2'] ==  'INFORMATION TECHNOLOGY' ):
                    print("entered  in IT coice 2")
                    print(it_ur_xop)
                    if(it_ur_xop>0 and d['allotment_status'] == 'Not Allotted'):
                        print("ITT CHOICE 2")
                        selected.append(d)
                        it_ur_xop= it_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        # data_ur_xop_list.append(d)
                        print(d['choice1']+":"+(d['allotment_result']))      
                        increaseFunction()    
                if(d['Choice2'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xop>0):
                        selected.append(d)
                        ece_ur_xop= ece_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xop>0):
                        selected.append(d)
                        ei_ur_xop= ei_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xop>0):
                        selected.append(d)
                        ee_ur_xop= ee_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xop>0):
                        selected.append(d)
                        ip_ur_xop= ip_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice2'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xop>0):
                        selected.append(d)
                        ce_ur_xop= ce_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xop>0):
                        selected.append(d)
                        bm_ur_xop= bm_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice2'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xop>0):
                        selected.append(d)
                        me_ur_xop= me_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice3'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xop)
                    if(cse_ur_xop>0):
                        selected.append(d)
                        cse_ur_xop= cse_ur_xop-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice3'] == 'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xop)
                    if(it_ur_xop>0):
                        selected.append(d)
                        it_ur_xop= it_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice3'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print("ECCC3")
                    if(ece_ur_xop>0 ):
                        print("ECCC 3")

                        # print("ddddddd")
                        # print("selecteeeeedddddd beforeeeee")
                        # # print(selected)
                        selected.append(d)
                        # print(d)
                        # print("selecteeeeedddddd")
                        # # print(selected)
                        ece_ur_xop= ece_ur_xop-1
                        #increaseFunction()
                        d['allotment_result'] = "ece"
                        d['allotment_status'] = "Allotted"
                        # data_ur_xop_list.append(d)
                        print(d['Choice3']+":"+(d['allotment_result']) , d['allotment_status'])
                        increaseFunction()
                if(d['Choice3'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xop>0):
                        selected.append(d)
                        ei_ur_xop= ei_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice3'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xop>0):
                        selected.append(d)
                        ee_ur_xop= ee_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice3'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xop>0):
                        selected.append(d)
                        ip_ur_xop= ip_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice3'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xop>0):
                        selected.append(d)
                        ce_ur_xop= ce_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice3'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xop>0):
                        selected.append(d)
                        bm_ur_xop= bm_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice3'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xop>0):
                        selected.append(d)
                        bm_ur_xop= bm_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                
                if(d['Choice4'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xop)
                    if(cse_ur_xop>0):
                        selected.append(d)
                        cse_ur_xop= cse_ur_xop-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()   
                if(d['Choice4'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xop)
                    if(it_ur_xop>0):
                        selected.append(d)
                        it_ur_xop= it_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()   
                if(d['Choice4'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xop>0):
                        selected.append(d)
                        ece_ur_xop= ece_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xop>0):
                        print("EIII 4")
                        selected.append(d)
                        ei_ur_xop= ei_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xop>0):
                        selected.append(d)
                        ee_ur_xop= ee_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xop>0):
                        selected.append(d)
                        ip_ur_xop= ip_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice4'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xop>0):
                        selected.append(d)
                        ce_ur_xop= ce_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xop>0):
                        selected.append(d)
                        bm_ur_xop= bm_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice4'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xop>0):
                        selected.append(d)
                        me_ur_xop= me_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice5'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xop)
                    if(cse_ur_xop>0):
                        selected.append(d)
                        cse_ur_xop= cse_ur_xop-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))  
                        increaseFunction() 
                if(d['Choice5'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xop)
                    if(it_ur_xop>0):
                        selected.append(d)
                        it_ur_xop= it_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice5'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xop>0):
                        selected.append(d)
                        ece_ur_xop= ece_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xop>0):
                        selected.append(d)
                        ei_ur_xop= ei_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xop>0):
                        selected.append(d)
                        ee_ur_xop= ee_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xop>0):
                        selected.append(d)
                        ip_ur_xop= ip_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice5'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xop>0):
                        selected.append(d)
                        ce_ur_xop= ce_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xop>0):
                        selected.append(d)
                        bm_ur_xop= bm_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice5'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xop>0):
                        selected.append(d)
                        me_ur_xop= me_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice6'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xop)
                    if(cse_ur_xop>0):
                        selected.append(d)
                        cse_ur_xop= cse_ur_xop-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice6'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xop)
                    if(it_ur_xop>0):
                        selected.append(d)
                        it_ur_xop= it_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice6'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xop>0):
                        selected.append(d)
                        ece_ur_xop= ece_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xop>0):
                        selected.append(d)
                        ei_ur_xop= ei_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xop>0):
                        selected.append(d)
                        ee_ur_xop= ee_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xop>0):
                        selected.append(d)
                        ip_ur_xop= ip_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice6'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xop>0):
                        selected.append(d)
                        ce_ur_xop= ce_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xop>0):
                        selected.append(d)
                        bm_ur_xop= bm_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice6'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xop>0):
                        selected.append(d)
                        me_ur_xop= me_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                
                if(d['Choice7'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xop)
                    if(cse_ur_xop>0):
                        selected.append(d)
                        cse_ur_xop= cse_ur_xop-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice7'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xop)
                    if(it_ur_xop>0):
                        selected.append(d)
                        it_ur_xop= it_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice7'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xop>0):
                        selected.append(d)
                        ece_ur_xop= ece_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xop>0):
                        selected.append(d)
                        ei_ur_xop= ei_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xop>0):
                        selected.append(d)
                        ee_ur_xop= ee_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xop>0):
                        selected.append(d)
                        ip_ur_xop= ip_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice7'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xop>0):
                        selected.append(d)
                        ce_ur_xop= ce_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xop>0):
                        selected.append(d)
                        bm_ur_xop= bm_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice7'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xop>0):
                        selected.append(d)
                        me_ur_xop= me_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()

                if(d['Choice8'] ==  'COMPUTER SCIENCE & ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    print(cse_ur_xop)
                    if(cse_ur_xop>0):
                        selected.append(d)
                        cse_ur_xop= cse_ur_xop-1
                        print("called")
                        #increaseFunction()
                        d['allotment_result']="cse"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice8'] ==  'INFORMATION TECHNOLOGY' and d['allotment_status'] == 'Not Allotted'):
                    print(it_ur_xop)
                    if(it_ur_xop>0):
                        selected.append(d)
                        it_ur_xop= it_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="it"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))   
                        increaseFunction()
                if(d['Choice8'] ==  'ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ece_ur_xop>0):
                        selected.append(d)
                        ece_ur_xop= ece_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ece"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'ELECTRONICS & INSTRUMENTATION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ei_ur_xop>0):
                        selected.append(d)
                        ei_ur_xop= ei_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ei"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'ELECTRICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ee_ur_xop>0):
                        selected.append(d)
                        ee_ur_xop= ee_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ee"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'INDUSTRIAL & PRODUCTION ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ip_ur_xop>0):
                        selected.append(d)
                        ip_ur_xop= ip_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ipe"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result'])) 
                        increaseFunction()
                if(d['Choice8'] ==  'CIVIL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(ce_ur_xop>0):
                        selected.append(d)
                        ce_ur_xop= ce_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="ce"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'BIOMEDICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(bm_ur_xop>0):
                        selected.append(d)
                        bm_ur_xop= bm_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="bm"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']))
                        increaseFunction()
                if(d['Choice8'] ==  'MECHANICAL ENGINEERING' and d['allotment_status'] == 'Not Allotted'):
                    if(me_ur_xop>0):
                        selected.append(d)
                        me_ur_xop= me_ur_xop-1
                        #increaseFunction()
                        d['allotment_result']="me"
                        d['allotment_status']= "Allotted"
                        print(d['choice1']+":"+(d['allotment_result']) + (d['allotment_status']))
                        increaseFunction()
                
                j +=1 
                # print(j , "j")
                print("hiiiiii")
            
                # # print(selected)
           
    

    # s = " SELECT * from data_major_final where category= 'ST' and Alloted_Class='XF' ORDER BY Theory1 DESC ; "
    # cursor.execute(s)
    # data_st_xf = cursor.fetchall()
    # # print(data_st_xf)
    # print("###############")
    # # ST_XF()
    # print("@@@@@@@@@@@")
    # # print(selected)

    # for i in selected:
    #     s= "UPDATE data_major_final SET allotment_status= 'Allotted' WHERE enrollment_no= %s"
    #     cursor.execute(s,(i['enrollment_no'],))
    # #     print(i['enrollment_no'])
    # #     mydb.commit()
    
    # s = " SELECT * from data_major_final where category= 'ST' ORDER BY Theory1 DESC ; "
    # cursor.execute(s)
    # data_st_xop = cursor.fetchall()
    # # print(data_st_xop)
    # print("*************************")
    # # ST_XOP()


    s = " SELECT * from data_major_final where category= 'SC' and Alloted_Class='XF' ORDER BY Theory1 DESC ; "
    cursor.execute(s)
    data_sc_xf = cursor.fetchall()
    # print(data_sc_xf)
    print("###############")
    SC_XF()
    print("@@@@@@@@@@@")
    # print(selected)

    for i in selected:
        s= "UPDATE data_major_final SET allotment_status= 'Allotted' WHERE enrollment_no= %s"
        cursor.execute(s,(i['enrollment_no'],))
    #     print(i['enrollment_no'])
    #     mydb.commit()
    
    s = "SELECT * from data_major_final where category= 'SC' ORDER BY Theory1 DESC; "
    cursor.execute(s)
    data_sc_xop = cursor.fetchall()
    # print(data_sc_xop)
    SC_XOP()
    

    s = " SELECT * from data_major_final where category= 'OBC' and Alloted_Class='XF' ORDER BY Theory1 DESC ; "
    cursor.execute(s)
    data_obc_xf = cursor.fetchall()
    # print(data_obc_xf)
    print("###############")
    # OBC_XF()
    print("@@@@@@@@@@@")
    # print(selected)

    for i in selected:
        s= "UPDATE data_major_final SET allotment_status= 'Allotted' WHERE enrollment_no= %s"
        cursor.execute(s,(i['enrollment_no'],))
    #     print(i['enrollment_no'])
    #     mydb.commit()
    
    s = " SELECT * from data_major_final where category= 'OBC' ORDER BY Theory1 DESC; "
    cursor.execute(s)
    data_obc_xop = cursor.fetchall()
    # print(data_obc_xop)
    # OBC_XOP()
    

    s = " SELECT * from data_major_final where Alloted_Class='XF' ORDER BY Theory1 DESC ; "
    cursor.execute(s)
    data_ur_xf = cursor.fetchall()
    # print(data_ur_xf)
    print("###############")
    # UR_XF()
    print("@@@@@@@@@@@")
    # print(selected)

    for i in selected:
        s= "UPDATE data_major_final SET allotment_status= 'Allotted' WHERE enrollment_no= %s"
        cursor.execute(s,(i['enrollment_no'],))
    #     print(i['enrollment_no'])
    #     mydb.commit()
    
    s = " SELECT * from data_major_final ORDER BY Theory1 DESC; "
    cursor.execute(s)
    data_ur_xop = cursor.fetchall()
    # print(data_ur_xop)
    # UR_XOP()

    print(cse_st_xf)
    # ST_XF()
    # ST_XOP()
    # SC_XF()
    # SC_XOP()
    # OBC_XF()
    # OBC_XOP()
    # UR_XF()
    # UR_XOP()

    for i in selected:
        s= "UPDATE data_major_final SET allotment_status= 'Allotted' WHERE enrollment_no= %s"
        cursor.execute(s,(i['enrollment_no'],))
    #     print(i['enrollment_no'])
    #     mydb.commit()
    print(selected)
    # print(data_st_xf_list)
    response = jsonify(selected )
    response1 = jsonify(data_st_xf_list)
    # print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
    
    return {
        'userid':1,
        'title':'timmmmmmmm'
    }


@app.route('/stxf', methods=['GET'])
def stxf_route():
    response = jsonify(data_st_xf_list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/stxop', methods=['GET'])
def stxop_route():
    response = jsonify(data_st_xop_list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/scxf', methods=['GET'])
def scxf_route():
    response = jsonify(data_sc_xf_list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/scxop', methods=['GET'])
def scxop_route():
    response = jsonify(data_sc_xop_list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/obcxf', methods=['GET'])
def obcxf_route():
    response = jsonify(data_obc_xf_list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/obcxop', methods=['GET'])
def obcxop_route():
    response = jsonify(data_obc_xop_list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/urxf', methods=['GET'])
def urxf_route():
    response = jsonify(data_ur_xf_list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/urxop', methods=['GET'])
def urxop_route():
    response = jsonify(data_ur_xop_list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# @app.route('/st', methods=['GET'])
# def st_route():
#     return 'This is the st route'
if __name__== '__main__':
    app.run(debug=True)
    
    
     






