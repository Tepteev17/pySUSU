LETTERS = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"


def is_left_parenthesis():
    return sym == '('


def is_right_parenthesis():
    return sym == ')'


def is_digit():
    return sym in DIGITS


def is_letter():
    return sym in LETTERS


def next():
    global s, m, sym, is_error
    m = m + 1
    if m == len(s):
        if sym in '(+-*/':
            is_error = True
            return
    try:
        sym = s[m]
    except IndexError:
        pass


def init():
    global s, m, sym, is_error
    s = input()
    m = 0
    sym = s[m]
    is_error = False


def recognize():
    if s != "":
        expression()
    if (not is_error) and s != "" and (m == len(s)):
        return "Correct"
    return "Incorrect"


def expression():
    global is_error
    if is_letter() or is_digit() or is_left_parenthesis():
        addend()
        while sym == '+' or sym == "-":
            next()
            addend()
            if m == len(s):
                return
    else:
        is_error = True


def addend():
    global is_error
    if is_letter() or is_digit() or is_left_parenthesis():
        factor()
        while sym == '*' or sym == '/':
            next()
            factor()
            if m == len(s):
                return
    else:
        is_error = True


def factor():
    global is_error
    if is_letter():
        next()
    else:
        if is_digit():
            number()
        else:
            if is_left_parenthesis():
                next()
                if is_error:
                    return
                expression()
                if is_right_parenthesis():
                    next()
                else:
                    is_error = True
            else:
                is_error = True


def number():
    while is_digit():
        next()
        if m == len(s):
            return


init()
print(recognize())

# tests

# a+b-c;            Correct;    Correct
# (a*b)+c;          Correct;    Correct
# a/(b+c);          Correct;    Correct
# (a+(b*c))-d;      Correct;    Correct
# (a+b*c)-d;        Correct;    Correct
# 3*x+2*y-z;        Correct;    Correct
# (x+y)*(z-1);      Correct;    Correct
# (3+4)*5/6;        Correct;    Correct
# a-(b/(c*d));      Correct;    Correct
# a-(b/c*d);        Correct;    Correct
# a-b/c*d;          Correct;    Correct
# (7-(x*2))+5;      Correct;    Correct
# (p/q)-(r*s)+t;    Correct;    Correct
# p/q-r*s+t;        Correct;    Correct
# a+*b;             Incorrect;  Incorrect
# (a+b));           Incorrect;  Incorrect
# c-*d;             Incorrect;  Incorrect
# *a+b;             Incorrect;  Incorrect
# (3+4)*5/6+;       Incorrect;  Incorrect
# a-/b;             Incorrect;  Incorrect
# p/q)-r*s+t;       Incorrect;  Incorrect
# (a+b)*c-d/e;      Correct;    Correct
# x*(y+z)-(a/b);    Correct;    Correct
# 5+(6*7)-8/9;      Correct;    Correct
# (1+2)*(3-4)/5;    Correct;    Correct
# z+(x*y)-(w/v);    Correct;    Correct
# (m-n)*(o/p)+q;    Correct;    Correct
# 3*(4+5)-6/(7-8);  Correct;    Correct
# (a+b*c;           Incorrect;  Incorrect
# d/e-);            Incorrect;  Incorrect
# (f+g)-*h;         Incorrect;  Incorrect
