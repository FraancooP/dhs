# Generated from /home/franco/Escritorio/Facultad/DHS/Antlr/Compilador/dhs/src/main/python/compilador.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,1,3,1,3,
        1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,58,8,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,3,9,76,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,0,2,1,0,14,15,2,0,13,13,21,21,98,0,30,1,0,0,0,2,37,1,0,0,0,
        4,39,1,0,0,0,6,41,1,0,0,0,8,43,1,0,0,0,10,45,1,0,0,0,12,57,1,0,0,
        0,14,59,1,0,0,0,16,65,1,0,0,0,18,75,1,0,0,0,20,77,1,0,0,0,22,81,
        1,0,0,0,24,86,1,0,0,0,26,90,1,0,0,0,28,97,1,0,0,0,30,31,3,2,1,0,
        31,32,5,0,0,1,32,1,1,0,0,0,33,34,3,12,6,0,34,35,3,2,1,0,35,38,1,
        0,0,0,36,38,1,0,0,0,37,33,1,0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,
        40,7,0,0,0,40,5,1,0,0,0,41,42,7,1,0,0,42,7,1,0,0,0,43,44,5,13,0,
        0,44,9,1,0,0,0,45,46,5,3,0,0,46,47,3,2,1,0,47,48,5,4,0,0,48,11,1,
        0,0,0,49,58,3,22,11,0,50,58,3,20,10,0,51,58,3,24,12,0,52,58,3,26,
        13,0,53,58,3,28,14,0,54,58,3,14,7,0,55,58,3,10,5,0,56,58,3,16,8,
        0,57,49,1,0,0,0,57,50,1,0,0,0,57,51,1,0,0,0,57,52,1,0,0,0,57,53,
        1,0,0,0,57,54,1,0,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,13,1,0,0,0,
        59,60,5,19,0,0,60,61,5,1,0,0,61,62,3,6,3,0,62,63,5,2,0,0,63,64,3,
        12,6,0,64,15,1,0,0,0,65,66,5,16,0,0,66,67,5,1,0,0,67,68,3,6,3,0,
        68,69,5,2,0,0,69,70,3,12,6,0,70,71,3,18,9,0,71,17,1,0,0,0,72,73,
        5,17,0,0,73,76,3,12,6,0,74,76,1,0,0,0,75,72,1,0,0,0,75,74,1,0,0,
        0,76,19,1,0,0,0,77,78,3,4,2,0,78,79,5,21,0,0,79,80,5,5,0,0,80,21,
        1,0,0,0,81,82,5,21,0,0,82,83,5,6,0,0,83,84,3,6,3,0,84,85,5,5,0,0,
        85,23,1,0,0,0,86,87,5,20,0,0,87,88,3,8,4,0,88,89,5,5,0,0,89,25,1,
        0,0,0,90,91,5,21,0,0,91,92,5,6,0,0,92,93,5,21,0,0,93,94,5,9,0,0,
        94,95,3,6,3,0,95,96,5,5,0,0,96,27,1,0,0,0,97,98,5,21,0,0,98,99,5,
        6,0,0,99,100,5,21,0,0,100,101,5,10,0,0,101,102,3,6,3,0,102,103,5,
        5,0,0,103,29,1,0,0,0,3,37,57,75
    ]

