from PIL import Image
import sqlite3
import os

server = r'link2sqldatabasefile.db'

def rgb2Hex(r,g,b):
    return f'#{r}{g}{b}'

def int2Hex(i):
    v = str(hex(i))
    v = v[2:]
    if len(v) == 1:
        v = str(0)+v
    return v

def insert_into (dbname, tblname, cols, vals):

    colnames = "[" + "], [".join(cols) + "]"
    values = "'" + "', '".join(map(str, vals)) + "'"
    print(values)
    con = sqlite3.connect(dbname)
    cur = con.cursor()

    db_cmd = "INSERT INTO " + "[" + tblname + "]" + " (" + colnames + ")" + " VALUES " +  "(" + values + ")"
    print(db_cmd)
    res = cur.execute(db_cmd)
    con.commit()
    cur.close()


path = r"pathtofolderwithpictures"
dir_list = os.listdir(path)
print(dir_list)

for i in dir_list:
    FILE = f'{path}\\{i}'
    try:
        im = Image.open(FILE)
        var = im.getcolors()
        
        for c in var:
            COUNT = c[0]
            R = c[1][0]
            G = c[1][1]
            B = c[1][2]
            A = c[1][3]
            HEX = rgb2Hex(int2Hex(R),int2Hex(G),int2Hex(B))           
            
            data = {
                'FILE_NM':i,
                'R':R,
                'G':G,
                'B':B,
                'A':A,
                'RGB_HEX':HEX,
                'COUNT':COUNT
            }
        
            keyValues = data.keys()
            valValues = data.values()
            var = insert_into(server,'COLORS',keyValues,valValues)
        
    except Exception as e:
        print(e)
