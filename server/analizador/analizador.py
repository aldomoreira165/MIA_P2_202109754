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
    salida = ""
    lineas = entry.splitlines()
    for linea in lineas:
        try:
            printConsole("Analizando comando: " + linea.lower())
            if re.search(r"^\s*#.*$", linea) or re.search(r"^\s*$", linea):
                pass
            else:
                split_args = shlex.split(linea.lower())
                command = split_args.pop(0)
                if(command == "mkdisk"):
                    print(" ------ Se detecto mkdisk ------ ")
                    salida += fn_mkdisk(split_args) + "\n"
                    print(" ------ Termino mkdisk ------ ")
                elif(command == "rmdisk"):
                    print(" ------ Se detecto rmdisk ------ ")
                    salida += fn_rmdisk(split_args) + "\n"
                    print(" ------ Termino rmdisk ------ ")
                elif(command == "fdisk"):
                    print(" ------ Se detecto fdisk ------ ")
                    salida += fn_fdisk(split_args) + "\n"
                    print(" ------ Termino fdisk ------ ")
                elif(command == "mount"):
                    print(" ------ Se detecto mount ------ ")
                    salida += fn_mount(split_args) + "\n"
                    print(" ------ Termino mount ------ ")
                elif (command == "mkfs"):
                    print(" ------ Se detecto mkfs ------ ")
                    salida += fn_mkfs(split_args) + "\n"
                    print(" ------ Termino mkfs ------ ")
                elif (command == "login"):
                    print(" ------ Se detecto login ------ ")
                    salida += fn_login(split_args) + "\n"
                    print(" ------ Termino login ------ ")
                elif (command == "logout"):
                    print(" ------ Se detecto logout ------ ")
                    salida +=  fn_logout() + "\n"
                    print(" ------ Termino logout ------ ")
                elif (command == "pause"):
                    print(" ------ Se detecto pause ------ ")
                    salida += "Pause detectado" + "\n"
                    print(" ------ Termino pause ------ ")
                elif (command == "rep"):
                    print(" ------ Se detecto rep ------ ")
                    salida += fn_rep(split_args) + "\n"
                    print(" ------ Termino rep ------ ")
                else:
                    printError("Comando no reconocido")
                    salida += "[Error] Comando no reconocido" + "\n"
        except Exception as e: pass

    return salida

def fn_logout():
    try:
        return execute_logout()

    except Exception as e: return "[Error] Análisis de argumentos \n " + str(e)

def fn_login(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-user", required=True, help="Usuario")
        parser.add_argument("-pass", required=True, help="Contraseña")
        parser.add_argument("-id", required=True, help="Id de la particion montada")
        args = parser.parse_args(split_args)

        return execute_login(args)

    except Exception as e: return "[Error] Análisis de argumentos \n " + str(e)
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

    except Exception as e: return "[Error] Análisis de argumentos \n " + str(e)

def fn_mkdisk(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-size", required=True, type=int, help="Tamaño del disco")
        parser.add_argument("-path", required=True, help="Ruta donde se creará el disco")
        parser.add_argument("-fit", required=False, choices=["bf", "ff", "wf"], default="ff",help="Tipo de ajuste de disco (opcional)")
        parser.add_argument("-unit", required=False, choices=["k", "m"], default="m", help="Unidad de tamaño (opcional)")
        args = parser.parse_args(split_args)

        return execute_mkdisk(args)

    except:
        return "[Error] Análisis de argumentos \n"

def fn_rmdisk(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-path", required=True, help="Ruta donde se encuentra el disco a eliminar")

        args = parser.parse_args(split_args)

        return execute_rmdisk(args)

    except Exception as e: return "[Error] Análisis de argumentos \n " + str(e)

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

    except Exception as e: return "[Error] Análisis de argumentos \n " + str(e)


def fn_mount(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-path", required=True, help="Ruta del disco a montar")
        parser.add_argument("-name", required=True, help="Nombre de la particion a cargar")
        args = parser.parse_args(split_args)

        return execute_mount(args)

    except Exception as e: return "[Error] Análisis de argumentos \n " + str(e)


def fn_mkfs(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-id", required=True, help="Id de la particion a formatear")
        parser.add_argument("-type", required=False, choices=["full"], default="full", help="Tipo de formateo")
        args = parser.parse_args(split_args)

        return execute_mkfs(args)

    except Exception as e: return "[Error] Análisis de argumentos \n " + str(e)

def fn_rep(split_args):
    try:
        parser = argparse.ArgumentParser(description="Parámetros")
        parser.add_argument("-name", required=True, choices=["mbr", "disk", "inode", "journaling", "block", "bm_inode", "bm_block", "tree", "sb", "file", "ls"], help="Nombre del reporte")
        parser.add_argument("-path", required=True, help="Ruta del reporte")
        parser.add_argument("-id", required=True, help="Id de la particion a reportar")
        parser.add_argument("-ruta", required=False, help="Nombre del archivo o carpeta del que se mostrara el reporte")
        args = parser.parse_args(split_args)

        return execute_rep(args)

    except Exception as e: return "[Error] Análisis de argumentos \n " + str(e)
