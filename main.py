from GPU import GPU
from CPU import CPU
from PWRSPL import PWRSPL
def main():
    AX1600I = PWRSPL(name='AX1600I', model='ATX', brand='Corsair', msrp=609.99, tdp=1600,
                           release_date='04-18-2018')

    ryzen_5900x = CPU(name='Ryzen 9', model='5900x', brand='AMD', msrp=380.00, tdp=105, release_date='11-05-2020')

    rtx_4090 = GPU(name='RTX 4090', model='MSI Dragon Cum', brand='NVIDIA', msrp=1300.00, tdp=400,
                   release_date='09-15-2022')
    looper = True
    while looper:
        print('Choose from the following:')
        selection = int(input('\n1 GPU List\n2 CPU List\n3 Power Supply List\n4 Say Bye\n5 Quit\nSelection:'))

        if selection == 1:
            print(rtx_4090.get_all())
        elif selection == 2:
            print(ryzen_5900x.get_all())
        elif selection == 3:
            print(PWRSPL.get_all())
        elif selection == 4:
            print('Say Bye')
        elif selection == 5:
            looper = False


main()