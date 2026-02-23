import sys

while True:
    print('Type exit to exit.')
    response = input()
    print('You typed ' + response + '.')
    if response == 'exit':
        sys.exit()

