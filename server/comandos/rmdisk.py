from elementos.superbloque import *
from elementos.inodo import *
from elementos.fileblock import *
from elementos.disco import *
        
def execute_rmdisk(args):   
    confirmacion = (input("Esta seguro que desea eliminar el disco? (S/N): ")).lower()
    if confirmacion == "s":
        return eliminarDisco(args.path)
    else:
        print("Eliminacion de disco cancelada") 
        return "Eliminacion de disco cancelada"