from op_tree import OpTree
class Equation:
    def __init__(self, line):
        parts = line.split(":")
        self.target = int(parts[0])
        self.components = [int(component) for component in parts[1].split()]

    def build_op_tree(self):
        reversed = self.components.copy()
        reversed.reverse()
        tree = self._build_subtree(reversed)
        tree.is_root = True
        return tree

    def _build_subtree(self, components):
        if components == []:
            return None
        node = components[0]
        subtree = self._build_subtree(components[1:])
        return OpTree(node, subtree)
        

    def is_satisfied(self):
        tree = self.build_op_tree()
        vals = tree.walk_tree()
        return self.target in vals
