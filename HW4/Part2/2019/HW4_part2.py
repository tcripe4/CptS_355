import re
import ast

# Travis Cripe 11519554 HW4 Part 2

opstack = []

def opPop():
    if (len(opstack) > 0):
        return opstack.pop(-1)
    else:
        print("ERROR in opstack")

def opPush(value):
    # print("Inside of opPush: ", value)
    opstack.append(value)
    # print("current stack: ", opstack)

dictstack = []

def dictPop():
    if len(dictstack) > 0:
        return dictstack.pop(-1)
    else:
        print("ERROR dictPop(): zero elements in dictstack")

def dictPush(d):
    dictstack.append(d)

def define(name, value):
    if len(dictstack) == 0:
        dictPush({})
    top = dictstack[-1]
    name = str(name)
    if len(name) > 1 and name[0] == '/':
        top[name[1:]] = value
    else:
        print("Error: invalid variable name")
    # print("current dictstack: ", dictstack)
    #newd = {}
    #newd[name] = value
    #dictPush(newd)

def lookup(name):
    newname = name
    new = None
    if len(dictstack) == 0:
        print("ERROR lookup(): dictstack empty")
    else:
        for item in dictstack:
            if newname in item:
                new = item[newname]
            else:
                continue
    return new

def add():
    if len(opstack) > 1:
        op2 = opPop()
        # print("add op2: ", op2)
        op1 = opPop()
        # print("add op1: ", op1)
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1+op2)
        else:
            print("Error: add - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: add expects 2 operands")

def sub():
    if len(opstack) > 0:
        x = opPop()
        y = opPop()
        if (isinstance(x, int) and isinstance(y, int)):
            opPush(y - x)
    else:
        print("ERROR sub(): zero elements on opstack")

def mul():
    if len(opstack) > 0:
        x = opPop()
        y = opPop()
        #if x.isdigit():
         #   x = int(x)
        #if y.isdigit():
         #   y = int(y)
        if (isinstance(x, int) and isinstance(y, int)):
            opPush(x * y)
            # print("inside mul: ", x * y)
    else:
        print("ERROR mul(): zero elements on opstack")

def eq():
    if len(opstack) > 0:
        x = opPop()
        y = opPop()
        if x == y:
            opPush(True)
        else:
            opPush(False)
    else:
        print("ERROR eq(): zero elements on opstack")

def lt():
    if len(opstack) > 0:
        x = opPop()
        y = opPop()
        if x < y:
            opPush(False)
        else:
            opPush(True)
    else:
        print("ERROR lt(): zero elements on opstack")

def gt():
    if len(opstack) > 0:
        x = opPop()
        y = opPop()
        if x > y:
            opPush(False)
        else:
            opPush(True)
    else:
        print("ERROR gt(): zero elements on opstack")

def psAnd():
    if len(opstack) > 0:
        x = opPop()
        y = opPop()
        if (isinstance(x, bool) and isinstance(y, bool)):
            if x == y:
                opPush(True)
            else:
                opPush(False)
    else:
        print("ERROR psAnd(): zero elements on opstack")

def psOr():
    if len(opstack) > 0:
        x = opPop()
        y = opPop()
        if (isinstance(x, bool) and isinstance(y, bool)):
            if x != y:
                opPush(True)
            elif x == y:
                if x == True:
                     opPush(True)
                else:
                    opPush(False)
    else:
        print("ERROR psOr(): zero elements on opstack")
def psNot():
    if len(opstack) > 0:
        x = opPop()
        if (isinstance(x, bool)):
            if x == True:
                opPush(False)
            else:
                opPush(True)
    else:
        print("ERROR psNot(): zero elements on opstack")

def length():
    if len(opstack) > 0:
        str = opPop()
        length = len(str)
        opPush(length)
    else:
        print("ERROR length(): zero elements on opstack")

def get():
    # print("Get(): opstack: ", opstack)
    if len(opstack) > 0:
        index = opPop()
        # print("get index: ", index)
        str = opPop()
        # print("get str:", str)
        opPush(str[index])
    else:
        print("ERROR get(): zero elements on opstack")

