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
// Token definitions for parentheses

//s : ID     {print("ID ->" + $ID.text + "<--") }         s
//  | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
//  | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
//  | EOF
//  ;

//  s : PA s PC s
//    |
//    ;

programa : instrucciones EOF ;

instrucciones : instruccion instrucciones 
              | /* Esto es la recursividad */ 
              ;
tipo : INT
     | DOUBLE
     ;
opal : NUMERO 
     | ID 
     ;
codigo : NUMERO ;
bloque : LLA instrucciones LLC ;
instruccion:  asignacion 
           |  declaracion
           |  retorno
           |  sumar
           |  restar
           |  iwhile
           |  bloque
           |  iif
           ;

iwhile : WHILE PA opal PC instruccion  ;
iif : IF PA opal PC instruccion ielse ;
ielse : ELSE instruccion
      | 
      ;
declaracion : tipo ID PYC ;
asignacion : ID ASIG opal PYC;
retorno : RETURN codigo PYC ;
sumar : ID ASIG ID SUMA opal PYC ;
restar : ID ASIG ID RESTA opal PYC ;
















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