from basicBlock import BasicBlock
from edge import Edge
from variable import Variable


class FlowGraph:
    edged: list;
    
    basic_blocks: list;
    
    def __init__(self):
        self.edged = [];
        self.basic_blocks = [];
        
    def add_edge(self, source: BasicBlock, target: BasicBlock):
        self.edged.append(Edge(source, target));
        if source not in self.basic_blocks:
            self.basic_blocks.append(source);
        if target not in self.basic_blocks:
            self.basic_blocks.append(target);
            
    def get_definitions(self, var: Variable):
        definitions = self.get_all_definitions();
        res = []
        for definition in definitions:
            if definition.var == var:
                res.append(definition);
        return res;
    
    def get_in_definition(self, var: Variable):
        res = [];
        for definition in self.get_all_definitions():
            if definition.expression.contains(var):
                res.append(definition);
        return res;
                
    
    def get_all_definitions(self):
        defs = [];
        for bb in self.basic_blocks:
            defs.extend(bb.statements);
        return defs;
            
    def calculate_reaching_definitions(self):
        for bb in self.basic_blocks:
            if isinstance(bb, BasicBlock):
                bb.calculate_local_reaching_definitions(self);
        # TODO global flow graph analysis
    
    def calculate_available_expressions(self):
        for bb in self.basic_blocks:
            if (isinstance(bb, BasicBlock)):
                bb.calculate_local_available_expressions(self);
        # TODO global flow graph analysis
        
    def calculate_live_variables(self):
        for bb in self.basic_blocks:
            if (isinstance(bb, BasicBlock)):
                bb.calculate_local_live_variables();
        # TODO global flow graph analysis
        
    def calculate_very_busy_expressions(self):
        for bb in self.basic_blocks:
            if (isinstance(bb, BasicBlock)):
                bb.calculate_very_busy_expressions(self);
        # TODO global flow graph analysis