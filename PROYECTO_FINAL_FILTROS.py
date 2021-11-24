import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageTk
import re
import os
from numpy.lib.type_check import imag



ventana=tk.Tk()
ventana.title("Prgrama Filtros")

miframe=tk.Frame(ventana)
miframe.pack()
miframe.config(bg="black",cursor='hand2')


#----------------------------------FUNCIONES----------------------------------------------------
def select():
    global imagen
    #BACK FUNCION PARA VOLVER AL MENÚ PRINCIPAL
    def back1():
        ventanaitf.destroy()
    def back2():
        ventanatf.destroy()
#------------------------FUNCIONES PARA FILTROS IDEALES FT-----------------------------
    def ITF():
        if menu1.current()==0:
            def regresar1():
                ventanapbi.destroy() 
            def Filtro1():
                num = entry.get()
                if num.isnumeric() == True:
                    num = int(num)
                    img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                    f=np.fft.fft2(img)
                    fshift=np.fft.fftshift(f)
                    rows,cols=img.shape
                    crow,ccol=int(rows/2),int(cols/2)
                    mask=np.ones((rows,cols), np.uint8)
                    D=num
                    mask[crow-D:crow+D, ccol-D:ccol+D]=0
                    f_ishift=fshift*mask
                    f_shift=np.fft.ifftshift(f_ishift)
                    img_back=np.fft.ifft2(f_shift)
                    img_back=np.abs(img_back)
                    plt.subplot(131),plt.imshow(img, cmap= 'gray')
                    plt.title('Original'), plt.xticks([]), plt.yticks([])
                    plt.subplot(132),plt.imshow(mask, cmap= 'gray')
                    plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                    plt.subplot(133),plt.imshow(img_back,cmap= 'gray')
                    plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                    plt.show()
                else:
                    messagebox.showerror(message="Ingresa solo datos numéricos",title="Error")

            ventanapbi=tk.Tk()
            ventanapbi.title("PASA BAJAS IDEAL POR TF")

            miframepbi=tk.Frame(ventanapbi)
            miframepbi.pack()
            miframepbi.config(bg="green",cursor='hand2')
            
            mensaje=tk.Label(miframepbi,text="Ingresa el valor para el radio",font=('Arial 20'),bg='green')
            mensaje.grid(row=0,column=1,padx=10,pady=10)
            
            entry = tk.Entry(miframepbi,font="Arial 18")
            entry.grid(row=1,column=1,padx=5,pady=5)
            entry.config(justify="center")
            
            boton9=tk.Button(miframepbi,text="FILTRAR",font="Arial 20",activebackground="green",command=Filtro1)
            boton9.grid(row=3,column=2,padx=5,pady=5)
            
            boton9=tk.Button(miframepbi,text="REGRESAR",font="Arial 20",activebackground="red",command = regresar1)
            boton9.grid(row=3,column=0,padx=5,pady=5)
            ventanapbi.mainloop()
        
        elif menu1.current()==1:
            def regresar2():
                ventanapai.destroy() 
            def Filtro2():
                num = entry.get()
                if num.isnumeric() == True:
                    num = int(num)
                    img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                    f=np.fft.fft2(img)
                    fshift=np.fft.fftshift(f)
                    rows,cols=img.shape
                    crow,ccol=int(rows/2),int(cols/2)
                    mask=np.zeros((rows,cols), np.uint8)
                    D=num
                    mask[crow-D:crow+D, ccol-D:ccol+D]=1
                    f_ishift=fshift*mask
                    f_shift=np.fft.ifftshift(f_ishift)
                    img_back=np.fft.ifft2(f_shift)
                    img_back=np.abs(img_back)
                    plt.subplot(131),plt.imshow(img, cmap= 'gray')
                    plt.title('Original'), plt.xticks([]), plt.yticks([])
                    plt.subplot(132),plt.imshow(mask, cmap= 'gray')
                    plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                    plt.subplot(133),plt.imshow(img_back,cmap= 'gray')
                    plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                    plt.show()
                else:
                    messagebox.showerror(message="Ingresa solo datos numéricos",title="Error")

            ventanapai=tk.Tk()
            ventanapai.title("PASA ALTAS IDEAL POR TF")

            miframepbi=tk.Frame(ventanapai)
            miframepbi.pack()
            miframepbi.config(bg="green",cursor='hand2')
            
            mensaje=tk.Label(miframepbi,text="Ingresa el valor para el radio",font=('Arial 20'),bg='green')
            mensaje.grid(row=0,column=1,padx=10,pady=10)
            
            entry = tk.Entry(miframepbi,font="Arial 18")
            entry.grid(row=1,column=1,padx=5,pady=5)
            entry.config(justify="center")
            
            boton9=tk.Button(miframepbi,text="FILTRAR",font="Arial 20",activebackground="green",command=Filtro2)
            boton9.grid(row=3,column=2,padx=5,pady=5)
            
            boton9=tk.Button(miframepbi,text="REGRESAR",font="Arial 20",activebackground="red",command = regresar2)
            boton9.grid(row=3,column=0,padx=5,pady=5)
            ventanapai.mainloop()
        
        elif menu1.current()==2:
            def regresar3():
                ventanapbani.destroy() 
            def Filtro3():
                num1 = entry1.get()
                num2 = entry2.get()
                if (num1.isnumeric()==True) and (num2.isnumeric()==True):
                    if num1<num2:
                        num1 = int(num1)
                        num2 = int(num2)
                        img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                        f=np.fft.fft2(img)
                        fshift=np.fft.fftshift(f)
                        rows,cols=img.shape
                        crow,ccol=int(rows/2),int(cols/2)
                        mask1=np.ones((rows,cols), np.uint8)
                        D1=num1
                        mask1[crow-D1:crow+D1, ccol-D1:ccol+D1]=0
                        mask2=np.zeros((rows,cols), np.uint8)
                        D2=num2
                        mask2[crow-D2:crow+D2, ccol-D2:ccol+D2]=1
                        mask=mask1*mask2
                        f_ishift=fshift*mask
                        f_shift=np.fft.ifftshift(f_ishift)
                        img_back=np.fft.ifft2(f_shift)
                        img_back=np.abs(img_back)
                        plt.subplot(131),plt.imshow(img, cmap= 'gray')
                        plt.title('Original'), plt.xticks([]), plt.yticks([])
                        plt.subplot(132),plt.imshow(mask, cmap= 'gray')
                        plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                        plt.subplot(133),plt.imshow(img_back,cmap= 'gray')
                        plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                        plt.show()
                    else:
                        messagebox.showerror(message="El primer dato debe ser menor al segundo",title="Error")
                else:
                    messagebox.showerror(message="Ingresa solo datos numéricos",title="Error")
            
            ventanapbani=tk.Tk()
            ventanapbani.title("PASA BANDAS IDEAL POR TF")

            miframepbi=tk.Frame(ventanapbani)
            miframepbi.pack()
            miframepbi.config(bg="green",cursor='hand2')
            
            mensaje1=tk.Label(miframepbi,text="Ingresa el valor menor para el radio",font=('Arial 20'),bg='green')
            mensaje1.grid(row=0,column=1,padx=10,pady=10)
            
            entry1 = tk.Entry(miframepbi,font="Arial 18")
            entry1.grid(row=1,column=1,padx=5,pady=5)
            entry1.config(justify="center")

            mensaje2=tk.Label(miframepbi,text="Ingresa el valor mayor para el radio",font=('Arial 20'),bg='green')
            mensaje2.grid(row=2,column=1,padx=10,pady=10)
            
            entry2 = tk.Entry(miframepbi,font="Arial 18")
            entry2.grid(row=3,column=1,padx=5,pady=5)
            entry2.config(justify="center")
            
            boton9=tk.Button(miframepbi,text="FILTRAR",font="Arial 20",activebackground="green",command=Filtro3)
            boton9.grid(row=4,column=2,padx=5,pady=5)
            
            boton9=tk.Button(miframepbi,text="REGRESAR",font="Arial 20",activebackground="red",command = regresar3)
            boton9.grid(row=4,column=0,padx=5,pady=5)
            ventanapbani.mainloop()
        
        elif menu1.current()==3:
            def regresar4():
                ventanarbani.destroy() 
            def Filtro4():
                num1 = entry1.get()
                num2 = entry2.get()
                if (num1.isnumeric()==True) and (num2.isnumeric()==True):
                    if num1<num2:
                        num1 = int(num1)
                        num2 = int(num2)
                        img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                        f=np.fft.fft2(img)
                        fshift=np.fft.fftshift(f)
                        rows,cols=img.shape
                        crow,ccol=int(rows/2),int(cols/2)
                        mask1=np.ones((rows,cols), np.uint8)
                        D1=num1
                        mask1[crow-D1:crow+D1, ccol-D1:ccol+D1]=0
                        mask2=np.zeros((rows,cols), np.uint8)
                        D2=num2
                        mask2[crow-D2:crow+D2, ccol-D2:ccol+D2]=1
                        mask=mask1*mask2
                        for i in range(crow*2):
                            for j in range(ccol*2):
                                if mask[i,j]==0:
                                    mask[i,j]=1
                                elif mask[i,j]==1:
                                    mask[i,j]=0
                        f_ishift=fshift*mask
                        f_shift=np.fft.ifftshift(f_ishift)
                        img_back=np.fft.ifft2(f_shift)
                        img_back=np.abs(img_back)
                        plt.subplot(131),plt.imshow(img, cmap= 'gray')
                        plt.title('Original'), plt.xticks([]), plt.yticks([])
                        plt.subplot(132),plt.imshow(mask, cmap= 'gray')
                        plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                        plt.subplot(133),plt.imshow(img_back,cmap= 'gray')
                        plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                        plt.show()
                    else:
                        messagebox.showerror(message="El primer dato debe ser menor al segundo",title="Error")
                else:
                    messagebox.showerror(message="Ingresa solo datos numéricos",title="Error")
            
            ventanarbani=tk.Tk()
            ventanarbani.title("PASA BANDAS IDEAL POR TF")

            miframepbi=tk.Frame(ventanarbani)
            miframepbi.pack()
            miframepbi.config(bg="green",cursor='hand2')
            
            mensaje1=tk.Label(miframepbi,text="Ingresa el valor menor para el radio",font=('Arial 20'),bg='green')
            mensaje1.grid(row=0,column=1,padx=10,pady=10)
            
            entry1 = tk.Entry(miframepbi,font="Arial 18")
            entry1.grid(row=1,column=1,padx=5,pady=5)
            entry1.config(justify="center")

            mensaje2=tk.Label(miframepbi,text="Ingresa el valor mayor para el radio",font=('Arial 20'),bg='green')
            mensaje2.grid(row=2,column=1,padx=10,pady=10)
            
            entry2 = tk.Entry(miframepbi,font="Arial 18")
            entry2.grid(row=3,column=1,padx=5,pady=5)
            entry2.config(justify="center")
            
            boton9=tk.Button(miframepbi,text="FILTRAR",font="Arial 20",activebackground="green",command=Filtro4)
            boton9.grid(row=4,column=2,padx=5,pady=5)
            
            boton9=tk.Button(miframepbi,text="REGRESAR",font="Arial 20",activebackground="red",command = regresar4)
            boton9.grid(row=4,column=0,padx=5,pady=5)
            ventanarbani.mainloop()

        else:
            messagebox.showerror(message="No has seleccionado un comando",title="Error")
