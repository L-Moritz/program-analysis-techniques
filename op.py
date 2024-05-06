from enum import Enum

class Operator(Enum):
    def __str__(self):
        if self.value == 1:
            return '+';
        elif self.value == 2:
            return '-';
        elif self.value == 3:
            return '*';
        elif self.value == 4:
            return '/';
        raise IndexError(f'Index {self.value} not in type Operator');

    def __eq__(self, value: object) -> bool:
        return self.value == value.value;

    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDE = 4
    