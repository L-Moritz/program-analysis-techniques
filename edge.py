from basicBlock import BasicBlock


class Edge:
    source: BasicBlock;
    target: BasicBlock;
    def __init__(self, source: BasicBlock, target: BasicBlock):
        self.source = source;
        self.target = target;