import math
from atomic_component import AtomicComponent


class buff(AtomicComponent):

    def __init__(self):
        super().__init__(buff)
        self.name = 'buffer'
        self.state = 'a'
        self.q = 0
        self.input = {'job': None, 'done': None}
        self.output = {'req': None}

    def internal_func(self):
        if self.state == 'b':
            self.q = self.q - 1
            self.state = 'c'

    def external_func(self):
        if self.state == 'a':
            self.q = 0
            if self.input['job'] == True:
                self.q = self.q + 1
                self.state = 'b'

        elif self.state == 'c':
            if self.input['job'] == True:
                self.q = self.q + 1
                self.state = 'c'
            elif self.input['done'] == True and self.q > 0:
                self.state = 'b'

            elif self.input['done'] == True and self.q == 0:
                self.state = 'a'

        elif self.state == 'b' and self.input['job'] == True:
            self.q = self.q + 1
            self.state = 'b'

    def get_q(self):
        return self.q

    # return self.state

    def lambda_func(self):
        if self.state == 'b':
            self.output['req'] = True
            return self.output

    def get_Ta(self):
        if self.state == 'a':
            return math.inf
        elif self.state == 'b':
            return 0
        elif self.state == 'c':
            return math.inf

        else:
            return -1


