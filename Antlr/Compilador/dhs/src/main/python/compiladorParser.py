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
        4,1,36,324,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,90,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        5,1,5,1,5,3,5,101,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,115,8,7,1,8,1,8,1,8,5,8,120,8,8,10,8,12,8,123,9,8,1,9,
        1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,139,8,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,3,13,153,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,3,14,168,8,14,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,185,8,16,
        1,17,1,17,1,17,1,17,1,17,1,17,3,17,193,8,17,1,17,1,17,1,17,1,17,
        1,17,1,17,5,17,201,8,17,10,17,12,17,204,9,17,1,18,1,18,1,18,5,18,
        209,8,18,10,18,12,18,212,9,18,1,18,3,18,215,8,18,1,19,1,19,1,19,
        1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,
        3,21,233,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,252,8,23,1,24,1,24,3,24,
        256,8,24,1,25,1,25,1,25,5,25,261,8,25,10,25,12,25,264,9,25,1,25,
        3,25,267,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,
        1,29,1,29,3,29,294,8,29,1,30,1,30,1,30,1,31,1,31,1,31,5,31,302,8,
        31,10,31,12,31,305,9,31,1,31,3,31,308,8,31,1,32,1,32,1,32,5,32,313,
        8,32,10,32,12,32,316,9,32,1,32,3,32,319,8,32,1,33,1,33,1,33,1,33,
        0,1,34,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,0,2,1,0,25,26,1,0,14,19,
        331,0,68,1,0,0,0,2,75,1,0,0,0,4,89,1,0,0,0,6,91,1,0,0,0,8,95,1,0,
        0,0,10,100,1,0,0,0,12,102,1,0,0,0,14,114,1,0,0,0,16,116,1,0,0,0,
        18,124,1,0,0,0,20,126,1,0,0,0,22,138,1,0,0,0,24,140,1,0,0,0,26,152,
        1,0,0,0,28,167,1,0,0,0,30,169,1,0,0,0,32,184,1,0,0,0,34,192,1,0,
        0,0,36,214,1,0,0,0,38,216,1,0,0,0,40,222,1,0,0,0,42,232,1,0,0,0,
        44,234,1,0,0,0,46,251,1,0,0,0,48,255,1,0,0,0,50,266,1,0,0,0,52,268,
        1,0,0,0,54,275,1,0,0,0,56,282,1,0,0,0,58,293,1,0,0,0,60,295,1,0,
        0,0,62,307,1,0,0,0,64,318,1,0,0,0,66,320,1,0,0,0,68,69,3,2,1,0,69,
        70,5,0,0,1,70,1,1,0,0,0,71,72,3,4,2,0,72,73,3,2,1,0,73,76,1,0,0,
        0,74,76,1,0,0,0,75,71,1,0,0,0,75,74,1,0,0,0,76,3,1,0,0,0,77,78,3,
        32,16,0,78,79,5,5,0,0,79,90,1,0,0,0,80,90,3,12,6,0,81,90,3,38,19,
        0,82,90,3,6,3,0,83,90,3,40,20,0,84,90,3,44,22,0,85,90,3,54,27,0,
        86,90,3,52,26,0,87,90,3,66,33,0,88,90,3,58,29,0,89,77,1,0,0,0,89,
        80,1,0,0,0,89,81,1,0,0,0,89,82,1,0,0,0,89,83,1,0,0,0,89,84,1,0,0,
        0,89,85,1,0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,5,1,
        0,0,0,91,92,5,3,0,0,92,93,3,2,1,0,93,94,5,4,0,0,94,7,1,0,0,0,95,
        96,7,0,0,0,96,9,1,0,0,0,97,98,5,6,0,0,98,101,3,18,9,0,99,101,1,0,
        0,0,100,97,1,0,0,0,100,99,1,0,0,0,101,11,1,0,0,0,102,103,3,8,4,0,
        103,104,5,34,0,0,104,105,3,10,5,0,105,106,3,14,7,0,106,107,5,5,0,
        0,107,13,1,0,0,0,108,109,5,13,0,0,109,110,5,34,0,0,110,111,3,10,
        5,0,111,112,3,14,7,0,112,115,1,0,0,0,113,115,1,0,0,0,114,108,1,0,
        0,0,114,113,1,0,0,0,115,15,1,0,0,0,116,121,3,18,9,0,117,118,5,13,
        0,0,118,120,3,18,9,0,119,117,1,0,0,0,120,123,1,0,0,0,121,119,1,0,
        0,0,121,122,1,0,0,0,122,17,1,0,0,0,123,121,1,0,0,0,124,125,3,20,
        10,0,125,19,1,0,0,0,126,127,3,24,12,0,127,128,3,22,11,0,128,21,1,
        0,0,0,129,130,5,9,0,0,130,131,3,24,12,0,131,132,3,22,11,0,132,139,
        1,0,0,0,133,134,5,10,0,0,134,135,3,24,12,0,135,136,3,22,11,0,136,
        139,1,0,0,0,137,139,1,0,0,0,138,129,1,0,0,0,138,133,1,0,0,0,138,
        137,1,0,0,0,139,23,1,0,0,0,140,141,3,28,14,0,141,142,3,26,13,0,142,
        25,1,0,0,0,143,144,5,11,0,0,144,145,3,28,14,0,145,146,3,26,13,0,
        146,153,1,0,0,0,147,148,5,12,0,0,148,149,3,28,14,0,149,150,3,26,
        13,0,150,153,1,0,0,0,151,153,1,0,0,0,152,143,1,0,0,0,152,147,1,0,
        0,0,152,151,1,0,0,0,153,27,1,0,0,0,154,155,5,1,0,0,155,156,3,20,
        10,0,156,157,5,2,0,0,157,168,1,0,0,0,158,168,5,34,0,0,159,160,5,
        34,0,0,160,161,5,7,0,0,161,162,3,18,9,0,162,163,5,8,0,0,163,168,
        1,0,0,0,164,168,5,32,0,0,165,168,5,33,0,0,166,168,3,56,28,0,167,
        154,1,0,0,0,167,158,1,0,0,0,167,159,1,0,0,0,167,164,1,0,0,0,167,
        165,1,0,0,0,167,166,1,0,0,0,168,29,1,0,0,0,169,170,3,18,9,0,170,
        171,7,1,0,0,171,172,3,18,9,0,172,31,1,0,0,0,173,174,5,34,0,0,174,
        175,5,6,0,0,175,185,3,18,9,0,176,177,5,23,0,0,177,185,5,34,0,0,178,
        179,5,24,0,0,179,185,5,34,0,0,180,181,5,34,0,0,181,185,5,23,0,0,
        182,183,5,34,0,0,183,185,5,24,0,0,184,173,1,0,0,0,184,176,1,0,0,
        0,184,178,1,0,0,0,184,180,1,0,0,0,184,182,1,0,0,0,185,33,1,0,0,0,
        186,187,6,17,-1,0,187,193,3,30,15,0,188,189,5,1,0,0,189,190,3,34,
        17,0,190,191,5,2,0,0,191,193,1,0,0,0,192,186,1,0,0,0,192,188,1,0,
        0,0,193,202,1,0,0,0,194,195,10,3,0,0,195,196,5,20,0,0,196,201,3,
        34,17,4,197,198,10,2,0,0,198,199,5,21,0,0,199,201,3,34,17,3,200,
        194,1,0,0,0,200,197,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,
        203,1,0,0,0,203,35,1,0,0,0,204,202,1,0,0,0,205,210,3,32,16,0,206,
        207,5,13,0,0,207,209,3,32,16,0,208,206,1,0,0,0,209,212,1,0,0,0,210,
        208,1,0,0,0,210,211,1,0,0,0,211,215,1,0,0,0,212,210,1,0,0,0,213,
        215,1,0,0,0,214,205,1,0,0,0,214,213,1,0,0,0,215,37,1,0,0,0,216,217,
        5,30,0,0,217,218,5,1,0,0,218,219,3,34,17,0,219,220,5,2,0,0,220,221,
        3,4,2,0,221,39,1,0,0,0,222,223,5,27,0,0,223,224,5,1,0,0,224,225,
        3,34,17,0,225,226,5,2,0,0,226,227,3,4,2,0,227,228,3,42,21,0,228,
        41,1,0,0,0,229,230,5,28,0,0,230,233,3,4,2,0,231,233,1,0,0,0,232,
        229,1,0,0,0,232,231,1,0,0,0,233,43,1,0,0,0,234,235,5,29,0,0,235,
        236,5,1,0,0,236,237,3,46,23,0,237,238,5,5,0,0,238,239,3,34,17,0,
        239,240,5,5,0,0,240,241,3,48,24,0,241,242,5,2,0,0,242,243,3,6,3,
        0,243,45,1,0,0,0,244,245,3,8,4,0,245,246,5,34,0,0,246,247,3,10,5,
        0,247,248,3,14,7,0,248,252,1,0,0,0,249,252,3,36,18,0,250,252,1,0,
        0,0,251,244,1,0,0,0,251,249,1,0,0,0,251,250,1,0,0,0,252,47,1,0,0,
        0,253,256,3,50,25,0,254,256,1,0,0,0,255,253,1,0,0,0,255,254,1,0,
        0,0,256,49,1,0,0,0,257,262,3,32,16,0,258,259,5,13,0,0,259,261,3,
        32,16,0,260,258,1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,262,263,
        1,0,0,0,263,267,1,0,0,0,264,262,1,0,0,0,265,267,1,0,0,0,266,257,
        1,0,0,0,266,265,1,0,0,0,267,51,1,0,0,0,268,269,3,8,4,0,269,270,5,
        34,0,0,270,271,5,1,0,0,271,272,3,62,31,0,272,273,5,2,0,0,273,274,
        5,5,0,0,274,53,1,0,0,0,275,276,3,8,4,0,276,277,5,34,0,0,277,278,
        5,1,0,0,278,279,3,62,31,0,279,280,5,2,0,0,280,281,3,6,3,0,281,55,
        1,0,0,0,282,283,5,34,0,0,283,284,5,1,0,0,284,285,3,64,32,0,285,286,
        5,2,0,0,286,57,1,0,0,0,287,288,5,31,0,0,288,289,3,18,9,0,289,290,
        5,5,0,0,290,294,1,0,0,0,291,292,5,31,0,0,292,294,5,5,0,0,293,287,
        1,0,0,0,293,291,1,0,0,0,294,59,1,0,0,0,295,296,3,8,4,0,296,297,5,
        34,0,0,297,61,1,0,0,0,298,303,3,60,30,0,299,300,5,13,0,0,300,302,
        3,60,30,0,301,299,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,
        1,0,0,0,304,308,1,0,0,0,305,303,1,0,0,0,306,308,1,0,0,0,307,298,
        1,0,0,0,307,306,1,0,0,0,308,63,1,0,0,0,309,314,3,18,9,0,310,311,
        5,13,0,0,311,313,3,18,9,0,312,310,1,0,0,0,313,316,1,0,0,0,314,312,
        1,0,0,0,314,315,1,0,0,0,315,319,1,0,0,0,316,314,1,0,0,0,317,319,
        1,0,0,0,318,309,1,0,0,0,318,317,1,0,0,0,319,65,1,0,0,0,320,321,3,
        56,28,0,321,322,5,5,0,0,322,67,1,0,0,0,24,75,89,100,114,121,138,
        152,167,184,192,200,202,210,214,232,251,255,262,266,293,303,307,
        314,318
    ]

