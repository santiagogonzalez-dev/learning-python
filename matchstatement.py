number_user_input = int(input('Insert an int: '))

match number_user_input:
    case 1:
        print("The user introduced a 1")
    case 2:
        print("The user introduced a 2")
    case 3:
        print("The user introduced a 3")
    case _:
        print("The user did not introduced a  1, 2 or 3")
