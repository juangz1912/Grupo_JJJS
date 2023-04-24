from random import randrange

class Sort:
    def __init__(self):
        pass

    def Merge(self, lista_i, lista_d):
        lista_resultado = []

        while(len(lista_i) > 0 and len(lista_d) > 0):
            if lista_i[0] < lista_d[0]:
                lista_resultado.append(lista_i[0])
                lista_i = lista_i[1:]
            else:
                lista_resultado.append(lista_d[0])
                lista_d = lista_d[1:]

        if len(lista_i) > 0:
            lista_resultado = lista_resultado + lista_i

        if len(lista_d) > 0:
            lista_resultado = lista_resultado + lista_d

        return lista_resultado

    def MergeSort(self, lista):
        if len(lista) <= 1:
            return lista

        lista_izquierda = lista[:len(lista)//2]  
        lista_derecha = lista[len(lista)//2:]

        lista_izquierda = self.MergeSort(lista_izquierda)
        lista_derecha = self.MergeSort(lista_derecha)

        return self.Merge(lista_izquierda, lista_derecha)
    
    def heapify(self, unsorted, index, heap_size):
        largest = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
            largest = left_index

        if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
            largest = right_index

        if largest != index:
            unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
            self.heapify(unsorted, largest, heap_size)

    def heap_sort(self, unsorted):
        n = len(unsorted)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(unsorted, i, n)
        for i in range(n - 1, 0, -1):
            unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
            self.heapify(unsorted, 0, i)
        return unsorted
    
    def quick_sort(self, collection: list) -> list:
        if len(collection) < 2:
            return collection
        pivot_index = randrange(len(collection))  # Use random element as pivot
        pivot = collection[pivot_index]
        greater: list[int] = []  # All elements greater than pivot
        lesser: list[int] = []  # All elements less than or equal to pivot

        for element in collection[:pivot_index]:
            (greater if element > pivot else lesser).append(element)

        for element in collection[pivot_index + 1 :]:
            (greater if element > pivot else lesser).append(element)

        return [*self.quick_sort(lesser), pivot, *self.quick_sort(greater)]
    
    def counting_sort(self, collection):
        # if the collection is empty, returns empty
        if collection == []:
            return []

        # get some information about the collection
        coll_len = len(collection)
        coll_max = max(collection)
        coll_min = min(collection)

        # create the counting array
        counting_arr_length = coll_max + 1 - coll_min
        counting_arr = [0] * counting_arr_length

        # count how much a number appears in the collection
        for number in collection:
            counting_arr[number - coll_min] += 1

        # sum each position with it's predecessors. now, counting_arr[i] tells
        # us how many elements <= i has in the collection
        for i in range(1, counting_arr_length):
            counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

        # create the output collection
        ordered = [0] * coll_len

        # place the elements in the output, respecting the original order (stable
        # sort) from end to begin, updating counting_arr
        for i in reversed(range(0, coll_len)):
            ordered[counting_arr[collection[i] - coll_min] - 1] = collection[i]
            counting_arr[collection[i] - coll_min] -= 1

        return ordered

    def radix_sort(self, list_of_ints):
        RADIX = 5
        placement = 1
        max_digit = max(list_of_ints)
        while placement <= max_digit:
            # declare and initialize empty buckets
            buckets: list[list] = [[] for _ in range(RADIX)]
            # split list_of_ints between the buckets
            for i in list_of_ints:
                tmp = int((i / placement) % RADIX)
                buckets[tmp].append(i)
            # put each buckets' contents into list_of_ints
            a = 0
            for b in range(RADIX):
                for i in buckets[b]:
                    list_of_ints[a] = i
                    a += 1
            # move to next
            placement *= RADIX
        return list_of_ints


    def bubble_sort(self, collection):
        length = len(collection)
        for i in range(length - 1):
            swapped = False
            for j in range(length - 1 - i):
                if collection[j] > collection[j + 1]:
                    swapped = True
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
            if not swapped:
                break  # Stop iteration if the collection is sorted.
        return collection