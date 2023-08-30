def remove_duplicates(sequence):
    if type(sequence)==tuple:
        sequence=tuple(set(sequence))
        print(sequence)
    elif type(sequence)==list:
        sequence=list(dict.fromkeys(sequence))
        print(sequence)
    else:
        print("insert a tuple or a list")    

    

remove_duplicates((1,2,3,4,5,5,5,6))    