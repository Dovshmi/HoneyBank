# HoneyBank V1 Password_Manager by Dovshmi
from ast import Break
from dis import dis
import string
from tkinter import *
import os
from turtle import color
import inputdatabase
import time
from tkinter import ttk
from tkinter import messagebox
import shutil
from datetime import date
from tkinter import filedialog
import base64
import webbrowser as wb
import pyautogui
import time
from pynput.mouse import Listener
import threading

print(os.path.expanduser('~')+'\Documents\Data.db')
dataxx = str(os.path.expanduser('~')+'/Documents/')
dataxy = 'Honeybank'
path = os.path.join(dataxx,dataxy)
xo ="no"
print(os.path.isdir(path))
if os.path.isdir(path) == False:
    os.mkdir(path)
    dataxy = 'Honeybank/beckup'
    path = os.path.join(dataxx,dataxy)
    os.mkdir(path)
    inputdatabase.new_master_file()
    inputdatabase.new_sites_file()
    xo = "yes"
root = Tk()
root.title("HB")
root.iconbitmap('')
root_location=inputdatabase.locate_settings()
screenw = str(root_location[0])
screenh = str(root_location[1])
screenw2 = str(root_location[2])
screenh2 = str(root_location[3])
root.geometry("238x135+"+str(screenw)+"+"+str(screenh))
root.attributes('-topmost',True) # make the window allways in the front lines
color_dic={"orange": ["#FCA652","#FCA660","black","#FFEFA0","#FC5404","#FFD57E"],
           "blue":["#7987FF","#7987FF","black","#99A7FF","#1B4079","#4361ee"],
           "green":["#99e2b4","#88d4ab","black","#67b99a","#469d89","#78c6a3"],
           "pink":["#ff85a1","#ff99ac","black","#fbb1bd","#ff477e","#ff99ac"],
           "sky":["#bfd7ff","#9bb1ff","black","#e2fdff","#5465ff","#788bff"],
           "business":["#bc8a5f","#a47148","black","#e7bc91","#ff9f1c","#d4a276"],
           "night":["#5e6572","#5e6572","white","#a9b4c2","#343a40","#6c757d"],
           "light":["#fdfffc","#ced4da","black","#f8f9fa","#adb5bd","#dee2e6"]}
