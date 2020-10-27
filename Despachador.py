import math 
from Micro import *
from Process import *
from tkinter import *

    
ventana=Tk()
ventana.title("GEO OS")
ventana.configure(bg="#ECF8FD")
w= Scrollbar(ventana)


##calcula a que micro entrar
def chooseMicro(mps, proceso):
      finalTimes = []
      for m in mps:
            val = m.finalTime
            finalTimes.append(val)
      minMicroTime = min(finalTimes)
      indexMinMicroTime = finalTimes.index(minMicroTime)
      if minMicroTime >= proceso.startTime:
            mps[indexMinMicroTime].fillTable(proceso)
      else:
            for m in mps:
                  if m.finalTime < proceso.startTime:
                        mps[mps.index(m)].fillTable(proceso)
                        #m.fillTable(proceso)
                        break
      


#imprime la tabla con interfaz gráfica
def printTable(processList, mp):
      #imprime titulos
      tccBox.destroy()
      tccBoxText.destroy()
      tbBox.destroy()
      tbBoxText.destroy()
      quantumBox.destroy()
      quantumBoxText.destroy()
      mpBox.destroy()
      mpBoxText.destroy()
      buttonCommit.destroy()

      microID=Text(ventana, height=1, width=10, bg="#85AFD5", fg="#0B2332",font="verdana")
      name=Text(ventana, height=1, width=10, bg="#85AFD5", fg="#0B2332",font="verdana")
      time=Text(ventana, height=1, width=10, bg="#85AFD5", fg="#0B2332",font="verdana")
      tcc=Text(ventana, height=1, width=10, bg="#85AFD5", fg="#0B2332",font="verdana")
      tvc=Text(ventana, height=1, width=10, bg="#85AFD5", fg="#0B2332",font="verdana")
      tb=Text(ventana, height=1, width=10, bg="#85AFD5", fg="#0B2332",font="verdana")
      tt=Text(ventana, height=1, width=10, bg="#85AFD5", fg="#0B2332",font="verdana")
      ti=Text(ventana, height=1, width=10, bg="#85AFD5", fg="#0B2332",font="verdana")
      tf=Text(ventana, height=1, width=10, bg="#85AFD5", fg="#0B2332",font="verdana")

      microID.insert(END, 'MICROID')
      name.insert(END, 'Process')
      time.insert(END, 'TIME')
      tcc.insert(END, 'TCC')
      tvc.insert(END, 'TVC')
      tb.insert(END, 'TB')
      tt.insert(END, 'TT')
      ti.insert(END, 'TI')
      tf.insert(END, 'TF')
      

      microID.configure(state=DISABLED)
      name.configure(state=DISABLED)
      time.configure(state=DISABLED)
      tcc.configure(state=DISABLED)
      tvc.configure(state=DISABLED)
      tb.configure(state=DISABLED)
      tt.configure(state=DISABLED)
      ti.configure(state=DISABLED)
      tf.configure(state=DISABLED)

      microID.grid(column=0 ,row=0,  padx=5 , pady=5)
      name.grid(column=1 ,row=0,  padx=5 , pady=5)
      time.grid(column=2 ,row=0,  padx=5 , pady=5)
      tcc.grid(column=3 ,row=0,  padx=5 , pady=5)
      tvc.grid(column=4 ,row=0,  padx=5 , pady=5)
      tb.grid(column=5 ,row=0,  padx=5 , pady=5)
      tt.grid(column=6 ,row=0,  padx=5 , pady=5)
      ti.grid(column=7 ,row=0,  padx=5 , pady=5)
      tf.grid(column=8 ,row=0,  padx=5 , pady=5)
      
      row=1
      for i in range(mp):
            #imprime los valores de los micros
            
            microTitle = Text(ventana, height=1, width=20, font="verdana")
            microText = "Microprocesador #"+ str(i+1)
            microTitle.insert(END, microText) 
            microTitle.configure(state=DISABLED)
            microTitle.grid(column=0 ,row=row,  padx=5 , pady=5)
            row += 1
            for p1 in processList:
                  if p1[0] == i+1:
                        for p2 in range(len(p1)):
                              value=Text(ventana, height=1, width=10, bg="#BDDBEF", fg="#0B2332", font="#0B2332") 
                              value.insert(END, p1[p2]) 
                              value.configure(state=DISABLED)
                              value.grid(column=p2 ,row=row,  padx=5 , pady=5)
                        row += 1
      w.grid(column=9, rowspan=row)
      
      
