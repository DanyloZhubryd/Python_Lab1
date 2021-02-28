from Laptop import Laptop

def main():
    Dell=Laptop("Dell", "Inspiron 3537", 3, 12, 24, 143267)
    HP=Laptop("HP", "250 G7", 3.1, 8, serial_number=257301)
    Acer=Laptop()
    print('Number of laprops available:', Laptop.Get_count())
    print(Dell)
    print(HP)
    print(Acer)

if __name__=="__main__":
    main()