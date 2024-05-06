import re

from op import Operator
from variable import Variable

def separate_expression(expression):
    components = re.findall(r'\b\w+\b|\S', expression)
    return components

def contains_operator(expression):
    operators = {'+', '-', '*', '/'}
    for char in expression:
        if char in operators:
            return True
    return False

class Expression:
    def __init__(self, expression: str):
        arr = separate_expression(expression);
        print(arr);
        
class AssignmentExpression(Expression):
    var: Variable;
    def __init__(self, expression: str):
        self.var = Variable(expression);
        
    def contains(self, var: Variable):
        return self.var == var
    
    def get_variables(self):
        return [v for v in [self.var] if not v.name.isnumeric()]
        
    def __str__(self):
        return str(self.var)

class OperationExpression(Expression):
    var1: Variable;
    operator: Operator;
    var2: Variable;
    def __init__(self, expression: str):
        arr = separate_expression(expression);
        self.var1 = Variable(arr[0]);
        if arr[1] == '+':
            self.operator = Operator.PLUS;
        elif arr[1] == '-':
            self.operator = Operator.MINUS;
        elif arr[1] == '*':
            self.operator = Operator.TIMES;
        elif arr[1] == '/':
            self.operator = Operator.DIVIDE;
        else:
            raise ValueError(f'operator {arr[1]} not available');
        
        self.var2 = Variable(arr[2]);
    
    def contains(self, var: Variable):
        return self.var1 == var or self.var2 == var;
    
    def get_variables(self):
        return [v for v in [self.var1, self.var2] if not v.name.isnumeric()]
        
    def __str__(self):
        return str(self.var1) + str(self.operator) + str(self.var2);
    
    def __eq__(self, value: object) -> bool:
        if (isinstance(value, AssignmentExpression)):
            return False;
        return self.var1 == value.var1 and self.operator == value.operator and self.var2 == value.var2;
        
    
class ExpressionBuilder:
    @staticmethod
    def create(expression: str) -> Expression:
        if (contains_operator(expression)):
            return OperationExpression(expression);
        else:
            return AssignmentExpression(expression);