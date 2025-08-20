task = []

def add(inp):
    task.append(inp)

def show():
    print(f'The next following are your list\n {task}')

def delete_one():
    task.pop()

def delete_all():
    task.clear()

while True:
    inp = input("What you want to do? ")
    if inp == 'adding':
        inp_add = input('What task you want to add?')
        add(inp_add)
    
    elif inp  == 'show':
        show()
    
    elif inp == "delete all":
        delete_all()
    
    elif inp == 'delete one':
        delete_one()
    elif inp == 'nothing':
        break
        
