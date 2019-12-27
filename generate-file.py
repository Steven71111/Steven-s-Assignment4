import os
import random

def generate_file(filename, line):
    
    f = open(filename, 'w')
    for i in range(0, line):
        f.write(str(random.randint(0, line)))
        f.write('\n') 
    f.close()
    return

def generate_data(dirs, line1, line2):
    if not os.path.exists(dirs):
        print("Path %s is not exist, creating..." % (dirs))
        os.makedirs(dirs)
        print("Create path %s success." % (dirs))
    generate_file(dirs + str(line1) + '.txt', line1)
    generate_file(dirs + str(line2) + '.txt', line2)

dirs = "/home/uic/Steven-s-Assignment4/data/"
line1 = 1000
line2 = 1000000
generate_data(dirs, line1, line2)