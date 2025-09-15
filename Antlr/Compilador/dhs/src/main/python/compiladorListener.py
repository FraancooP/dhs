# Generated from /home/franco/Escritorio/Facultad/DHS/Antlr/Compilador/dhs/src/main/python/compilador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete listener for a parse tree produced by compiladorParser.
class compiladorListener(ParseTreeListener):

    # Enter a parse tree produced by compiladorParser#programa.
    def enterPrograma(self, ctx:compiladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladorParser#programa.
    def exitPrograma(self, ctx:compiladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladorParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladorParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladorParser#tipo.
    def enterTipo(self, ctx:compiladorParser.TipoContext):
        pass

    # Exit a parse tree produced by compiladorParser#tipo.
    def exitTipo(self, ctx:compiladorParser.TipoContext):
        pass


    # Enter a parse tree produced by compiladorParser#opal.
    def enterOpal(self, ctx:compiladorParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladorParser#opal.
    def exitOpal(self, ctx:compiladorParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladorParser#codigo.
    def enterCodigo(self, ctx:compiladorParser.CodigoContext):
        pass

    # Exit a parse tree produced by compiladorParser#codigo.
    def exitCodigo(self, ctx:compiladorParser.CodigoContext):
        pass


    # Enter a parse tree produced by compiladorParser#bloque.
    def enterBloque(self, ctx:compiladorParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladorParser#bloque.
    def exitBloque(self, ctx:compiladorParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladorParser#instruccion.
    def enterInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladorParser#instruccion.
    def exitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladorParser#iwhile.
    def enterIwhile(self, ctx:compiladorParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladorParser#iwhile.
    def exitIwhile(self, ctx:compiladorParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladorParser#iif.
    def enterIif(self, ctx:compiladorParser.IifContext):
        pass

    # Exit a parse tree produced by compiladorParser#iif.
    def exitIif(self, ctx:compiladorParser.IifContext):
        pass


    # Enter a parse tree produced by compiladorParser#ielse.
    def enterIelse(self, ctx:compiladorParser.IelseContext):
        pass

    # Exit a parse tree produced by compiladorParser#ielse.
    def exitIelse(self, ctx:compiladorParser.IelseContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracion.
    def enterDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracion.
    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladorParser#asignacion.
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#asignacion.
    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#retorno.
    def enterRetorno(self, ctx:compiladorParser.RetornoContext):
        pass

    # Exit a parse tree produced by compiladorParser#retorno.
    def exitRetorno(self, ctx:compiladorParser.RetornoContext):
        pass


    # Enter a parse tree produced by compiladorParser#sumar.
    def enterSumar(self, ctx:compiladorParser.SumarContext):
        pass

    # Exit a parse tree produced by compiladorParser#sumar.
    def exitSumar(self, ctx:compiladorParser.SumarContext):
        pass


    # Enter a parse tree produced by compiladorParser#restar.
    def enterRestar(self, ctx:compiladorParser.RestarContext):
        pass

    # Exit a parse tree produced by compiladorParser#restar.
    def exitRestar(self, ctx:compiladorParser.RestarContext):
        pass



del compiladorParser