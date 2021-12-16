import pymysql as sql
import datetime


def ask_people(theme, id):
    
    con  = sql.connect(host='localhost', user='root', password='password', database= "roman")

    with con:
        cur = con.cursor()
        cur.execute("select " + theme +  " from people where name = '" + id +"'")
        return cur.fetchone()[0]

def add_people(theme, id):
    
    con  = sql.connect(host='localhost', user='root', password='password', database= "roman")

    with con:
        cur = con.cursor()
        cur.execute("select " + theme +  " from people where name = '" + id +"'")
        return cur.fetchone()[0]

def dont_die():
    con  = sql.connect(host='localhost', user='root', password='password', database= "roman")

    with con:
        cur = con.cursor()
        cur.execute("describe people")
        return cur.fetchone()[2]

def describe():
    lst = []
    con  = sql.connect(host='localhost', user='root', password='password', database= "roman")

    with con:
        cur = con.cursor()
        cur.execute("describe people")
        desc = cur.description
        for i in desc: lst+= [i[0]]
        return lst

def table_to_list(quarrie:str):
    lst = []
    con  = sql.connect(host='localhost', user='root', password='password', database= "roman")

    with con:
        cur = con.cursor()
        cur.execute(quarrie)
        desc = cur.description
        names = []
        for i in desc: names+= [i[0]]
        lst += [names]

        rows = cur.fetchall()
        for row in rows:
            newlist = []
            for i in range(len(row)): newlist+= [row[i]]
            lst += [newlist]
    
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == None: lst[i][j] = "NULL"
            elif isinstance(lst[i][j], datetime.date): lst[i][j] = lst[i][j].strftime('%Y-%m-%d')
            elif isinstance(lst[i][j], int): 
                lst[i][j] = str(lst[i][j])
    return lst
    
def find_ewherepeople(line:str):
    return table_to_list("SELECT * FROM people WHERE name LIKE '"'%{line}%'"' OR surname LIKE '"'%{line}%'"' OR phone LIKE '"'%{line}%'"' OR email LIKE '"'%{line}%'"' OR of_note LIKE '"'%{line}%'"';".format(line = line))    

def filter_listSugg(data:list, line:str):
    ans = data
    for i in range(len(ans)): ans[i][0] = ans[i][1] + " " + ans[i][2]

    for i in range(1, len(ans)):
        k = -1
        for j in range(1, len(ans[i])):
            if line.lower() in ans[i][j].lower(): 
                k = j+1
                ans[i].insert(j+1, ans[0][j])
                #ans[i][j+1] = ans[0][j]
                break
        for j in range(len(ans[i])-1, 0, -1):
            if j != k-1 and j != k: ans[i].pop(j)

    ans = ans[1:]
    return ans

#table = filter_listSugg(find_ewherepeople("NULL"), "NULL")
#for i in table: print(i)

