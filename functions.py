import sys
import getopt
from colorama import Fore
import os

def read(route,r_all=True,li=False):
    if verify_file(route):
        f = open(route,'r')
        if r_all:
            print(f.read())
        else:
            li -= 1
            print(f.readlines()[li])
        f.close()
    else:
        print(Fore.RED,'El archivo no existe')

def write(route,text,w_in=False):
    if verify_file(route):
        if w_in:
            content = open(route).read().splitlines()
            if w_in > len(content):
                print('La linea no existe')
                exit()
            w_in -= 1
            content[w_in] += text
            f = open(route,'w')
            f.writelines('\n'.join(content))
            print('Hecho')
            f.close()
        else:
            f = open(route,'a')

            f.write('\n' + text)
            print('Hecho')
            f.close()
    else:
        print(Fore.RED,'El archivo no existe')
    exit()

def d_write(route,text):
    if verify_file(route):
        f = open(route,'w')
        f.write(text)
        print('Hecho')
        f.close()
    else:
        print(Fore.RED,'El archivo no existe')
    exit()

def create_file(route,name):
    if verify_dir(route):
        f = open(route + name,'w')
        f.write('Gracias Por Usar Mi Script :)')
        print('ruta: ' + route + name)
        f.close()
    else:
        print(Fore.RED,'El directorio no existe')
    exit()

def create_dir(route,name):
    if verify_dir(route):
        os.mkdir(route + name)
        print('Hecho')
    else:
        print(Fore.RED,'El directorio no existe')
    exit()

def _help():
    args = [
        '-r: para activar la lectura',
        '-w: para activar la escritura',
        '-a: para activar el borrado-lectura',
        '-c: para activar la creacion de archivos',
        '-d: para activar la creacion de directorios'
    ]

    for i in args:
        print(i)

def verify_file(route):
    try :
        with open(route) as f:
            return True
    except FileNotFoundError as e:
        return False

def verify_dir(route):
    if os.path.isdir(route):
        return True
    else:
        return False
