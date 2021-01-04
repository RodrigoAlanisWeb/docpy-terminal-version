import sys
import getopt
import functions
from colorama import Fore

def docpy():
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv,"ho:ro:lo:wo:a:co:do:vo",['help','read','line:','write','a','create','create-dir','version'])
    except getopt.GetoptError as err:
        print(Fore.RED,err)

    for opt, arg in opts:
        if opt in ['-h','--help']:
            functions._help()
            sys.exit()
        elif opt in ['-r','--read']:
            if '-l' in argv or '--line' in argv:
                return functions.read(argv[1],False,int(argv[3]))

            return functions.read(argv[1])
        elif opt in ['-w','--write']:
            if '-l' in argv or '--line' in argv:
                return functions.write(argv[1],argv[2],int(argv[4]))
            return functions.write(argv[1],argv[2])
        elif opt in ['-a']:
            return functions.d_write(argv[1],argv[2])
        elif opt in ['-c','--create']:
            return functions.create_file(argv[1],argv[2])
        elif opt in ['-d','-create-dir']:
            return functions.create_dir(argv[1],argv[2])
        elif opt in ['-v','--version']:
            print('Docpy Terminal-version v1')

if __name__ == '__main__':
    docpy()