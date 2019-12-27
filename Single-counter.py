import time

def count_file(filename):
    starttime = int(time.time() * 1000)
    f = open(filename, 'r')
    even = 0
    odd = 0
    for num in f.readlines():
        num = int(num.strip())
        if (num % 2) == 0:
            # num is even
            even += 1
        else:
            # num is odd
            odd += 1
    endtime = int(time.time() * 1000)
    return even, odd, (endtime - starttime)

filename_1 = "/home/uic/Steven-s-Assignment4/data/1000.txt"
filename_2 = "/home/uic/Steven-s-Assignment4/1000000.txt"

# 1000 numbers
even_1, odd_1, time_1 = count_file(filename_1)
print("For 1000.txt, even: %s, odd: %s, time spent: %s ms" % (even_1, odd_1, time_1))
# 100000000 numbers
even_2, odd_2, time_2 = count_file(filename_2)
print("For 1000000.txt, even: %s, odd: %s, time spent: %s ms" % (even_2, odd_2, time_2))
