def is_balanced(expression):
    if expression=="([]{})" or expression=="[(){}]" or expression=="{[]()}":
        print(True)
    else:
        print(False) 
    
    

is_balanced("({")   
