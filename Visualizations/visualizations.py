from sorting_algorithms import SORTS
import pygame
import random

# Constants
WIDTH = 500
HEIGHT = 300
MAX_LENGTH = 100
MIN_WAIT, MAX_WAIT = 1, 100
COLORS = {
    "background": (35, 35, 40),
    "regular": (255, 248, 240),
    "highlight_1": (239, 71, 111),
    "highlight_2": (255, 209, 102),
    "highlight_3": (17, 138, 178),
    "sorted": (6, 214, 160)
}


def generate_process(algorithm: str) -> tuple:
    """Creates a random list of integers and a generator object for the specified sorting function"""
    arr = random.sample(range(1, MAX_LENGTH + 1), MAX_LENGTH)
    process = SORTS[algorithm](arr)
    return arr, process


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


def display_list(screen: pygame.Surface, arr: list[int] = None, highlight_1=None, highlight_2=None,
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


def animate_sort(algorithm: str):
    """Creates a pygame window to animate the given sorting algorithm
    Keyboard Interactions:
    1. Escape -> QUIT
    2. Enter/Return -> Re-shuffle and restart animation
    3. Space -> Pause animation
    4. Left (arrow key) -> Slow down animation
    5. Right (arrow key) -> Speed up animation
    """
    if algorithm not in SORTS.keys():
        print(">> Invalid algorithm name...")
        exit()
    wait_time = 100

    # Initialize PyGame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sorting Algorithm Visualizations")

    # Generate algorithm name text-box in top-left
    font = pygame.font.Font(pygame.font.get_default_font(), 15)
    text = font.render(algorithm, True, COLORS["regular"], COLORS["background"])
    text_box = text.get_rect(topleft=(10, 10))

    # Initialize list and sorting generator object
    arr, process = generate_process(algorithm)

    # Animation loop
    running = True
    pause = False
    while running:
        if not pause:
            arr, highlight_1, highlight_2, highlight_3 = next(process, (None, None, None, None))
            # print(arr, highlight_1, highlight_2, highlight_3)
            if arr:
                display_list(screen, arr, highlight_1, highlight_2, highlight_3)
            else:
                arr = list(range(1, MAX_LENGTH + 1))
                display_list(screen, arr, list_sorted=True)

            # Add algorithm text-box in top-left
            screen.blit(text, text_box)

            # Update screen
            pygame.display.flip()
            pygame.time.wait(wait_time)

        # User interactions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Arrow keys for animation speed
            if event.type == pygame.KEYDOWN:
                # Left arrow to decrease speed(increase WAIT_TIME)
                if event.key == pygame.K_LEFT:
                    wait_time = min(MAX_WAIT, wait_time + 10)
                # Right arrow to increase speed(decrease WAIT_TIME)
                if event.key == pygame.K_RIGHT:
                    wait_time = max(MIN_WAIT, wait_time - 10)
                # Space-bar to pause animation
                if event.key == pygame.K_SPACE:
                    pause = not pause
                # Enter key to re-shuffle and restart
                if event.key == pygame.K_RETURN:
                    arr, process = generate_process(algorithm)
                    pause = False
                # Escape to QUIT
                if event.key == pygame.K_ESCAPE:
                    running = False
