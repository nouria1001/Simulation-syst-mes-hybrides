import math
from atomic_component import AtomicComponent
import math


class proc(AtomicComponent):

    def __init__(self):

        super().__init__(proc)
        self.state = 'free'
        self.input = {'req': None}
        self.output = {'done': None}

    def internal_func(self):
        if self.state == "busy":
            self.state = "free"
        # return self.state

    def external_func(self):
        if self.state == "free" and self.input['req'] == True:
            self.state = "busy"
        # return self.state

    def lambda_func(self):
        if self.state == "busy":
            self.output['done'] = True
            return self.output

    def get_Ta(self):
        if self.state == "free":
            return math.inf

        elif self.state == "busy":
            return 3
        else:
            return -1


