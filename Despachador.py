import math 
from Micro import *
from Process import *

# Primer proceso:
# TE= 100ms

# Datos:
# Núm. MP = 1
# Quantum: 50ms
# TCC: 10ms
# TB: 10ms
# TVC: 10ms


# TE= P1.TE
# TCC = Boolean
# TVC = ParseInt((TE/QUANTUM -1)) * TVC
# TB = TB 
# TT= TE+TCC+TVC+TB
# TI= Boolean
# TF = TT + TI



tcc = 10
tb=10
quantum=100
mp= 2

      


microProcessors=[]
microProcessors.append(Micro(1, tb, quantum, tcc))
microProcessors.append(Micro(2, tb, quantum, tcc))

##calcula a que micro entrar
def chooseMicro(mps, proceso):
      finalTimes = []
      for m in mps:
            val = m.finalTime
            finalTimes.append(val)
            print(finalTimes)
      print("Final Times :", finalTimes)
      minMicroTime = min(finalTimes)
      print(minMicroTime)
      indexMinMicroTime = finalTimes.index(minMicroTime)
      print(indexMinMicroTime)
      if minMicroTime >= proceso.startTime:
            
            mps[indexMinMicroTime].fillTable(proceso)
      else:
            
            for m in mps:
                  if m.finalTime < proceso.startTime:
                        m.fillTable(proceso)
                        break






processes = []
processes.append(Process("A", 80, 1,0))
processes.append(Process("B", 300, 2, 0))
processes.append(Process("C", 1000, 3, 0))
processes.append(Process("D", 150, 0, 0))
processes.append(Process("E", 2000, 3, 0))
processes.append(Process("F", 100, 1, 0))
processes.append(Process("G", 1500, 4, 0))
processes.append(Process("H", 5000, 8, 0))
processes.append(Process("I", 450, 1, 0))
processes.append(Process("J", 800, 2, 0))
processes.append(Process("K", 300, 1, 0))
processes.append(Process("L", 700, 0, 0))
processes.append(Process("M", 900, 3, 0))
processes.append(Process("N", 810, 2, 0))


for p in processes:
      chooseMicro(microProcessors, p)

