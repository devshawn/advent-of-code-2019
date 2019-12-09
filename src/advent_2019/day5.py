class IntcodeComputer:
    def __init__(self, memory, inputs):
        self.memory = memory.copy()
        self.inputs = inputs
        self.outputs = []
        self.opcode_string = None
        self.i = 0

    @staticmethod
    def get_opcode(current_value):
        return int(current_value) if len(current_value) <= 2 else int(current_value[2:])

    @staticmethod
    def get_parameter_modes(current_value):
        if len(current_value) == 3:
            return int(current_value[0]), 0, 0
        elif len(current_value) == 4:
            return int(current_value[1]), int(current_value[0]), 0
        elif len(current_value) == 5:
            return int(current_value[2]), int(current_value[1]), int(current_value[0])
        else:
            return 0, 0, 0

    def get_parameter(self, parameter_position):
        if self.get_parameter_modes(self.opcode_string)[parameter_position - 1] == 0:
            return self.memory[self.i + parameter_position]
        else:
            return self.i + parameter_position

    def advance_position(self, count):
        self.i += count

    def execute(self):
        finished = False
        while finished is False:
            self.opcode_string = str(self.memory[self.i])
            opcode = self.get_opcode(self.opcode_string)

            if opcode == 1:
                self.memory[self.get_parameter(3)] = self.memory[self.get_parameter(1)] + self.memory[self.get_parameter(2)]
                self.advance_position(4)
            elif opcode == 2:
                self.memory[self.get_parameter(3)] = self.memory[self.get_parameter(1)] * self.memory[self.get_parameter(2)]
                self.advance_position(4)
            elif opcode == 3:
                self.memory[self.get_parameter(1)] = self.inputs.pop(0)
                self.advance_position(2)
            elif opcode == 4:
                self.outputs.append(self.memory[self.get_parameter(1)])
                self.advance_position(2)
            elif opcode == 5:
                if self.memory[self.get_parameter(1)] is not 0:
                    self.i = self.memory[self.get_parameter(2)]
                else:
                    self.advance_position(3)
            elif opcode == 6:
                if self.memory[self.get_parameter(1)] is 0:
                    self.i = self.memory[self.get_parameter(2)]
                else:
                    self.advance_position(3)
            elif opcode == 7:
                self.memory[self.get_parameter(3)] = 1 if self.memory[self.get_parameter(1)] < self.memory[
                    self.get_parameter(2)] else 0
                self.advance_position(4)
            elif opcode == 8:
                self.memory[self.get_parameter(3)] = 1 if self.memory[self.get_parameter(1)] == self.memory[
                    self.get_parameter(2)] else 0
                self.advance_position(4)
            elif opcode == 99:
                finished = True

        return self.outputs