#Obtiene, hace los calculos y manda a imprimir
def retrieve_input():
      microProcessors=[]
      tcc=int(tccBox.get("1.0","end-1c"))
      tb=int(tbBox.get("1.0","end-1c"))
      quantum=int(quantumBox.get("1.0","end-1c"))
      mp=int(mpBox.get("1.0","end-1c"))
      for a in range(mp):
            microProcessors.append(Micro((a+1), tb, quantum, tcc))
      processes = []

      # processes.append(Process("A", 80, 1,0))
      # processes.append(Process("B", 300, 2, 0))
      # processes.append(Process("C", 1000, 3, 0))
      # processes.append(Process("D", 150, 0, 0))
      # processes.append(Process("E", 2000, 3, 0))
      # processes.append(Process("F", 100, 1, 0))
      # processes.append(Process("G", 1500, 4, 0))
      # processes.append(Process("H", 5000, 8, 0))
      # processes.append(Process("I", 450, 1, 0))
      # processes.append(Process("J", 800, 2, 0))
      # processes.append(Process("K", 300, 1, 0))
      # processes.append(Process("L", 700, 0, 0))
      # processes.append(Process("M", 900, 3, 0))
      # processes.append(Process("N", 810, 2, 0))

      processes.append(Process("B", 300, 2, 0))
      processes.append(Process("D", 100, 2, 0))
      processes.append(Process("F", 500, 3, 0))
      processes.append(Process("H", 700, 4, 0))

      processes.append(Process("J", 300, 2, 1500))
      processes.append(Process("L", 3000, 5, 1500))
      processes.append(Process("N", 50, 2, 1500))
      processes.append(Process("O", 600, 3, 1500))

      processes.append(Process("A", 400, 2, 3000))
      processes.append(Process("C", 50, 2, 3000))
      processes.append(Process("E", 1000, 5, 3000))
      processes.append(Process("G", 10, 2, 3000))
      processes.append(Process("I", 450, 3, 3000))

      processes.append(Process("K", 100, 2, 4000))
      processes.append(Process("M", 80, 2, 4000))
      processes.append(Process("P", 800, 4, 4000))
      processes.append(Process("Ñ", 500, 3, 8000))



      for p in processes:
            chooseMicro(microProcessors, p)

      printing = microProcessors[0].processList
      printTable(printing, mp)
      
      
#interfaz inicial 
tccBox=Text(ventana, height=2, width=10)
tccBoxText=Text(ventana, height=2, width=10)
tbBox=Text(ventana, height=2, width=10)
tbBoxText=Text(ventana, height=2, width=10)
quantumBox=Text(ventana, height=2, width=10)
quantumBoxText=Text(ventana, height=2, width=10)
mpBox=Text(ventana, height=2, width=10)
mpBoxText=Text(ventana, height=2, width=10)
buttonCommit=Button(ventana, height=1, width=10, text="Despachar", 
                    command=lambda: retrieve_input())

tccBoxText.insert(END, 'TCC')
tbBoxText.insert(END, 'TB')
quantumBoxText.insert(END, 'QUANTUM')
mpBoxText.insert(END, 'MICROS')

tccBoxText.configure(state=DISABLED)
tbBoxText.configure(state=DISABLED)
quantumBoxText.configure(state=DISABLED)
mpBoxText.configure(state=DISABLED)

tccBox.grid(column=1 ,row=0,  padx=5 , pady=5)
tccBoxText.grid(column=0,row=0,padx=5,pady=5)
tbBox.grid(column=1, row=1,  padx=5,pady=5)
tbBoxText.grid(column=0,row=1,  padx=5,pady=5)
quantumBox.grid(column=1,row=2, padx=5,pady=5)
quantumBoxText.grid(column=0,row=2,padx=5,pady=5)
mpBox.grid(column=1, row=3, padx=5,pady=5)
mpBoxText.grid(column=0,row=3, padx=5,pady=5)
buttonCommit.grid(row=4)


mainloop()


