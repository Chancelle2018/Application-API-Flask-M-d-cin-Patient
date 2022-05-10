# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 00:28:37 2021

@author: chane
"""
from app import app
from flask import render_template
from flask import request, session
import json
import requests
import sqlite3

f = open('login_mdp.json')
global data
data = json.load(f)
f.close()

@app.route('/')
def index():
    user={'login' : 'Chancelle', 'surname':'Kizima'}
    if session=={}:
        return render_template('Bienvenu_Page.html', title='Bienvenu', utilisateur=user)
    else :
        return render_template('Welcome_Page_connected.html', title=str(session['login']), utilisateur=user)
    

@app.route('/Patient')#,methods=["POST"]
def Patient():
    identifiant = request.args.get("id")
    
    Organisation =  'app/kaggle/Organization/0.json'
    info_organisation = json.load(open(Organisation))
    open(Organisation).close()
    
    Patient = 'app/kaggle/Patient/'+str(identifiant)+'.json'
    info_patient = json.load(open(Patient))
    open(Patient).close()
    
    
    Medecin = 'app/kaggle/Medecin/'+str(identifiant)+'.json'
    info_medecin = json.load(open(Medecin))
    open(Medecin).close()

   

    MedicationRequest = 'app/kaggle/MedicationRequest/'+str(identifiant)+'.json'
    Medication = json.load(open(MedicationRequest))
  
    return render_template( 'Patient.html',Patient=info_patient,   Medecin=info_medecin,   Organisation=info_organisation,Medication=Medication)




@app.route('/Medecin')#,methods=["POST"]
def medecin():
    identifiant = request.args.get("id")
    Organisation =  'app/kaggle/Organization/0.json'
    info_organisation = json.load(open(Organisation))
    open(Organisation).close()
    Patient = 'app/kaggle/Patient/'+str(identifiant)+'.json'
    info_patient = json.load(open(Patient))
    open(Patient).close()
    
    
    Medecin = 'app/kaggle/Medecin/'+str(identifiant)+'.json'
    info_medecin = json.load(open(Medecin))
    open(Medecin).close()

   

    MedicationRequest = 'app/kaggle/MedicationRequest/'+str(identifiant)+'.json'
    Medication = json.load(open(MedicationRequest))
   
    return render_template('Medecin.html', medecin=info_medecin, Patient=info_patient,   Medecin=info_medecin,   Organisation=info_organisation,Medication=Medication)


    





@app.route("/confirmation",methods=['POST'])
def informations_medecin():    
    identifiant = request.form.get('identifier')
    nom = request.form.get('name')
    genre = request.form.get('gender')
    date = request.form.get('birthDate')
    adresse = request.form.get('address')
    covid = request.form.get('covid')
    dtp = request.form.get('dtp')
    coqueluche = request.form.get('Coqueluche')
    rubeole=request.form.get('Rubeole')
    hepatite=request.form.get('Hepatite')
    rougeole=request.form.get('Rougeole')
    oreillons=request.form.get('Oreillons')

    medecin = {
              "resourceType" : "Medecin",
              "identifier" : identifiant,
              "active" : "<boolean>",
              "name" : nom,
              "telecom" : "[{ ContactPoint }]",
              "gender" : genre,
              "birthDate" : date,
              "deceasedBoolean" : "<boolean>",
              "deceasedDateTime" : "<dateTime>",
              "address" : adresse,
              "maritalStatus" : "{ CodeableConcept }",
              "multipleBirthBoolean" : "<boolean>",
              "multipleBirthInteger" : "<integer>",
              "photo" : "[{ Attachment }]",
              "contact" : [{
                "relationship" : "[{ CodeableConcept }]",
                "name" : "{ HumanName }",
                "telecom" : "[{ ContactPoint }]",
                "address" : "{ Address }",
                "gender" : "<code>",
                "organization" : "{ Reference(Organization) }",
                "period" : "{ Period }"
              }],
              "communication" : [{
                "language" : "{ CodeableConcept }",
                "preferred" : "<boolean>"
              }],
              "generalPractitioner" : "[{ Reference(Organization|Practitioner|PractitionerRole) }]",
              "managingOrganization" : "{ Reference(Organization) }",
              "link" : [{ 
                "other" : "{ Reference(Medecin|RelatedPerson) }",
                "type" : "<code>"
              }]
            }
    with open("app/fhir/Medecin/"+str(identifiant)+".json", "w") as f_write:
        json.dump(medecin, f_write, indent=1)
        
    Vaccins = {
        "Covid" : covid,
        'DTP' : dtp,
        'Coqueluche': coqueluche,
        'Rubeole' : rubeole,
        'Hepatite': hepatite,
        'Rougeole' : rougeole,
        'Oreillons' : oreillons
        }
        
    with open("app/fhir/Vaccins/"+str(identifiant)+".json", "w") as f_write:
        json.dump(Vaccins, f_write, indent=2)
    
    return ("<a href='/'>Page principale</a>")










@app.route("/confirmation",methods=['GET','POST'])
def informations_patient():    
    identifiant = request.form.get('identifier')
    nom = request.form.get('name')
    genre = request.form.get('gender')
    date = request.form.get('birthDate')
    adresse = request.form.get('address')
    covid = request.form.get('covid')
    dtp = request.form.get('dtp')
    coqueluche = request.form.get('Coqueluche')
    rubeole=request.form.get('Rubeole')
    hepatite=request.form.get('Hepatite')
    rougeole=request.form.get('Rougeole')
    oreillons=request.form.get('Oreillons')

    patient = {
              "resourceType" : "Patient",
              "identifier" : identifiant,
              "active" : "<boolean>",
              "name" : nom,
              "telecom" : "[{ ContactPoint }]",
              "gender" : genre,
              "birthDate" : date,
              "deceasedBoolean" : "<boolean>",
              "deceasedDateTime" : "<dateTime>",
              "address" : adresse,
              "maritalStatus" : "{ CodeableConcept }",
              "multipleBirthBoolean" : "<boolean>",
              "multipleBirthInteger" : "<integer>",
              "photo" : "[{ Attachment }]",
              "contact" : [{
                "relationship" : "[{ CodeableConcept }]",
                "name" : "{ HumanName }",
                "telecom" : "[{ ContactPoint }]",
                "address" : "{ Address }",
                "gender" : "<code>",
                "organization" : "{ Reference(Organization) }",
                "period" : "{ Period }"
              }],
              "communication" : [{
                "language" : "{ CodeableConcept }",
                "preferred" : "<boolean>"
              }],
              "generalPractitioner" : "[{ Reference(Organization|Practitioner|PractitionerRole) }]",
              "managingOrganization" : "{ Reference(Organization) }",
              "link" : [{ 
                "other" : "{ Reference(Patient|RelatedPerson) }",
                "type" : "<code>"
              }]
            }
    with open("app/fhir/Patient/"+str(identifiant)+".json", "w") as f_write:
        json.dump(patient, f_write, indent=2)
        
    Vaccins = {
        "Covid" : covid,
        'DTP' : dtp,
        'Coqueluche': coqueluche,
        'Rubeole' : rubeole,
        'Hepatite': hepatite,
        'Rougeole' : rougeole,
        'Oreillons' : oreillons
        }
        
    with open("app/fhir/Vaccins/"+str(identifiant)+".json", "w") as f_write:
        json.dump(Vaccins, f_write, indent=2)
    
    return ("<a href='/'>Page principale</a>")


















@app.route('/Signin',methods=["POST"])
def Signin():
    if request.method == 'POST':
        login = request.form['login']
        valid_member=False
        
        # conn= sqlite3.connect ( 'database.db')
        

        # print("Base de données ouverte avec succès")

        # conn.execute( 'CREATE TABLE member(login TEXT, mdp TEXT, role TEXT, Nom TEXT, Prenom Text )')

        # print("Table créée avec succès")

        # conn.close()
        
        
        # with sqlite3.connect("database.db") as con:
        #     cur= con.cursor()
        #     cur.execute("INSERT INTO member(login,mdp, role,Nom, Prenom) VALUES (?,?,?,?,?)", ("","","","",""))
        #     con.commit()
        # con.close()
        
        
        
        
        
        
        # print("Base de données ouverte avec succès")

        # conn.execute( 'CREATE TABLE carateristik(login TEXT, age TEXT diagnostic )')

        # print("Table créée avec succès")

        # conn.close()
        
        
        # with sqlite3.connect("database.db") as con:
        #     cur= con.cursor()
        #     cur.execute("INSERT INTO carateristik(login,age, diagnostic) VALUES (?,?,?)", ("","",""))
        #     con.commit()
        # con.close()

        
        
        
        

        
        with sqlite3.connect("database.db") as con:
            cur= con.cursor()
            cur.execute("SELECT * FROM member")
            a=cur.fetchall()
            print(a)
            return render_template('Authentification.html', title='Authentification Réussi!')
        con.close()
    
    
       
              
@app.route('/Authentification')
def authentification():
    return render_template('Authentification.html', title='Authentification Réussi!')

@app.route('/Erreur')
def errer():
    return render_template('Erreur.html', title='Erreur')




















   
    
   
    
   
@app.route('/Deconnecter')#,methods=["POST"]
def deconnecter():
    session.pop('login',None)
    session.pop('role',None)
    return render_template('Bienvenu_Page.html', title='Bienvenu')


