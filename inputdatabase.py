import sqlite3
from sqlite3 import Error
import hashlib
import os
import base64
dataxx = str(os.path.expanduser('~')+'/Documents/')
dataxy = 'Honeybank'
path = os.path.join(dataxx,dataxy)
dataxx = str(path+'/Data.db')
print(dataxx)
def password_hashing(password): #hashing algoritam
    salt = os.urandom(32)
    password2 = password
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password2.encode('utf-8'),
        salt,
        100000 
    )
    storage = salt + key
    return storage
def print_salt(storage): # ptint the alt or storage value
    salt_from_storage = storage[:32] # 32 is the length of the salt
    key_from_storage = storage[32:]
    return salt_from_storage
def new_master_file():# create anew master table in the database
    
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute ("""CREATE TABLE masters (
       salt text,
       id text,
       loaded text
        )""")
    conn.commit()
    c.execute ("""CREATE TABLE settings (
       little_x text,
       little_y text,
       big_x text,
       big_y text,
       color text,
        id text
        )""")
    conn.commit()
    c.execute("INSERT INTO settings VALUES (?, ?, ?, ?, ?, ?)", ('500','500','500','500','orange','1'))
    conn.commit()
    c.execute("INSERT INTO masters VALUES (?, ?, ?)", ('a','1',dataxx))
    conn.commit()
    conn.close()
    
    
def insert_color_settings(color_name):
    master_id = '1'
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute("""UPDATE settings SET color=? WHERE id=?""", (color_name,master_id))
    conn.commit()
    conn.close()
def insert_location_settings(l_x,l_y,b_x,b_y):
    master_id = '1'
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute("""UPDATE settings SET little_x=?, little_y=?, big_x=?, big_y=? WHERE id=?""", (l_x,l_y,b_x,b_y,master_id))
    conn.commit()
    conn.close()
def locate_settings():
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute ("SELECT * FROM settings")
    name = c.fetchall()
    name = name[0]
    print(name)
    conn.commit()
    conn.close()
    return name
    
def insert_masterdate(password):#insert a new id and password to the masters table in the data base with hash
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    password = password
    hashed_p = password_hashing(password)
    t= '1'
    c.execute("""UPDATE masters SET salt=?, loaded=? WHERE id=?""", (hashed_p,dataxx,t))
    conn.commit()
    conn.close()

def verifi(password):# verify that the password is true
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    storage = c.execute("SELECT * FROM masters")
    name = c.fetchone()
    password2 = password
    name2 = name[0]
    salt = name2[:32]
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password2.encode('utf-8'), # Convert the password to bytes
        salt, 
        100000
    )
    name3 = salt + new_key
    if name3 == name2:
        return True
    else:
        return False
    conn.commit()
    conn.close()
def new_sites_file(): # ceate a new sites fide database
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute ("""CREATE TABLE sites (
       sitename text,
       username text,
       password text,
       category text,
       secondusername text,
       loginurl text
        )""")
    conn.commit()
    conn.close()
def insert_newdate(sitein, namein, passwordin, categoryin ,secondusernamein, loginurlin): # insert new data into sites table
    en_passwordin = passwordin[::-1]
    urlSafeEncodedBytes = base64.urlsafe_b64encode(en_passwordin.encode("utf-8"))
    urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")
    en_passwordin = urlSafeEncodedStr[::-1]
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute ("INSERT INTO sites VALUES (?, ?, ?, ?, ?, ?)", (sitein, namein, en_passwordin, categoryin, secondusernamein, loginurlin))
    conn.commit()
    conn.close()
def update_database(loginuser, loginpass, loginsite,nameold, siteold,secondusernamein):
    loginuser1 = loginuser
    en_passwordin = loginpass[::-1]
    urlSafeEncodedBytes = base64.urlsafe_b64encode(en_passwordin.encode("utf-8"))
    urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")
    en_passwordin = urlSafeEncodedStr[::-1]
    loginpass = en_passwordin
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute("""UPDATE sites SET username=?, password=?, sitename=?, secondusername=? WHERE username=? AND sitename=?""", (loginuser,loginpass,loginsite,secondusernamein,nameold,siteold))
    conn.commit()
    conn.close()
def find_user(sitename,siteuser): # find a user
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute ("SELECT * FROM sites WHERE sitename=? AND username=?", (sitename,siteuser))
    name = c.fetchall()
    name2 = name[0]
    loginuser = name2[1]
    loginpassword = name2[2]
    login_id = name2[4]
    conn.commit()
    conn.close()
    return login_id
def show_alldata():# show all data in the sites table
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute("SELECT * FROM sites")
    name =c.fetchall()
    conn.commit()
    conn.close()
    return name
def show_siteusers(sitename): # show user in a site
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute ("SELECT * FROM sites WHERE sitename=?", (sitename,))
    name =c.fetchall()
    conn.commit()
    conn.close()
    for i in range(len(name)):
        print (name[i])
def remove_siteuser(sitename, user): # remove a user
    conn = sqlite3.connect(dataxx)
    c = conn.cursor()
    c.execute("DELETE FROM sites WHERE sitename=? AND username=?", (sitename, user,))
    conn.commit()
    conn.close()

#insert_newdate("google","dovshmi","jdaisojas","american")
#insert_newdate("google","dovname","31233213","american")
#insert_newdate("הפועלים","shmidov","jdaisojas","banks")
#insert_newdate("braude","dovshmi","dddddddd","work/learning")
#insert_newdate("github","dovshmi","wowowowowo","american")



