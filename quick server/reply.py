import quarries as qa
import andrpack as pack
import socket

def suggestion(conn):
    size = pack.int_from_bytes(conn.recv(4))
    data = conn.recv(size)
    sugg_line = data.decode("utf-8")
    table = qa.filter_listSugg(qa.find_ewherepeople(sugg_line), sugg_line)

    reply = pack.table_to_bytes(table)
    ans = pack.int_to_bytes(1, 4) + pack.int_to_bytes(len(reply), 4) + reply
    conn.send(ans)

def find_person(conn):
    size = pack.int_from_bytes(conn.recv(4))
    data = conn.recv(size)
    name = data.decode("utf-8")
    table = qa.table_to_list("SELECT * FROM people WHERE CONCAT(name, ' ', surname) = '" + name +"'")
    table = table[1:]
    
    reply = pack.table_to_bytes(table)
    ans = pack.int_to_bytes(2, 4) + pack.int_to_bytes(len(reply), 4) + reply
    conn.send(ans)


