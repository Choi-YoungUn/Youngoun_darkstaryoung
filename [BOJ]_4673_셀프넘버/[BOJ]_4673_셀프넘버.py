lists = [n for n in range(10001)]
for k in range(1,10000):
    sums = k
    if k >= 1000:
        sums += k // 1000
    if k >= 100:
        sums += k % 1000 //100
    if k >= 10:
        sums += k % 100 //10
    sums += k % 10
    
    if sums <= 10000 and k != sums:
        lists[sums] = 0
        
for pr in lists:
    if pr != 0:
        print(pr)