def even_numbers(limit):
    for i in range( 2 , limit+2  , 2):
        yield i

for i in even_numbers(8) :
    print(i)