color_pic=root_location[4]
color_pic= color_dic.get(str(color_pic))
mainbg_color = str(color_pic[0])
tree_header_color = str(color_pic[1])
tree_header_title_color = str(color_pic[2])
tree_field_color = str(color_pic[3])
selecter_color = str(color_pic[4])
tree_site_color = str(color_pic[5])
root.configure(bg=mainbg_color)
flase = 0
header = Label(root, text="       Enter The Master Password       ",background=mainbg_color)
header.grid(column= 0, row= 1,sticky='ew')
header0 = Label(root, text="",background=mainbg_color)
header0.grid(column= 0, row= 0)
entry_password = Entry(root, show="*")
entry_password.grid(column= 0, row= 3)
header00 = Label(root, text="",background=mainbg_color)
header00.grid(column= 0, row= 4)
def prin():
    if xo == "yes":
        inputdatabase.insert_masterdate(entry_password.get())
    x = inputdatabase.verifi(entry_password.get())
    if x == True:
        root.title("HoneyBank")
        root.geometry("520x408+"+str(screenw2)+"+"+str(screenh2))
        header.grid_forget()
        header0.grid_forget()
        header00.grid_forget()
        master_button.grid_forget()
        entry_password.grid_forget()
        category=["american","shopping","banks","work/learning"]
        category2=[]
        ranger2 = inputdatabase.show_alldata()
        for h in range(len(ranger2)):
            ranger2_2 = ranger2[h]
            sitecategory = ranger2_2[3]
            category2.append(sitecategory)
            newlist2 = category2
            for h in category2:
                ij = 0
                for h2 in newlist2:
                    if h == h2:
                        ij = ij +1
                while ij != 1:
                    category2.remove(h)
                    ij = ij -1
        sitenames=[]
        ranger = inputdatabase.show_alldata()
        for i in range(len(ranger)):
            ranger_2 = ranger[i]
            sitedata = ranger_2[0]
            sitenames.append(sitedata)
        newlist = sitenames
        for i in sitenames:
            im = 0
            for i2 in newlist:
                if i == i2:
                    im = im + 1 
            while im != 1:    
                sitenames.remove(i)
                im = im -1
        def showalldata():
            category2=[]
            ranger2 = inputdatabase.show_alldata()
            for h in range(len(ranger2)):
                ranger2_2 = ranger2[h]
                sitecategory = ranger2_2[3]
                category2.append(sitecategory)
            newlist2 = category2
            for h in category2:
                ij = 0
                for h2 in newlist2:
                    if h == h2:
                        ij = ij +1
                while ij != 1:
                    category2.remove(h)
                    ij = ij -1
            sitenames=[]
            ranger = inputdatabase.show_alldata()
            for i in range(len(ranger)):
                ranger_2 = ranger[i]
                sitedata = ranger_2[0]
                sitenames.append(sitedata)
            newlist = sitenames
            for i in sitenames:
                im = 0
                for i2 in newlist:
                    if i == i2:
                        im = im + 1 
                while im != 1:    
                    sitenames.remove(i)
                    im = im -1
            #add some theme and color
            style = ttk.Style()
            style.theme_use("default")
            style.configure("Treeview", 
            background = mainbg_color,
            foreground = tree_header_title_color,
            fieldbackground=tree_field_color,
            )
            style.configure("Treeview.Heading", foreground=tree_header_title_color ,background=tree_header_color)
            style.map('Treeview.Heading', background=[('selected','C')],)
            style.map('Treeview', background=[('selected',selecter_color)],)
            tree = ttk.Treeview(root, height=10, column=("category\site", "user", "pass"), show='headings')
            tree.heading('#0', text='\n') #change the hight of the colums
            tree.column("#1",width=200, anchor=CENTER)
            tree.heading("#1", text="Category \ Site")
            tree.column("#2",width=160, anchor=W)
            tree.heading("#2", text="User")
            tree.column("#3",width=160,anchor=W)
            tree.heading("#3", text="Password")
            num = 0
            showall = inputdatabase.show_alldata()
            for h3 in category2:
                tree.tag_configure('siterow', background=mainbg_color)
                tree.insert("", index='end',iid=h3, values=(h3), tags=('siterow',))
                num2=0
                for i3 in sitenames:
                    numfor = 0
                    for h in range(len(showall)):
                        showall_value = showall[h]
                        loginsite = showall_value[0]
                        loginuser = showall_value[1]
                        loginpassword = showall_value[2]
                        logincategory = showall_value[3]
                        if i3 == loginsite and logincategory == h3 and numfor == 0:
                            tree.tag_configure('siterow2', background=tree_site_color)
                            num2 = num2+1
                            tree.insert(h3, index='end',iid=i3, values=(i3), tags=('siterow2',))
                            numfor = numfor +1
            showall = inputdatabase.show_alldata()
            num = 0
            for i2 in sitenames:
                for i in range(len(showall)):
                    showall_value = showall[i]
                    loginsite = showall_value[0]
                    loginuser = showall_value[1]
                    loginpassword = showall_value[2]
                    logincategory = showall_value[3]
                    urlSafeEncodedStr = loginpassword[::-1]
                    decodedBytes = base64.b64decode(urlSafeEncodedStr)
                    decodedStr = str(decodedBytes, "utf-8")
                    decodedStr = decodedStr[::-1]
                    loginpassword = decodedStr
                    if i2 == loginsite:
                        tree.tag_configure('color', background=tree_site_color)
                        num = num +1
                        tree.insert(i2, index='end',iid=num, values=("-->>", loginuser, loginpassword), tags=('color',))
            answerwow = " "
            def showtree():
                global answerwow
                global step
                answerwow = "User"
                x = tree.focus()
                y= tree.item(x)
                parent_iid = tree.parent(x)
                z = y['values']
                loginuser = z[1]
                loginpassword = z[2]
                loginsite = parent_iid
                print(loginuser)
                print(loginpassword)
                showall = inputdatabase.show_alldata()                
                for i in showall:
                    if loginsite == i[0] and loginuser == i[1]:
                        loginurl = i[5]
                        loginid = i[4]
                print(loginurl)
                print(loginid)
                def aoutologin(user, password, siteurl,id):
                    count = [user,password, id]
                    list = []
                    list.append(user)
                    list.append(password)
                    if id != "Null":
                        list.append(id)
                    def openuerl():
                        wb.open(siteurl)
                        time.sleep(2)
                        pyautogui.hotkey('tab')
                    openuerl()
                    press = 0
                    print (len(list))
                    button2.grid_forget()
                    button3.grid_forget()
                    button_delete.grid_forget()
                    button_update.grid_forget()
                    buttonsettings.grid_forget()
                    tree.grid_forget()
                    global answerwow
                    global countuserfeild
                    global step
                    step = "/2)"
                    if len(list)>2:
                        step = "/3)"
                    countuserfeild = 0 
                    def clickit():
                        time.sleep(0.5)# add a space
                        pyautogui.hotkey('ctrl', 'a')
                        time.sleep(0.5)
                        pyautogui.write(list[0])
                    def clickit2():
                        time.sleep(0.4)# add a space
                        pyautogui.hotkey('ctrl', 'a')
                        time.sleep(0.4)
                        pyautogui.write(list[1])
                    def clickit3():
                        time.sleep(0.6)# add a space
                        pyautogui.hotkey('ctrl', 'a')
                        time.sleep(0.6)
                        pyautogui.write(list[2])
                    # write a skip funcion and wire the tetoriel, and wite the ending function
                    def on_click(x,y,button,pressed):
                        global answerwow
                        global countuserfeild
                        global step
                        if pressed:
                            print(button)
                            buttonstring = str(button)
                            if buttonstring =="Button.left":
                                print("user")
                                answerwow = "password"
                                threading.Thread(target=clickit).start()
                                
                                answerwow = "password"
                            if buttonstring =="Button.right":
                                answerwow = "Done"
                                countuserfeild = countuserfeild +1
                                header_testleft.grid_forget()
                                header_test1.grid_forget()
                                header_test2.grid_forget()
                                header_test3.grid_forget()
                                header_test4.grid_forget()
                                showalldata()
                                
                                return False
                        else:
                            return False
                    def on_click2(x,y,button,pressed):
                        global answerwow
                        global countuserfeild
                        global step
                        if pressed:
                            buttonstring = str(button)
                            if buttonstring =="Button.left":
                                if len(list)<3:
                                    step2 ="           Done (step 2"+step
                                    header_username3 = Label(root, text=step2, background=mainbg_color)
                                    header_username3.grid(column= 1, row= 5, sticky='ew')
                                    answerwow = "Done"
                                    header_testleft.grid_forget()
                                    header_test1.grid_forget()
                                    header_test2.grid_forget()
                                    header_test3.grid_forget()
                                    header_test4.grid_forget()
                                    showalldata()
                                threading.Thread(target=clickit2).start()       
                                if len(list)>2:
                                    answerwow = "id"
                            if buttonstring =="Button.right":            
                                answerwow = "User"
                        else:
                            return False
                    def on_click3(x,y,button,pressed):
                        global answerwow
                        global step
                        if pressed:
                            buttonstring = str(button)
                            if buttonstring =="Button.left":
                                print("id")
                                step2 ="           Done (step 3"+step
                                header_username3 = Label(root, text=step2, background=mainbg_color)
                                header_username3.grid(column= 1, row= 5, sticky='ew')
                                answerwow = "Done"
                                threading.Thread(target=clickit3).start()
                                header_testleft.grid_forget()
                                header_test1.grid_forget()
                                header_test2.grid_forget()
                                header_test3.grid_forget()
                                header_test4.grid_forget()
                                showalldata()
                            if buttonstring =="Button.right":
                                answerwow = "password"
                        else:
                            return False
                    def hope():
                        global countuserfeild
                        global step
                        while answerwow != "Done":
                            if answerwow == "User":
                                step2 ="Pick a Username field (step 1"+step
                                header_username3 = Label(root, text=step2, background=mainbg_color)
                                header_username3.grid(column= 1, row= 5, sticky='ew')
                                with Listener(on_click=on_click) as listener:
                                    listener.join()
                            if answerwow =="Done":
                                countuserfeild = countuserfeild + 1
                                for i in range(countuserfeild+1):
                                    header_username3.grid_forget()
                                    
                                    
                            if answerwow == "password":
                                step2 ="Pick a Password field (step 2"+step
                                header_username2 = Label(root, text=step2, background=mainbg_color)
                                header_username2.grid(column= 1, row= 5, sticky='ew')
                                with Listener(on_click=on_click2) as listener:
                                    listener.join()
                                header_username3.grid_forget()
                                header_username2.grid_forget()
                            if len(list) > 2:
                                if answerwow =="id":
                                    step2 ="Pick a Id field (step 3"+step
                                    header_username3 = Label(root, text=step2, background=mainbg_color)
                                    header_username3.grid(column= 1, row= 5, sticky='ew')
                                    with Listener(on_click=on_click3) as listener:
                                        listener.join()
                                    header_username3.grid_forget()
                                    header_username2.grid_forget()
                    print(user)
                    header_testleft = Label(root,text="                                              ", background=mainbg_color)
                    header_testleft.grid(column= 0, row= 0,)
                    header_test1 = Label(root,text="                                  ", background=mainbg_color)
                    header_test1.grid(column= 2, row= 1,)
                    header_test2 = Label(root,text="                                  ", background=mainbg_color)
                    header_test2.grid(column= 2, row= 2,)
                    header_test3 = Label(root,text="                                  ", background=mainbg_color)
                    header_test3.grid(column= 2, row= 3,)
                    header_test4 = Label(root,text="                                  ", background=mainbg_color)
                    header_test4.grid(column= 2, row= 4,)
                    
                    threading.Thread(target=hope).start()
                aoutologin(loginuser, loginpassword, loginurl,loginid)
            def Delete():
                x = tree.focus()
                y= tree.item(x)
                z = y['values']
                parent_iid = tree.parent(x)
                loginuser = z[1]
                loginsite = parent_iid
                inputdatabase.remove_siteuser(loginsite, loginuser)
                tree.delete(x)
            def Update():
                x = tree.focus()
                y= tree.item(x)
                z = y['values']
                parent_iid = tree.parent(x)
                loginuser = z[1]
                loginpassword = z[2]
                login_id = inputdatabase.find_user(parent_iid,loginuser)
                button2.grid_forget()
                button3.grid_forget()
                button_delete.grid_forget()
                button_update.grid_forget()
                buttonsettings.grid_forget()
                header_site = Label(root, text="Update user values", background=mainbg_color)
                header_site.grid(column= 0, row= 1, sticky='ew', columnspan=2)
                header_username = Label(root, text="Username:", background=mainbg_color)
                header_username.grid(column= 0, row= 2, sticky='ew')
                entr_username1 = Entry(root)
                entr_username1.grid(column= 1, row= 2, sticky='ew')
                entr_username1.insert(0,loginuser)
                header_password = Label(root, text="Password", background=mainbg_color)
                header_password.grid(column= 0, row= 3, sticky='ew')
                entr_password1 = Entry(root)
                entr_password1.grid(column= 1, row= 3, sticky='ew')
                entr_password1.insert(0,loginpassword) # show where the password is and inserts it
                header3 = Label(root, text="id/specielusername", background=mainbg_color)
                header3.grid(column= 0, row= 4, sticky='ew')
                entr_id = Entry(root,state='normal')
                entr_id.grid(column= 1, row= 4, sticky='ew')
                entr_id.insert(0,login_id)
                if len(login_id) > 0:
                    entr_id['state'] = 'normal'
                else:
                    entr_id['state'] = 'disabled'
                origin_user = entr_username1.get()
                origin_site = parent_iid
                originsite_id = ["clalit", "macabi", "migdal"]
                for i in originsite_id:
                    if origin_site == i:
                        entr_id['state'] = 'normal'    
                def Submit_change():
                    new_user = entr_username1.get()
                    new_pass = entr_password1.get()
                    new_site = parent_iid
                    new_id = entr_id.get()
                    inputdatabase.update_database(new_user, new_pass, new_site, origin_user,origin_site,new_id)
                    tree.grid_forget()
                    entr_id.grid_forget()
                    header3.grid_forget()
                    button_subnitchange.grid_forget()
                    button_subnitback.grid_forget()
                    header_site.grid_forget()
                    header_username.grid_forget()
                    entr_username1.grid_forget()
                    header_password.grid_forget()
                    entr_password1.grid_forget()
                    button_update.grid_forget()
                    button_update.grid_forget()
                    showalldata()
                button_subnitchange = Button(root, text="Submit Change", command=Submit_change,background=mainbg_color)
                button_subnitchange.grid(column= 1, row = 5, sticky='ew')
                def Submit_back():
                    tree.grid_forget()
                    entr_id.grid_forget()
                    header3.grid_forget()
                    button_subnitchange.grid_forget()
                    button_subnitback.grid_forget()
                    header_site.grid_forget()
                    header_username.grid_forget()
                    entr_username1.grid_forget()
                    header_password.grid_forget()
                    entr_password1.grid_forget()
                    button_update.grid_forget()
                    button_update.grid_forget()
                    showalldata()
                button_subnitback = Button(root, text="Back", command=Submit_back,background=mainbg_color)
                button_subnitback.grid(column= 0, row = 5, sticky='ew')
            def insert():
                button2.grid_forget()
                button3.grid_forget()
                button_delete.grid_forget()
                button_update.grid_forget()
                buttonsettings.grid_forget()
                def Submit_insert():
                    v_category = category_combo.get()
                    v_option = site_combo.get()
                    v_user = entr_username.get()
                    v_password = entr_password.get()
                    v_id = entr_id.get()
                    v_url = entr_url.get()
                    sitempty = "Select Site"
                    categoryempy = "Category"
                    countit= 0
                    showall = inputdatabase.show_alldata()
                    for i in showall:
                        if v_option == i[0]:
                            if v_category != i[3]:
                                countit = 1
                    if not v_password or not v_user:
                        messagebox.showinfo("Wow", message="Please write down the username and password")
                    elif v_option == sitempty or v_category == categoryempy:
                        messagebox.showinfo("Wow", message="The category was not chosen")
                    elif v_url == sitempty:
                        messagebox.showinfo("Wow", message="no url was found")
                    elif v_url == "Paste a URL here":
                        messagebox.showinfo("Wow", message="no url was found")
                    elif countit == 1:
                        messagebox.showinfo("Wow", message="you already chose a category for this site")
                    else:
                        if v_id == "Use as a third loggin field" or v_id == "":
                            v_id = "Null"
                        inputdatabase.insert_newdate(v_option, v_user, v_password, v_category,v_id,v_url)
                        tree.grid_forget()
                        header.grid_forget()
                        header2.grid_forget()
                        header3.grid_forget()
                        entr_id.grid_forget()
                        entr_username.grid_forget()
                        entr_password.grid_forget()
                        button4.grid_forget()
                        button5.grid_forget()
                        category_combo.grid_forget()
                        site_combo.grid_forget()
                        entr_url.grid_forget()
                        showalldata()
                def showsiteoption(v_category):
                    v_category = category_combo.get()
                    optionsite= []
                    site_combo['state'] = 'normal'
                    if v_category == "Add category":
                        category_combo['state'] = 'normal'
                        category_combo.set("")
                        site_combo.config(value="")
                    else:
                        showall = inputdatabase.show_alldata()
                        sitenamesforcategory=[]
                        for i in showall:
                            if i[3] == v_category:
                                sitenamesforcategory.append(i[0])
                        sitenamesforcategory = list(dict.fromkeys(sitenamesforcategory))
                        site_combo.config(value=sitenamesforcategory)
                        site_combo.current()
                def back():
                    tree.grid_forget()
                    header.grid_forget()
                    header2.grid_forget()
                    header2.grid_forget()
                    entr_username.grid_forget()
                    entr_password.grid_forget()
                    button4.grid_forget()
                    button5.grid_forget()
                    category_combo.grid_forget()
                    site_combo.grid_forget()
                    entr_id.grid_forget()
                    header3.grid_forget()
                    entr_url.grid_forget()
                    showalldata()
                #combobox has readonly,normal,disabled
                category3 = ["Add category"]
                for i in category2:
                    category3.append(i)     
                category_combo = ttk.Combobox(root, value=category3,background=mainbg_color)
                category_combo.set("Category")
                category_combo.grid(column=0, row=1, sticky='ew')
                category_combo.bind("<<ComboboxSelected>>",showsiteoption)
                category_combo['state'] = 'readonly'
                site_combo = ttk.Combobox(root, value=" ", background=mainbg_color)
                site_combo.grid(column=1, row=1, sticky='ew')
                site_combo['state'] = 'disabled'
                entr_username = Entry(root)
                header = Label(root, text="Username:", background=mainbg_color)
                header.grid(column= 0, row= 2, sticky='ew')
                entr_username.grid(column= 1, row= 2, sticky='ew')
                header2 = Label(root, text="Password:", background=mainbg_color)
                header2.grid(column= 0, row= 3, sticky='ew')
                entr_password = Entry(root, show="*")
                entr_password.grid(column= 1, row= 3, sticky='ew')
                def print_selection():
                    if var1.get() == 0:
                        entr_id.insert(END, 'Use as a third loggin field')
                        entr_id['state'] = 'readonly'
                    if var1.get() == 1:
                        entr_id['state'] = 'normal'
                        entr_id.delete(0,END)
                var1 = IntVar()
                header3 = Checkbutton(root, text="Special Slot", background=mainbg_color,variable=var1, onvalue=1, offvalue=0, command=print_selection)
                header3.grid(column= 0, row= 4, sticky='ew')
                entr_id = Entry(root)
                entr_id.grid(column= 1, row= 4, sticky='ew')
                entr_id.insert(END, 'Use as a third loggin field')
                entr_id['state'] = 'readonly'
                entr_url = Entry(root, justify=CENTER,border=1, background=tree_field_color)
                entr_url.grid(column= 0, row= 5, sticky='ew', columnspan=2)
                entr_url.insert(END, 'Paste a URL here')
                def clearit(event): # clears the url one
                    letsee=entr_url.get()
                    if letsee == "Paste a URL here":
                        entr_url.delete(0,END)
                entr_url.bind("<Button-1>", clearit)
                button4 = Button(root, text="Submit", command=Submit_insert,background=mainbg_color)
                button4.grid(column= 1, row = 6, sticky='ew')
                button5 = Button(root, text="Back", command=back,background=mainbg_color)
                button5.grid(column= 0, row = 6, sticky='ew')
            def Setting():
                button2.grid_forget()
                button3.grid_forget()
                button_delete.grid_forget()
                button_update.grid_forget()
                buttonsettings.grid_forget()
                tree.grid_forget()
                not_set = 0
                def space():
                    header_settings.grid_forget()
                    button_space.grid_forget()
                    header_test1.grid_forget()
                    header_test2.grid_forget()
                    header_test3.grid_forget()
                    header_test4.grid_forget()
                    button_make_beckup.grid_forget()
                    button_load_beckup.grid_forget()
                    header_testleft.grid_forget()
                    button_back.grid_forget()
                    button_color.grid_forget()
                    root.geometry("238x135+"+str(screenw)+"+"+str(screenh))
                    def Submit_first():
                        little_x = str(root.winfo_x())
                        little_y = str(root.winfo_y())
                        #Put in command that adds it to the dataabase
                        button_little.grid_forget()
                        header_testfirst.grid_forget()
                        root.geometry("520x408+"+str(screenw2)+"+"+str(screenh2))
                        def Submit_second():
                            big_x = str(root.winfo_x())
                            big_y = str(root.winfo_y())
                            #Put in command that adds it to the database
                            inputdatabase.insert_location_settings(little_x,little_y,big_x,big_y)
                            button_big.grid_forget()
                            header_testsecond.grid_forget()
                            showalldata()
                        header_testsecond = Label(root,text="                                              ", background=mainbg_color)
                        header_testsecond.grid(column= 0, row= 0,)
                        button_big=Button(root,text="Submit Position Change (2/2)",command=Submit_second, background=mainbg_color,border=1)
                        button_big.grid(column=1,row=1, sticky='ew')
                    header_testfirst = Label(root,text="   ", background=mainbg_color)
                    header_testfirst.grid(column= 0, row= 0,)
                    button_little=Button(root,text="Submit Position Change (1/2)",command=Submit_first, background=mainbg_color,border=1)
                    button_little.grid(column=1,row=1, sticky='ew')
                def new_beckup():
                    frm = str(dataxx + "Honeybank/Data.db")
                    print (frm)
                    today = date.today()
                    d1 = today.strftime("%d-%m-%Y")
                    path2 = str(path + "/beckup/")
                    too = str(path2) + "beckup_"
                    too = str(too) + str(d1) + str(".db")
                    too =str(too)
                    print(too)
                    shutil.copy(frm,str(too))
                    progress = ttk.Progressbar(root, orient = HORIZONTAL,
                    length = 100, mode = 'determinate')
                    progress.grid(column=1, row=8)
                    i=0
                    for i in range(0,100,2):
                        progress['value'] = i
                        root.update_idletasks()
                        time.sleep(0.1)
                        if i ==98:
                            progress.grid_forget()
                def load_beckup():
                    display = filedialog.askopenfile(initialdir="~/Documents/Honeybank/beckup")
                    x = str(display)
                    x = x.split(' ')
                    x = x[1]
                    x = x.split('=')
                    x = x[1]
                    x = x[1:-1]
                    print (x)
                    frm = str(dataxx + "Honeybank/Data.db")
                    print (frm)
                    shutil.copy(x,str(frm))
                def back():
                    tree.grid_forget()
                    header.grid_forget()
                    header_testleft.grid_forget()
                    header_test1.grid_forget()
                    header_settings.grid_forget()
                    header_test2.grid_forget()
                    button_space.grid_forget()
                    header_test3.grid_forget()
                    button_make_beckup.grid_forget()
                    header_test4.grid_forget()
                    button_load_beckup.grid_forget()
                    header_test5.grid_forget()
                    button_back.grid_forget()
                    header_test6.grid_forget()
                    button_color.grid_forget()
                    showalldata()
                def color_change():
                    tree.grid_forget()
                    header.grid_forget()
                    header_testleft.grid_forget()
                    header_test1.grid_forget()
                    header_settings.grid_forget()
                    header_test2.grid_forget()
                    button_space.grid_forget()
                    header_test3.grid_forget()
                    button_make_beckup.grid_forget()
                    header_test4.grid_forget()
                    button_load_beckup.grid_forget()
                    header_test5.grid_forget()
                    button_back.grid_forget()
                    header_test6.grid_forget()
                    button_color.grid_forget()
                    def back2():
                        button_color2.grid_forget()
                        button_color3.grid_forget()
                        button_color4.grid_forget()
                        button_color5.grid_forget()
                        button_color6.grid_forget()
                        button_color7.grid_forget()
                        button_color8.grid_forget()
                        button_color9.grid_forget()
                        button_color10.grid_forget()   
                        button_back2.grid_forget()
                        header_testleft1.grid_forget()
                        header_testleft2.grid_forget()
                        header_settings2.grid_forget()
                        showalldata()
                    header_testleft1 = Label(root,text="                      ", background=mainbg_color)
                    header_testleft1.grid(column= 0, row= 0,)
                    header_testleft2 = Label(root,text="                                            ", background=mainbg_color)
                    header_testleft2.grid(column= 1, row= 0,)
                    header_settings2 = Label(root,text="", background=mainbg_color)
                    header_settings2.grid(column= 1, row= 6)
                    button_color2= Button(root,text="Honey Theme",command=lambda: inputdatabase.insert_color_settings("orange"),background="#FCA652",border=1)
                    button_color2.grid(column=1,row=2, sticky='ew')
                    button_color3= Button(root,text="     Pink Theme     ",command=lambda: inputdatabase.insert_color_settings("pink"),background="#ff85a1",border=1)
                    button_color3.grid(column=2,row=2, sticky='ew')
                    button_color4= Button(root,text="Blue Navy Theme",command=lambda: inputdatabase.insert_color_settings("blue"),background="#7987FF",border=1)
                    button_color4.grid(column=1,row=3, sticky='ew')
                    button_color5= Button(root,text="     Money Green Theme     ",command=lambda: inputdatabase.insert_color_settings("green"),background="#99e2b4",border=1)
                    button_color5.grid(column=2,row=3, sticky='ew')
                    button_color6= Button(root,text="Sky Dream Theme",command=lambda: inputdatabase.insert_color_settings("sky"),background="#bfd7ff",border=1)
                    button_color6.grid(column=1,row=4, sticky='ew')
                    button_color7= Button(root,text="     Business Thme     ",command=lambda: inputdatabase.insert_color_settings("business"),background="#bc8a5f",border=1)
                    button_color7.grid(column=2,row=4, sticky='ew')
                    button_color8= Button(root,text="Night Theme",command=lambda: inputdatabase.insert_color_settings("night"),background="#5e6572",border=1)
                    button_color8.grid(column=1,row=5, sticky='ew')
                    button_color9= Button(root,text="     Light Theme     ",command=lambda: inputdatabase.insert_color_settings("light"),background="#fdfffc",border=1)
                    button_color9.grid(column=2,row=5, sticky='ew')
                    button_color10= Button(root,text="Save and Exit",command=root.destroy,background=mainbg_color,border=1)
                    button_color10.grid(column=1,row=7, sticky='ew')
                    button_back2= Button(root,text="back",command=back2,background=mainbg_color,border=1)
                    button_back2.grid(column=2,row=7, sticky='ew')
                header_testleft = Label(root,text="                                  ", background=mainbg_color)
                header_testleft.grid(column= 0, row= 0,)
                header_test1 = Label(root,text="                                  ", background=mainbg_color)
                header_test1.grid(column= 1, row= 0,)
                header_settings = Label(root,text="Settings And Backup", background=mainbg_color)
                header_settings.grid(column= 1, row= 1)
                header_test2 = Label(root,text="                                  ", background=mainbg_color)
                header_test2.grid(column= 1, row= 2)
                button_space = Button(root,text="Change the placement of the app",command=space,background=mainbg_color,border=1)
                button_space.grid(column=1,row=3, sticky='ew')
                header_test3 = Label(root,text="                                  ", background=mainbg_color)
                header_test3.grid(column= 1, row= 4)
                button_make_beckup = Button(root,text="Create a new beckup file",command=new_beckup,background=mainbg_color,border=1)
                button_make_beckup.grid(column=1,row=5, sticky='ew')
                header_test4 = Label(root,text="                                  ", background=mainbg_color)
                header_test4.grid(column= 1, row= 6)
                button_load_beckup= Button(root,text="Load a beckup file",command=load_beckup,background=mainbg_color,border=1)
                button_load_beckup.grid(column=1,row=7, sticky='ew')
                header_test5 = Label(root,text="                                  ", background=mainbg_color)
                header_test5.grid(column= 1, row= 8)
                button_color= Button(root,text="Change color",command=color_change,background=mainbg_color,border=1)
                button_color.grid(column=1,row=9, sticky='ew')
                header_test6 = Label(root,text="                                  ", background=mainbg_color)
                header_test6.grid(column= 1, row= 10)
                button_back= Button(root,text="Back",command=back,background=mainbg_color,border=1)
                button_back.grid(column=1,row=11, sticky='ew') 
                #add reset option 22/11 2.0
                #set secret option 2.0
                #change lenguege in 2.0 (maby create a new app or make a huge if statment) create a verieble that says the english word and make it done i[0] or i[1]
            button2 = Button(root, text="Magic login", command=showtree,background=mainbg_color,border=1)
            button2.grid(column= 0, row = 1, sticky='ew',columnspan=2)
            button3 = Button(root, text="Sigh in a new user", command=insert,background=mainbg_color,border=1)
            button3.grid(column= 0, row = 2, sticky='ew',columnspan=2)
            button_delete = Button(root, text="Delete a user", command=Delete,background=mainbg_color,border=1)
            button_delete.grid(column= 0, row = 3, sticky='ew',columnspan=2)
            button_update = Button(root, text="Update user values", command=Update,background=mainbg_color,border=1)
            button_update.grid(column= 0, row = 4, sticky='ew',columnspan=2)
            buttonsettings = Button(root, text= "Settings",command=Setting, background=mainbg_color,border=1)
            buttonsettings.grid(column= 0, row = 5, sticky='ew',columnspan=2)
            tree.grid(column=0, row=0,columnspan=2)
        showalldata()
    else:
        messagebox.showinfo("Wow", message="Incorrect password")
master_button = Button(root, text="Login", command=prin,background=mainbg_color,border=1) 
master_button.grid(column= 0, row = 5, sticky='ew',columnspan=1)
root.mainloop()