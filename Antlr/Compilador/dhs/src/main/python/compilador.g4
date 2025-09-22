grammar compilador;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;
PA : '(' ;
PC : ')' ;
LLA : '{' ;
LLC : '}' ;
PYC : ';' ;
ASIG : '=' ;
CA : '[' ;
CC : ']' ;
SUMA : '+' ;
RESTA : '-' ;
MULT : '*' ;
DIV : '/' ;
COMA : ',' ;
MENOR : '<' ;
MAYOR : '>' ;
MENORIGUAL : '<=' ;
MAYORIGUAL : '>=' ;
IGUAL : '==' ;
DIFERENTE : '!=' ;
//Fragmentes para definir partes de tokens que no se usan directamente

NUMERO : ('+' | '-')? DIGITO+ ;
INT : 'int' ;
DOUBLE : 'double' ;
IF : 'if' ;
ELSE : 'else' ;
FOR : 'for' ;
WHILE : 'while' ;
RETURN : 'return' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;
WS : [ \t\r\n] -> skip ;
OTRO : . ;
programa : instrucciones EOF ;

instrucciones : instruccion instrucciones 
              |
              ;
tipo : INT
     | DOUBLE
     ;
//Aritmetica 
opal : exp  
     ;

//Sumatoria de cosas
exp  : term  e ;

e    : SUMA term e
     | RESTA term e
     |  
     ;
//Producto de cosas
//estamos cumpliendo con la precedencia de operadores
term : factor t ;

t    : MULT factor t
     | DIV factor t
     |   
     ;

//falta agregar llamada a funcion!!
//ademas, la resta y la division van a salir mal cuando
//volvemos del arbol
factor : PA exp PC
       | ID
       | NUMERO
       ;






     


codigo : NUMERO ;

declaracion : tipo listaDeclaradores PYC ;

listaDeclaradores : declarador (COMA declarador)* ;

declarador : ID
           | ID ASIG opal
           ;
listaAsignaciones : asignacion (COMA asignacion)* //Eto no ta bueno
                 |
                 ;


listaContadores : contador (COMA contador)* //Eto no ta bueno
                |
                ;

contador : ID SUMA
         | ID RESTA
         | ID ASIG opal
         ;

     
bloque : LLA instrucciones LLC ;
comparacion : opal (SUMA | RESTA | MULT | DIV) opal ;
instruccion:  asignacion PYC
           |  declaracion
           |  retorno
           |  sumar
           |  restar
           |  iwhile
           |  bloque
           |  iif
           |  ifor
           ;

iwhile : WHILE PA opal PC instruccion  ;
iif : IF PA opal PC instruccion ielse ;
ielse : ELSE instruccion
      | 
      ;
//declaracion : tipo ID PYC ;
asignacion : ID ASIG opal;
retorno : RETURN codigo PYC ;
sumar : ID ASIG ID SUMA opal PYC ;
restar : ID ASIG ID RESTA opal PYC ;





//Implementacion de for:
ifor : FOR PA forInit PYC forCond PYC forInc PC bloque  ;

forInit : listaAsignaciones
         |  
         ;

forCond : comparacion
         |  
         ;

forInc: listaContadores
       |  
       ;




//Analizador sintactico descendente: desde raiz hasta las hojas.
//s:s(s)s
// |
//Internamente se arma una tabla donde se arranca con el simbolo inciial y del otro lado la entrada.
//$s      (())()$
//D -> derivar (Deriva desde el simbolo inicial)
//M -> match
//$s      (())()$D
//$s)s(   (())()$M
//$s)s    ())()$D
//$s)s)s( ())()$M
//$s)s)s  ))()$D
//$s)s)    ))()$M
//$s)s     )()$D
//$s)      )()$M
//$s       ()$D
//$s)s)       ()$M
//$s        $D
//$         $ (Fin de cadena)