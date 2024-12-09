class OpTree:
    def __init__(self, value, subtree):
        self.value = value
        self.subtree = subtree
        self.is_root = False

    def walk_tree(self):
        if self.subtree is None:
            return [self.value]

        subtree_vals = self.subtree.walk_tree()
        # if self.subtree_vals is None
        #     self.subtree_vals = self.subtree.walk_tree()

        mul_vals = [self.value * val for val in subtree_vals]
        plu_vals = [self.value + val for val in subtree_vals]
        cat_vals = [int(str(val) + str(self.value)) for val in subtree_vals]
        return mul_vals + plu_vals + cat_vals