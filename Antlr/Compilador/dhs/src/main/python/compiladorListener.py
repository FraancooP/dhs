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


    # Enter a parse tree produced by compiladorParser#instruccion.
    def enterInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladorParser#instruccion.
    def exitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladorParser#bloque.
    def enterBloque(self, ctx:compiladorParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladorParser#bloque.
    def exitBloque(self, ctx:compiladorParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladorParser#tipo.
    def enterTipo(self, ctx:compiladorParser.TipoContext):
        pass

    # Exit a parse tree produced by compiladorParser#tipo.
    def exitTipo(self, ctx:compiladorParser.TipoContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracion.
    def enterDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracion.
    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaDeclaradores.
    def enterListaDeclaradores(self, ctx:compiladorParser.ListaDeclaradoresContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaDeclaradores.
    def exitListaDeclaradores(self, ctx:compiladorParser.ListaDeclaradoresContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaOpal.
    def enterListaOpal(self, ctx:compiladorParser.ListaOpalContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaOpal.
    def exitListaOpal(self, ctx:compiladorParser.ListaOpalContext):
        pass


    # Enter a parse tree produced by compiladorParser#declarador.
    def enterDeclarador(self, ctx:compiladorParser.DeclaradorContext):
        pass

    # Exit a parse tree produced by compiladorParser#declarador.
    def exitDeclarador(self, ctx:compiladorParser.DeclaradorContext):
        pass


    # Enter a parse tree produced by compiladorParser#opal.
    def enterOpal(self, ctx:compiladorParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladorParser#opal.
    def exitOpal(self, ctx:compiladorParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladorParser#exp.
    def enterExp(self, ctx:compiladorParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladorParser#exp.
    def exitExp(self, ctx:compiladorParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladorParser#e.
    def enterE(self, ctx:compiladorParser.EContext):
        pass

    # Exit a parse tree produced by compiladorParser#e.
    def exitE(self, ctx:compiladorParser.EContext):
        pass


    # Enter a parse tree produced by compiladorParser#term.
    def enterTerm(self, ctx:compiladorParser.TermContext):
        pass

    # Exit a parse tree produced by compiladorParser#term.
    def exitTerm(self, ctx:compiladorParser.TermContext):
        pass


    # Enter a parse tree produced by compiladorParser#t.
    def enterT(self, ctx:compiladorParser.TContext):
        pass

    # Exit a parse tree produced by compiladorParser#t.
    def exitT(self, ctx:compiladorParser.TContext):
        pass


    # Enter a parse tree produced by compiladorParser#factor.
    def enterFactor(self, ctx:compiladorParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladorParser#factor.
    def exitFactor(self, ctx:compiladorParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladorParser#comparacion.
    def enterComparacion(self, ctx:compiladorParser.ComparacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#comparacion.
    def exitComparacion(self, ctx:compiladorParser.ComparacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#asignacion.
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#asignacion.
    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#expresionLogica.
    def enterExpresionLogica(self, ctx:compiladorParser.ExpresionLogicaContext):
        pass

    # Exit a parse tree produced by compiladorParser#expresionLogica.
    def exitExpresionLogica(self, ctx:compiladorParser.ExpresionLogicaContext):
        pass


    # Enter a parse tree produced by compiladorParser#logica.
    def enterLogica(self, ctx:compiladorParser.LogicaContext):
        pass

    # Exit a parse tree produced by compiladorParser#logica.
    def exitLogica(self, ctx:compiladorParser.LogicaContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaAsignaciones.
    def enterListaAsignaciones(self, ctx:compiladorParser.ListaAsignacionesContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaAsignaciones.
    def exitListaAsignaciones(self, ctx:compiladorParser.ListaAsignacionesContext):
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


    # Enter a parse tree produced by compiladorParser#ifor.
    def enterIfor(self, ctx:compiladorParser.IforContext):
        pass

    # Exit a parse tree produced by compiladorParser#ifor.
    def exitIfor(self, ctx:compiladorParser.IforContext):
        pass


    # Enter a parse tree produced by compiladorParser#forInit.
    def enterForInit(self, ctx:compiladorParser.ForInitContext):
        pass

    # Exit a parse tree produced by compiladorParser#forInit.
    def exitForInit(self, ctx:compiladorParser.ForInitContext):
        pass


    # Enter a parse tree produced by compiladorParser#forInc.
    def enterForInc(self, ctx:compiladorParser.ForIncContext):
        pass

    # Exit a parse tree produced by compiladorParser#forInc.
    def exitForInc(self, ctx:compiladorParser.ForIncContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaContadores.
    def enterListaContadores(self, ctx:compiladorParser.ListaContadoresContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaContadores.
    def exitListaContadores(self, ctx:compiladorParser.ListaContadoresContext):
        pass


    # Enter a parse tree produced by compiladorParser#prototipoDeFuncion.
    def enterPrototipoDeFuncion(self, ctx:compiladorParser.PrototipoDeFuncionContext):
        pass

    # Exit a parse tree produced by compiladorParser#prototipoDeFuncion.
    def exitPrototipoDeFuncion(self, ctx:compiladorParser.PrototipoDeFuncionContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracionDeFuncion.
    def enterDeclaracionDeFuncion(self, ctx:compiladorParser.DeclaracionDeFuncionContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracionDeFuncion.
    def exitDeclaracionDeFuncion(self, ctx:compiladorParser.DeclaracionDeFuncionContext):
        pass


    # Enter a parse tree produced by compiladorParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:compiladorParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by compiladorParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:compiladorParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by compiladorParser#retorno.
    def enterRetorno(self, ctx:compiladorParser.RetornoContext):
        pass

    # Exit a parse tree produced by compiladorParser#retorno.
    def exitRetorno(self, ctx:compiladorParser.RetornoContext):
        pass


    # Enter a parse tree produced by compiladorParser#parametro.
    def enterParametro(self, ctx:compiladorParser.ParametroContext):
        pass

    # Exit a parse tree produced by compiladorParser#parametro.
    def exitParametro(self, ctx:compiladorParser.ParametroContext):
        pass


    # Enter a parse tree produced by compiladorParser#parametros.
    def enterParametros(self, ctx:compiladorParser.ParametrosContext):
        pass

    # Exit a parse tree produced by compiladorParser#parametros.
    def exitParametros(self, ctx:compiladorParser.ParametrosContext):
        pass


    # Enter a parse tree produced by compiladorParser#argumentos.
    def enterArgumentos(self, ctx:compiladorParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by compiladorParser#argumentos.
    def exitArgumentos(self, ctx:compiladorParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by compiladorParser#llamadaFuncionInstruccion.
    def enterLlamadaFuncionInstruccion(self, ctx:compiladorParser.LlamadaFuncionInstruccionContext):
        pass

    # Exit a parse tree produced by compiladorParser#llamadaFuncionInstruccion.
    def exitLlamadaFuncionInstruccion(self, ctx:compiladorParser.LlamadaFuncionInstruccionContext):
        pass



del compiladorParser