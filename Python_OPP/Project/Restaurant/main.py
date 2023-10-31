from Menu import Pizza, Burger, Menu, Drinks

def main():
    menu  = Menu()
    pizza_1 = Pizza("Shutki Pizza", 600 ,'Large', ['Shutki', 'onion'])
    menu.add_menu_item('Pizza', pizza_1)
    pizza_2 = Pizza("Shutki Pizza", 200 ,'Small', ['Potato', 'dal'])
    menu.add_menu_item('Pizza', pizza_2)
    pizza_3 = Pizza("Shutki Pizza", 500 ,'Large', ['oil'])
    menu.add_menu_item('Pizza', pizza_3)

    # add burver to the menu 
    burger_1 = Burger('naga burver', 100, 'Chiken', ['Bred', 'chilli'])
    menu.add_menu_item('burver', burger_1)
    burger_2 = Burger('Meat burver', 100, 'Chiken', ['Bred', 'chilli'])
    menu.add_menu_item('burver', burger_2)


    # add drinks to the menu 
    drinks_1 = Drinks('Cokr', 100, True)
    menu.add_menu_item('burver', drinks_1)


    #show menu 
    menu.show_menu()

    
# call the main 
if __name__ == '__main__':
    main()


