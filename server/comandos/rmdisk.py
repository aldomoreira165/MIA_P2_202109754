from elementos.superbloque import *
from elementos.inodo import *
from elementos.fileblock import *
from elementos.disco import *
        
def execute_rmdisk(args):   
        return eliminarDisco(args.path)