import pickle

class Vehiculo:
      def __init__(self):
          color = 'negro'
          ano = 2015

      def encender(self):
          return True
      def apagar(self):
          return False

vehi = Vehiculo()

f = open('datos.bin','wb')
pickle.dump(vehi,f)
f.close()

f = open('datos.bin','f')
nuevoVehi = pickle.load(f)
f.close()
nuevoVehi.encender()