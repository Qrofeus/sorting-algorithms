# Visualizations for Sorting Algorithms

The animations for the sorting algorithms is achieved by using the PyGame python-module. The list contents are drawn as rectangles with heights matching the list elements. The whole representation is compared to a bar graph with each bar corresponding to a list element.

The animations use up-to 3 different colors (Yellow, Blue and Red) to highlight important processes in the running of the algorithm. These highlights included currently comparing elements (Shell sort, Insertion sort, ...), swapped elements (Exchange sort, Bubble sort, ...) or heap structures (Heap sort).

## Running the Animations

In the `main.py` file there is only one line of code that is used for generating the animations for different sorting algorithms. The main.py imports the `animate_sort()` function from the visualizations.py python script where the animation constants and functionality is defined.

To generate the animation for a sorting algorithm, change the name of the algorithm passed to the animate_sort() function-call the `main()` function. Changing the wait_time value, will decide how fast or how slow the animation will move. The speed can also be adjusted during run-time as mentioned in [Controlling-the-animation](#controlling-the-animation).
```python
visualizations.animate_sort(algorithm="Shell Sort", wait_time=50)
```
The available sorting algorithms from which to select one to animate are mentioned above the animate_sort function-call in a comment. Any other algorithm names or misspellings in the name of the sorting algorithm in the function-call will prompt an `>> Invalid algorithm name...` message and the program will end its execution.
```python
['Bubble Sort', 'Bogo Sort', 'Exchange Sort', 'Brick Sort', 'Comb Sort', 'Cocktail Sort', 'Gnome Sort',
 'Insertion Sort', 'Binary Insertion Sort', 'Selection Sort', 'Heap Sort', 'Shell Sort']
```

## Controlling the animation

This implementation using PyGame allows user to control some of the features while the program is running. These controls include changing the speed of the animation, pausing the animation, and re-shuffling the list to start the animation again.

These controls can be accessed by their corresponding keys:
1. Escape -> QUIT
2. Enter/Return -> Re-shuffle and restart animation
3. Space -> Pause animation
4. Left (arrow key) -> Slow down animation
5. Right (arrow key) -> Speed up animation

The key interactions can also be viewed when using the `visualizations.animate_sort()` in the code editor by looking at the doc-string for that function.

Note: As the code uses `pygame.event`, key interactions are registered only on key-release. Long key-presses do not result in continuous effect stacking for the corresponding functionality.

## Modifying the Animations

Before running the `main.py` file, there are certain variables that may be changed if required. In the `visualizations.py` file, there are a few constants declared at the top of the file that dictate how the PyGame window will look and operate.
```python
# Constants
HEIGHT, WIDTH = 400, 800
LIST_SIZE = 100
MIN_WAIT, MAX_WAIT = 1, 100
COLORS = {
    "background": (35, 35, 40),     # Black
    "regular": (255, 248, 240),     # White
    "highlight_1": (239, 71, 111),  # Yellow
    "highlight_2": (255, 209, 102), # Red
    "highlight_3": (17, 138, 178),  # Blue
    "sorted": (6, 214, 160)         # Green
}
```
`HEIGHT` and `WIDTH` specify the size of the PyGame window that will be created when the program is run for animation. `LIST_SIZE` specifies the size of the list of number that will be generated to be sorted by the selected sorting-algorithm. When changing the HEIGHT, WIDTH or LIST_SIZE make sure that the height and width are divisible by the list-size for cleaner animation results.

Wait-time is the time interval where the PyGame will pause defined in milliseconds. `MIN_WAIT` corresponds to the fastest animation speed and `MAX_WAIT` slowest animation speed defined for the program. Altering the wait-times will allow you to speed-up/slow-down in between the newly defined range.

`COLORS` dictionary provides the different colors that are used when animating the sorting algorithms. If the colors are altered, make sure the altered colors are accepted by PyGame as a valid color value. The `pygame.draw.rect()` function used in this implementation allows for the following types of inputs for the 'color' parameter:
```python
color: Color | Color | int | str | tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int]
```
When selecting different colors for the animation, their interactions with each other should be considered as colors with higher contrast between them are easier to differentiate and will help in understanding the working of the sorting algorithm.

Below are all the animations for the implemented sorting algorithms:

## Bubble Sort:

![Bubble Sort - Animation](assets/gifs/Bubble%20Sort.gif)

## Selection Sort:

![Selection Sort - Animation](assets/gifs/Selection%20Sort.gif)

## Brick Sort:

![Brick Sort - Animation](assets/gifs/Brick%20Sort.gif)

## Exchange Sort:

![Exchange Sort - Animation](assets/gifs/Exchange%20Sort.gif)

## Comb Sort:

![Comb Sort - Animation](assets/gifs/Comb%20Sort.gif)

## Cocktail Sort:

![Cocktail Sort - Animation](assets/gifs/Cocktail%20Sort.gif)

## Gnome Sort:

![Gnome Sort - Animation](assets/gifs/Gnome%20Sort.gif)

## Insertion Sort:

![Insertion Sort - Animation](assets/gifs/Insertion%20Sort.gif)

## Binary Insertion Sort

![Binary Insertion Sort - Animation](assets/gifs/Binary%20Insertion%20Sort.gif)

## Shell Sort:

![Shell Sort - Animation](assets/gifs/Shell%20Sort.gif)

## Heap Sort:

![Heap Sort - Animation](assets/gifs/Heap%20Sort.gif)
