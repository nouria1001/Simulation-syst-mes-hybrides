class AtomicComponent:

    def __init__(self, name):
        self.name = name

    def internal_func(self):
        pass

    def external_func(self):

        pass

    def lambda_func(self):
        pass

    def print_name(self):
        print(f"we're working on {self.name}\n")

    def set_Te(self, Te):
         self.Te = Te

    def get_Te(self):
        return self.Te

    def set_Tr(self, Tr):
        self.Tr = Tr

    def get_Tr(self):
        return self.Tr

    def get_Ta(self):
        pass

    def received(self):
        a = 0
        for v in self.input.values():
            if v != None:
                return 0

        return -1


