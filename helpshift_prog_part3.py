'''
PS: Design an efficient program that picks the first N among an array of numbers representing customer ratings from -5 to 5 based on sentiment . Positive or Negative Sentiments are ranked higher than median/unbiased ones. eg: -4 should be sorted higher than 3; 2 sorted higher than -1; 5 is sorted higher than 4, and -5 is sorted higher than -4, etc. The array may be of any size < 100, will be un-sorted, and you need to pick only N.
Author: Krishnasagar S.
Dt. : 18th March 2016
'''

temp = raw_input('Enter sequence of customer ratings: ')
cust_ratings = [int(i) for i in temp.split(" ")]
n = len(cust_ratings)
N = int(raw_input('Enter N: '))

def eff_sort2(cr):
    '''
    Input: cr - array customer ratings of variable size
    Return: cr - sorted customer ratings array
    Reference: https://en.wikipedia.org/wiki/Timsort
    '''
    sortedcr = sorted(cr)
    crLen = len(cr)
    i = (crLen - 1)/2
    med = 0
    if crLen % 2 == 0:
        med = sortedcr[i]
    else:
        med = (sortedcr[i] + sortedcr[i + 1])/2.0
    cr_list = [(i, abs(med-abs(i))) for i in cust_ratings] #distance from median calculation.
    res = sorted(cr_list, key=lambda r: r[1]) #sort based on distance from median
    cr = [i[0] for i in res]
    return cr

def eff_sort1(cr):
    '''
    Input: cr - array customer ratings of variable size
    Return: cr - sorted customer ratings array
    '''
    for i in range(len(cr)):
        for j in range(i+1, len(cr)):
            if abs(cr[i]) > abs(cr[j]):
                temp = cr[i]
                cr[i] = cr[j]
                cr[j] = temp
            #this condition is enabled if absolute ratings same but positive value > negative value
            if abs(cr[i]) == abs(cr[j]) and cr[i] > cr[j]: 
                temp = cr[i]
                cr[i] = cr[j]
                cr[j] = temp
    return cr

#cr = eff_sort1(cust_ratings) #1st solution
'''efficiency n*(n-2)/2 best case O(n), worst case O(n^2) average case O(n^2)
pros - a systematic way for same level sentiment ratings from median negative rating to positive rating
cons - efficiency fails at worst case.'''
cr = eff_sort2(cust_ratings) # more efficient 2nd solution.
'''This is because of using hybrid sort(adaptive insertion and merge sort) - best case O(n), worst case and average case O(n*logn)
pros - efficiency survives at worst case.
'''

print cr
if N > n:
    print cr
else:
    print cr[n-N:]
