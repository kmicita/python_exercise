var=0
val_carr=0
cont=0
gan=0
carr_mayor=0
km_r=int(input("ingrese km a recorrer: ")) 
while km_r>0:
  carr=int(input("ingrese km recorrio en la carreras: "))
  km_r-=carr
  val_carr=int(input("ingrese valor carrera: "))
  gan+=val_carr
  if carr_mayor==0:
    carr_mayor=carr
  if km_r>=0: 
    print("km por recorrer",km_r)
    cont+=1
    if carr> carr_mayor:
      carr_mayor=carr
  else:
    km_r+=carr
    s=input("distancia excedida, ingrese km recorrio en la carreras : " )
    if int(s)>km_r:
      continue
    km_r-=int(s)
    print("km restantes es",km_r)
    cont+=1
    if int(s)> carr_mayor:
      carr_mayor=int(s)
promedio=gan/cont
print("valor del promedio acomulado es: ",promedio,"\ningreso total:$",gan)
print("el careeras realizadas ",cont)
print(".I.")

# Juan test