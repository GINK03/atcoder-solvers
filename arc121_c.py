

def m(inp_arr):
    inp_arr = [(x, i ) for i,x in enumerate(inp_arr)]
    cnt = [0, 0]
    buff = [[], [] ]
    def merge_sort(inp_arr):
        #global cnt, buff
        size = len(inp_arr)
        if size > 1:
            middle = size // 2
            left_arr = inp_arr[:middle]
            right_arr = inp_arr[middle:]
     
            merge_sort(left_arr)
            merge_sort(right_arr)
     
            p = 0
            q = 0
            r = 0
     
            left_size = len(left_arr)
            right_size = len(right_arr)
            while p < left_size and q < right_size:
                if left_arr[p] < right_arr[q]:
                  inp_arr[r] = left_arr[p]
                  p += 1
                else:
                    inp_arr[r] = right_arr[q]
                    if left_arr[p][1]%2 == 0:
                        cnt[0] += 1
                        buff[0].append(left_arr[p][1])
                    else:
                        cnt[1] += 1
                        buff[1].append(left_arr[p][1])
                    q += 1
                 
                r += 1
     
            
            while p < left_size:
                inp_arr[r] = left_arr[p]
                p += 1
                r += 1
     
            while q < right_size:
                inp_arr[r]=right_arr[q]
                q += 1
                r += 1
    merge_sort(inp_arr)
    ans = []
    cnt = 0
    for i in range(max(len(buff[0]), len(buff[1]))):
        if i < len(buff[0]):
            ans.append(buff[0][i]+1)
        if i < len(buff[1]):
            ans.append(buff[1][i]+1)
    print(len(buff[0]) +len(buff[1]))
    print(*ans, sep=" ")

T = int(input())


AS = []
for _ in range(T):
    N = int(input())
    *A,=map(int,input().split())
    AS.append(A)

for A in AS:
    *A, = map(lambda x:x-1, A)
    m(A)


