# CptS 355 - Fall 2020 - Assignment 3
# Please include your name and the names of the students with whom you discussed any of the problems in this homework
import functools
from functools import reduce
CDCdata = { 'King':{'Mar':2706,'Apr':3620,'May':1860,'Jun':2157,'July':5014,'Aug':4327,'Sep':2843},
            'Pierce':{'Mar':460,'Apr':965,'May':522,'Jun':647,'July':2470,'Aug':1776,'Sep':1266},
            'Snohomish':{'Mar':1301,'Apr':1145,'May':532,'Jun':568,'July':1540,'Aug':1134,'Sep':811},
            'Spokane':{'Mar':147,'Apr':222,'May':233,'Jun':794,'July':2412,'Aug':1530,'Sep':1751},
            'Whitman' : {'Apr':7,'May':5,'Jun':19,'July':51,'Aug':514,'Sep':732, 'Oct':278} }

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




## problem 1-b) getMonthlyCases - 15%


## problem 1-c) mostCases - 15%


## problem 2a) searchDicts(L,k) - 5%
def searchDicts(L, k):
    count = 0
    i = -1  # starts at end
    while count < len(L):
        if L[i].get(k, None) is None:
            i -= 1
            count += 1
        else:
            return L[i].get(k, None)

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



## problem 4 - getLongest - 10%


## problem 5 - apply2nextN - 20%


if __name__ == '__main__':
     getNumCases(CDCdata, ['Whitman'], ['Apr', 'May', 'Jun'])
