import re
import os
import argparse
import shlex
from funciones.utilities import printConsole,printError
from comandos.fdisk import *
from comandos.mkdisk import *
from comandos.mkfs import *
from comandos.login import *
from comandos.mount import *
from comandos.rmdisk import *
from comandos.rep import execute_rep
   
def AnalyzeType(entry): 
    try:
        printConsole("Analizando comando: " + entry.lower())
        if re.search(r"^\s*#.*$", entry) or re.search(r"^\s*$", entry):
            return ""
        else:
            split_args = shlex.split(entry.lower())
            command = split_args.pop(0)
            if (command == "execute"):
                print(" ------ Se detecto execute ------ ")
                return fn_execute(split_args)
                print(" ------ Termino execute ------ ")
            elif(command == "mkdisk"):
                print(" ------ Se detecto mkdisk ------ ")
                return fn_mkdisk(split_args)
                print(" ------ Termino mkdisk ------ ")
            elif(command == "rmdisk"):
                print(" ------ Se detecto rmdisk ------ ")
                return fn_rmdisk(split_args)
                print(" ------ Termino rmdisk ------ ")
            elif(command == "fdisk"):
                print(" ------ Se detecto fdisk ------ ")
                return fn_fdisk(split_args)
                print(" ------ Termino fdisk ------ ")
            elif(command == "mount"):
                print(" ------ Se detecto mount ------ ")
                return fn_mount(split_args)
                print(" ------ Termino mount ------ ")
            elif (command == "mkfs"):
                print(" ------ Se detecto mkfs ------ ")
                return fn_mkfs(split_args)
                print(" ------ Termino mkfs ------ ")
            elif (command == "login"):
                print(" ------ Se detecto login ------ ")
                return fn_login(split_args)
                print(" ------ Termino login ------ ")
            elif (command == "logout"):
                print(" ------ Se detecto logout ------ ")
                return fn_logout()
                print(" ------ Termino logout ------ ")
            elif (command == "pause"):
                print(" ------ Se detecto pause ------ ")
                input("Presione enter para continuar...")
                print(" ------ Termino pause ------ ")
            elif (command == "rep"):
                print(" ------ Se detecto rep ------ ")
                return fn_rep(split_args)
                print(" ------ Termino rep ------ ")
            else:
                printError("Comando no reconocido")
                return "[Error] Comando no reconocido"
    except Exception as e: pass

def fn_logout():
    try:
        execute_logout()

    except SystemExit: printError("Análisis de argumentos")
    except Exception as e: printError(str(e))

def fn_login(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-user", required=True, help="Usuario")
        parser.add_argument("-pass", required=True, help="Contraseña")
        parser.add_argument("-id", required=True, help="Id de la particion montada")
        args = parser.parse_args(split_args)

        return execute_login(args)

    except SystemExit: printError("Análisis de argumentos")
    except Exception as e: printError(str(e))

def fn_execute(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-path", required=True, help="Ruta del archivo a ejecutar")
        args = parser.parse_args(split_args)

        salida = ""

        if os.path.exists(args.path):
            with open(args.path, 'r') as file:
                for line in file:
                    line = line.lower()
                    salida += AnalyzeType(line) + "\n"
                salida += "Execute finalizado."
                return salida
        else:
            print(f"El archivo {args.path} no existe.")
            return f"El archivo {args.path} no existe."

    except SystemExit: printError("Análisis de argumentos")
    except Exception as e: printError(str(e))

def fn_mkdisk(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-size", required=True, type=int, help="Tamaño del disco")
        parser.add_argument("-path", required=True, help="Ruta donde se creará el disco")
        parser.add_argument("-fit", required=False, choices=["bf", "ff", "wf"], default="ff",help="Tipo de ajuste de disco (opcional)")
        parser.add_argument("-unit", required=False, choices=["k", "m"], default="m", help="Unidad de tamaño (opcional)")
        args = parser.parse_args(split_args)

        return execute_mkdisk(args)

    except SystemExit: printError("Análisis de argumentos")
    except Exception as e: printError(str(e))

def fn_rmdisk(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-path", required=True, help="Ruta donde se encuentra el disco a eliminar")

        args = parser.parse_args(split_args)

        return execute_rmdisk(args)

    except SystemExit: printError("Análisis de argumentos")
    except Exception as e: printError(str(e))

def fn_fdisk(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-size", required=True, type=int, help="Tamaño de la particion")
        parser.add_argument("-path", required=True, help="Ruta del disco en donde se creara la particion")
        parser.add_argument("-name", required=True, help="Nombre de la particion")
        parser.add_argument("-unit", required=False, choices=["b","k", "m"], default="k", help="Unidad de tamaño (opcional)")
        parser.add_argument("-type", required=False, choices=["p", "e", "l"], default="p", help="Tipo de particion (opcional)")
        parser.add_argument("-fit", required=False, choices=["bf", "ff", "wf"], default="wf",help="Tipo de ajuste de disco (opcional)")
        args = parser.parse_args(split_args)

        return execute_fdisk(args)

    except SystemExit: printError("Análisis de argumentos")
    except Exception as e: printError(str(e))


def fn_mount(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-path", required=True, help="Ruta del disco a montar")
        parser.add_argument("-name", required=True, help="Nombre de la particion a cargar")
        args = parser.parse_args(split_args)

        return execute_mount(args)

    except SystemExit: printError("Análisis de argumentos")
    except Exception as e: printError(str(e))


def fn_mkfs(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-id", required=True, help="Id de la particion a formatear")
        parser.add_argument("-type", required=False, choices=["full"], default="full", help="Tipo de formateo")
        parser.add_argument("-fs", required=False, choices=["2fs", "3fs"], default="2fs", help="Tipo de sistema de archivos")
        args = parser.parse_args(split_args)

        execute_mkfs(args)

    except SystemExit: printError("Análisis de argumentos")
    except Exception as e: printError(str(e))

def fn_rep(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-name", required=True, choices=["mbr", "disk", "inode", "journaling", "block", "bm_inode", "bm_block", "tree", "sb", "file", "ls"], help="Nombre del reporte")
        parser.add_argument("-path", required=True, help="Ruta del reporte")
        parser.add_argument("-id", required=True, help="Id de la particion a reportar")
        parser.add_argument("-ruta", required=False, help="Nombre del archivo o carpeta del que se mostrara el reporte")
        args = parser.parse_args(split_args)

        return execute_rep(args)

    except SystemExit: printError("Análisis de argumentos")
    except Exception as e: printError(str(e))
