from GPU import GPU


def main():

    rtx_4090 = GPU(name='RTX 4090', model='MSI Dragon Cum', brand='NVIDIA', msrp=1300.00, tdp=400,
                   release_date='09-15-2022')
    looper = True
    while looper:
        print('Choose from the following:')
        selection = int(input('\n1 GPU List\n2 Say Bye\n3 Quit\nSelection: '))

        if selection == 1:
            print(rtx_4090.get_all())
        elif selection == 2:
            print('Bye')
        elif selection == 3:
            looper = False

main()