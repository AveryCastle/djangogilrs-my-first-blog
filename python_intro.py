def hi(name):
    if name == 'Ola':
        print('Hi, Ola!')
    elif name == 'Onyou':
        print('How are you, Onyou?')
    else:
        print('Hi, ' + name + '?')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You', 'Onyou']

for name in girls:
    hi(name)
    print('Next girl~')
