
N = int(input())
S = input()

terms = S.replace('.', '').split()

a = sum([1 for term in terms if term in ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun'] ])
print(a)

