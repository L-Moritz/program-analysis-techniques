from expression import Expression, ExpressionBuilder
from variable import Variable

class Statement():
    last_id = 0;

    id: int;
    var: Variable;
    expression: Expression;
    def __init__(self, statement: str):
        if (statement.count('=') != 1):
            raise ValueError
        statement = statement.replace(' ', '')
        var, expression = statement.split('=');
        self.var = Variable(var);
        self.expression = ExpressionBuilder.create(expression);
        
        Statement.last_id += 1;
        self.id = Statement.last_id;
        
    def __str__(self):
        return str(self.id) + ': ' + str(self.var) + '=' + str(self.expression);
    
    def __eq__(self, value: object) -> bool:
        return self.var == value.var and self.expression == value.expression and self.id == value.id
