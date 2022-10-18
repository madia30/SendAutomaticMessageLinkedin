import mysql.connector
from mysql.connector import Error

from datetime import datetime


#Creation de la bd
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='projet_idia_db',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Création des tables

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='projet_idia_db',
                                         user='root',
                                         password='')

    mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS message_send ( 
                             Id int(11) NOT NULL AUTO_INCREMENT,
                             prenom varchar(100),
                             nom varchar(100),
                             send_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    mySql_Create_Table_Query1 = """CREATE TABLE IF NOT EXISTS message_open ( 
                             Id int(11) NOT NULL AUTO_INCREMENT,
                             prenom varchar(100),
                             nom varchar(100),
                             open_date Date NOT NULL,
                             PRIMARY KEY (Id)) """


    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    result1 = cursor.execute(mySql_Create_Table_Query1)
    print("\n Tables created successfully ")


except mysql.connector.Error as error:
    print("\Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# Insertion dans les tables



def insert_varibles_into_table_messagesend(prenom, nom, send_date):
    try:
       connection = mysql.connector.connect(host='localhost',
                                         database='projet_idia_db',
                                         user='root',
                                         password='')
       cursor = connection.cursor()
       mySql_insert_query = """INSERT INTO message_send (prenom, nom, send_date) 
                                VALUES (%s, %s, %s) """
       record = (prenom, nom, send_date)
       cursor.execute(mySql_insert_query, record)
       connection.commit()
       print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

           # dsbulk load -h 172.17.0.2 -url /home/data/Téléchargements/USA_facebook.txt -k fatima -t face -delim ';' -m "number=number,UID=uid,first_name=first_name,last_name=last_name,sexe=sexe,city_of_birth=city_of_birth,city=city,status=status,company=compagny,last_publication=last_publication,mail=mail,date_of_birth=date_of_birth"
