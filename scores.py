from sqlite3 import connect
from datetime import datetime

def new_score(winner):
    conn = connect('/home/ruben/final-port/TTT-Python-Advanced/testdb.db')
    curs = conn.cursor()
    curs.execute('SELECT MAX(id) FROM scores')
    i = curs.fetchone()
    new_id = i[0]
    #print(new_id)
    new_id+=1
    new_id = str(new_id)
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    statement ='INSERT INTO scores VALUES('+new_id+',\''+winner+'\',\''+dt_string+'\')'
    #print(statement)
    curs.execute(statement)
    statement2 = 'SELECT * FROM ( select * from scores ORDER BY id DESC LIMIT 5 ) ORDER BY id ASC;'
    curs.execute(statement2)
    table = curs.fetchall()
    print("GAME--Inits-----Date------Time----")
    for row in table:
        print(row)
    conn.commit()
    conn.close()
    return