# CptS 355 - Fall 2020 - Assignment 3
# Please include your name and the names of the students with whom you discussed any of the problems in this homework

import total as total

CDCdata = { 'King':{'Mar':2706,'Apr':3620,'May':1860,'Jun':2157,'July':5014,'Aug':4327,'Sep':2843},
            'Pierce':{'Mar':460,'Apr':965,'May':522,'Jun':647,'July':2470,'Aug':1776,'Sep':1266},
            'Snohomish':{'Mar':1301,'Apr':1145,'May':532,'Jun':568,'July':1540,'Aug':1134,'Sep':811},
            'Spokane':{'Mar':147,'Apr':222,'May':233,'Jun':794,'July':2412,'Aug':1530,'Sep':1751},
            'Whitman' : {'Apr':7,'May':5,'Jun':19,'July':51,'Aug':514,'Sep':732, 'Oct':278} }



L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]

L2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}),
(1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]

debugging = False
def debug(*s):
     if debugging:
          print(*s)

## problem 1-a) getNumCases - 10%
def getNumCases(data,counties,months):
        total = 0
        for (key,lildict) in data.items(): ## going through the counties
            if key in counties: ## checking if county in list is in given ones
                for (k,v) in lildict.items(): ## going through the months
                       if k in months:
                          total += v
        print(total)
        return total



## problem 1-b) getMonthlyCases - 15%
def getMonthlyCases(data):
    new = {}
    for (bigkey,lildict) in data.items():
        for (k,v) in lildict.items():
            if k in new.keys():
                new[k][bigkey] = v
            else:
                new[k] = {}
                new[k][bigkey] = v
  ##  print(new)
    return new

## problem 1-c) mostCases - 15%
# This is basically impossible. This questions sucks
def mostCases(data):
    from functools import reduce
    d = getMonthlyCases(data)
    #returned_value = list(reduce(lambda a, b: a+b, d.items()))
    #print(returned_value)

   # lildict = list(d.values())
   # print(lildict)

   # blah = list(reduce(lambda x, y: (y for x,y in d.items()), d))
    #sum1 = reduce(lambda x, y: x + y, blah)

   # print(blah)

    maxtotal = ('none',0)
    for (month, lildict) in d.items():
        maxmonth = 0
        for (county,num) in lildict.items():
            maxmonth += num
        if maxmonth > maxtotal[1]:
            maxtotal = (month, maxmonth)
    print(maxtotal)
    return(maxtotal)




## problem 2a) searchDicts(L,k) - 5%
def searchDicts(L, k):
    count = 0
    i = -1  # starts at end
    while count < len(L):
        if L[i].get(k, None) is None:
            i -= 1
            count += 1
        else:
            return print(L[i].get(k, None))

## problem 2b) searchDicts2(L,k) - 10%
# helper func for searchDicts2()
def nextIndex(tL, k, index):
    tLsub = tL[index]
    d = tLsub[1]
    length = len(d.values())
    newIndex = tLsub[0]
    for (key, value) in d.items():
        if key == k:
            return value
        else:
            continue
    if newIndex == index:
        return None
    return nextIndex(tL, k, newIndex)

def searchDicts2(tL, k):
    size = len(tL) - 1
    return nextIndex(tL, k, size)

## problem 3 - adduptoZero - 10%

def adduptoZero(L,n):
    from itertools import combinations
    new = []
    d = combinations(L, n)
    y = list(d)
    for i in y:
       x = 0
       for j in i:
            x += j
       if (x == 0):
           new.append(list(i))
    print(new)




## problem 4 - getLongest - 10%
def flatt(list1, tem):
    for x in list1:
        if type(x) == list:
            flatt(x, tem)
        else:
            tem.append(x)

def getLongest (L):
    longest = ""
    temp = []
    flatt(L, temp)
    return max(temp)



## problem 5 - apply2nextN - 20%
# Create an iterator that represents the aggregated sequence of values from
# an input iterator. The iterator will be initialized with a combining function (op),
# an integer value (n) , and an input iterator (input). When the iterator’s __next__()
# method is called, it will combine the next “n” values in the “input“ by applying
# the “op” function and it will return the combined value. The iterator should stop
# when it reaches the end of the input sequence. If the input sequence is infinite,
# the apply2nextN will return an infinite sequence as well.
class apply2nextN ():
    def __init__(self, op, n, input):
        self.operator = op
        self.num = n
        self.inputs = input
        self.check = []
        self.current = self.inputs.__next__()
        result = self.current
        try:
            while self.inputs:
                x = 0
                while x < self.num - 1:
                    yeet = self.inputs.__next__()
                    result = self.operator(result, yeet)
                    x += 1
                self.check.append(result)
                result = self.inputs.__next__()
        except:
            if result:
                self.check.append(result)
            self.current = None

    def __next__(self):
        try:
            if self.check is None:
                raise StopIteration
            result = self.check.pop(0)
            return result

        except:
            raise StopIteration
    def __iter__(self):
        return self



if __name__ == '__main__':
    mostCases(CDCdata)