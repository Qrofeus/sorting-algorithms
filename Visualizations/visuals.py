import pygame
from sorting_algorithms import bubble_sort
from random import sample

WIDTH = 500
HEIGHT = 250
MAX_LENGTH = 50
WAIT_TIME = 20
COLORS = {
    "background": (35, 35, 40),
    "regular": (255, 248, 240),
    "highlight_1": (239, 71, 111),
    "highlight_2": (255, 209, 102),
    "highlight_3": (17, 138, 178),
    "sorted": (6, 214, 160)
}


def get_list(size: int = 10) -> list:
    """Returns a shuffled list of integer numbers from 0 to size"""
    return sample(range(1, size + 1), size)


def draw_bar(screen: pygame.Surface, arr: list[int], index: int, color: tuple, bar_width: int) -> None:
    """Draws single bar with height equal to selected element in the list to the pygame screen"""
    # Bar dimension
    _, max_height = screen.get_size()
    bar_height = max_height // len(arr) * arr[index]

    # Bar position
    x_pos = bar_width * index
    y_pos = max_height - bar_height

    # drawing the bar to the screen
    bar = pygame.Rect(x_pos, y_pos, bar_width, bar_height)
    pygame.draw.rect(screen, color, bar)


def display_list(arr: list[int], screen: pygame.Surface, highlight_1=None, highlight_2=None,
                 highlight_3=None, list_sorted: bool = False) -> None:
    """Traverses the list, using draw_bar() displays all elements in the list on the pygame screen"""
    screen.fill(COLORS["background"])

    max_width, _ = screen.get_size()
    bar_width = max_width // len(arr)

    if list_sorted:
        for i in range(len(arr)):
            draw_bar(screen, arr, i, COLORS["sorted"], bar_width)
    else:
        for i in range(len(arr)):
            draw_bar(screen, arr, i, COLORS["regular"], bar_width)
        for i in highlight_1:
            draw_bar(screen, arr, i, COLORS["highlight_1"], bar_width)
        for i in highlight_2:
            draw_bar(screen, arr, i, COLORS["highlight_2"], bar_width)
        for i in highlight_3:
            draw_bar(screen, arr, i, COLORS["highlight_3"], bar_width)


def main():
    # Initialize PyGame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Initialize list and sorting generator object
    arr = get_list(MAX_LENGTH)
    process = bubble_sort(arr)

    # print(COLORS)
    # Animation loop
    running = True
    while running:
        arr, highlight_1, highlight_2, highlight_3 = next(process, (None, None, None, None))
        # print(arr, highlight_1, highlight_2, highlight_3)
        if arr:
            display_list(arr, screen, highlight_1, highlight_2, highlight_3)
        else:
            arr = list(range(1, MAX_LENGTH + 1))
            display_list(arr, screen, list_sorted=True)

        # Update screen
        pygame.display.flip()
        # User interactions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.time.wait(WAIT_TIME)


if __name__ == '__main__':
    main()
