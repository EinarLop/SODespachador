import math
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




procesos=[80,1000,200,500]





tcc = 10
tb=10

quantum=100
mp= 2
mps=[]
 
 ##arreglo de microprocesadores
for i in range(mp):
      mps.append([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
      
##calcula el tiempo por vencimiento de cuantum
def tvcM(proceso):
      value = (math.ceil(proceso / quantum) -1 ) * tcc
      return value

##calcula a que micro entrar
def chooseMicro(mps):
      minVal = []
      for m in mps:
            val =m[len(m)-1][6] 
            minVal.append(val)
      
      #return( minVal.index(min(minVal)))
      return( [minVal.index(min(minVal)), min(minVal)])


##se usa como tiempo inicial
#x=0 
##se usa como tiempo por cambio de contexto
#y=0

for p in procesos:
      te= p
      z=chooseMicro(mps)
      if z[1] != 0:
            tcc=10
      else:
            tcc=0
      tvc= tvcM(p)
      tb= tb
      tt= te+tcc+ tvc+ tb
      ti = z[1] 
      tf = tt + ti
      mps[z[0]].append([te, tcc,tvc,tb,tt,ti,tf])
      #print ("Procesos del micro :",mps)
      #x = tf    
      #y=10
for m in mps:
      
      print ("Procesos del micro :",m)



 
