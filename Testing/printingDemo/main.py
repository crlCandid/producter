from controllers.main import Baggers, Orders

def main():
    baggers = Baggers()
    orders = Orders()

    print('Available Bagger List:')
    baggers.printCatalog()

    tryCounter = 0
    while not baggers.selected:
        tryCounter += 1

        try:
            result = int(input('\nPlease, enter Option number for required printer: '))
            baggers.setSelected(result)
        except:
            if tryCounter > 2:
                print('\nExiting program')
                exit()
            print('\nIncorrect/Invalid input. Please, try again')

    tryCounter = 0
    while True:
        scan = input('Please scan order or leave blank to quit program: \n')

        if scan == "":
            print('\nExiting program')
            exit()

        order = orders.getOrder(scan)

        if not order:
            print('Order not found')

        baggers.sendToPrinter(order)

if __name__ == "__main__":
    main()