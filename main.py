from basicBlock import BasicBlock
from flowGraph import FlowGraph

separator = '\n----------------\n'

def ex3():
    b1 = BasicBlock('B1', 'a = 4', 'c = d + e', 'c = c + 5');
    b2 = BasicBlock('B2', 'b = e/7', 'a = 2*a');
    b3 = BasicBlock('B3', 'e = 3', 'b = e + 1');
    b4 = BasicBlock('B4', 'd = 2 - c', 'a = 6');
    b5 = BasicBlock('B5', 'c = 2 - c');
    b6 = BasicBlock('B6', 'e = 2*a', 'b = c + 5');
    b7 = BasicBlock('B7', 'e = d + e');
    
    flow_graph = FlowGraph()
    
    flow_graph.add_edge(b1, b2);
    flow_graph.add_edge(b2, b3);
    flow_graph.add_edge(b3, b4);
    flow_graph.add_edge(b3, b5);
    flow_graph.add_edge(b4, b6);
    flow_graph.add_edge(b4, b7);
    flow_graph.add_edge(b5, b2);
    flow_graph.add_edge(b6, b3);
        
    flow_graph.calculate_reaching_definitions();
    flow_graph.calculate_available_expressions();
    flow_graph.calculate_very_busy_expressions();
    flow_graph.calculate_live_variables();
    
    print('Reaching Definitions:')
    for bb in flow_graph.basic_blocks:
        if isinstance(bb, BasicBlock):
            bb.print_reaching_definitions();
    print(separator);
    
    print('Available Expressions:')
    for bb in flow_graph.basic_blocks:
        if isinstance(bb, BasicBlock):
            bb.print_available_expressions();
    print(separator);
    
    print('Very Busy Expressions:')
    for bb in flow_graph.basic_blocks:
        if isinstance(bb, BasicBlock):
            bb.print_very_busy_expressions();
    print(separator);
    
    print('Live Variables:')
    for bb in flow_graph.basic_blocks:
        if isinstance(bb, BasicBlock):
            bb.print_live_variables();
    print(separator);

def main():
    ex3();


if __name__ == "__main__":
    main();