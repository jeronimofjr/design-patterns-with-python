
class Computer:
    def __init__(self, serial_number) -> None:
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None
    
    def __str__(self):
        info = (
                f'Memory: {self.memory}GB',
                f'Hard Disk: {self.hdd}GB',
                f'Graphics Card: {self.gpu}'            
        )
        return '\n'.join(info)
    

class ComputerBuilder:
    def __init__(self) -> None:
        self.computer = Computer('AG23385193')
    
    def configure_hdd(self,amount):
        self.computer.hdd = amount
    
    def configure_gpu(self, amount):
        self.computer.gpu = amount
    
    def configure_memory(self, amount):
        self.computer.memory = amount


class HardwareEngineer:
    def __init__(self) -> None:
        self.builder = None 

    def constructor_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)
    
    @property
    def computer(self):
        return self.builder.computer
    
def main():
    engineer = HardwareEngineer()
    engineer.constructor_computer(memory=8, hdd=500, gpu='GeForce GTX 650 TI')

    computer = engineer.computer
    print(computer)

if __name__ == '__main__':
    main()