class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "'['", "']'", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "'int'", "'double'", "'if'", "'else'", "'for'", "'while'", 
                     "'return'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "ASIG", 
                      "CA", "CC", "SUMA", "RESTA", "MULT", "DIV", "NUMERO", 
                      "INT", "DOUBLE", "IF", "ELSE", "FOR", "WHILE", "RETURN", 
                      "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_tipo = 2
    RULE_opal = 3
    RULE_codigo = 4
    RULE_bloque = 5
    RULE_instruccion = 6
    RULE_iwhile = 7
    RULE_iif = 8
    RULE_ielse = 9
    RULE_declaracion = 10
    RULE_asignacion = 11
    RULE_retorno = 12
    RULE_sumar = 13
    RULE_restar = 14

    ruleNames =  [ "programa", "instrucciones", "tipo", "opal", "codigo", 
                   "bloque", "instruccion", "iwhile", "iif", "ielse", "declaracion", 
                   "asignacion", "retorno", "sumar", "restar" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    PYC=5
    ASIG=6
    CA=7
    CC=8
    SUMA=9
    RESTA=10
    MULT=11
    DIV=12
    NUMERO=13
    INT=14
    DOUBLE=15
    IF=16
    ELSE=17
    FOR=18
    WHILE=19
    RETURN=20
    ID=21
    WS=22
    OTRO=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladorParser.EOF, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.instrucciones()
            self.state = 31
            self.match(compiladorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladorParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 14, 15, 16, 19, 20, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.instruccion()
                self.state = 34
                self.instrucciones()
                pass
            elif token in [-1, 4]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladorParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladorParser.DOUBLE, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = compiladorParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladorParser.NUMERO, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compiladorParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_opal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not(_la==13 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodigoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladorParser.NUMERO, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_codigo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodigo" ):
                listener.enterCodigo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodigo" ):
                listener.exitCodigo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCodigo" ):
                return visitor.visitCodigo(self)
            else:
                return visitor.visitChildren(self)




    def codigo(self):

        localctx = compiladorParser.CodigoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_codigo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(compiladorParser.NUMERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladorParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladorParser.LLC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladorParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(compiladorParser.LLA)
            self.state = 46
            self.instrucciones()
            self.state = 47
            self.match(compiladorParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionContext,0)


        def retorno(self):
            return self.getTypedRuleContext(compiladorParser.RetornoContext,0)


        def sumar(self):
            return self.getTypedRuleContext(compiladorParser.SumarContext,0)


        def restar(self):
            return self.getTypedRuleContext(compiladorParser.RestarContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladorParser.IwhileContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladorParser.IifContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladorParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_instruccion)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.declaracion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.retorno()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.sumar()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.restar()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.iwhile()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 55
                self.bloque()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 56
                self.iif()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladorParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_iwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIwhile" ):
                listener.enterIwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIwhile" ):
                listener.exitIwhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIwhile" ):
                return visitor.visitIwhile(self)
            else:
                return visitor.visitChildren(self)




    def iwhile(self):

        localctx = compiladorParser.IwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(compiladorParser.WHILE)
            self.state = 60
            self.match(compiladorParser.PA)
            self.state = 61
            self.opal()
            self.state = 62
            self.match(compiladorParser.PC)
            self.state = 63
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladorParser.IF, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def ielse(self):
            return self.getTypedRuleContext(compiladorParser.IelseContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_iif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIif" ):
                listener.enterIif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIif" ):
                listener.exitIif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIif" ):
                return visitor.visitIif(self)
            else:
                return visitor.visitChildren(self)




    def iif(self):

        localctx = compiladorParser.IifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(compiladorParser.IF)
            self.state = 66
            self.match(compiladorParser.PA)
            self.state = 67
            self.opal()
            self.state = 68
            self.match(compiladorParser.PC)
            self.state = 69
            self.instruccion()
            self.state = 70
            self.ielse()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compiladorParser.ELSE, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_ielse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIelse" ):
                listener.enterIelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIelse" ):
                listener.exitIelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIelse" ):
                return visitor.visitIelse(self)
            else:
                return visitor.visitChildren(self)




    def ielse(self):

        localctx = compiladorParser.IelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ielse)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(compiladorParser.ELSE)
                self.state = 73
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladorParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.tipo()
            self.state = 78
            self.match(compiladorParser.ID)
            self.state = 79
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladorParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(compiladorParser.ID)
            self.state = 82
            self.match(compiladorParser.ASIG)
            self.state = 83
            self.opal()
            self.state = 84
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladorParser.RETURN, 0)

        def codigo(self):
            return self.getTypedRuleContext(compiladorParser.CodigoContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno" ):
                listener.enterRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno" ):
                listener.exitRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = compiladorParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(compiladorParser.RETURN)
            self.state = 87
            self.codigo()
            self.state = 88
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.ID)
            else:
                return self.getToken(compiladorParser.ID, i)

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def SUMA(self):
            return self.getToken(compiladorParser.SUMA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_sumar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumar" ):
                listener.enterSumar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumar" ):
                listener.exitSumar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumar" ):
                return visitor.visitSumar(self)
            else:
                return visitor.visitChildren(self)




    def sumar(self):

        localctx = compiladorParser.SumarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sumar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(compiladorParser.ID)
            self.state = 91
            self.match(compiladorParser.ASIG)
            self.state = 92
            self.match(compiladorParser.ID)
            self.state = 93
            self.match(compiladorParser.SUMA)
            self.state = 94
            self.opal()
            self.state = 95
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.ID)
            else:
                return self.getToken(compiladorParser.ID, i)

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def RESTA(self):
            return self.getToken(compiladorParser.RESTA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_restar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestar" ):
                listener.enterRestar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestar" ):
                listener.exitRestar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestar" ):
                return visitor.visitRestar(self)
            else:
                return visitor.visitChildren(self)




    def restar(self):

        localctx = compiladorParser.RestarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_restar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(compiladorParser.ID)
            self.state = 98
            self.match(compiladorParser.ASIG)
            self.state = 99
            self.match(compiladorParser.ID)
            self.state = 100
            self.match(compiladorParser.RESTA)
            self.state = 101
            self.opal()
            self.state = 102
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





