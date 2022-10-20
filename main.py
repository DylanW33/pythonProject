
def main():
    looper = True
    while looper:
        print('Choose from the following:')
        selection = int(input('\n1 Say Hi\n2 Say Bye\n3 Quit\nSelection: '))

        if selection == 1:
            print('Hi')
        elif selection == 2:
            print('Bye')
        elif selection == 3:
            looper = False

main()