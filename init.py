with open('informacion.txt','r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(';')
        if(datos[1][0] == 'B'):
            print(f"*Nombres*: {datos[0]} *Apellidos*: {datos[1]} *Direccion*: {datos[2]} *Correo*: {datos[3]} ")
