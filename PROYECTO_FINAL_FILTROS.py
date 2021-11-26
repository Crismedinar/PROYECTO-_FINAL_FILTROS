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
            def limpiar1():
                entry.delete(0,tk.END)
            def Filtro1():
                num = entry.get()
                if num.isnumeric() == True:
                    try:
                        num = int(num)
                        img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                        f=np.fft.fft2(img)
                        fshift=np.fft.fftshift(f)
                        dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                        dft_shift = np.fft.fftshift(dft)
                        tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
                        rows,cols=img.shape
                        crow,ccol=int(rows/2),int(cols/2)
                        mask=np.ones((rows,cols), np.uint8)
                        D=num
                        mask[crow-D:crow+D, ccol-D:ccol+D]=0
                        f_ishift=fshift*mask
                        f_shift=np.fft.ifftshift(f_ishift)
                        img_back=np.fft.ifft2(f_shift)
                        img_back=np.abs(img_back)
                        plt.subplot(221),plt.imshow(img, cmap= 'gray')
                        plt.title('Original'), plt.xticks([]), plt.yticks([])
                        plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                        plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                        plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                        plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                        plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                        plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                        plt.show()
                    except:
                        messagebox.showerror(message="Verifica los datos",title="Error")
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
            
            botonpbi=tk.Button(miframepbi,text="BORRAR",font="Arial 20",activebackground="green",command=limpiar1)
            botonpbi.grid(row=3,column=1,padx=5,pady=5)

            boton9=tk.Button(miframepbi,text="REGRESAR",font="Arial 20",activebackground="red",command = regresar1)
            boton9.grid(row=3,column=0,padx=5,pady=5)
            ventanapbi.mainloop()
        
        elif menu1.current()==1:
            def regresar2():
                ventanapai.destroy()
            def limpiar2():
                entry.delete(0,tk.END)
            def Filtro2():
                num = entry.get()
                if num.isnumeric() == True:
                    try:
                        num = int(num)
                        img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                        f=np.fft.fft2(img)
                        fshift=np.fft.fftshift(f)
                        dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                        dft_shift = np.fft.fftshift(dft)
                        tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
                        rows,cols=img.shape
                        crow,ccol=int(rows/2),int(cols/2)
                        mask=np.zeros((rows,cols), np.uint8)
                        D=num
                        mask[crow-D:crow+D, ccol-D:ccol+D]=1
                        f_ishift=fshift*mask
                        f_shift=np.fft.ifftshift(f_ishift)
                        img_back=np.fft.ifft2(f_shift)
                        img_back=np.abs(img_back)
                        plt.subplot(221),plt.imshow(img, cmap= 'gray')
                        plt.title('Original'), plt.xticks([]), plt.yticks([])
                        plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                        plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                        plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                        plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                        plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                        plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                        plt.show()
                    except:
                        messagebox.showerror(message="Verifica los datos",title="Error")
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
            
            botonpbi=tk.Button(miframepbi,text="BORRAR",font="Arial 20",activebackground="green",command=limpiar2)
            botonpbi.grid(row=3,column=1,padx=5,pady=5)

            boton9=tk.Button(miframepbi,text="REGRESAR",font="Arial 20",activebackground="red",command = regresar2)
            boton9.grid(row=3,column=0,padx=5,pady=5)
            ventanapai.mainloop()
        
        elif menu1.current()==2:
            def regresar3():
                ventanapbani.destroy()
            def limpiar3():
                entry1.delete(0,tk.END)
                entry2.delete(0,tk.END)
            def Filtro3():
                num1 = entry1.get()
                num2 = entry2.get()
                if (num1.isnumeric()==True) and (num2.isnumeric()==True):
                    num1=int(num1)
                    num2=int(num2)
                    if num1<num2:
                        try:
                            img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                            f=np.fft.fft2(img)
                            fshift=np.fft.fftshift(f)
                            dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                            dft_shift = np.fft.fftshift(dft)
                            tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
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
                            plt.subplot(221),plt.imshow(img, cmap= 'gray')
                            plt.title('Original'), plt.xticks([]), plt.yticks([])
                            plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                            plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                            plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                            plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                            plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                            plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                            plt.show()
                        except:
                            messagebox.showerror(message="Verifica los datos",title="Error")
                    else:
                        messagebox.showerror(message="El radio PB tiene que ser mayor que el radio PA",title="Error")
                else:
                    messagebox.showerror(message="Ingresa solo datos numéricos",title="Error")
            
            ventanapbani=tk.Tk()
            ventanapbani.title("PASA BANDAS IDEAL POR TF")

            miframepbi=tk.Frame(ventanapbani)
            miframepbi.pack()
            miframepbi.config(bg="green",cursor='hand2')
            
            mensaje1=tk.Label(miframepbi,text="Ingresa el valor del radio PA",font=('Arial 20'),bg='green')
            mensaje1.grid(row=0,column=1,padx=10,pady=10)
            
            entry1 = tk.Entry(miframepbi,font="Arial 18")
            entry1.grid(row=1,column=1,padx=5,pady=5)
            entry1.config(justify="center")

            mensaje2=tk.Label(miframepbi,text="Ingresa el valor del radio PB",font=('Arial 20'),bg='green')
            mensaje2.grid(row=2,column=1,padx=10,pady=10)
            
            entry2 = tk.Entry(miframepbi,font="Arial 18")
            entry2.grid(row=3,column=1,padx=5,pady=5)
            entry2.config(justify="center")
            
            boton9=tk.Button(miframepbi,text="FILTRAR",font="Arial 20",activebackground="green",command=Filtro3)
            boton9.grid(row=4,column=2,padx=5,pady=5)

            botonpbi=tk.Button(miframepbi,text="BORRAR",font="Arial 20",activebackground="green",command=limpiar3)
            botonpbi.grid(row=4,column=1,padx=5,pady=5)
            
            boton9=tk.Button(miframepbi,text="REGRESAR",font="Arial 20",activebackground="red",command = regresar3)
            boton9.grid(row=4,column=0,padx=5,pady=5)
            ventanapbani.mainloop()
        
        elif menu1.current()==3:
            def regresar4():
                ventanarbani.destroy()
            def limpiar4():
                entry1.delete(0,tk.END)
                entry2.delete(0,tk.END)
            def Filtro4():
                num1 = entry1.get()
                num2 = entry2.get()
                if (num1.isnumeric()==True) and (num2.isnumeric()==True):
                    num1=int(num1)
                    num2=int(num2)
                    if num1<num2:
                        try:
                            img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                            f=np.fft.fft2(img)
                            fshift=np.fft.fftshift(f)
                            dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                            dft_shift = np.fft.fftshift(dft)
                            tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
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
                            plt.subplot(221),plt.imshow(img, cmap= 'gray')
                            plt.title('Original'), plt.xticks([]), plt.yticks([])
                            plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                            plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                            plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                            plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                            plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                            plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                            plt.show()
                        except:
                            messagebox.showerror(message="Verifica los datos",title="Error")
                    else:
                        messagebox.showerror(message="El radio PA tiene que ser mayor que el radio PB",title="Error")
                else:
                    messagebox.showerror(message="Ingresa solo datos numéricos",title="Error")
            
            ventanarbani=tk.Tk()
            ventanarbani.title("RECHAZO DE BANDA IDEAL POR TF")

            miframepbi=tk.Frame(ventanarbani)
            miframepbi.pack()
            miframepbi.config(bg="green",cursor='hand2')
            
            mensaje1=tk.Label(miframepbi,text="Ingresa el valor del radio PB",font=('Arial 20'),bg='green')
            mensaje1.grid(row=0,column=1,padx=10,pady=10)
            
            entry1 = tk.Entry(miframepbi,font="Arial 18")
            entry1.grid(row=1,column=1,padx=5,pady=5)
            entry1.config(justify="center")

            mensaje2=tk.Label(miframepbi,text="Ingresa el valor del radio PA",font=('Arial 20'),bg='green')
            mensaje2.grid(row=2,column=1,padx=10,pady=10)
            
            entry2 = tk.Entry(miframepbi,font="Arial 18")
            entry2.grid(row=3,column=1,padx=5,pady=5)
            entry2.config(justify="center")
            
            boton9=tk.Button(miframepbi,text="FILTRAR",font="Arial 20",activebackground="green",command=Filtro4)
            boton9.grid(row=4,column=2,padx=5,pady=5)
            
            botonpbi=tk.Button(miframepbi,text="BORRAR",font="Arial 20",activebackground="green",command=limpiar4)
            botonpbi.grid(row=4,column=1,padx=5,pady=5)

            boton9=tk.Button(miframepbi,text="REGRESAR",font="Arial 20",activebackground="red",command = regresar4)
            boton9.grid(row=4,column=0,padx=5,pady=5)
            ventanarbani.mainloop()

        else:
            messagebox.showerror(message="No has seleccionado un comando",title="Error")
    
    def TF():
        def backButter():
            ventanaButter.destroy()
        def FiltroButter():
            if menuButter.current()==0:
                def limpiar5():
                    entryButter0.delete(0,tk.END)
                    entry2Butter0.delete(0,tk.END)  
                def backButter0():
                    ventanaButter0.destroy()
                def Butter0():
                    radio0=entryButter0.get()
                    orden0=entry2Butter0.get()
                    if radio0.isnumeric() == True and orden0.isnumeric()==True:
                        try:
                            radio0=int(radio0)
                            orden0=int(orden0)
                            img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                            f=np.fft.fft2(img) 
                            fshift=np.fft.fftshift(f)
                            dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                            dft_shift = np.fft.fftshift(dft)
                            tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
                            rows,cols=img.shape
                            crow,ccol=int(rows/2),int(cols/2)
                            D0=radio0
                            N=orden0
                            mask=np.zeros((rows,cols))
                            for i in range (rows):
                                for j in range (cols):
                                    dist=(i-crow)**2+(j-ccol)**2
                                    mask[i,j]=np.sqrt((1+(dist/D0)**(2*N)))**(-1)
                            f_ishift=fshift*mask
                            f_shift=np.fft.ifftshift(f_ishift)
                            img_back=np.fft.ifft2(f_shift)
                            img_back=np.abs(img_back)
                            plt.subplot(221),plt.imshow(img, cmap= 'gray')
                            plt.title('Original'), plt.xticks([]), plt.yticks([])
                            plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                            plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                            plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                            plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                            plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                            plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                            plt.show()
                        except:
                            messagebox.showerror(message="Verifica los datos",title="Error")
                    else:
                        messagebox.showerror(message="Los datos ingresados no son númericos",title="Error")
                ventanaButter0=tk.Tk()
                ventanaButter0.title("Pasa Bajas Butterworth")
                miframeButter0=tk.Frame(ventanaButter0)
                miframeButter0.pack()
                miframeButter0.config(bg="green",cursor='hand2')
                
                mensajeButter0=tk.Label(miframeButter0,text="Ingresa el valor del radio",font=('Arial 20'),bg='green')
                mensajeButter0.grid(row=0,column=1,padx=10,pady=10)
                
                entryButter0 = tk.Entry(miframeButter0,font="Arial 18")
                entryButter0.grid(row=1,column=1,padx=5,pady=5)
                entryButter0.config(justify="center")
                
                mensajeButter0=tk.Label(miframeButter0,text="Ingresa el orden del filtro",font=('Arial 20'),bg='green')
                mensajeButter0.grid(row=2,column=1,padx=10,pady=10)
                
                entry2Butter0 = tk.Entry(miframeButter0,font="Arial 18")
                entry2Butter0.grid(row=3,column=1,padx=5,pady=5)
                entry2Butter0.config(justify="center")
                
                botonButter0=tk.Button(miframeButter0,text="FILTRAR",font="Arial 20",activebackground="green",command=Butter0)
                botonButter0.grid(row=4,column=2,padx=5,pady=5)
                
                boton3Butter0=tk.Button(miframeButter0,text="BORRAR",font="Arial 20",activebackground="green",command =limpiar5)
                boton3Butter0.grid(row=4,column=1,padx=5,pady=5)
                
                boton2Butter0=tk.Button(miframeButter0,text="REGRESAR",font="Arial 20",activebackground="red",command = backButter0)
                boton2Butter0.grid(row=4,column=0,padx=5,pady=5)
                ventanaButter0.mainloop()
                
            elif menuButter.current()==1:
                def limpiar5():
                    entryButter1.delete(0,tk.END)
                    entry2Butter1.delete(0,tk.END)  
                def backButter1():
                    ventanaButter1.destroy()
                def Butter1():
                    radio1=entryButter1.get()
                    orden1=entry2Butter1.get()
                    if radio1.isnumeric() == True and orden1.isnumeric()==True:
                        try:
                            radio1=int(radio1)
                            orden1=int(orden1)
                            img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                            f=np.fft.fft2(img) 
                            fshift=np.fft.fftshift(f)
                            dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                            dft_shift = np.fft.fftshift(dft)
                            tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
                            rows,cols=img.shape
                            crow,ccol=int(rows/2),int(cols/2)
                            D0=radio1
                            N=orden1
                            mask=np.ones((rows,cols))
                            for i in range (rows):
                                for j in range (cols):
                                    dist=(i-crow)**2+(j-ccol)**2
                                    if dist==0:
                                        continue
                                    mask[i,j]=np.sqrt((1+(D0/dist)**(2*N)))**(-1)
                            f_ishift=fshift*mask
                            f_shift=np.fft.ifftshift(f_ishift)
                            img_back=np.fft.ifft2(f_shift)
                            img_back=np.abs(img_back)
                            plt.subplot(221),plt.imshow(img, cmap= 'gray')
                            plt.title('Original'), plt.xticks([]), plt.yticks([])
                            plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                            plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                            plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                            plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                            plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                            plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                            plt.show()
                        except:
                            messagebox.showerror(message="Verifica los datos",title="Error")
                    else:
                        messagebox.showerror(message="Los datos ingresados no son númericos",title="Error")
                ventanaButter1=tk.Tk()
                ventanaButter1.title("Pasa Altas Butterworth")
                miframeButter1=tk.Frame(ventanaButter1)
                miframeButter1.pack()
                miframeButter1.config(bg="purple1",cursor='hand2')
                mensajeButter0=tk.Label(miframeButter1,text="Ingresa el valor del radio",font=('Arial 20'),bg='purple1')
                mensajeButter0.grid(row=0,column=1,padx=10,pady=10)
                
                entryButter1 = tk.Entry(miframeButter1,font="Arial 18")
                entryButter1.grid(row=1,column=1,padx=5,pady=5)
                entryButter1.config(justify="center")
                
                mensajeButter1=tk.Label(miframeButter1,text="Ingresa el orden del filtro",font=('Arial 20'),bg='purple1')
                mensajeButter1.grid(row=2,column=1,padx=10,pady=10)
                
                entry2Butter1 = tk.Entry(miframeButter1,font="Arial 18")
                entry2Butter1.grid(row=3,column=1,padx=5,pady=5)
                entry2Butter1.config(justify="center")
                
                botonButter1=tk.Button(miframeButter1,text="FILTRAR",font="Arial 20",activebackground="green",command=Butter1)
                botonButter1.grid(row=4,column=2,padx=5,pady=5)
                
                boton3Butter1=tk.Button(miframeButter1,text="BORRAR",font="Arial 20",activebackground="green",command =limpiar5)
                boton3Butter1.grid(row=4,column=1,padx=5,pady=5)
                
                boton2Butter1=tk.Button(miframeButter1,text="REGRESAR",font="Arial 20",activebackground="red",command = backButter1)
                boton2Butter1.grid(row=4,column=0,padx=5,pady=5)
                ventanaButter1.mainloop()
            if menuButter.current()==2:
                def backButter2():
                    ventanaButter2.destroy()
                def limpiar():
                    entryButter2.delete(0,tk.END)
                    entry2Butter2.delete(0,tk.END)
                    entry3Butter2.delete(0,tk.END)
                    entry4Butter2.delete(0,tk.END)
                def Butter2():
                    radio2=entryButter2.get()
                    orden2=entry2Butter2.get()
                    radio3=entry3Butter2.get()
                    orden3=entry4Butter2.get()
                    if radio2.isnumeric()==True and orden2.isnumeric()==True and radio3.isnumeric()==True and orden3.isnumeric()==True:
                        radio2 = int(radio2)
                        orden2 = int(orden2)
                        radio3 = int(radio3)
                        orden3 = int(orden3)
                        if radio2>radio3:
                            try:
                                img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                                f=np.fft.fft2(img)
                                fshift=np.fft.fftshift(f)
                                dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                                dft_shift = np.fft.fftshift(dft)
                                tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
                                rows,cols=img.shape
                                crow,ccol=int(rows/2),int(cols/2)
                                D0=radio2
                                N=orden2
                                mask1=np.zeros((rows,cols))
                                for i in range (rows):
                                    for j in range (cols):
                                        dist=(i-crow)**2+(j-ccol)**2
                                        mask1[i,j]=np.sqrt((1+(dist/D0)**(2*N)))**(-1)
                                D0=radio3
                                N=orden3
                                mask2=np.ones((rows,cols))
                                for i in range (rows):
                                    for j in range (cols):
                                        dist=(i-crow)**2+(j-ccol)**2
                                        if dist==0:
                                            continue
                                        mask2[i,j]=np.sqrt((1+(D0/dist)**(2*N)))**(-1)
                                mask=mask1*mask2
                                f_ishift=fshift*mask
                                f_shift=np.fft.ifftshift(f_ishift)
                                img_back=np.fft.ifft2(f_shift)
                                img_back=np.abs(img_back)
                                plt.subplot(221),plt.imshow(img, cmap= 'gray')
                                plt.title('Original'), plt.xticks([]), plt.yticks([])
                                plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                                plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                                plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                                plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                                plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                                plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                                plt.show()
                            except:
                                messagebox.showerror(message="Verifica los datos",title="Error")
                        else:
                            messagebox.showerror(message="El radio PB tiene que ser mayor que el radio PA",title="Error")
                    else:
                        messagebox.showerror(message="Los datos ingresados no son númericos",title="Error")
                ventanaButter2=tk.Tk()
                ventanaButter2.title("Pasa Bandas Butterworth")
                miframeButter2=tk.Frame(ventanaButter2)
                miframeButter2.pack()
                miframeButter2.config(bg="salmon2",cursor='hand2')
                #----------------------------PB------------------------------------------------------------------
                mensajeButter0=tk.Label(miframeButter2,text="Ingresa el valor del radio PB",font=('Arial 15'),bg='salmon2')
                mensajeButter0.grid(row=0,column=0,padx=10,pady=10)
                
                entryButter2 = tk.Entry(miframeButter2,font="Arial 18")
                entryButter2.grid(row=1,column=0,padx=5,pady=5)
                entryButter2.config(justify="center")
                
                mensajeButter2=tk.Label(miframeButter2,text="Ingresa el orden del filtro PB",font=('Arial 15'),bg='salmon2')
                mensajeButter2.grid(row=2,column=0,padx=10,pady=10)
                
                entry2Butter2 = tk.Entry(miframeButter2,font="Arial 18")
                entry2Butter2.grid(row=3,column=0,padx=5,pady=5)
                entry2Butter2.config(justify="center")
                #-----------------------------PA--------------------------------------------------------------
                mensajeButter0=tk.Label(miframeButter2,text="Ingresa el valor del radio PA",font=('Arial 15'),bg='salmon2')
                mensajeButter0.grid(row=0,column=2,padx=10,pady=10)
                
                entry3Butter2 = tk.Entry(miframeButter2,font="Arial 18")
                entry3Butter2.grid(row=1,column=2,padx=5,pady=5)
                entry3Butter2.config(justify="center")
                
                mensajeButter2=tk.Label(miframeButter2,text="Ingresa el orden del filtro PA",font=('Arial 15'),bg='salmon2')
                mensajeButter2.grid(row=2,column=2,padx=10,pady=10)
                
                entry4Butter2 = tk.Entry(miframeButter2,font="Arial 18")
                entry4Butter2.grid(row=3,column=2,padx=5,pady=5)
                entry4Butter2.config(justify="center")
                
                
                botonButter2=tk.Button(miframeButter2,text="FILTRAR",font="Arial 20",activebackground="green",command=Butter2)
                botonButter2.grid(row=4,column=2,padx=5,pady=5)
                
                boton3Butter2=tk.Button(miframeButter2,text="BORRAR",font="Arial 20",activebackground="green",command=limpiar)
                boton3Butter2.grid(row=4,column=1,padx=5,pady=5)
                
                boton2Butter2=tk.Button(miframeButter2,text="REGRESAR",font="Arial 20",activebackground="red",command = backButter2)
                boton2Butter2.grid(row=4,column=0,padx=5,pady=5)
                ventanaButter2.mainloop()
            if menuButter.current()==3:
                def backButter3():
                    ventanaButter3.destroy()
                def limpiar3():
                    entryButter3.delete(0,tk.END)
                    entry2Butter3.delete(0,tk.END)
                    entry3Butter3.delete(0,tk.END)
                    entry4Butter3.delete(0,tk.END)
                def Butter3():
                    radio2=entryButter3.get()
                    orden2=entry2Butter3.get()
                    radio3=entry3Butter3.get()
                    orden3=entry4Butter3.get()
                    if radio2.isnumeric()==True and orden2.isnumeric()==True and radio3.isnumeric()==True and orden3.isnumeric()==True:
                        radio2 = int(radio2)
                        orden2 = int(orden2)
                        radio3 = int(radio3)
                        orden3 = int(orden3)
                        if radio2>radio3:
                            try:
                                img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                                f=np.fft.fft2(img)
                                fshift=np.fft.fftshift(f)
                                dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                                dft_shift = np.fft.fftshift(dft)
                                tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
                                rows,cols=img.shape
                                crow,ccol=int(rows/2),int(cols/2)
                                D0=radio2
                                N=orden2
                                mask1=np.zeros((rows,cols))
                                for i in range (rows):
                                    for j in range (cols):
                                        dist=(i-crow)**2+(j-ccol)**2
                                        mask1[i,j]=np.sqrt((1+(dist/D0)**(2*N)))**(-1)
                                D0=radio3
                                N=orden3
                                mask2=np.ones((rows,cols))
                                for i in range (rows):
                                    for j in range (cols):
                                        dist=(i-crow)**2+(j-ccol)**2
                                        if dist==0:
                                            continue
                                        mask2[i,j]=np.sqrt((1+(D0/dist)**(2*N)))**(-1)
                                mask=-mask1*mask2
                                f_ishift=fshift*mask
                                f_shift=np.fft.ifftshift(f_ishift)
                                img_back=np.fft.ifft2(f_shift)
                                img_back=np.abs(img_back)
                                plt.subplot(221),plt.imshow(img, cmap= 'gray')
                                plt.title('Original'), plt.xticks([]), plt.yticks([])
                                plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                                plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                                plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                                plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                                plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                                plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                                plt.show()
                            except:
                                messagebox.showerror(message="Verifica los datos",title="Error")
                        else:
                            messagebox.showerror(message="El radio PA tiene que ser mayor que el radio PB",title="Error")
                    else:
                        messagebox.showerror(message="Los datos ingresados no son númericos",title="Error")
                ventanaButter3=tk.Tk()
                ventanaButter3.title("Rechaza Banda Butterworth")
                miframeButter3=tk.Frame(ventanaButter3)
                miframeButter3.pack()
                miframeButter3.config(bg="bisque",cursor='hand2')
                #----------------------------PB------------------------------------------------------------------
                mensajeButter0=tk.Label(miframeButter3,text="Ingresa el valor del radio PA",font=('Arial 15'),bg='bisque')
                mensajeButter0.grid(row=0,column=0,padx=10,pady=10)
                
                entryButter3 = tk.Entry(miframeButter3,font="Arial 18")
                entryButter3.grid(row=1,column=0,padx=5,pady=5)
                entryButter3.config(justify="center")
                
                mensajeButter0=tk.Label(miframeButter3,text="Ingresa el orden del filtro PA",font=('Arial 15'),bg='bisque')
                mensajeButter0.grid(row=2,column=0,padx=10,pady=10)
                
                entry2Butter3 = tk.Entry(miframeButter3,font="Arial 18")
                entry2Butter3.grid(row=3,column=0,padx=5,pady=5)
                entry2Butter3.config(justify="center")
                #-----------------------------PA--------------------------------------------------------------
                mensajeButter0=tk.Label(miframeButter3,text="Ingresa el valor del radio PB",font=('Arial 15'),bg='bisque')
                mensajeButter0.grid(row=0,column=2,padx=10,pady=10)
                
                entry3Butter3 = tk.Entry(miframeButter3,font="Arial 18")
                entry3Butter3.grid(row=1,column=2,padx=5,pady=5)
                entry3Butter3.config(justify="center")
                
                mensajeButter2=tk.Label(miframeButter3,text="Ingresa el orden del filtro PB",font=('Arial 15'),bg='bisque')
                mensajeButter2.grid(row=2,column=2,padx=10,pady=10)
                
                entry4Butter3 = tk.Entry(miframeButter3,font="Arial 18")
                entry4Butter3.grid(row=3,column=2,padx=5,pady=5)
                entry4Butter3.config(justify="center")
                
                
                botonButter3=tk.Button(miframeButter3,text="FILTRAR",font="Arial 20",activebackground="green",command=Butter3)
                botonButter3.grid(row=4,column=2,padx=5,pady=5)
                
                boton3Butter3=tk.Button(miframeButter3,text="BORRAR",font="Arial 20",activebackground="green",command=limpiar3)
                boton3Butter3.grid(row=4,column=1,padx=5,pady=5)
                
                boton2Butter3=tk.Button(miframeButter3,text="REGRESAR",font="Arial 20",activebackground="red",command = backButter3)
                boton2Butter3.grid(row=4,column=0,padx=5,pady=5)
                ventanaButter3.mainloop()
            else:
                messagebox.showerror(message="No has seleccionado un comando",title="Error")
        def backGauss():
            ventanaGauss.destroy()
        def FiltroGauss():
            if menuGauss.current()==0:
                def backGauss0():
                    ventanaGauss0.destroy()
                def limpiar4():
                    entryGauss0.delete(0,tk.END)
                def Gauss0():
                    radio0=entryGauss0.get()
                    if radio0.isnumeric() == True:
                        try:
                            radio0=int(radio0)
                            img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                            f=np.fft.fft2(img) 
                            fshift=np.fft.fftshift(f)
                            dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                            dft_shift = np.fft.fftshift(dft)
                            tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
                            rows,cols=img.shape
                            crow,ccol=int(rows/2),int(cols/2)
                            D0=radio0
                            mask=np.zeros((rows,cols))
                            for i in range (rows):
                                for j in range (cols):
                                    dist=(i-crow)**2+(j-ccol)**2
                                    mask[i,j]=np.exp(-(((dist)**(2))/((2)*((D0)**(2)))))
                            f_ishift=fshift*mask
                            f_shift=np.fft.ifftshift(f_ishift)
                            img_back=np.fft.ifft2(f_shift)
                            img_back=np.abs(img_back)
                            plt.subplot(221),plt.imshow(img, cmap= 'gray')
                            plt.title('Original'), plt.xticks([]), plt.yticks([])
                            plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                            plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                            plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                            plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                            plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                            plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                            plt.show()
                        except:
                            messagebox.showerror(message="Verifica los datos",title="Error")
                    else:
                        messagebox.showerror(message="Los datos ingresados no son númericos",title="Error")
                ventanaGauss0=tk.Tk()
                ventanaGauss0.title("Pasa Bajas Gaussiano")
                miframeGauss0=tk.Frame(ventanaGauss0)
                miframeGauss0.pack()
                miframeGauss0.config(bg="green",cursor='hand2')
                
                mensajeGauss0=tk.Label(miframeGauss0,text="Ingresa el valor del radio",font=('Arial 20'),bg='green')
                mensajeGauss0.grid(row=0,column=1,padx=10,pady=10)
                
                entryGauss0 = tk.Entry(miframeGauss0,font="Arial 18")
                entryGauss0.grid(row=1,column=1,padx=5,pady=5)
                entryGauss0.config(justify="center")
                
                botonGauss0=tk.Button(miframeGauss0,text="FILTRAR",font="Arial 20",activebackground="green",command=Gauss0)
                botonGauss0.grid(row=4,column=2,padx=5,pady=5)
                
                boton1Gauss0=tk.Button(miframeGauss0,text="BORRAR",font="Arial 20",activebackground="green",command=limpiar4)
                boton1Gauss0.grid(row=4,column=1,padx=5,pady=5)
                
                boton2Gauss0=tk.Button(miframeGauss0,text="REGRESAR",font="Arial 20",activebackground="red",command = backGauss0)
                boton2Gauss0.grid(row=4,column=0,padx=5,pady=5)
                ventanaGauss0.mainloop()
                
            elif menuGauss.current()==1:
                def limpiar():
                    entryGauss1.delete(0,tk.END)
                def backGauss1():
                    ventanaGauss1.destroy()
                def Gauss1():
                    radio1=entryGauss1.get()
                    if radio1.isnumeric() == True:
                        try:
                            radio1=int(radio1)
                            img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                            f=np.fft.fft2(img) 
                            fshift=np.fft.fftshift(f)
                            dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                            dft_shift = np.fft.fftshift(dft)
                            tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
                            rows,cols=img.shape
                            crow,ccol=int(rows/2),int(cols/2)
                            D0=radio1
                            mask=np.ones((rows,cols))
                            for i in range (rows):
                                for j in range (cols):
                                    dist=(i-crow)**2+(j-ccol)**2
                                    if dist==0:
                                        continue
                                    mask[i,j]=1-(np.exp(-(((dist)**(2))/((2)*((D0)**(2))))))
                            f_ishift=fshift*mask
                            f_shift=np.fft.ifftshift(f_ishift)
                            img_back=np.fft.ifft2(f_shift)
                            img_back=np.abs(img_back)
                            plt.subplot(221),plt.imshow(img, cmap= 'gray')
                            plt.title('Original'), plt.xticks([]), plt.yticks([])
                            plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                            plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                            plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                            plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                            plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                            plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                            plt.show()
                        except:
                            messagebox.showerror(message="Verifica los datos",title="Error")
                    else:
                        messagebox.showerror(message="Los datos ingresados no son númericos",title="Error")
                ventanaGauss1=tk.Tk()
                ventanaGauss1.title("Pasa Altas Gaussiano")
                miframeGauss1=tk.Frame(ventanaGauss1)
                miframeGauss1.pack()
                miframeGauss1.config(bg="purple1",cursor='hand2')
                mensajeGauss0=tk.Label(miframeGauss1,text="Ingresa el valor del radio",font=('Arial 20'),bg='purple1')
                mensajeGauss0.grid(row=0,column=1,padx=10,pady=10)
                
                entryGauss1 = tk.Entry(miframeGauss1,font="Arial 18")
                entryGauss1.grid(row=1,column=1,padx=5,pady=5)
                entryGauss1.config(justify="center")
                
                botonGauss1=tk.Button(miframeGauss1,text="FILTRAR",font="Arial 20",activebackground="green",command=Gauss1)
                botonGauss1.grid(row=4,column=2,padx=5,pady=5)
                
                botonGauss2=tk.Button(miframeGauss1,text="BORRAR",font="Arial 20",activebackground="green",command=limpiar)
                botonGauss2.grid(row=4,column=1,padx=5,pady=5)
                
                boton2Gauss1=tk.Button(miframeGauss1,text="REGRESAR",font="Arial 20",activebackground="red",command = backGauss1)
                boton2Gauss1.grid(row=4,column=0,padx=5,pady=5)
                ventanaGauss1.mainloop()
            if menuGauss.current()==2:
                def backGauss2():
                    ventanaGauss2.destroy()
                def limpiar():
                    entryGauss2.delete(0,tk.END)
                    entry3Gauss2.delete(0,tk.END)
                def Gauss2():
                    radio2=entryGauss2.get()
                    radio3=entry3Gauss2.get()
                    if radio2.isnumeric()==True and radio3.isnumeric()==True:
                        radio2 = int(radio2)
                        radio3 = int(radio3)
                        if radio2>radio3:
                            try:
                                img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                                f=np.fft.fft2(img)
                                fshift=np.fft.fftshift(f)
                                dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                                dft_shift = np.fft.fftshift(dft)
                                tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
                                rows,cols=img.shape
                                crow,ccol=int(rows/2),int(cols/2)
                                D0=radio2
                                mask1=np.ones((rows,cols))
                                for i in range (rows):
                                    for j in range (cols):
                                        dist=(i-crow)**2+(j-ccol)**2
                                        mask1[i,j]=(np.exp(-(((dist)**(2))/((2)*((D0)**(2))))))
                                D0=radio3
                                mask2=np.ones((rows,cols))
                                for i in range (rows):
                                    for j in range (cols):
                                        dist=(i-crow)**2+(j-ccol)**2
                                        if dist==0:
                                            continue
                                        mask2[i,j]=1-(np.exp(-(((dist)**(2))/((2)*((D0)**(2))))))
                                mask=mask1*mask2
                                f_ishift=fshift*mask
                                f_shift=np.fft.ifftshift(f_ishift)
                                img_back=np.fft.ifft2(f_shift)
                                img_back=np.abs(img_back)
                                plt.subplot(221),plt.imshow(img, cmap= 'gray')
                                plt.title('Original'), plt.xticks([]), plt.yticks([])
                                plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                                plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                                plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                                plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                                plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                                plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                                plt.show()
                            except:
                                messagebox.showerror(message="Verifica los datos",title="Error")
                        else:
                            messagebox.showerror(message="El radio PB tiene que ser mayor que el radio PA",title="Error")
                    else:
                        messagebox.showerror(message="Los datos ingresados no son númericos",title="Error")
                ventanaGauss2=tk.Tk()
                ventanaGauss2.title("Pasa Bandas Gaussiano")
                miframeGauss2=tk.Frame(ventanaGauss2)
                miframeGauss2.pack()
                miframeGauss2.config(bg="salmon2",cursor='hand2')
                #----------------------------PB------------------------------------------------------------------
                mensajeGauss0=tk.Label(miframeGauss2,text="Ingresa el valor del radio PB",font=('Arial 15'),bg='salmon2')
                mensajeGauss0.grid(row=0,column=0,padx=10,pady=10)
                
                entryGauss2 = tk.Entry(miframeGauss2,font="Arial 18")
                entryGauss2.grid(row=1,column=0,padx=5,pady=5)
                entryGauss2.config(justify="center")
                
                #-----------------------------PA--------------------------------------------------------------
                mensajeGauss0=tk.Label(miframeGauss2,text="Ingresa el valor del radio PA",font=('Arial 15'),bg='salmon2')
                mensajeGauss0.grid(row=0,column=2,padx=10,pady=10)
                
                entry3Gauss2 = tk.Entry(miframeGauss2,font="Arial 18")
                entry3Gauss2.grid(row=1,column=2,padx=5,pady=5)
                entry3Gauss2.config(justify="center")                
                
                botonGauss2=tk.Button(miframeGauss2,text="FILTRAR",font="Arial 20",activebackground="green",command=Gauss2)
                botonGauss2.grid(row=4,column=2,padx=5,pady=5)
                
                boton3Gauss2=tk.Button(miframeGauss2,text="BORRAR",font="Arial 20",activebackground="green",command=limpiar)
                boton3Gauss2.grid(row=4,column=1,padx=5,pady=5)
                
                boton2Gauss2=tk.Button(miframeGauss2,text="REGRESAR",font="Arial 20",activebackground="red",command = backGauss2)
                boton2Gauss2.grid(row=4,column=0,padx=5,pady=5)
                ventanaGauss2.mainloop()
            if menuGauss.current()==3:
                def backGauss3():
                    ventanaGauss3.destroy()
                def limpiar3():
                    entryGauss3.delete(0,tk.END)
                    entry3Gauss3.delete(0,tk.END)
                def Gauss3():
                    radio2=entryGauss3.get()
                    radio3=entry3Gauss3.get()
                    if radio2.isnumeric()==True and radio3.isnumeric()==True:
                        radio2 = int(radio2)
                        radio3 = int(radio3)
                        if radio2>radio3:
                            try:
                                img = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                                f=np.fft.fft2(img)
                                fshift=np.fft.fftshift(f)
                                dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
                                dft_shift = np.fft.fftshift(dft)
                                tff= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
                                rows,cols=img.shape
                                crow,ccol=int(rows/2),int(cols/2)
                                D0=radio2
                                mask1=np.ones((rows,cols))
                                for i in range (rows):
                                    for j in range (cols):
                                        dist=(i-crow)**2+(j-ccol)**2
                                        mask1[i,j]=(np.exp(-(((dist)**(2))/((2)*((D0)**(2))))))
                                D0=radio3
                                mask2=np.ones((rows,cols))
                                for i in range (rows):
                                    for j in range (cols):
                                        dist=(i-crow)**2+(j-ccol)**2
                                        if dist==0:
                                            continue
                                        mask2[i,j]=1-(np.exp(-(((dist)**(2))/((2)*((D0)**(2))))))
                                mask=-mask1*mask2
                                f_ishift=fshift*mask
                                f_shift=np.fft.ifftshift(f_ishift)
                                img_back=np.fft.ifft2(f_shift)
                                img_back=np.abs(img_back)
                                plt.subplot(221),plt.imshow(img, cmap= 'gray')
                                plt.title('Original'), plt.xticks([]), plt.yticks([])
                                plt.subplot(222),plt.imshow(tff, cmap= 'gray')
                                plt.title('Transformada'), plt.xticks([]), plt.yticks([])
                                plt.subplot(223),plt.imshow(mask, cmap= 'gray')
                                plt.title('Mascarilla'), plt.xticks([]), plt.yticks([])
                                plt.subplot(224),plt.imshow(img_back,cmap= 'gray')
                                plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])
                                plt.show()
                            except:
                                messagebox.showerror(message="Verifica los datos",title="Error")
                        else:
                            messagebox.showerror(message="El radio PA tiene que ser mayor que el radio PB",title="Error")
                    else:
                        messagebox.showerror(message="Los datos ingresados no son númericos",title="Error")
                ventanaGauss3=tk.Tk()
                ventanaGauss3.title("Rechaza Banda Gaussiano")
                miframeGauss3=tk.Frame(ventanaGauss3)
                miframeGauss3.pack()
                miframeGauss3.config(bg="bisque",cursor='hand2')
                #----------------------------PB------------------------------------------------------------------
                mensajeGauss0=tk.Label(miframeGauss3,text="Ingresa el valor del radio PA",font=('Arial 15'),bg='bisque')
                mensajeGauss0.grid(row=0,column=0,padx=10,pady=10)
                
                entryGauss3 = tk.Entry(miframeGauss3,font="Arial 18")
                entryGauss3.grid(row=1,column=0,padx=5,pady=5)
                entryGauss3.config(justify="center")
                
                #-----------------------------PA--------------------------------------------------------------
                mensajeGauss0=tk.Label(miframeGauss3,text="Ingresa el valor del radio PB",font=('Arial 15'),bg='bisque')
                mensajeGauss0.grid(row=0,column=2,padx=10,pady=10)
                
                entry3Gauss3 = tk.Entry(miframeGauss3,font="Arial 18")
                entry3Gauss3.grid(row=1,column=2,padx=5,pady=5)
                entry3Gauss3.config(justify="center")
                
                botonGauss3=tk.Button(miframeGauss3,text="FILTRAR",font="Arial 20",activebackground="green",command=Gauss3)
                botonGauss3.grid(row=4,column=2,padx=5,pady=5)
                
                boton3Gauss3=tk.Button(miframeGauss3,text="BORRAR",font="Arial 20",activebackground="green",command=limpiar3)
                boton3Gauss3.grid(row=4,column=1,padx=5,pady=5)
                
                boton2Gauss3=tk.Button(miframeGauss3,text="REGRESAR",font="Arial 20",activebackground="red",command = backGauss3)
                boton2Gauss3.grid(row=4,column=0,padx=5,pady=5)
                ventanaGauss3.mainloop()
            else:
                messagebox.showerror(message="No has seleccionado un comando",title="Error")
        
        #-----------------------------BUTTERWORTH-------------------------------------------------------------
        if menu2.current()==0:
            ventanaButter=tk.Tk()
            ventanaButter.title("Filtros Butterworth")
            miframeButter=tk.Frame(ventanaButter)
            miframeButter.pack()   
            miframeButter.config(bg="green3",cursor='hand2')
            menuButter=ttk.Combobox(miframeButter,font="Arial 20",justify=tk.CENTER,width=35,state="readonly")
            menuButter.grid(row=1,column=1,padx=15,pady=15)
            opcionesButter=["Pasa Bajas","Pasa Altas","Pasa Banda","Rechazo de Banda"]
            menuButter["values"]=opcionesButter
            botonButter=tk.Button(miframeButter,text="SELECCIONAR",font="Arial 20",activebackground="green",command=FiltroButter)
            botonButter.grid(row=2,column=1,padx=5,pady=5)
            botonButter1=tk.Button(miframeButter,text="REGRESAR",font="Arial 20",activebackground="red",command=backButter)
            botonButter1.grid(row=3,column=1,padx=5,pady=5)
            ventanaButter.mainloop()
        #-----------------------------GAUSSIANO-------------------------------------------------------------
        elif menu2.current()==1:
            ventanaGauss=tk.Tk()
            ventanaGauss.title("Filtros Gaussianos")
            miframeGauss=tk.Frame(ventanaGauss)
            miframeGauss.pack()   
            miframeGauss.config(bg="green3",cursor='hand2')
            menuGauss=ttk.Combobox(miframeGauss,font="Arial 20",justify=tk.CENTER,width=35,state="readonly")
            menuGauss.grid(row=1,column=1,padx=15,pady=15)
            opcionesGauss=["Pasa Bajas","Pasa Altas","Pasa Banda","Rechazo de Banda"]
            menuGauss["values"]=opcionesGauss
            botonGauss=tk.Button(miframeGauss,text="SELECCIONAR",font="Arial 20",activebackground="green",command=FiltroGauss)
            botonGauss.grid(row=2,column=1,padx=5,pady=5)
            botonGauss1=tk.Button(miframeGauss,text="REGRESAR",font="Arial 20",activebackground="red",command=backGauss)
            botonGauss1.grid(row=3,column=1,padx=5,pady=5)
            ventanaGauss.mainloop()
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
        boton7=tk.Button(miframetf,text="SELECCIONAR",font="Arial 20",activebackground="green",command=TF)
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