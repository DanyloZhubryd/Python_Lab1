class Laptop:
    __count=0
    def __init__(self, name_of_manufacturer = " ", model = " " , cpu_speed_in_GHz = 0, amount_of_RAM_in_GB = 0, warranty_in_months = 0, serial_number = 0):
        Laptop.__count+=1
        self.name_of_manufacturer = name_of_manufacturer
        self.model = model
        self.cpu_speed_in_GHz = cpu_speed_in_GHz
        self.amount_of_RAM_in_GB = amount_of_RAM_in_GB
        self.warranty_in_months = warranty_in_months
        self.serial_number = serial_number

    def __del__(self):
        print(self.name_of_manufacturer+" destroyed")

    def __str__(self):
        return f"Manufacturer: {self.name_of_manufacturer}\n\
Model: {self.model}\n\
CPU speed: {self.cpu_speed_in_GHz} GHz\n\
RAM: {self.amount_of_RAM_in_GB} GB\n\
Warranty: {self.warranty_in_months} months\n\
Serial number: {self.serial_number}\n"
    
    @staticmethod
    def Get_count():
        return Laptop.__count