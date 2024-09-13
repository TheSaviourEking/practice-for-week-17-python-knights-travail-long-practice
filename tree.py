class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)

            if node.parent:
                node.parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None

    @property
    def parent(self):
        return self._parent

    # @parent.setter
    # def parent(self, node):
    #     if node:
    #         if self.parent:
    #             self.parent.remove_child(self)
    #         self.parent = node
    #         node.add_child(self)

    @parent.setter
    def parent(self, new_parent):
        if self._parent is not new_parent:
            old_parent = self._parent
            self._parent = new_parent

            if old_parent:
                old_parent.children.remove(self)
            if new_parent:
                new_parent.add_child(self)

    # RECURSIVE SOLUTION
    def depth_search(self, value):
        if self._value == value:
            return self

        for child in self._children:
            result = child.depth_search(value)
            if result is not None:
                return result
        return None

    # ITERATIVE SOLUTION
    # def depth_search(self, target):
    #     visited = set()
    #     stack = [self]

    #     while stack:
    #         vertex = stack.pop()

    #         if vertex.value == target:
    #             return vertex

    #         if vertex not in visited:
    #             visited.add(vertex)
    #             for child in reverse(vertex.children):
    #                 if child not in visited:
    #                     stack.append(child)

    #     return None

    def breadth_search(self, value):
        queue = [self]
        visited = set()

        while queue:
            vertex = queue.pop(0)

            if vertex.value == value:
                return vertex

            if vertex not in visited:
                visited.add(vertex)

                for child in vertex.children:
                    if child not in visited:
                        queue.append(child)

        return None


if __name__ == "__main__":
    node1 = Node("root1")
    node2 = Node("root2")
    node3 = Node("root3")

    node3.parent = node1
    node3.parent = node2

    child1 = Node("child1")
    parent = Node("parent")
    child2 = Node("child2")

    child1.parent = parent
    child2.parent = parent

    child1.add_child(child2)
    print(list(child1.children), [child2])

    print(node1.children, '[]')
    print(node2.children, "[node-3]")
    print(node3.parent, 'node-2\n', node3, 'node-3\n')
    print(node2, 'node-2\n', node1, 'node-1')

    print(node2.depth_search("root3"))
