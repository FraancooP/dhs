# Generated from /home/franco/Escritorio/Facultad/DHS/Antlr/Compilador/dhs/src/main/python/compilador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete generic visitor for a parse tree produced by compiladorParser.

class compiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladorParser#programa.
    def visitPrograma(self, ctx:compiladorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instruccion.
    def visitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#bloque.
    def visitBloque(self, ctx:compiladorParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#tipo.
    def visitTipo(self, ctx:compiladorParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracion.
    def visitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listaDeclaradores.
    def visitListaDeclaradores(self, ctx:compiladorParser.ListaDeclaradoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listaOpal.
    def visitListaOpal(self, ctx:compiladorParser.ListaOpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declarador.
    def visitDeclarador(self, ctx:compiladorParser.DeclaradorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#opal.
    def visitOpal(self, ctx:compiladorParser.OpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#exp.
    def visitExp(self, ctx:compiladorParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#e.
    def visitE(self, ctx:compiladorParser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#term.
    def visitTerm(self, ctx:compiladorParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#t.
    def visitT(self, ctx:compiladorParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#factor.
    def visitFactor(self, ctx:compiladorParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#comparacion.
    def visitComparacion(self, ctx:compiladorParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignacion.
    def visitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expresionLogica.
    def visitExpresionLogica(self, ctx:compiladorParser.ExpresionLogicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#logica.
    def visitLogica(self, ctx:compiladorParser.LogicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listaAsignaciones.
    def visitListaAsignaciones(self, ctx:compiladorParser.ListaAsignacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iwhile.
    def visitIwhile(self, ctx:compiladorParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iif.
    def visitIif(self, ctx:compiladorParser.IifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ielse.
    def visitIelse(self, ctx:compiladorParser.IelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ifor.
    def visitIfor(self, ctx:compiladorParser.IforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#forInit.
    def visitForInit(self, ctx:compiladorParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#forInc.
    def visitForInc(self, ctx:compiladorParser.ForIncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listaContadores.
    def visitListaContadores(self, ctx:compiladorParser.ListaContadoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#prototipoDeFuncion.
    def visitPrototipoDeFuncion(self, ctx:compiladorParser.PrototipoDeFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracionDeFuncion.
    def visitDeclaracionDeFuncion(self, ctx:compiladorParser.DeclaracionDeFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:compiladorParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#retorno.
    def visitRetorno(self, ctx:compiladorParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametro.
    def visitParametro(self, ctx:compiladorParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametros.
    def visitParametros(self, ctx:compiladorParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#argumentos.
    def visitArgumentos(self, ctx:compiladorParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#llamadaFuncionInstruccion.
    def visitLlamadaFuncionInstruccion(self, ctx:compiladorParser.LlamadaFuncionInstruccionContext):
        return self.visitChildren(ctx)



del compiladorParser