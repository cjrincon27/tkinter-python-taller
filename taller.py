from  tkinter  import *
def vv(re):
    ventana2=Toplevel()
    ventana2.geometry('200x355')
    ventana2.title("formula voltaje")
    ventana2.iconbitmap('logo.ico')
    img=PhotoImage(file='vol.png')
    label=Label(ventana2,image=img)
    label.place(x=0,y=30)
    label1=Label(ventana2,text='VOLTAJE',bg='orange',fg='blue', width = "200")
    label1.pack()
    label2=Label(ventana2,text=(re,"v"),bg='red',fg='white',width = "200")
    label2.pack()
    ventana2.mainloop()
    


    
def vi(re):
    ventana3=Toplevel()
    ventana3.geometry('200x370')
    ventana3.title("formula corriente")
    ventana3.iconbitmap('logo.ico')
    img=PhotoImage(file='corr.png')
    label=Label(ventana3,image=img)
    label.place(x=0,y=30)
    label1=Label(ventana3,text='CORRIENTE',bg='orange',fg='blue', width = "200")
    label1.pack()
    label2=Label(ventana3,text=(re,"a"),bg='red',fg='white',width = "200")
    label2.pack()
    ventana3.mainloop()
    
    
def vr(re):
    ventana4=Toplevel()
    ventana4.geometry('200x340')
    ventana4.title("formula resistencia")
    ventana4.iconbitmap('logo.ico')
    img=PhotoImage(file='re.png')
    label=Label(ventana4,image=img)
    label.place(x=0,y=30)
    label1=Label(ventana4,text='RESISTENCIA',bg='orange',fg='blue', width = "200")
    label1.pack()
    label2=Label(ventana4,text=(re,"h"),bg='red',fg='white',width = "200")
    label2.pack()
    ventana4.mainloop()
   
def send_data():
  v_info = v.get()
  i_info = i.get()
  r_info = r.get()
  print(v_info,"\t", i_info,"\t", r_info,"\t")
  if v_info==0:
   result=i_info*r_info
   vv(result)
   
  if i_info==0:
    result=v_info/r_info
    vi(result)
    
  if r_info==0:
    result=v_info/i_info
    vr(result)
  return 
 
  
#leo imagen con PhotoImage para usarla de fondo 

ventana=Tk()
imagen = PhotoImage(file = "ohm.png")
ventana.geometry('612x400')
ventana.iconbitmap('logo.ico')
ventana.title("aplicacion ley de hom ")
ventana.resizable(False,False)#funciona para que la ventana nno se pueda cambiar de tamaño 
background = Label(image = imagen)
background.place(x = 0, y = 25, relwidth = 1, relheight = 1)
main_title = Label(text = "LEY DE HOM", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()
#ubico titulos
age_label = Label(text = "INGRESE LOS VALORES CONOCIDOS ", bg = "aquamarine1")
age_label.place(x =350, y = 70)
v_label = Label(text = "voltaje", bg = "blue",fg="white")
v_label.place(x = 350, y = 110)
i_label = Label(text = "corriente", bg = "red",fg="white")
i_label.place(x = 350, y = 170)
r_label = Label(text = "resistencia", bg = "green",fg="white")
r_label.place(x = 350, y = 230)
#- llenar  valores
#declarovariables
v =DoubleVar()
i= DoubleVar()
r=DoubleVar()
#ubicacion tamaño y forma de la entrada 
v_entry = Entry(textvariable = v, width = "20", bg = "alice blue")
i_entry = Entry(textvariable = i, width = "20",  bg = "alice blue")
r_entry = Entry(textvariable = r, width = "20", bg = "alice blue")
v_entry.place(x = 350, y = 130)
i_entry.place(x = 350, y = 190)
r_entry.place(x = 350, y = 250)
#capturo los valores ingresados 
submit_btn = Button(ventana,text = "descubre el resultado =", width = "25", height = "1", command = send_data, bg = "pink")
submit_btn.place(x = 400, y = 320)


