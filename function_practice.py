def  hello():
    print("Welcome to the function")

def pack(item1, item2, item3):
    pack_list = [item1, item2, item3]
    print(pack_list)

def eat_lunch(list):
    if len(list) == 0:
        print("My lunch box is empty")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")
        


hello()
pack("sandwich", "soda", "Banana")
eat_lunch(["sandwich", "chips", "banana", "chwey bar", "fruity snacks"])