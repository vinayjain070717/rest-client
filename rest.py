from tkinter import *
import requests

def setRequestType(value):
 root.requestType=value 

def sendRequest():
 errorLabel.config(text='')
 if(root.requestType!='GET' and root.requestType!='POST'):
  errorLabel.config(text='Please select one request type : GET or POST from Option pane')
  return
 if(len(URL.get())==0):
   errorLabel.config(text='Please Give URL')
   return
 if(root.requestType=='GET'):
  try:
   text3.delete("1.0",END)
   r=requests.get(url=URL.get(),params=text1.get("1.0",END))
   data=r.json()
   statusCode=r.status_code
   if(statusCode==200):
    label2.config(text=r.status_code,bg='green')
   else:
     label2.config(text=r.status_code,bg='red')
   text3.insert("1.0",data)
  except Exception as e:
     errorLabel.config(text=e)
 if(root.requestType=='POST'):
  try:
   text3.delete("1.0",END)
   r=requests.post(url=URL.get(),data=text2.get("1.0",END))
   d=r.text
   statusCode=r.status_code
   if(statusCode==200):
    label2.config(text=r.status_code,bg='green')
   else:
     label2.config(text=r.status_code,bg='red')
   text3.insert("1.0",d)
  except Exception as e:
   errorLabel.config(text=e)

root=Tk()
URL=StringVar()
root.requestType=NONE
root.geometry('1000x600+100+50')
label1=Label(root,text='REST CLIENT',padx=400,pady=5,font=("Courier",40),bg='white')
label1.place(x=0,y=0)

errorLabel=Label(root,text='',padx=200,font=("Helvetica",12,'bold'),fg='red')
errorLabel.place(x=50,y=75)
Label(root,text='Method : ',font=('Helvetica',12)).place(x=10,y=100)
v1=StringVar(root)
v1.set("<SELECT OPTION>")
option=OptionMenu(root,v1,"GET","POST",command=setRequestType)
option.place(x=80,y=100)

Label(root,text='URL/HOST : ',font=('Helvetica',12)).place(x=240,y=100)
entry=Entry(root,width=75,textvariable=URL)
entry.place(x=340,y=100)

button=Button(root,text='SEND',padx=30,pady=5,command=sendRequest)
button.place(x=850,y=100)
Label(root,text='Add Header ... :',font=('Helvetica',12)).place(x=140,y=130)
text1=Text(root,width=50,height=9)
text1.place(x=50,y=150)

Label(root,text='Body (For Post method only) : ').place(x=550,y=130)
text2=Text(root,width=50,height=9)
text2.place(x=500,y=150)

Label(root,text='Response',font=('Helvetica',20,'bold')).place(x=60,y=300)
label2=Label(root,text="",padx=423,pady=5,font=('Helvetica',15,'bold'))
label2.place(x=50,y=330)

text3=Text(root,width=110,height=12)
text3.place(x=50,y=360)
root.mainloop()