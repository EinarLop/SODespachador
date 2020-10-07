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




procesos=[80,1000,100,1500, 450]


inp = {"tcc":10, "tb":10,"tvc":10 ,"quantum":100 }


def tvcM(proceso):
      value = (math.ceil(proceso / inp["quantum"]) -1 ) * inp["tvc"]
      return value


x=0
y=0
for p in procesos:
      te= p
      tcc=y
      tvc= tvcM(p)
      tb= inp["tb"]
      tt= te+tcc+ tvc+ tb
      ti = x
      tf = tt + ti
      print ("tcc:", tcc, "te:" , te   , "tvc:" , tvc , "tb:", tb, "tt:", tt, "ti:", ti, "tf:" ,tf)
      x = tf    
      y=10



 
