import sys
from ErrorListener import MiErrorListener 
from antlr4 import *
from compiladorLexer import compiladorLexer
from compiladorParser import compiladorParser
from Escucha import Escucha


#antlr4 -Dlanguage=Python3 -visitor compilador.g4 -o .





def main(argv):
    archivo = "/home/franco/Escritorio/Facultad/DHS/Antlr/Compilador/input/prueba_con_errores.txt"
    if len(argv) > 1:
        archivo = argv[1]
    
    input = FileStream(archivo, encoding='utf-8')
    lexer = compiladorLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladorParser(stream)
    
    error_listener = MiErrorListener()
    parser.removeErrorListeners()  # Eliminar los listeners por defecto
    parser.addErrorListener(error_listener)
    
    
    
    
    escucha = Escucha()
    parser.addParseListener(escucha)
    tree = parser.programa()
    

    # Siempre mostrar el reporte de errores sintácticos
    print(error_listener.obtener_reporte())

if __name__ == '__main__':
    main(sys.argv)