#-------------------------------------------------------------------------------------------

    #SEGUNDA VENTANA
    menu1 = str(menu.current())
    if menu1 == "-1":
        messagebox.showerror(message="No has seleccionado un comando",title="Error")
    if menu.current()==0:
        ventanaitf=tk.Tk()
        ventanaitf.title("Filtro Ideal por TF")
        miframeitf=tk.Frame(ventanaitf)
        miframeitf.pack()   
        miframeitf.config(bg="blue",cursor='hand2')
        menu1=ttk.Combobox(miframeitf,font="Arial 20",justify=tk.CENTER,width=35,state="readonly")
        menu1.grid(row=1,column=1,padx=15,pady=15)
        opciones2=["Pasa Bajas","Pasa Altas","Pasa Banda","Rechazo de Banda"]
        menu1["values"]=opciones2
        boton4=tk.Button(miframeitf,text="SELECCIONAR",font="Arial 20",activebackground="green",command=ITF)
        boton4.grid(row=2,column=1,padx=5,pady=5)
        boton5=tk.Button(miframeitf,text="REGRESAR",font="Arial 20",activebackground="red",command=back1)
        boton5.grid(row=3,column=1,padx=5,pady=5)
        
        ventanaitf.mainloop()
        
    #TERCERA VENTANA 
    if menu.current()==1:
        ventanatf=tk.Tk()
        ventanatf.title("Filtro No Ideal por TF")
        miframetf=tk.Frame(ventanatf)
        miframetf.pack()   
        miframetf.config(bg="red",cursor='hand2')
        menu2=ttk.Combobox(miframetf,font="Arial 20",justify=tk.CENTER,width=35,state="readonly")
        menu2.grid(row=1,column=1,padx=15,pady=15)
        opciones3=["Butterworth","Gaussiano"]
        menu2["values"]=opciones3
        boton7=tk.Button(miframetf,text="SELECCIONAR",font="Arial 20",activebackground="green")
        boton7.grid(row=2,column=1,padx=5,pady=5)
        boton8=tk.Button(miframetf,text="REGRESAR",font="Arial 20",activebackground="red",command=back2)
        boton8.grid(row=3,column=1,padx=5,pady=5)
        ventanatf.mainloop()

