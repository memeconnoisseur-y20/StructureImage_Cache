import tkinter
from tkinter import *
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
import urllib.request
import threading
from tkinter import ttk
import base64
import socket
import threading
import mysql.connector

'''this program might be stable or unstable.....who cares
PRE-SETUP REQUIREMENTS: PLEASE READ
1) Create a new folder named "StructureImage cache" in the same directory of this program
2) Install python-mysql-connector module
'''

top=tkinter.Tk()
top.title("CS Project")
#global connection
s='''- structure, chemical names, physical and chemical properties, classification, patents, literature, biological activities, safety/hazards/toxicity information, supplier lists, and more.'''
ans="y"
snip1=["Search and explore chemical information in the world's largest freely accessible chemistry database."]

global emp
# So what you are witnessing below is an image converted into base64-64 format so that we can just store em
# inside the program!
emp='''R0lGODlhLAEsAXAAACwAAAAALAEsAYH19fUAAAAAAAAAAAACfoSPqcvtD6OctNqLs968+w+G4kiW5omm6sq27gvH8kzX9o3n+s73/g8MCofEovGITCqXzKbzCY1Kp9Sq9YrNarfcrvcLDovH5LL5jE6r1+y2+w2Py+f0uv2Oz+v3/L7/DxgoOEhYaHiImKi4yNjo+AgZKTlJWWl5iZmpucnZ6UD5CRoqOkpaanqKmqq6ytrq+gobKztLW2t7i5uru8vb6/sLHCw8TFxsfIycrLzM3Oz8DB0tPU1dbX2Nna29zd3tM/0NHi4+Tl5ufo6err7O3u7+Dh8vP09fb3+Pn6+/z9/v/w8woMCBBAsaPIgwocKFDBs6fC8IMaLEiRQrWryIMaPGjRw7evwIMqTIkSRLmjyJMqXKlSxbunwJM6bMmTRr2ryJMymnzp08e/r8CTSo0KFEixo9ijSp0qVMmzp9CjWq1KlUq1q9ijWr1q1cuyV6/Qo2rNixZMuaPYs2rdq1bNu6fQs3rty5dOvavYs3r969fPv6I/0LOLDgwYQLGz6MOLHixYwbO34MObLkyZQrW76MObPmzZw7E3v+DDq06NGkS5s+jTq16tVICwAAOw=='''
logo='''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'''
sym='''R0lGODlhPgBHAHAAACH5BAEAAIsALAAAAAA+AEcAhwAAAH9/fyQkJCcnJxUVFWJiYv///3l5eREREQICAgEBATQ0NERERBgYGAsLCwcHBwkJCQUFBWxsbGZmZlNTUwwMDAMDA0VFRXNzcy8vLzo6OkhISAgICDMzM1VVVSsrK0xMTImJiRAQEAQEBBMTE3V1dVtbWx0dHTIyMmNjYyoqKh8fH1BQUBoaGhcXFzg4OE9PTyUlJVFRUUdHRxYWFjs7OwoKCklJSZmZmSgoKG1tbT4+Pj09PUFBQVRUVGFhYRISElZWVhsbG1hYWEpKSg4ODlxcXHFxcQ8PDzExMUZGRjU1NV1dXU5OTjY2NgYGBl5eXl9fXyEhIVJSUjk5OSwsLA0NDRwcHCYmJhQUFDc3N0NDQzAwMEtLSyIiIh4eHmBgYHh4eI2NjSkpKU1NTS4uLldXV2pqamlpaYuLiy0tLWhoaCsrJCMrO1VVqhMPDz8/PwABAhcXKRkZGQAABAIBAhYaHgEAAAQAAEVcXBcHBw8SHAYBAAAAAT8/Tzw8PBwODgYDACwbFgEBAgUAADIkHQIAACAgIBEUFyQdGSUrNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAj/ABcJHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePHxGA3AigZMmRFhGUVGkSAMqILV0KbPmyYcyDLGXWPGhSpEKaOwcCZeil586hD3P6DGmUYk6PLZdaRHqxKUmTVVeCVDrx6cucOhl6DTr2Z0kvMGNatYnVbFq1MaUuLBqWZ12FZQtSdcuXYduFLB2e7GtW7sLBh+/qVVxQpWG/jAkiRjiZcmSFdBNrJpx2c8LKix8/BC358iLSQk1D5mwQ9UzREF27nnlZNdvPpmXbXm3Zc+vdvhcHL51R9/DUxSPPPq0cOGvkz2knx30c+tTm1aVfj27dblbu2qlTmNQqvjxCx+Nzq+fdOXt48HZhd/fOVn5p++/ps1UPAH/+37HdRNte8P0lGFwEnmcgTgmatSBkDyoYYUcCBjhhcsslRt5VG17XYUVRcQSWXWGBVmFHI5aG2GQnbmWSHqmtqFODHznQloCD0TgSVicBQId2GR7lEo/OCSldkEEBqWOS1i3JJHMxFlkTi0gmaRgC/j2p5ZZcdhQQADs='''
#Below defines globals are used in functions that indicate whether we are online or not
global online
global offline
global refresh
online='''R0lGODlhHAAcAHAAACH5BAEAALgALAAAAAAcABwAhwAAAFWqVVGiaC65WB3FSxzDSxzGSxzFTBvGTDiuWVmZZgD/AFSpZynHVQ7QRA3PRA7QRQ7RRQ/PRDTHXlmZcmaZZiO/URLPRw3RRA/PRQ3PRQ7PRA3QRRDPRke3Z1+ffx3MTRHQRxHMRxbIRzysWn9/f06TazG2VhHNRg/QRDjOYx7MTg/QRhDORhbJSUulWiTEUTO/XDe2WC26UziyWxDQRUSuY1WUahLMRQ7PRRjHSVV/fzSzViy4VSu7Uym8Uiu8VEOpYCm/UhHMRW2RbS22URLLR1SbcRe9Rx/BTFyLcwD//w7ORA7RRDSvVw/ORTWxWFujbRzCShXLSTmsWhDMRhDNRybHUibCUw/ORGKcdVqUah3DTRPOSH+ffxjJSFKcalmZbDKvV2mWeGiWcy+0VQ3QRFObaVuXbWuTeGSRbT6nXVOcZlybajGwVm+Pb2WYcFuabSLBTRHORmKJdSzCVVegZVSNcSHFUBrGSxfMShTLSEOlYR3CTBLMR0+fbz+lWRLORj+tYg/QRRTJRxy9Sl2haxHPSDC6VA/NRS67V0aiYzK1VzG2VzG3VjW2WTywWxjKSRDORTy0YRDPRTi2WRLNRg/PRji3WyfBUhDQRii+UnWJdVChaxnJSR3KT////yTEUi+/WU+fZ0WpXBvASBLNRx7OTz62YBLQRw3ORCbCT2ObcT3EYCvKV0+nYGqUakGrYCa+USPATyLAUCO/TiO/Tyu8UgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjYAHEJHEiwoMGDCBMqXCgQCYghIBgmxKBqiMWLFiUOHKJKFQaOHSuqapKR4RCKQxBy/LiQZMqFHjEkbMJS4skmBy8eRGTh4MeXBDkCFYixJEGKBXUSHEkTw8+hTSoulTqQaZOmP4NyXAp1yNWvTTseVRWU7EanYLGaJboWF1WBTjGkvYp0YF22U+fSHSq2aluveqO29Rj0rlu0af8aFdi3qtyvKAsPdfuW8UmRSQkX7Dh5odPOuJSa3IrQpUnNCb0u1lp55ueQnEfW1NgxLmzQGi3o7qmxt8KAADs='''
offline='''R0lGODlhHAAcAHAAACH5BAEAAMEALAAAAAAcABwAhwAAAKpVVa1RUcw5QdwpMNsoL90nL90nLt0oL75ARKVZWf8AALNeXtw1OescJOobJOocJOwcJOscI+scJdxARJlmZtQuNekgKOwcI+kcJOocI+sbI+oeJsdPU59ff+QnL+ofJucfJuIlKrtDS59fX39/f5xYWMY7QuceJ+sdJeRDS+QqMOkeJeMjKrRLS9cvOOobI9I8QsdCQuoeJ+oeJc01PMFCR+geJeodJcBKUJRVauUeJuMkK8o5P802O881O9E0Os42O7VJT9U0OOcdJZFtbcg2O+QgJ6ljY9UlK9gqMItzc8E9QekdJcM7QaNbbdgoMOYhKb1BSuUeJ9sxN9gxOukeJuodJJxiYtwoMOcgKJ9/f+EkKqRaWp9fZsA+QpZpaZZoaMk6P6ZYXqNhYZNra+wbI5pkbbpKSqZYXaJjY8E5QY9vb5hlZcFCRppkZNYtNekgJ+keJ5x1ddg0PKdXXo1xcesdJN0rMusbJN4oMOUjK+geJKlUY+QhKaxLS9kpL+YhJ69fX7JGTOgfJ79LS+EhKNMnLukdI65dXekfJ+kbI8o4PNA5P7FNVMk7Qck6QMY9Q8JCSOMkLuceJqJcXMNLS8ZARMk5QOcgJ+seJcZCR9cyOeocJdIyN4l1deAmLekdJuofJ+EpMf///9oxN9U8P6dXV6lUcapqarlNTdUnLekcJeodJuUrM8pITOkhKegcJOkcI+kgJtgxNdhESeE3Pq9PV5RqarhKT9MwN9ctNNcuNNQuNNcuNc82Oq5QXQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjMAIMJHEiwoMGDCBMqXCjQgAFDBhgmNEORoiYzF81IHKgpY8WPFiV27Igwo6aFsEgurJjw4kmRZgwdzHjQk6eDIQsuilnQI0WDPwkaCjpwZ0WPBFkOpLgoKcanHwlqWvRSINFgPi1GXaqRq1OXIK+K7Wo1LFiywTA6dfo0K1qVZaWGhVo1bd2cVsF6bDowZd20aAF/nFrXZU+eSanu5MuV8cChgVeqNThyI16gVxFi/EtZKeWOkQ8aWgxyJOKNi4wOlrnRoKdDr1vLThgQADs='''
refresh='''R0lGODlhHAAcAHAAACH5BAEAADsALAAAAAAcABwAhQAAAG1tbSMjIxERERAQEBUVFQwMDBMTE0RERH9/f2NjY1xcXC8vLwEBAQICAg4ODj4+PkpKSgYGBgcHB3V1dWZmZg8PDwMDAx4eHgoKCnd3dyAgIDs7OwQEBAkJCS0tLVRUVFVVVQsLC19fX0VFRTc3N09PTxYWFiQkJF1dXQUFBXFxcQgICGpqajo6Oj8/P1BQUDMzMzk5OU5OTjQ0NCgoKCkpKSsrKxwcHEFBQUNDQwAAAAAAAAAAAAAAAAAAAAZmwJ1wSCwaj8ikcslsOp/EwQAwhRIB2Kx2MMQutWDtbgpQhgGCczYJPp6RW3bbvUaSxfQy/G28m8NHflZ9WAKDhF6HUXWKXYmNQniQcXZ6X5JXjH9gaYBNanNOd2Fcg1Onj5Cqq5BBADs='''

