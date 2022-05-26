

class ficheros:

    def __init__(self,nombreFichero,tipo):
        self.nombreFichero = nombreFichero+'.'+tipo
        self.file = ''


    def crearFicheros(self):
        self.file = open(self.nombreFichero,'a')
        self.file.close()

    def leerFicheros(self):
        self.file = open(self.nombreFichero,'r')
        leer = self.file.read()
        print(leer)
        self.file.close()

    def escribir(self):
        self.file = open(self.nombreFichero,'a')
        texto = 'creando nuevo texto\n'
        self.file.writelines(texto)
        self.file.close



archivos = ficheros('prueba','txt')
archivos.crearFicheros()
archivos.escribir()
archivos.leerFicheros()


