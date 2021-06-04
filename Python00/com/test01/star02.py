# -*- coding:utf-8 -*-

# 1
print('\n'.join([''.join(['*' for i in range(i + 1)]) for i in range(5)]))

# 2
print('\n'.join([''.join(['*' for i in range(i)]) for i in range(5, 0, -1)]))

# 3
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(i + 1)]) for i in range(5)]))

# 4
print('\n'.join([''.join([' ' for i in range(i)] + ['*' for i in range(5 - i)]) for i in range(5)]))

# 5
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(2 * i + 1)]) for i in range(5)]))