class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "'['", "']'", "'+'", "'-'", "'*'", "'/'", "','", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='", "'&&'", "'||'", 
                     "'!'", "'++'", "'--'", "'int'", "'double'", "'if'", 
                     "'else'", "'for'", "'while'", "'return'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "ASIG", 
                      "CA", "CC", "SUMA", "RESTA", "MULT", "DIV", "COMA", 
                      "MENOR", "MAYOR", "MENORIGUAL", "MAYORIGUAL", "IGUAL", 
                      "DIFERENTE", "AND", "OR", "NOT", "INCREMENT", "DECREMENT", 
                      "INT", "DOUBLE", "IF", "ELSE", "FOR", "WHILE", "RETURN", 
                      "NUMERO_CON_PUNTO", "NUMERO", "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_bloque = 3
    RULE_tipo = 4
    RULE_inic = 5
    RULE_declaracion = 6
    RULE_listavar = 7
    RULE_listaOpal = 8
    RULE_opal = 9
    RULE_exp = 10
    RULE_e = 11
    RULE_term = 12
    RULE_t = 13
    RULE_factor = 14
    RULE_comparacion = 15
    RULE_asignacion = 16
    RULE_expresionLogica = 17
    RULE_listaAsignaciones = 18
    RULE_iwhile = 19
    RULE_iif = 20
    RULE_ielse = 21
    RULE_ifor = 22
    RULE_forInit = 23
    RULE_forInc = 24
    RULE_listaContadores = 25
    RULE_prototipoDeFuncion = 26
    RULE_declaracionDeFuncion = 27
    RULE_llamadaFuncion = 28
    RULE_retorno = 29
    RULE_parametro = 30
    RULE_parametros = 31
    RULE_argumentos = 32
    RULE_llamadaFuncionInstruccion = 33

    ruleNames =  [ "programa", "instrucciones", "instruccion", "bloque", 
                   "tipo", "inic", "declaracion", "listavar", "listaOpal", 
                   "opal", "exp", "e", "term", "t", "factor", "comparacion", 
                   "asignacion", "expresionLogica", "listaAsignaciones", 
                   "iwhile", "iif", "ielse", "ifor", "forInit", "forInc", 
                   "listaContadores", "prototipoDeFuncion", "declaracionDeFuncion", 
                   "llamadaFuncion", "retorno", "parametro", "parametros", 
                   "argumentos", "llamadaFuncionInstruccion" ]

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
    COMA=13
    MENOR=14
    MAYOR=15
    MENORIGUAL=16
    MAYORIGUAL=17
    IGUAL=18
    DIFERENTE=19
    AND=20
    OR=21
    NOT=22
    INCREMENT=23
    DECREMENT=24
    INT=25
    DOUBLE=26
    IF=27
    ELSE=28
    FOR=29
    WHILE=30
    RETURN=31
    NUMERO_CON_PUNTO=32
    NUMERO=33
    ID=34
    WS=35
    OTRO=36

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
            self.state = 68
            self.instrucciones()
            self.state = 69
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
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 23, 24, 25, 26, 27, 29, 30, 31, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.instruccion()
                self.state = 72
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


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def declaracion(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladorParser.IwhileContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladorParser.IifContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladorParser.IforContext,0)


        def declaracionDeFuncion(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionDeFuncionContext,0)


        def prototipoDeFuncion(self):
            return self.getTypedRuleContext(compiladorParser.PrototipoDeFuncionContext,0)


        def llamadaFuncionInstruccion(self):
            return self.getTypedRuleContext(compiladorParser.LlamadaFuncionInstruccionContext,0)


        def retorno(self):
            return self.getTypedRuleContext(compiladorParser.RetornoContext,0)


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
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.asignacion()
                self.state = 78
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.declaracion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.iwhile()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.bloque()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.iif()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 84
                self.ifor()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 85
                self.declaracionDeFuncion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 86
                self.prototipoDeFuncion()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 87
                self.llamadaFuncionInstruccion()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 88
                self.retorno()
                pass


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
        self.enterRule(localctx, 6, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(compiladorParser.LLA)
            self.state = 92
            self.instrucciones()
            self.state = 93
            self.match(compiladorParser.LLC)
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
        self.enterRule(localctx, 8, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
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


    class InicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_inic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInic" ):
                listener.enterInic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInic" ):
                listener.exitInic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInic" ):
                return visitor.visitInic(self)
            else:
                return visitor.visitChildren(self)




    def inic(self):

        localctx = compiladorParser.InicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inic)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(compiladorParser.ASIG)
                self.state = 98
                self.opal()
                pass
            elif token in [5, 13]:
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


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compiladorParser.ListavarContext,0)


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
        self.enterRule(localctx, 12, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.tipo()
            self.state = 103
            self.match(compiladorParser.ID)
            self.state = 104
            self.inic()
            self.state = 105
            self.listavar()
            self.state = 106
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListavarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compiladorParser.ListavarContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listavar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListavar" ):
                listener.enterListavar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListavar" ):
                listener.exitListavar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListavar" ):
                return visitor.visitListavar(self)
            else:
                return visitor.visitChildren(self)




    def listavar(self):

        localctx = compiladorParser.ListavarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listavar)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(compiladorParser.COMA)
                self.state = 109
                self.match(compiladorParser.ID)
                self.state = 110
                self.inic()
                self.state = 111
                self.listavar()
                pass
            elif token in [5]:
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


    class ListaOpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.OpalContext)
            else:
                return self.getTypedRuleContext(compiladorParser.OpalContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.COMA)
            else:
                return self.getToken(compiladorParser.COMA, i)

        def getRuleIndex(self):
            return compiladorParser.RULE_listaOpal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaOpal" ):
                listener.enterListaOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaOpal" ):
                listener.exitListaOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaOpal" ):
                return visitor.visitListaOpal(self)
            else:
                return visitor.visitChildren(self)




    def listaOpal(self):

        localctx = compiladorParser.ListaOpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_listaOpal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.opal()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 117
                self.match(compiladorParser.COMA)
                self.state = 118
                self.opal()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


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
        self.enterRule(localctx, 18, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladorParser.EContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compiladorParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.term()
            self.state = 127
            self.e()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compiladorParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladorParser.EContext,0)


        def RESTA(self):
            return self.getToken(compiladorParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = compiladorParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_e)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(compiladorParser.SUMA)
                self.state = 130
                self.term()
                self.state = 131
                self.e()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(compiladorParser.RESTA)
                self.state = 134
                self.term()
                self.state = 135
                self.e()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladorParser.TContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.factor()
            self.state = 141
            self.t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladorParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladorParser.TContext,0)


        def DIV(self):
            return self.getToken(compiladorParser.DIV, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compiladorParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_t)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(compiladorParser.MULT)
                self.state = 144
                self.factor()
                self.state = 145
                self.t()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(compiladorParser.DIV)
                self.state = 148
                self.factor()
                self.state = 149
                self.t()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def CA(self):
            return self.getToken(compiladorParser.CA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def CC(self):
            return self.getToken(compiladorParser.CC, 0)

        def NUMERO_CON_PUNTO(self):
            return self.getToken(compiladorParser.NUMERO_CON_PUNTO, 0)

        def NUMERO(self):
            return self.getToken(compiladorParser.NUMERO, 0)

        def llamadaFuncion(self):
            return self.getTypedRuleContext(compiladorParser.LlamadaFuncionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_factor)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(compiladorParser.PA)
                self.state = 155
                self.exp()
                self.state = 156
                self.match(compiladorParser.PC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(compiladorParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(compiladorParser.ID)
                self.state = 160
                self.match(compiladorParser.CA)
                self.state = 161
                self.opal()
                self.state = 162
                self.match(compiladorParser.CC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.match(compiladorParser.NUMERO_CON_PUNTO)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.match(compiladorParser.NUMERO)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 166
                self.llamadaFuncion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.OpalContext)
            else:
                return self.getTypedRuleContext(compiladorParser.OpalContext,i)


        def MENOR(self):
            return self.getToken(compiladorParser.MENOR, 0)

        def MAYOR(self):
            return self.getToken(compiladorParser.MAYOR, 0)

        def MENORIGUAL(self):
            return self.getToken(compiladorParser.MENORIGUAL, 0)

        def MAYORIGUAL(self):
            return self.getToken(compiladorParser.MAYORIGUAL, 0)

        def IGUAL(self):
            return self.getToken(compiladorParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(compiladorParser.DIFERENTE, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)




    def comparacion(self):

        localctx = compiladorParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.opal()
            self.state = 170
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 171
            self.opal()
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


        def INCREMENT(self):
            return self.getToken(compiladorParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(compiladorParser.DECREMENT, 0)

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
        self.enterRule(localctx, 32, self.RULE_asignacion)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(compiladorParser.ID)
                self.state = 174
                self.match(compiladorParser.ASIG)
                self.state = 175
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(compiladorParser.INCREMENT)
                self.state = 177
                self.match(compiladorParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.match(compiladorParser.DECREMENT)
                self.state = 179
                self.match(compiladorParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.match(compiladorParser.ID)
                self.state = 181
                self.match(compiladorParser.INCREMENT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.match(compiladorParser.ID)
                self.state = 183
                self.match(compiladorParser.DECREMENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionLogicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacion(self):
            return self.getTypedRuleContext(compiladorParser.ComparacionContext,0)


        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def expresionLogica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.ExpresionLogicaContext)
            else:
                return self.getTypedRuleContext(compiladorParser.ExpresionLogicaContext,i)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def AND(self):
            return self.getToken(compiladorParser.AND, 0)

        def OR(self):
            return self.getToken(compiladorParser.OR, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_expresionLogica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionLogica" ):
                listener.enterExpresionLogica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionLogica" ):
                listener.exitExpresionLogica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionLogica" ):
                return visitor.visitExpresionLogica(self)
            else:
                return visitor.visitChildren(self)



    def expresionLogica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = compiladorParser.ExpresionLogicaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expresionLogica, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 187
                self.comparacion()
                pass

            elif la_ == 2:
                self.state = 188
                self.match(compiladorParser.PA)
                self.state = 189
                self.expresionLogica(0)
                self.state = 190
                self.match(compiladorParser.PC)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 200
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = compiladorParser.ExpresionLogicaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresionLogica)
                        self.state = 194
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 195
                        self.match(compiladorParser.AND)
                        self.state = 196
                        self.expresionLogica(4)
                        pass

                    elif la_ == 2:
                        localctx = compiladorParser.ExpresionLogicaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresionLogica)
                        self.state = 197
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 198
                        self.match(compiladorParser.OR)
                        self.state = 199
                        self.expresionLogica(3)
                        pass

             
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ListaAsignacionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(compiladorParser.AsignacionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.COMA)
            else:
                return self.getToken(compiladorParser.COMA, i)

        def getRuleIndex(self):
            return compiladorParser.RULE_listaAsignaciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaAsignaciones" ):
                listener.enterListaAsignaciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaAsignaciones" ):
                listener.exitListaAsignaciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaAsignaciones" ):
                return visitor.visitListaAsignaciones(self)
            else:
                return visitor.visitChildren(self)




    def listaAsignaciones(self):

        localctx = compiladorParser.ListaAsignacionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_listaAsignaciones)
        self._la = 0 # Token type
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.asignacion()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 206
                    self.match(compiladorParser.COMA)
                    self.state = 207
                    self.asignacion()
                    self.state = 212
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [5]:
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


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladorParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def expresionLogica(self):
            return self.getTypedRuleContext(compiladorParser.ExpresionLogicaContext,0)


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
        self.enterRule(localctx, 38, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(compiladorParser.WHILE)
            self.state = 217
            self.match(compiladorParser.PA)
            self.state = 218
            self.expresionLogica(0)
            self.state = 219
            self.match(compiladorParser.PC)
            self.state = 220
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

        def expresionLogica(self):
            return self.getTypedRuleContext(compiladorParser.ExpresionLogicaContext,0)


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
        self.enterRule(localctx, 40, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(compiladorParser.IF)
            self.state = 223
            self.match(compiladorParser.PA)
            self.state = 224
            self.expresionLogica(0)
            self.state = 225
            self.match(compiladorParser.PC)
            self.state = 226
            self.instruccion()
            self.state = 227
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
        self.enterRule(localctx, 42, self.RULE_ielse)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(compiladorParser.ELSE)
                self.state = 230
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


    class IforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladorParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def forInit(self):
            return self.getTypedRuleContext(compiladorParser.ForInitContext,0)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.PYC)
            else:
                return self.getToken(compiladorParser.PYC, i)

        def expresionLogica(self):
            return self.getTypedRuleContext(compiladorParser.ExpresionLogicaContext,0)


        def forInc(self):
            return self.getTypedRuleContext(compiladorParser.ForIncContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_ifor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfor" ):
                listener.enterIfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfor" ):
                listener.exitIfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfor" ):
                return visitor.visitIfor(self)
            else:
                return visitor.visitChildren(self)




    def ifor(self):

        localctx = compiladorParser.IforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(compiladorParser.FOR)
            self.state = 235
            self.match(compiladorParser.PA)
            self.state = 236
            self.forInit()
            self.state = 237
            self.match(compiladorParser.PYC)
            self.state = 238
            self.expresionLogica(0)
            self.state = 239
            self.match(compiladorParser.PYC)
            self.state = 240
            self.forInc()
            self.state = 241
            self.match(compiladorParser.PC)
            self.state = 242
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compiladorParser.ListavarContext,0)


        def listaAsignaciones(self):
            return self.getTypedRuleContext(compiladorParser.ListaAsignacionesContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = compiladorParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forInit)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.tipo()
                self.state = 245
                self.match(compiladorParser.ID)
                self.state = 246
                self.inic()
                self.state = 247
                self.listavar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.listaAsignaciones()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForIncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaContadores(self):
            return self.getTypedRuleContext(compiladorParser.ListaContadoresContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_forInc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInc" ):
                listener.enterForInc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInc" ):
                listener.exitForInc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInc" ):
                return visitor.visitForInc(self)
            else:
                return visitor.visitChildren(self)




    def forInc(self):

        localctx = compiladorParser.ForIncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forInc)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.listaContadores()
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


    class ListaContadoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(compiladorParser.AsignacionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.COMA)
            else:
                return self.getToken(compiladorParser.COMA, i)

        def getRuleIndex(self):
            return compiladorParser.RULE_listaContadores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaContadores" ):
                listener.enterListaContadores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaContadores" ):
                listener.exitListaContadores(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaContadores" ):
                return visitor.visitListaContadores(self)
            else:
                return visitor.visitChildren(self)




    def listaContadores(self):

        localctx = compiladorParser.ListaContadoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_listaContadores)
        self._la = 0 # Token type
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.asignacion()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 258
                    self.match(compiladorParser.COMA)
                    self.state = 259
                    self.asignacion()
                    self.state = 264
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [2]:
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


    class PrototipoDeFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladorParser.ParametrosContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_prototipoDeFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrototipoDeFuncion" ):
                listener.enterPrototipoDeFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrototipoDeFuncion" ):
                listener.exitPrototipoDeFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototipoDeFuncion" ):
                return visitor.visitPrototipoDeFuncion(self)
            else:
                return visitor.visitChildren(self)




    def prototipoDeFuncion(self):

        localctx = compiladorParser.PrototipoDeFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_prototipoDeFuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.tipo()
            self.state = 269
            self.match(compiladorParser.ID)
            self.state = 270
            self.match(compiladorParser.PA)
            self.state = 271
            self.parametros()
            self.state = 272
            self.match(compiladorParser.PC)
            self.state = 273
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionDeFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladorParser.ParametrosContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_declaracionDeFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionDeFuncion" ):
                listener.enterDeclaracionDeFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionDeFuncion" ):
                listener.exitDeclaracionDeFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionDeFuncion" ):
                return visitor.visitDeclaracionDeFuncion(self)
            else:
                return visitor.visitChildren(self)




    def declaracionDeFuncion(self):

        localctx = compiladorParser.DeclaracionDeFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_declaracionDeFuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.tipo()
            self.state = 276
            self.match(compiladorParser.ID)
            self.state = 277
            self.match(compiladorParser.PA)
            self.state = 278
            self.parametros()
            self.state = 279
            self.match(compiladorParser.PC)
            self.state = 280
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladorParser.ArgumentosContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_llamadaFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFuncion" ):
                listener.enterLlamadaFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFuncion" ):
                listener.exitLlamadaFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncion" ):
                return visitor.visitLlamadaFuncion(self)
            else:
                return visitor.visitChildren(self)




    def llamadaFuncion(self):

        localctx = compiladorParser.LlamadaFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_llamadaFuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(compiladorParser.ID)
            self.state = 283
            self.match(compiladorParser.PA)
            self.state = 284
            self.argumentos()
            self.state = 285
            self.match(compiladorParser.PC)
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

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


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
        self.enterRule(localctx, 58, self.RULE_retorno)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(compiladorParser.RETURN)
                self.state = 288
                self.opal()
                self.state = 289
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.match(compiladorParser.RETURN)
                self.state = 292
                self.match(compiladorParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = compiladorParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.tipo()
            self.state = 296
            self.match(compiladorParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.ParametroContext)
            else:
                return self.getTypedRuleContext(compiladorParser.ParametroContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.COMA)
            else:
                return self.getToken(compiladorParser.COMA, i)

        def getRuleIndex(self):
            return compiladorParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = compiladorParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.parametro()
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 299
                    self.match(compiladorParser.COMA)
                    self.state = 300
                    self.parametro()
                    self.state = 305
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [2]:
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


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.OpalContext)
            else:
                return self.getTypedRuleContext(compiladorParser.OpalContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.COMA)
            else:
                return self.getToken(compiladorParser.COMA, i)

        def getRuleIndex(self):
            return compiladorParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = compiladorParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.opal()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 310
                    self.match(compiladorParser.COMA)
                    self.state = 311
                    self.opal()
                    self.state = 316
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [2]:
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


    class LlamadaFuncionInstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def llamadaFuncion(self):
            return self.getTypedRuleContext(compiladorParser.LlamadaFuncionContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_llamadaFuncionInstruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFuncionInstruccion" ):
                listener.enterLlamadaFuncionInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFuncionInstruccion" ):
                listener.exitLlamadaFuncionInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncionInstruccion" ):
                return visitor.visitLlamadaFuncionInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def llamadaFuncionInstruccion(self):

        localctx = compiladorParser.LlamadaFuncionInstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_llamadaFuncionInstruccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.llamadaFuncion()
            self.state = 321
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expresionLogica_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresionLogica_sempred(self, localctx:ExpresionLogicaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




