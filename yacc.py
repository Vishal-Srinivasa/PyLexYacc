from ply import yacc

from lex_python import tokens

def p_statement(p):
    '''
    statement : if 
        | while 
        | try_except 
        | assignment 
        | function 
        | print
        | statement SEMICOLON statement
        | statement SEMICOLON
    '''

def p_print(p):
    '''
    print : PRINT LPAREN parameter_list RPAREN
        | PRINT LPAREN RPAREN
    parameter_list : parameter COMMA parameter_list
        | parameter
    parameter : expression
        | IDENTIFIER
    
    '''

def p_if(p):
    '''
    if : IF conditionif COLON statement
    conditionif : LPAREN expression RPAREN 
        | expression
    '''

def p_while(p):
    '''
    while : WHILE conditionw COLON statement
    conditionw : LPAREN expression RPAREN 
        | expression
    '''

def p_try_except(p):
    '''
    try_except : TRY COLON statement EXCEPT COLON statement
    '''

def p_assignment(p):
    '''
    assignment : IDENTIFIER ASSIGNMENT expression
    '''

def p_function(p):
    '''
    function : DEF IDENTIFIER LPAREN func_parameters RPAREN COLON statement 
        | DEF IDENTIFIER LPAREN RPAREN COLON statement
    func_parameters : IDENTIFIER COMMA func_parameters 
        | IDENTIFIER
    '''

def p_expression_w_logical(p):
    '''
    expression : expression_1 
        | expression AND expression 
        | expression OR expression 
        | NOT expression
    '''

def p_expression_w_comparisson(p):
    '''
    expression_1 : expression_2 
        | expression_1 COMPARISON expression_1
    '''

def p_expression(p):
    '''
    expression_2 : expression_2 PLUS term 
        | expression_2 MINUS term 
        | term
    '''

def p_term_(p):
    '''
    term : term TIMES factor 
        | term DIVIDE factor 
        | factor
    '''

def p_factor(p):
    '''
    factor : NUMBER 
        | LPAREN expression RPAREN
    '''


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

while True:
    multiline_s = ''
    error = 0
    try:
        i = 1
        while True:
            s = input('>')
            if s == "quit()":
                break
            i += 1
            if multiline_s == '':
                multiline_s = s
            else:
                multiline_s = multiline_s + '\n' + s
        s1 = multiline_s
        print(multiline_s)
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(multiline_s, tracking=True)
    print(result)