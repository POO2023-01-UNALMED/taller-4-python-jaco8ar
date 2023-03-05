class Asignatura:

    def __init__(self, nombre, salon = None):
        self._nombre = nombre
        self._salon = salon
    

    def __str__(self):
        if self._salon == None:
            alPrint = f"{self._nombre} remoto"
        else:
            alPrint = self._nombre +" "+ self._salon
        return alPrint
