import requests
import json
from pandas import json_normalize
from Sorts import Sort

sorter = Sort()
link = "https://www.datos.gov.co/resource/gt2j-8ykr.json"
data = requests.get(link)
datos = json.loads(data.text)
datos = json_normalize(datos)

lista1 = datos.edad.values.tolist()
lista = []
for i in lista1:
    lista.append(int(i))

print("Ingrese el tipo de sort que quiere realizar ")
print("1. Heap Sort")
print("2. Merge Sort")
print("3. Quick Sort")
print("4. Counting Sort")
print("5. Radix Sort")
print("6. Bubble Sort")
sort_type = int(input(" "))

if sort_type == 1:
    print(sorter.heap_sort(lista))
elif sort_type == 2:
    print(sorter.MergeSort(lista))
elif sort_type == 3:
    print(sorter.quick_sort(lista))
elif sort_type == 4:
    print(sorter.counting_sort(lista))
elif sort_type == 5:
    print(sorter.radix_sort(lista))
elif sort_type == 6:
    print(sorter.bubble_sort(lista))
