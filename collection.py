# import psycopg2
# def one_collection(user_id):
#     def get_collections(user_id):
#         try:
#             con = psycopg2.connect("db_psql")
#             cursorObj = con.cursor()
#             cursorObj.execute("SELECT collection_name FROM collection_collection WHERE user_id ="+str(user_id))
#             return cursorObj.fetchall()
#         except:
#             print("Sorry database not found!")
#         finally:
#             con.close()
#
#     def get_collection_details(name,user_id):
#         try:
#             con = psycopg2.connect("db_psql")
#             cursorObj = con.cursor()
#             cursorObj.execute('SELECT * FROM user_collections WHERE collection_name = \"'+ name + '\" AND user_id='+str(user_id))
#             return cursorObj.fetchone()
#         except:
#             print("Sorry database not found!")
#         finally:
#             con.close()
#
#     query = get_collections(1)
#     cols = {}
#
#     k=0
#     for col in query:
#         cols[k] = {}
#         col_deets =get_collection_details(col[0],1)
#         cols[k]['name']=col_deets[1]
#         cols[k]["image"] = col_deets[4]
#         k+=1
#
#     return cols
#
# print(one_collection(8))
