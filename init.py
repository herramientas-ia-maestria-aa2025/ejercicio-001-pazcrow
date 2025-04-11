with open('informacion.txt','r') as archivo:
    datos = archivo.read()
    datos_separados = datos.strip().split(';')
    print(datos)