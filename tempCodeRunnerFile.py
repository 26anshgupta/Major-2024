 list = []
    
#     for j in data_common:
#         # print(j)
#         d = {}
#         for i,col in enumerate(cursor.description):
#             # print(col[0])
#             # print(j[i])
#             d[col[0]] = j[i]
#             # print(d)
#         list.append(d)



#     selected = []
    
#     j=0
#     while(j < len(data_st) and cse_st>0):
#         # print(j)
#         item = data_st[j]
#         d = {}
#         for i,col in enumerate(cursor.description):
#             # print(col[0])
#             # print(j[i])
#             d[col[0]] = item[i]
#         # print(d['choice1']+":"+(d['allotment_result']))
#         if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING'):
#             selected.append(d)
#             j= j+1
#             cse_st= cse_st-1
#             print(d['choice1']+":"+(d['allotment_result']))
#         else:
#             j=j+1
#     print(cse_st)
#     if(cse_st!=0):
#         cse_sc= cse_sc+ (cse_st)
#     print(cse_sc)


#     j=0
#     while(j < len(data_sc) and cse_sc>0):
#         # print(j)
#         item = data_sc[j]
#         d = {}
#         for i,col in enumerate(cursor.description):
#             # print(col[0])
#             # print(j[i])
#             d[col[0]] = item[i]
#         # print(d['choice1']+":"+(d['allotment_result']))
#         if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING'):
#             selected.append(d)
#             j= j+1
#             cse_sc= cse_sc-1
#             print(d['choice1']+":"+(d['allotment_result']))
#         else:
#             j=j+1
#     print(cse_sc)
#     if(cse_st!=0):
#         cse_obc= cse_obc+ (cse_sc)
#     print(cse_obc)


#     j=0
#     while(j < len(data_obc) and cse_obc>0):
#         # print(j)
#         item = data_obc[j]
#         d = {}
#         for i,col in enumerate(cursor.description):
#             # print(col[0])
#             # print(j[i])
#             d[col[0]] = item[i]
#         # print(d['choice1']+":"+(d['allotment_result']))
#         if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING'):
#             selected.append(d)
#             j= j+1
#             cse_obc= cse_obc-1
#             print(d['choice1']+":"+(d['allotment_result']))
#         else:
#             j=j+1
#     print(cse_obc)
#     if(cse_obc!=0):
#         cse= cse+ (cse_sc)
#     print(cse)


#     j=0
#     while(j < len(data_ur) and cse>0):
#         # print(j)
#         item = data_ur[j]
#         d = {}
#         for i,col in enumerate(cursor.description):
#             # print(col[0])
#             # print(j[i])
#             d[col[0]] = item[i]
#         # print(d['choice1']+":"+(d['allotment_result']))
#         if(d['choice1'] ==  'COMPUTER SCIENCE & ENGINEERING'):
#             selected.append(d)
#             j= j+1
#             cse= cse-1
#             print(d['choice1']+":"+(d['allotment_result']))
#         else:
#             j=j+1
#     print(cse)

#     for i in selected:
#         s= "UPDATE commoncopy SET allotment_result= 'Alloted' WHERE Enrollment_no= %s"
#         cursor.execute(s,(i['Enrollment_no'],))
#         print(i['Enrollment_no'])
#         mydb.commit()
    
#     # query = "CREATE TABLE selected_students(name VARCHAR(255))"
#     # cursor.execute(query)

    
#     # for i in range(0,cse):
#     #     print("hii",end="\n")

#     #     selected.append(data1[i])
#     #     print("ALLOTED")
#     #     s = "INSERT INTO selected_students(name) SELECT Cname FROM commoncopy WHERE enrollment_no= %s " 
#     #     cursor.execute(s, (data1[i][0],))
#     #     s= "UPDATE commoncopy SET allotment_result= 'Alloted' WHERE Enrollment_no= %s"
#     #     cursor.execute(s,(data1[i][0],))
#     #     mydb.commit()
#     #     s= "select * from selected_students ;"   
#     #     cursor.execute(s)
#     #     ans = cursor.fetchall()
#     #     print(ans)
#     #     print("loop end")
    
            
        
#     # s= "select * from selected ;"   
#     # cursor.execute(s)
#     # ans = cursor.fetchall()
#     # print(ans)
#     # print(selected)
#     response = jsonify(list)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
    
#     # return {
#     #     'userid':1,
#     #     'title':'timmmmmmmm'
#     # }
# if __name__== '__main__':
#     app.run()