def salir():
    ventana.destroy()
    os._exit(0)
    
def select1():
    global imagen
    imagen=cv2.imread('tomografia.jpg')
    select()
    
def select2():
    global imagen
    imagen=cv2.imread('camaleon.jpeg')
    select()

def select3():
    global imagen
    imagen=cv2.imread('paisaje.jpg')
    select()

#-----------------------------------------------------------------------------------------------
mensaje=tk.Label(miframe,text="Elige una de las 3 imagenes y el comando a utilizar",font=('Arial 20'),bg='white')
mensaje.grid(row=0,column=1,padx=10,pady=10)

img1=Image.open('tomografia.jpg')
img1=img1.resize((220, 220),Image.ANTIALIAS)
img1=ImageTk.PhotoImage(img1)
img2=Image.open('camaleon.jpeg')
img2=img2.resize((220, 220),Image.ANTIALIAS)
img2=ImageTk.PhotoImage(img2)
img3=Image.open('paisaje.jpg')
img3=img3.resize((220, 220),Image.ANTIALIAS)
img3=ImageTk.PhotoImage(img3)

boton1=tk.Button(miframe,image=img1,command=select1)
boton1.grid(row=2,column=0,padx=2,pady=2)
boton2=tk.Button(miframe,image=img2,command=select2)
boton2.grid(row=2,column=1,padx=2,pady=2)
boton3=tk.Button(miframe,image=img3,command=select3)
boton3.grid(row=2,column=2,padx=2,pady=2)

#Menu
menu=ttk.Combobox(miframe,font="Arial 12",justify=tk.CENTER,width=35,state="readonly")
menu.grid(row=1,column=1,padx=15,pady=15)
opciones1=["Filtro Ideal por Transformada de Fourier","Filtro No Ideal por Transformada de Fourier"]
menu["values"]=opciones1

#Boton principal de salida
Salir=tk.Button(miframe,text="SALIR",width=10,activebackground="red",font="Arial 18",command=salir)
Salir.grid(row=5,column=1,padx=10,pady=10)

ventana.mainloop()