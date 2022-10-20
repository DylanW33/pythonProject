from GPU import GPU
from CPU import CPU

def main():

    ryzen_5900x = CPU(name='Ryzen 9', model='5900x', brand='AMD', msrp=380.00, tdp=105, release_date='11-05-2020')

    rtx_4090 = GPU(name='RTX 4090', model='MSI Dragon Cum', brand='NVIDIA', msrp=1300.00, tdp=400,
                   release_date='09-15-2022')
    looper = True
    while looper:
        print('Choose from the following:')
        selection = int(input('\n1 GPU List\n2 CPU List\n3 Say Bye\n4 Quit\nSelection: '))

        if selection == 1:
            print(rtx_4090.get_all())
        elif selection == 2:
            print(ryzen_5900x.get_all())
        elif selection == 3:
            print('Say Bye')
        elif selection == 4:
            looper = False


main()