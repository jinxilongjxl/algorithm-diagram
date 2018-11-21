def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)
res = countdown(3)
print(res)