imagePath2 = PhotoImage(data=offline) # By default, image for offline is placed
widgetf2 = Label(top,  image=imagePath2,bg="#ffd2ab")  # Defining the widget so we can place it
widgetf2.place(x=0,y=0) # Here we place the widger we created earlier

def is_connected(): # Check if we are connected to the internet
    global online
    global offline
    try:
        socket.create_connection(("www.google.com", 80))  # Ping Google server, if we get response we are online
        state = "Online"
        stat  = online

    except OSError: # IF we don't get response, we are offline
        state = "Offline"
        stat  = offline

    # The code below will update the offline image(set as default) to online or offline, depending on connection
    imagePath2 = PhotoImage(data=stat) 
    widgetf2 = Label(top,  image=imagePath2,bg="#ffd2ab")
    widgetf2.image=imagePath2
    widgetf2.place(x=0,y=0)
    top.update_idletasks()
    top.after(100, is_connected)

# Once target repository is connected, we initialise the tkinter GUI application    
tt3 =threading.Event()
t3=threading.Thread(target=is_connected)
t3.start()


imagePath = PhotoImage(data=emp) #Emp is the variable for the place where we are placing the chemical structure image
widgetf = Label(top,  image=imagePath,bd=3,  bg="#3399ff")
widgetf.place(x=60,y=80)

