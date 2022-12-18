import quicksort 
import hairbrushsort
import timeit

t = timeit.timeit()

def function():
    print('Введите список:')
    a = list(eval(input()))
    print('Выберите метод сортировки: quicksort/hairbrush')
    b = input()
    
    if b in 'quicksort':
        quicksort.quick_sort(a)
        print(a)
        print(t)
    
    elif b in 'hairbrush':
        hairbrushsort.hairbrush(a)
        print(a)
        print(t)

    else:
        print('Fatal error')
        
function()