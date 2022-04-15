'''There is an array with some numbers. All numbers are equal except for one.'''

from collections import Counter
def find_uniq(arr):
    result = 0
    ilosc = Counter(arr)
    for k,v in ilosc.items():
        if v == 1:
            result += k

    return print(result)

find_uniq([ 0, 0, 0.55, 0, 0 ])