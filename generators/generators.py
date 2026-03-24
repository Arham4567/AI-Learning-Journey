def my_gen():
    i=1
    while True:
        yield i * i
        i+=i

for i in my_gen():
    if i>25:
        break
    else:
        print(i)