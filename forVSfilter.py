import time

def test_for(length):
    sub_list = []
    begin = time.perf_counter()
    for i in range(length):
        if i % 2 == 0:
            sub_list.append(i)
    end = time.perf_counter()
    print('the time for used:', (end - begin))

def test_filter(length):
    def check(i):
        return i % 2 == 0
    begin = time.perf_counter()
    sub_list = filter(check, range(length))
    end = time.perf_counter()
    print('the time filter used:', (end - begin))


test_for(100000)
test_filter(100000)

#the time for used: 0.010848700000000003
#the time filter used: 5.599999999994498e-06