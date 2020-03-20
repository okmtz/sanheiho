import itertools

n = input('please input number')

#リストを作成
lst = [i for i in range(int(n))]

# 組み合わせを作成
c = itertools.combinations(lst,3)

# 答えを入れる配列
answer = []


for i in c:
    a = i[0]
    b = i[1]
    c = i[2]
    if c**2 == a **2 + b **2:
        answer.append(i)

print(answer)






