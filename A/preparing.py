import os
path = os.path.dirname(__file__)
file = open(path + '/index.h', 'w')
file.write('int sqr(int x) { return x * x; }\n')
