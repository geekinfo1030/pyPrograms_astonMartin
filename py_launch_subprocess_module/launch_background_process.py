import os

from subprocess import *

pgm = [r'secondscript1.py', r'secondscript2.py']

p = Popen([pgm[0], 'ArcView'], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()
print(output[0])

p = Popen([pgm[1], 'ArcView'], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()
print(output[0])