def getinterval():
    if len(opstack) > 0:
        count = opPop()
        # print("printing count", count)
        index = opPop()
        # print("printing index", index)

        str = opPop()
        if str[0] == "(" and str[-1] == ")":
            str = str[1:-1]
        if str[0] == "[" and str[-1] == "]":
            str = str[1:-1]
            index = index * 2
            count = count * 2
        newstr = str[index:index+count]
        # print("printing new string", newstr)
        opPush(newstr)
    else:
        print("ERROR getinterval(): zero elements on opstack")

def putinterval():
    if len(opstack) > 2:
        substitute = opPop()
        index = opPop()
        list = opPop()
        list[index:index+len(substitute)] = substitute
    else:
        print("Error: opstack of size is too small")
    #if len(opstack) > 0:
        # print("inside putinterval")
    #    str = opPop()
    #    index = opPop()
    #    index = index * 2
    #    num = len(str)
    #    new = opPop()
    #    part1 = new[:index]
        # print("part1: ", part1)
    #    num += index
        #        new.append(str[:index])
    #    part1 += " "
    #    part1 += str
    #    last = len(new)
    #    part1 += new[num + 1:last]
    #    print(part1)
    #    opPop() #take off dup from stack
    #    new_l = part1
    #    if not isinstance(part1, list):
    #        new_l = list(part1.strip('[]').split(" "))
    #    newL = [int(i) for i in new_l]
        # print("new_l: ", newL)

        #opPush(newL)
    #else:
        #print("ERROR putinterval(): zero elements on opstack")

def put():
    if len(opstack) > 0:
        value = opPop()
        index = opPop()
        array = opPop()
        if isinstance(index, int) and isinstance(array, list):
            array[index] = value
    else:
        print("ERROR put(): zero elements on opstack")

def dup():
    if len(opstack) > 0:
        x = opPop()
        # print("dup: ", x)
        opPush(x)
        opPush(x)
    else:
        print("ERROR dup(): zero elements on opstack")

def copy():
    if len(opstack) > 0:
        x = opPop()
        help1 = []
        help2 = []
        print("x = ", x)
        if not isinstance(x, int) or x > len(opstack):
            print("ERROR copy(): value greater than stack")
        else:
            for n in range(x):
                val = opPop()
                help1.append(val)
                help2.append(val)
            for n in range(x):
                val = help1.pop(-1)
                opPush(val)
            for n in range(x):
                val = help2.pop(-1)
                opPush(val)
    else:
        print("ERROR copy(): zero elements on opstack")

def pop():
    if len(opstack) > 0:
        return opPop()
    else:
        print("ERROR pop(): zero elements on opstack")

def clear():
    opstack.clear()

def exch():
    if len(opstack) > 0:
        x = opPop()
        y = opPop()
        opPush(x)
        opPush(y)
    else:
        print("ERROR exch(): zero elements on opstack")

def mark():
    opPush('-mark-')

def cleartomark():
    count = 0
    temp = []
    num = opstack.__len__()
    num -= 1
    while num >= 0:
        temp.append(opPop())
        num -= 1
    num = temp.__len__()
    num -= 1
    index = 0
    while temp[index] != '-mark-':
        index += 1
    num = temp.__len__()
    num -= 1
    while num > index:
        opPush(temp[num])
        num -= 1


def counttomark():
    count = 0
    temp = []
    num = opstack.__len__()
    num -= 1
    while num >= 0:
        temp.append(opPop())
        num -= 1
    for x in temp:
        if x != '-mark-':
            count += 1
        if x == '-mark-':
            num = temp.__len__()
            num -= 1
            while num >= 0:
                opPush((temp[num]))
                num -= 1
            opPush(count)
            return

# takes the initial size of the dict from the stack and puts a new empty
# dict on the opstack
def psDict():
    opPop()
    opPush({})

# takes a dict from top of opstack and pushes onto the dictstack
def begin():
    if len(opstack) > 0:
        d = opPop()
        if type(d) is dict:
            dictPush(d)
        else:
            opPush(d)
            print("begin() ERROR: element not of dictionary type")
    else:
        print("opstack is empty!")

