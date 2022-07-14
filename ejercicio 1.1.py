#EJERCICIO CON MARCOS Y DEMAS CARACTERISTICAS.
import tkinter as tk
#pone un titulo con fondo y un determinado grosor o profundidad 
ventana=tk.Tk()
ventana.title('Conversor')
ventana.geometry('400x600+700+100')
ventana.minsize(width=400,height=100)
ventana.configure(bg='lightblue')
label=tk.Label(ventana,text='Procesar Ley de OHM',bg='lightblue',fg='black',
               font='consolas 20 bold',relief=tk.GROOVE,bd=2,padx=10,pady=10)
label.pack(padx=20,pady=20)

#Primer marco
frame=tk.LabelFrame(ventana,text='Recoger Datos',bg='orange')
label=tk.Label(frame,text="Borrar",bg="grey")
label.pack(padx=20,pady=20)
label1=tk.Label(frame,text="Salir",bg="blue")
label1.pack(padx=20,pady=20)
frame.pack(fill=tk.X)

#segundo marco
frame1=tk.LabelFrame(ventana,text='Operación de Datos',bg='yellow')
label=tk.Label(frame1,text="Borrar",bg="red")
label.pack(padx=20,pady=20)
label2=tk.Label(frame1,text="Salir",bg="blue")
label2.pack(padx=20,pady=20)
frame1.pack(fill=tk.X)

#tercer marco
frame2=tk.LabelFrame(ventana,text='Resultados',bg='pink')
label=tk.Label(frame2,text="Suma",bg="green")
label.pack(padx=20,pady=20)
label3=tk.Label(frame2,text="Resta",bg="gold")
label3.pack(padx=20,pady=20)
frame2.pack(fill=tk.X)



            
