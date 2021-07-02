
import statistics
N = int(input())
X,Y = [], []
for n in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
x_med = statistics.median(X)
y_med = statistics.median(Y)
# print(x_med, y_med)
print( int(sum([abs(x-x_med) for x in X]) + sum([abs(y-y_med) for y in Y]) ))