# pop the top dict from dictstack and throw it away
def end():
    if len(opstack) > 0:
        dictPop()
    else:
        print("Dictstack is already empty!")
    #dictPop()

def psDef():
    if len(opstack) > 1:
        val = opPop()
        name = opPop()
        define(name, val)
    else:
        print("ERROR psDef(): zero elements on opstack")

def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    # print(it)
    for c in it:
        if c == '}':
            return {'codearray': res}
        elif c == '{':
    # Note how we use a recursive call to group the tokens inside the # inner matching parenthesis.
    # Once the recursive call returns the code-array for the inner
    # parenthesis, it will be appended to the list we are constructing # as a whole.
            res.append(groupMatch(it))
        else:
            res.append(convertion(c))
    return False


def convertion(c):
    # print(c)
    if c == 'true':
        ret = True
    elif c == 'false':
        ret = False
    elif c.isdigit() or c[0] == '-' and c[1:].isdigit():
        ret = int(c)
    elif c[0] == '[' and c[-1] == ']':
        ret = []
        for each in c[1:-1].split(' '):
            if each.isdigit() or (each[0] == '-' and each[1:].isdigit()):
                ret.append(int(each))
            elif each == 'true':
                ret.append(True)
            elif each == 'false':
                ret.append(False)
            else:
                ret.append(each)
    else:
        ret = c
    return ret

def count():
    opPush(len(opstack))

# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c == '}': #non matching closing parenthesis; return false since there is # a syntax error in the Postscript code.
            return False
        elif c == '{':
            res.append(groupMatch(it))
        else:
            res.append(convertion(c))
    return {'codearray':res}

# COMPLETE THIS FUNCTION 
# This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them. 
def interpretSPS(code): # code is a code array
    functions = {"add": add, "sub": sub, "mul": mul, "eq": eq, "lt": lt, "gt": gt, "length": length, "count":count,
                 "get": get, "putinterval": putinterval, "getinterval": getinterval, "put": put, "dup": dup, "copy": copy, "pop": pop,
                 "clear": clear, "exch": exch, "dict": psDict, "begin": begin, "or": psOr, "not": psNot,
                 "end": end, "def": psDef, "if": psIf, "ifelse": psIfelse, "repeat": repeat, "forall": forAll, 'and':psAnd}

    # print("code: ", code)
    # print("code type: ", type(code))
    if isinstance(code, dict):
        arr = code["codearray"]
    else:
        arr = code

    for each in arr:
        if isinstance(each, str) and each[0] != "/":
            print("opstack: ", opstack)
            if each in functions.keys():
                call = functions[each]
                call()
            elif lookup(each) is not None:
                token1 = lookup(each)
                if token1 is not None:
                    if isinstance(token1, dict):
                        interpretSPS(token1)
                    else:
                        opPush(token1)
            else:
                opPush(each)
        else:
            opPush(each)

# if the condition arg is true, first code-array is interpreted, otherwise the
# second code-array is evaluated
def psIfelse():
    if len(opstack) != 0:
        code2 = opPop()
        code1 = opPop()
        boolobj = opPop()
        if isinstance(boolobj,bool):
            if boolobj is True:
                interpretSPS(code1)
            else:
                interpretSPS(code2)
    else:
        print("ERROR psIfelse(): opstack is empty")

def psIf():
    if len(opstack) != 0:
        code = opPop()
        boolobj = opPop()
        if boolobj is True:
            interpretSPS(code)
    else:
        print("ERROR psIf(): opstack is empty")


def repeat():
    if len(opstack) > 1:
        code = opPop()
        num = opPop()
        for _ in range(num):
            interpretSPS(code)


def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))


#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []

# <array> <procedure> forall
# Postscript defines a forall operator that takes an array and a procedure as
# # operands. The procedure is performed on each member of the array.
def forAll():
    if len(opstack) > 1:
        print("forall opstack: ", opstack)
        procedure = opPop()
        array = opPop()
        mark()
        interpretSPS(array)
        a = opPop()
        temp = []
        while (a != '-mark-'):
            temp.append(a)
            a = opPop()
        temp.reverse()
        array = temp
        for value in array:
            opPush(value)
            interpretSPS(procedure)