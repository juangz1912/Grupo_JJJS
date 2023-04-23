import requests
import json
from pandas import json_normalize
import Sorts
link = "https://www.datos.gov.co/resource/gt2j-8ykr.json"
data = requests.get(link)
datos = json.loads(data.text)
datos = json_normalize(datos)
print(datos.edad.values)

lista = datos.edad.values
print(lista)
print("Ingrese el tipo de sort que quiere realizar ")
print("1. Heap Sort")
print("2. Merge Sort")
print("3. Quick Sort")
print("4. Counting Sort")
print("5. Radix Sort")
print("6. Bubble Sort")
sort_type = input()

if sort_type == 1:
    Sorts.Sort.heap_sort(lista)
elif sort_type == 2:
    Sorts.Sort.MergeSort(lista)
elif sort_type == 3:
    Sorts.Sort.quick_sort(lista)
elif sort_type == 4:
    Sorts.Sort.counting_sort(lista)
elif sort_type == 5:
    Sorts.Sort.radix_sort(lista)
elif sort_type == 6:
    Sorts.Sort.bubble_sort(lista)