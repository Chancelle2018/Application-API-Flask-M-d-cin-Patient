# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:28:51 2021

@author: chane
"""
import sqlite3
from app import app

# conn= sqlite3.connect ( 'database.db')
# print("Base de données ouverte avec succès")

# conn.execute( 'CREATE TABLE member(login TEXT, mdp TEXT, role TEXT , Nom TEXT, Prenom TEXT )')

# print("Table créée avec succès")
# conn.close()


# with sqlite3.connect("database.db") as con:
#     cur= con.cursor()
#     cur.execute("SELECT * FROM member")
#     a=cur.fetchall()
#     print(a)
    
    
    
# conn= sqlite3.connect ( 'database.db')
# print("Base de données ouverte avec succès")

# conn.execute( 'CREATE TABLE carateristik(login TEXT, age TEXT, diagnostic TEXT )')

# print("Table créée avec succès")
# conn.close()
    
# with sqlite3.connect("database.db") as con:
#     cur= con.cursor()
#     cur.execute("SELECT * FROM carateristik")
#     a=cur.fetchall()
#     print(a)
        
    
    
    
    
     
    #return render_template('Authentification.html', title='Authentification Réussi!')
#con.close()

# with sqlite3.connect("database.db") as con:
#     cur= con.cursor()
#     cur.execute("INSERT INTO member(login,mdp) VALUES (?,?)", (" chancelle","1234"))
#     cur.execute("INSERT INTO member(login,mdp) VALUES (?,?)", (" maelle","2018"))
#     cur.execute("INSERT INTO member(login,mdp) VALUES (?,?)", (" kizima","1995"))
#     con.commit()
# con.close()


app.run(debug = False, port = 80, host='0.0.0.0')
app.run(debug = True, port = 80, host='0.0.0.0')