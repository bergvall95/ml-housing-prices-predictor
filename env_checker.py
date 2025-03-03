import sys 

def is_venv():
    return (hasattr(sys, 'real_prefix') or 
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if is_venv():
    print("You are in a virtual environment.")
else:   
    print("You are not in a virtual environment.")