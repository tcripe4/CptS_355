# WRITE YOUR NAME and YOUR COLLABORATORS HERE

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in Python is a no-op: replace it with your code.

def opPop():
    if (len(opstack) > 0):
        return opstack.pop(-1)
    else:
        print("ERROR in opstack")
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

#-------------------------- 16% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():

    if len(dictstack) > 0:
        return dictstack.pop(-1)
    else:
        print("ERROR dictPop(): zero elements in dictstack")
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)

def define(name, value):
    newd = {}
    newd[name] = value
    dictPush(newd)
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and

def lookup(name):
    newname = "/"+name
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
    # return the value associated with name


#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, eq, lt, gt 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if (isinstance(op1, int) and isinstance(op2, int)):
            opPush(op1 + op2)
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
        if (isinstance(x, int) and isinstance(y, int)):
            opPush(x * y)
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

#--------------------------- 20% -------------------------------------
# String operators: define the string operators length, get, getinterval,  putinterval, search
def length():
    if len(opstack) > 0:
        str = opPop()
        length = len(str)
        if str[0] == '(':
            if str[-1] == ')':
                length = length -2
        opPush(length)
    else:
        print("ERROR length(): zero elements on opstack")

def get():
    if len(opstack) > 1:
        index = opPop()
        str = opPop()
        new = ''
        for x in str:
            if x != '(':
                if x != ')':
                    new += x
        print(ord(new[index]))
        opPush(ord(new[index]))
    else:
        print("ERROR get(): zero elements on opstack")

def getinterval():
    if len(opstack) > 0:
        count = opPop()
        index = opPop()

        str = opPop()
        if str[0] == "(" and str[-1] == ")":
            str = str[1:-1]
        if str[0] == "[" and str[-1] == "]":
            str = str[1:-1]
            index = index * 2
            count = count * 2
        newstr = str[index:index + count]
        newstr = '(' + newstr + ')'
        opPush(newstr)
    else:
        print("ERROR getinterval(): zero elements on opstack")

def putinterval():
    if len(opstack) > 0:
        new = []
        count = opPop()
        index = opPop()
        str = opPop()
        str2 = opPop()
        print("count, index, str")
        print(count, index, str)

        new = ''
        for x in count:
            if x != '(':
                if x != ')':
                    new += x
        print("printing new ", new)

        part1 = str[:(index + 1)]
        print("printing part1 ", part1)

        part1 += new
        num = len(count)
        print("part1 2 ", part1)

        index += num
        index -= 1
        part1 += str[index:]
        print("opstack ", opstack)
        print("part1 3 ", part1)


        opPush(part1)
        print("dictstack ", dictstack)
        print("opstack ", opstack)

    else:
        print("ERROR putinterval(): zero elements on opstack")


def search():
    if len(opstack) > 0:
        new = ''
        old = ''
        index_num = 0
        split = opPop()
        str_split = ''
        string = opPop()
        for x in split:
            if x != '(':
                if x != ')':
                    str_split += x
        if str_split in string:
            index_num = str(string).index(str_split)
            new = string[:index_num] + ')'
            old = '(' + string[index_num + 1:]
            opPush(old)
            opPush(split)
            opPush(new)
            opPush(True)
        else:
            opPush(string)
            opPush(False)
            print("Delimiter not found!")


#--------------------------- 18% -------------------------------------
# Array functions and operators:
#      define the helper function evaluateArray
#      define the array operators aload, astore

def evaluateArray(aInput):
    functions = {"add": add, "sub": sub, "mul": mul, "eq": eq, "lt": lt, "gt": gt, "length": length, "count": count,
                 "get": get, "putinterval": putinterval, "getinterval": getinterval, "dup": dup,
                 "copy": copy, "pop": pop, "clear": clear, "exch": exch, "dict": psDict, "begin": begin,
                 "end": end, "def": psDef, "seach": search}
    new = []
    for each in aInput:
        if isinstance(each, str):
            if each in functions.keys():
                call = functions[each]
                call()
            elif lookup(each) is not None:
                token1 = lookup(each)
                if token1 is not None:
                    opPush(token1)
            else:
                opPush(each)
        else:
           opPush(each)
        print(opstack)

    return opstack
    #should return the evaluated array

def aload():
    new = opPop()
    for x in new:
        opPush(x)
    opPush(new)
    print(opstack)

def astore():
    print(opstack)
    new = opPop()
    num = 0
    count = len(new)
    new_arr = []
    while num < count:
        new_arr.insert(0, opPop())
        num += 1
    opPush(new_arr)
    print(opstack)

#--------------------------- 6% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, stack
def dup():
    if len(opstack) > 0:
        x = opPop()
        opPush(x)
        opPush(x)
    else:
        print("ERROR dup(): zero elements on opstack")

def copy():
    if len(opstack) > 0:
        x = opPop()
        help1 = []
        help2 = []
        if x > len(opstack):
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

def count():
    pass

def pop():
    def pop():
        if len(opstack) > 0:
            return opPop()
        else:
            print("ERROR pop(): zero elements on opstack")

def clear():
    global opstack
    opstack = []

def exch():
    if len(opstack) > 0:
        x = opPop()
        y = opPop()
        opPush(x)
        opPush(y)
    else:
        print("ERROR exch(): zero elements on opstack")

def stack():
    pass

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.
def psDict():
    opPop()
    opPush({})

def begin():
    d = opPop()
    if type(d) is dict:
        dictPush(d)
    else:
        print("begin() ERROR: element not of dictionary type")

def end():
    dictPop()

def psDef():
    if len(opstack) > 0:
        val = opPop()
        name = opPop()
        define(name, val)
    else:
        print("ERROR psDef(): zero elements on opstack")
