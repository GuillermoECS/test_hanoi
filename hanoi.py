""" Solvo: Hanoi Test """
""" Python Version: 3.5.3 """

__author__ = "Guillermo Esteban Castro Sánchez"
__email__ = "guillermoestebancs@gmail.com"

# Libraries
import os
import copy

n = int(input("Please enter disks number: "))  # Disks
minimun_moves = 2**n-1  # Minimum moves
my_moves = 0  # My moves
tower_one = []  # Tower #1
disk_numbers = copy.copy(n)  # Disk numbers
while disk_numbers > 0:
    tower_one.append(disk_numbers)  # Insert n disks in tower one
    disk_numbers -= 1
tower_two = []  # Tower #2
tower_tree = []  # Tower #3
working_tower = 1  # Working tower
disk_poped = 0  # Disk poped


def clear():
    '''Clear command line'''
    return os.system('clear')


def hanoi_towers_recursive_solution():
    '''Hanoi Towers: Recursive solution'''
    if(len(tower_tree) == n):
        clear()
        print('Congratulations, Game over!')
        print('Minimun moves =', minimun_moves)
        print('Your moves =', my_moves)
    else:
        # Tower #1: Origin
        if working_tower == 1:
            if(n % 2 == 0):
                manageDisks(tower_one, tower_two, tower_tree, 1)
            else:
                manageDisks(tower_one, tower_tree, tower_two, 1)
        # Tower #2: Intermediate
        if working_tower == 2:
            if(n % 2 == 0):
                manageDisks(tower_two, tower_tree, tower_one, 2)
            else:
                manageDisks(tower_two, tower_one, tower_tree, 2)
        # Tower #3: Destiny
        if working_tower == 3:
            if(n % 2 == 0):
                manageDisks(tower_tree, tower_one, tower_two, 3)
            else:
                manageDisks(tower_tree, tower_two, tower_one, 3)

        hanoi_towers_recursive_solution()


def manageDisks(tower_one, tower_two, tower_tree, tower_number):
    ''' Pop and append disks according to last disk poped and working_tower'''
    global my_moves, working_tower, disk_poped
    if tower_one:
        if tower_one[-1] != disk_poped:
            if tower_two:
                if tower_one[-1] < tower_two[-1]:
                    disk_poped = tower_one.pop()
                    tower_two.append(disk_poped)
                    my_moves += 1
                    game_information()
                else:
                    if tower_tree:
                        if tower_one[-1] < tower_tree[-1]:
                            disk_poped = tower_one.pop()
                            tower_tree.append(disk_poped)
                            my_moves += 1
                            game_information()
                        else:
                            if(tower_number == 3):
                                working_tower = 1
                            else:
                                working_tower += 1
                    else:
                        disk_poped = tower_one.pop()
                        tower_tree.append(disk_poped)
                        my_moves += 1
                        game_information()
            else:
                disk_poped = tower_one.pop()
                tower_two.append(disk_poped)
                my_moves += 1
                game_information()
        else:
            if(tower_number == 3):
                working_tower = 1
            else:
                working_tower += 1
    else:
        if(tower_number == 3):
            working_tower = 1
        else:
            working_tower += 1


def show_towers_status():
    '''Show towers status'''
    print('=======================================================')
    print("Tower #1 Origin: ", tower_one)
    print("Tower #2 Intermediate: ", tower_two)
    print("Tower #3 Destiny: ", tower_tree)
    print('=======================================================')
    wait = input("Pres enter to continue !")
    clear()


def game_information():
    '''Show game information'''
    # Hanoi Test using n disks
    print('Hanoi Test : %d Disks' % (n))
    print('Mininum moves = {minimun_moves}'.format(
        minimun_moves=minimun_moves))
    print('Your moves =', my_moves)
    print('============Move #%d====================================' % (my_moves))
    show_towers_status()


# Hanoi towers: Recursive Solution
clear()
hanoi_towers_recursive_solution()
