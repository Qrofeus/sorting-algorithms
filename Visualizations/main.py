import visualizations


def main():
    # sorts = visualizations.get_sorting_algorithms()
    # print(sorts)
    # ['Bubble Sort', 'Bogo Sort', 'Exchange Sort', 'Brick Sort', 'Comb Sort', 'Cocktail Sort', 'Gnome Sort',
    #  'Insertion Sort', 'Binary Insertion Sort', 'Selection Sort', 'Heap Sort', 'Shell Sort']
    visualizations.animate_sort("Shell Sort", wait_time=50)


if __name__ == '__main__':
    main()
