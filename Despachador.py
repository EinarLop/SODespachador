import math
from Process import *
from Micro import *
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
mps=[]
      


microProcessors=[]
microProcessors.append(Micro(1, tb, quantum, tcc))
microProcessors.append(Micro(2, tb, quantum, tcc))

##calcula a que micro entrar
def chooseMicro(mps, proceso):
      finalTimes = []
      for m in mps:
            val = m.finalTime
            finalTimes.append([val, mps.index(m)])
      
      minMicroTime = min(finalTimes[0])
      print(minMicroTime)
      indexMinMicroTime = finalTimes[0].index(minMicroTime)
      print(indexMinMicroTime)
      if minMicroTime >= proceso.startTime:
            print("primera cond")
            mps[indexMinMicroTime].fillTable(proceso)
      else:
            print("segunda cond" )
            for m in mps:
                  if m.finalTime < proceso.startTime:
                        m.fillTable(proceso)
                        break






processes = []
processes.append(Process("A", 100, 1, 0))
processes.append(Process("B", 500, 1, 120))


for p in processes:
      chooseMicro(microProcessors, p)