imagePath1 = PhotoImage(data=logo) # Logo is, well the logo
widgetf1 = Label(top,  image=imagePath1,bg="#ffd2ab")
widgetf1.place(x=100,y=3)


def molecularweight(CID): #Get Molecular weight from repository
    global gmw
    mwlink="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/"+CID+"/property/MolecularWeight/txt"
    mwdata=requests.get(mwlink)
    mw= BeautifulSoup(mwdata.text, "html.parser") # Google this on your own 
    mw=str(mw).lstrip().rstrip()
    gmw=mw
    compweight2.config(text=mw)

    
def select(comp): # Get structures
    img = Image.open("StructureImage cache\\"+comp+".gif")
    tkimage = ImageTk.PhotoImage(img)
    structure = Label(top,image = tkimage,bd=3,bg="#3399ff")
    structure.image=tkimage
    structure.place(x=60,y=80)
    top.update_idletasks()

def save_info(v_srch_name,v_mlclr_name,v_mlclr_frml, v_mlclr_wght): # Save the 3 data units from repo and our search to a SQL table
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='divith',
                                 user='root',
                                 password='1234')
        if connection.is_connected():
           db_Info = connection.get_server_info()
           print("Connected to MySQL database... MySQL Server version on ",db_Info)
           cursor = connection.cursor()
           cursor.execute("select database();")
           record = cursor.fetchone()
           print ("Your connected to - ", record)
    except:
        print ("Error while connecting to MySQL")
    cur = connection.cursor()
    cur.execute('insert into chembook_history values (%s,%s,%s,%s)',(v_srch_name,v_mlclr_name,v_mlclr_frml, v_mlclr_wght))
    connection.commit()

            
