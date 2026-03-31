import random
import time
import os

# ------------ Sorting Algorithms ------------ #
def selection_sort(arr: list[int]) -> None:
    n = len(arr)
    passes = 0
    for i in range(n-1):
        passes += 1
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print_viz("Selection Sort", arr, passes)
    print("Passes: ")
    print(passes)
    
def bubble_sort(arr: list[int]) -> None:
    n = len(arr)
    passes = 0
    for i in range(n):
        passes += 1
        swapped = False
        # Last i elements are in place
        # Each pass, the size of elements checked gets smaller
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    print("Passes: ")
    print(passes)

# ------------ Utilities ------------ #
def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()
    
def print_viz(sorting_type: str, arr: list[int], passes: int) -> None:
    print("Sorting Type: ", sorting_type)
    print("Passes: ", passes)
    for i in range(0, len(arr)):
        print(str(arr[i]) + ": " + ("[]" * arr[i]))
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_array(arr):
    for i in range(9):
        arr.append(random.randint(1,10))
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# ------------ Main ------------ #
unsorted_list = []
generate_array(unsorted_list)

clear_screen()
print(" [ 1 ]: Selection\n [ 2 ]: Bubble\n [ 3 ]: Insertion\n [ 4 ]: Selection\n")
choice = input("Select Sorting Algorithm: ")
clear_screen()

if choice == "1":
    selection_sort(unsorted_list)
elif choice == "2":
    bubble_sort(unsorted_list)