vlan = int(input("Ingrese numero de vlan: "))
if 1 <= vlan <= 1005:
    print("Vlan normal")
elif 1006 <= vlan <= 4094:
    print("Vlan extendida")
else:
    print("Numero de la vlan fuera del rango valido")