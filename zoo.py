# 12.1
def hours():
    print("Open 9-5 daily")

'''
import zoo
zoo.hours()
'''

# 12.2

'''
import zoo as menagerie
menagerie.hours()
'''

# 12.3

'''
from zoo import hours
hours()
'''

# 12.4

'''
from zoo import hours as info
info()

'''

# 12.5

plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)


# 12.6

from collections import OrderedDict

fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)
