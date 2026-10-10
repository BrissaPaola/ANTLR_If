grammar Cond1;

prog: stat+ EOF ;

stat: 'if' cond stat ('else' stat)?   # IfStat
    | 'imprime' expr                  # PrintStat
    ;

cond: expr op=('<'|'>') expr ;

expr: expr op=('*'|'/') expr   # MulDiv
    | expr op=('+'|'-') expr   # AddSub
    | INT                       # Int
    | '(' expr ')'              # Parens
    ;

INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
