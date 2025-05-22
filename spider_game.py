import os
import random

GRID_SIZE = 5
NUM_SPIDERS = 3


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_grid(player_pos, spiders):
    for y in range(GRID_SIZE):
        row = []
        for x in range(GRID_SIZE):
            if (x, y) == tuple(player_pos):
                row.append('P')
            elif (x, y) in spiders:
                row.append('X')
            else:
                row.append('.')
        print(' '.join(row))


def main():
    player = [0, 0]
    spiders = set()
    while len(spiders) < NUM_SPIDERS:
        pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if pos != tuple(player):
            spiders.add(pos)

    moves = 0
    while True:
        clear_screen()
        print('Move with WASD keys. Step on the spiders (X)!')
        display_grid(player, spiders)
        if not spiders:
            print(f'You win in {moves} moves!')
            break
        move = input('Your move: ').lower()
        if not move:
            continue
        if move[0] == 'w' and player[1] > 0:
            player[1] -= 1
        elif move[0] == 's' and player[1] < GRID_SIZE - 1:
            player[1] += 1
        elif move[0] == 'a' and player[0] > 0:
            player[0] -= 1
        elif move[0] == 'd' and player[0] < GRID_SIZE - 1:
            player[0] += 1
        current = tuple(player)
        if current in spiders:
            spiders.remove(current)
            print('You squashed a spider!')
        moves += 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nBye!')
