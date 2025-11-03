// Generated from /home/franco/Escritorio/Facultad/DHS/Antlr/Compilador/dhs/src/main/python/compilador.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link compiladorParser}.
 */
public interface compiladorListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link compiladorParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(compiladorParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(compiladorParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void enterInstrucciones(compiladorParser.InstruccionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void exitInstrucciones(compiladorParser.InstruccionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccion(compiladorParser.InstruccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccion(compiladorParser.InstruccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#bloque}.
	 * @param ctx the parse tree
	 */
	void enterBloque(compiladorParser.BloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#bloque}.
	 * @param ctx the parse tree
	 */
	void exitBloque(compiladorParser.BloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(compiladorParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(compiladorParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#inic}.
	 * @param ctx the parse tree
	 */
	void enterInic(compiladorParser.InicContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#inic}.
	 * @param ctx the parse tree
	 */
	void exitInic(compiladorParser.InicContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion(compiladorParser.DeclaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion(compiladorParser.DeclaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#listavar}.
	 * @param ctx the parse tree
	 */
	void enterListavar(compiladorParser.ListavarContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#listavar}.
	 * @param ctx the parse tree
	 */
	void exitListavar(compiladorParser.ListavarContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#listaOpal}.
	 * @param ctx the parse tree
	 */
	void enterListaOpal(compiladorParser.ListaOpalContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#listaOpal}.
	 * @param ctx the parse tree
	 */
	void exitListaOpal(compiladorParser.ListaOpalContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#opal}.
	 * @param ctx the parse tree
	 */
	void enterOpal(compiladorParser.OpalContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#opal}.
	 * @param ctx the parse tree
	 */
	void exitOpal(compiladorParser.OpalContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(compiladorParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(compiladorParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#e}.
	 * @param ctx the parse tree
	 */
	void enterE(compiladorParser.EContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#e}.
	 * @param ctx the parse tree
	 */
	void exitE(compiladorParser.EContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(compiladorParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(compiladorParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#t}.
	 * @param ctx the parse tree
	 */
	void enterT(compiladorParser.TContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#t}.
	 * @param ctx the parse tree
	 */
	void exitT(compiladorParser.TContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(compiladorParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(compiladorParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#comparacion}.
	 * @param ctx the parse tree
	 */
	void enterComparacion(compiladorParser.ComparacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#comparacion}.
	 * @param ctx the parse tree
	 */
	void exitComparacion(compiladorParser.ComparacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(compiladorParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(compiladorParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#expresionLogica}.
	 * @param ctx the parse tree
	 */
	void enterExpresionLogica(compiladorParser.ExpresionLogicaContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#expresionLogica}.
	 * @param ctx the parse tree
	 */
	void exitExpresionLogica(compiladorParser.ExpresionLogicaContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#logica}.
	 * @param ctx the parse tree
	 */
	void enterLogica(compiladorParser.LogicaContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#logica}.
	 * @param ctx the parse tree
	 */
	void exitLogica(compiladorParser.LogicaContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#listaAsignaciones}.
	 * @param ctx the parse tree
	 */
	void enterListaAsignaciones(compiladorParser.ListaAsignacionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#listaAsignaciones}.
	 * @param ctx the parse tree
	 */
	void exitListaAsignaciones(compiladorParser.ListaAsignacionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#iwhile}.
	 * @param ctx the parse tree
	 */
	void enterIwhile(compiladorParser.IwhileContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#iwhile}.
	 * @param ctx the parse tree
	 */
	void exitIwhile(compiladorParser.IwhileContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#iif}.
	 * @param ctx the parse tree
	 */
	void enterIif(compiladorParser.IifContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#iif}.
	 * @param ctx the parse tree
	 */
	void exitIif(compiladorParser.IifContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#ielse}.
	 * @param ctx the parse tree
	 */
	void enterIelse(compiladorParser.IelseContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#ielse}.
	 * @param ctx the parse tree
	 */
	void exitIelse(compiladorParser.IelseContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#ifor}.
	 * @param ctx the parse tree
	 */
	void enterIfor(compiladorParser.IforContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#ifor}.
	 * @param ctx the parse tree
	 */
	void exitIfor(compiladorParser.IforContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#forInit}.
	 * @param ctx the parse tree
	 */
	void enterForInit(compiladorParser.ForInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#forInit}.
	 * @param ctx the parse tree
	 */
	void exitForInit(compiladorParser.ForInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#forInc}.
	 * @param ctx the parse tree
	 */
	void enterForInc(compiladorParser.ForIncContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#forInc}.
	 * @param ctx the parse tree
	 */
	void exitForInc(compiladorParser.ForIncContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#listaContadores}.
	 * @param ctx the parse tree
	 */
	void enterListaContadores(compiladorParser.ListaContadoresContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#listaContadores}.
	 * @param ctx the parse tree
	 */
	void exitListaContadores(compiladorParser.ListaContadoresContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#prototipoDeFuncion}.
	 * @param ctx the parse tree
	 */
	void enterPrototipoDeFuncion(compiladorParser.PrototipoDeFuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#prototipoDeFuncion}.
	 * @param ctx the parse tree
	 */
	void exitPrototipoDeFuncion(compiladorParser.PrototipoDeFuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#declaracionDeFuncion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracionDeFuncion(compiladorParser.DeclaracionDeFuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#declaracionDeFuncion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracionDeFuncion(compiladorParser.DeclaracionDeFuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#llamadaFuncion}.
	 * @param ctx the parse tree
	 */
	void enterLlamadaFuncion(compiladorParser.LlamadaFuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#llamadaFuncion}.
	 * @param ctx the parse tree
	 */
	void exitLlamadaFuncion(compiladorParser.LlamadaFuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#retorno}.
	 * @param ctx the parse tree
	 */
	void enterRetorno(compiladorParser.RetornoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#retorno}.
	 * @param ctx the parse tree
	 */
	void exitRetorno(compiladorParser.RetornoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#parametro}.
	 * @param ctx the parse tree
	 */
	void enterParametro(compiladorParser.ParametroContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#parametro}.
	 * @param ctx the parse tree
	 */
	void exitParametro(compiladorParser.ParametroContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#parametros}.
	 * @param ctx the parse tree
	 */
	void enterParametros(compiladorParser.ParametrosContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#parametros}.
	 * @param ctx the parse tree
	 */
	void exitParametros(compiladorParser.ParametrosContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void enterArgumentos(compiladorParser.ArgumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void exitArgumentos(compiladorParser.ArgumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladorParser#llamadaFuncionInstruccion}.
	 * @param ctx the parse tree
	 */
	void enterLlamadaFuncionInstruccion(compiladorParser.LlamadaFuncionInstruccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladorParser#llamadaFuncionInstruccion}.
	 * @param ctx the parse tree
	 */
	void exitLlamadaFuncionInstruccion(compiladorParser.LlamadaFuncionInstruccionContext ctx);
}