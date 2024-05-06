from functools import reduce;

from statement import Statement

class BasicBlock:
    
    name: str;
    statements: list;
    
    # reaching definitions
    gen = [];
    kill = [];
    
    # available expressions
    e_gen = [];
    e_kill = [];
    
    # live variables
    use = [];
    def_ = [];
    
    ## very busy expressions
    used = [];
    killed = [];

    def __init__(self, name: str, *args):
        """consists of a name and any number of statements 

        Args:
            name (str): name of the basic block
            *args: any number of statements of type string that can be converted to a statement
        """
        self.statements = [];
        self.name = name;
        for arg in args:
            self.statements.append(Statement(arg));
        
    def __str__(self):
        res = '';
        for stmt in self.statements:
            res += str(stmt) + '\n';
        return res;

    def get_expressions(self):
        expressions = [];
        for s in self.statements:
            expressions.append(s.expression);
        return expressions;

    
    def print_reaching_definitions(self):
        print(self.name)
        print("gen: {" + ",".join('(' + str(e) + ')' for e in self.gen) + "}")
        print("kill: {" + ",".join('(' + str(e) + ')' for e in self.kill) + "}")
            
    def print_available_expressions(self):
        print(self.name)
        print("e-gen: {" + ",".join('(' + str(e) + ')' for e in self.e_gen) + "}")
        print("e-kill: {" + ",".join('(' + str(e) + ')' for e in self.e_kill) + "}")
            
    def print_live_variables(self):
        print(self.name)
        print("def: {" + ",".join('(' + str(e) + ')' for e in self.def_) + "}")
        print("use: {" + ",".join('(' + str(e) + ')' for e in self.use) + "}")
            
    def print_very_busy_expressions(self):
        print(self.name)
        print("used: {" + ",".join('(' + str(e) + ')' for e in self.used) + "}")
        print("killed: {" + ",".join('(' + str(e) + ')' for e in self.killed) + "}")
            
    
    def calculate_local_reaching_definitions(self, flow_graph):
        gen = [];
        kill = [];
        for statement in self.statements:
            gen.append(statement);
            if statement in kill:
                kill.remove(statement);
            var = statement.var;
            equal_definition = flow_graph.get_definitions(var);
            kill.extend([eq for eq in equal_definition if eq != statement])
            
            for s in kill:
                if s in gen:
                    gen.remove(s);
            
            # remove duplicates
            gen = reduce(lambda re, x: re+[x] if x not in re else re, gen, [])
            kill = reduce(lambda re, x: re+[x] if x not in re else re, kill, [])
        
        self.kill = sorted(kill, key=lambda s: s.id)
        self.gen = sorted(gen, key=lambda s: s.id)
        
    def calculate_local_available_expressions(self, flow_graph):
        e_gen = [];
        e_kill = [];
        for statement in self.statements:
            e_gen.append(statement.expression);
            e_gen = [e for e in e_gen if not e.contains(statement.var)];
            
            e_kill.extend([s.expression for s in flow_graph.get_in_definition(statement.var)]);
            e_kill = [e for e in e_kill if e not in e_gen]

        # remove possible duplicates
        self.e_gen = reduce(lambda re, x: re+[x] if x not in re else re, e_gen, [])
        self.e_kill = reduce(lambda re, x: re+[x] if x not in re else re, e_kill, [])
        
    def calculate_local_live_variables(self):
        rev_statements = list(reversed(self.statements));
        use = [];
        def_ = [];
        for statement in rev_statements:
            # 1st step:
            if statement.var in use:
                use.remove(statement.var);
            if statement.var not in def_:
                def_.append(statement.var);
            
            # 2nd step:
            _expression_variables = statement.expression.get_variables();
            use.extend(_expression_variables);
            for var in _expression_variables:
                if var in def_:
                    def_.remove(var);
        self.def_ = def_;
        self.use = use;
        
    def calculate_very_busy_expressions(self, flow_graph):
        rev_statements = list(reversed(self.statements));
        used = [];
        killed = [];
        
        all_statements = flow_graph.get_all_definitions();
        
        for statement in rev_statements:
            used = [u for u in used if statement.var not in u.get_variables()];
            used.append(statement.expression);
            
            killed.extend([s.expression for s in all_statements if statement.var in s.expression.get_variables()])
            # remove duplicates
            killed = reduce(lambda re, x: re+[x] if x not in re else re, killed, [])
            # newly used expressions are not killed
            killed = [k for k in killed if k not in used];
            
        
        self.used = used;
        self.killed = killed;
        
        
