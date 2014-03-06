from math import*

def stunde(stunde, min, sec):
  result = stunde + min/60 + sec/3600
  return(result)
  
def rest(a, b):
  while a >= b:
    a -= b
  return(a)  
  
def hmin(stunden,i):
  y = 1
  if(stunden < 0):
    y = -1
    stunden = - stunden
  result = [0,0,0]
  result[0] = y*(stunden - rest(stunden,1))
  result[2] = rest(60*(stunden - result[0]), 1)*60*y
  result[1] = (rest(stunden, 1)*60-result[2]/60)*y
  return(result[i])
  
def azimut(unitime):
  sternzeit_gr = stunde(10, 46, 43.4579)
  pos_B = stunde(0, 43, 33.5)
  tt = unitime + stunde(0, 0, 67.2)
  alpha_0 = stunde(22,58,32.34)/12*3.14159265
  alpha_1 = stunde(23, 02, 15.84) /12*3.14159265
  delta_0 = -1*stunde(6, 33, 7.6)/180*3.14159265
  delta_1 = -1*stunde(6, 10, 0.6) /180*3.14159265
  alpha = alpha_0 + (alpha_1 - alpha_0)*(tt/24.0)
  delta = delta_0 + (delta_1 - delta_0)*(tt/24.0)
  Phi = stunde(49, 53, 9)/180*3.14159265 
 
  theta_Bam = sternzeit_gr + pos_B + unitime*1.002738
  
  tau_sol = theta_Bam/12*3.14159265 - alpha

  M = atan(tan(delta)/cos(tau_sol))

  az = atan((cos(M)*tan(tau_sol))/(sin(Phi-M)))

  print("alpha = ", hmin(alpha,0), hmin(alpha,1), hmin(alpha,2) )
  print("delta = ", hmin(delta*180/3.141592,0), hmin((delta *180/3.141592),1), hmin(delta *180/3.141592 ,2) )
  print("theta_Bam = ", hmin(theta_Bam,0), hmin(theta_Bam,1), hmin(theta_Bam,2))
  print("Tau_Sonne = ", hmin(tau_sol*12/3.141592,0), hmin(tau_sol*12/3.141592,1), hmin(tau_sol*12/3.141592,2) )
  print("M = ", hmin(M*180/3.141592,0), hmin(M*180/3.141592,1), hmin(M*180/3.141592,2) )
  print("a_Sonne = ", hmin(az*180/3.141592, 0), hmin(az*180/3.141592, 1), hmin(az*180/3.141592, 2))
  

