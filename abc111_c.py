
n = int(input())

vs = [int(v) for v in input().split()]


evens = [ v for index, v in enumerate(vs) if index%2 == 0 ]
odds  = [ v for index, v in enumerate(vs) if index%2 == 1 ]

#print(evens)
#print(odds)

from collections import Counter
even_most_freq = sorted( dict(Counter(evens)).items(), key=lambda x:x[1] )[-1][0]
odd_most_freq  = sorted( dict(Counter(odds)).items(), key=lambda x:x[1] )[-1][0]

#print(even_most_freq, odd_most_freq)
if even_most_freq != odd_most_freq:
    count_evens = sum( [1 for x in evens if x != even_most_freq] )
    count_odds = sum( [1 for x in odds if x != odd_most_freq] )
    print( count_evens + count_odds)
else:
    maxed = min( [len(evens), len(odds)] ) 
    count_evens = sum( [1 for x in evens if x != even_most_freq] )
    count_odds = sum( [1 for x in odds if x != odd_most_freq] )
    print( count_evens + count_odds + maxed)