def getinfo(event): # Get dat info and structure
    global gmw
    compound=txt.get()
    basepage = "https://pubchem.ncbi.nlm.nih.gov/compound/"+compound

    pagehtmldata = requests.get(basepage)

    soup = BeautifulSoup(pagehtmldata.text, "html.parser")

    try:
        name_formula = soup.find("meta", {"name": "description"})["content"]
        name_formula = name_formula.replace(s,"")
        name_formula = name_formula.split('|')
        if name_formula==snip1:
            name_formula="Please Check your formula again!"
        
        compoundname=name_formula[0]
        compoundform=name_formula[1]
        
        x=name_formula[2].lstrip().rstrip().split(" ")
                
        compformula2.config(text=compoundform)
        compname2.config(text=compoundname)
        molecularweight(x[1])

        
    except:
        print("Error in Getting Formula of given Compound")
        
    try:
        image = soup.find("meta", {"property": "og:image"})["content"]

        try:
            urllib.request.urlretrieve(image, r"StructureImage cache\\"+compound+".gif")#you have to create a new folder named "StructureImage cache" in the same directory of this program
        except:
            pass
    except:
        print("Error in Finding image of the given Compound")

    select(compound)
    save_info(compound,compoundname, compoundform,gmw )
    
def reset(): # Reset the input and output fields
    global emp
    compformula2.config(text="")
    compname2.config(text="")
    compweight2.config(text="")
    txt.delete(0,"end")
    
    imagePath = PhotoImage(data=emp)
    widgetf = Label(top,  image=imagePath,bd=3)#,  bg="#3399ff")
    widgetf.place(x=60,y=80)
    top.update_idletasks()    

# Below we remove the downloaded chemical structure and replace it with a blank image

refpic=PhotoImage(data=refresh)
ref=Button(top,image=refpic,bg="#ffd2ab",bd=0,command=reset)
ref.place(x=0,y=35)

txt=Entry(top,bd=5,font=("Arial Rounded MT",17),width=23)
txt.place(x=60,y=400)

# Below we just initialise output fields and their headers

compformula1 = Label(top,font=("cooper",17),text="Molecular Formula",bg="#ffd2ab",fg="#cc0066")
compformula1.place(x=115,y=450)

compformula2 = Label(top,font=("cooper",16),text=" ",width=25,bd=5)
compformula2.place(x=60,y=480)


compname1 = Label(top,font=("cooper",17),text="Molecular Name",bg="#ffd2ab",fg="#cc0066")
compname1.place(x=115,y=530)

compname2 = Label(top,font=("cooper",16),text=" ",width=25,bd=5)
compname2.place(x=60,y=560)


compweight1 = Label(top,font=("cooper",17),text="Molecular Weight",bg="#ffd2ab",fg="#cc0066")
compweight1.place(x=115,y=610)

compweight2 = Label(top,font=("cooper",16),text=" ",width=25,bd=5)
compweight2.place(x=60,y=640)

top.bind('<Return>', getinfo)

# Defines shape and size of application
top.configure(background="#ffd2ab")
top.geometry('430x700')
top.update()
top.mainloop()
