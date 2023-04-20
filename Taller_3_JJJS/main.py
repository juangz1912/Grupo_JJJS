import Sorts
lista = [7, 69, 34, 0, 5, 105]
print("Ingrese el tipo de sort que quiere realizar ")
print("1. Heap Sort")
print("2. Merge Sort")
print("3. Quick Sort")
print("4. Counting Sort")
print("5. Radix Sort")
print("6. Bubble Sort")
print(lista)
sort_type = input()

match sort_type:
    case 1:
        Sorts.Sort.heap_sort(lista)
    case 2:
        Sorts.Sort.MergeSort(lista)
    case 3:
        Sorts.Sort.quick_sort(lista)
    case 4:
        Sorts.Sort.counting_sort(lista)
    case 5:
        Sorts.Sort.radix_sort(lista)
    case 6:
        Sorts.Sort.bubble_sort(lista)