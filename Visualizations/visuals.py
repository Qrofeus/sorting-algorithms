import pygame
# from sorting_algorithms import bubble_sort
from random import sample

WIDTH = 500
HEIGHT = 250


def draw_bar(screen: pygame.Surface, arr: list[int], index: int, color: pygame.Color, bar_width: int) -> None:
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


def display_list(arr: list[int], screen: pygame.Surface) -> None:
    """Traverses the list, using draw_bar() displays all elements in the list on the pygame screen"""
    screen.fill(pygame.Color("black"))

    max_width, max_height = screen.get_size()
    bar_width = max_width // len(arr)

    for i in range(len(arr)):
        draw_bar(screen, arr, i, pygame.Color("yellow"), bar_width)


def main():
    # Initialize PyGame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Animation loop
    running = True
    while running:
        arr = get_list(50)
        display_list(arr, screen)

        # Update screen
        pygame.display.flip()
        # User interactions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.time.wait(100)


def get_list(size: int = 10) -> list:
    return sample(range(1, size + 1), size)


if __name__ == '__main__':
    main()
