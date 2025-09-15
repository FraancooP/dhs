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


    # Visit a parse tree produced by compiladorParser#tipo.
    def visitTipo(self, ctx:compiladorParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#opal.
    def visitOpal(self, ctx:compiladorParser.OpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#codigo.
    def visitCodigo(self, ctx:compiladorParser.CodigoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#bloque.
    def visitBloque(self, ctx:compiladorParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instruccion.
    def visitInstruccion(self, ctx:compiladorParser.InstruccionContext):
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


    # Visit a parse tree produced by compiladorParser#declaracion.
    def visitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignacion.
    def visitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#retorno.
    def visitRetorno(self, ctx:compiladorParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#sumar.
    def visitSumar(self, ctx:compiladorParser.SumarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#restar.
    def visitRestar(self, ctx:compiladorParser.RestarContext):
        return self.visitChildren(ctx)



del compiladorParser