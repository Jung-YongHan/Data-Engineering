epsilon = 0
a = 1.0
while (1.0+a) != 1.0:
    epsilon = a
    a = a/2.0

print(f'epsilon={epsilon}')
# epsilon=2.220446049250313e-16