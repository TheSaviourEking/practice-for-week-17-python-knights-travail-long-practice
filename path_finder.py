from tree import Node

BOARD_SIZE = 8


class KnightPathFinder:
    def __init__(self, coordinates):
        self._root = Node(coordinates)
        self._considered_positions = set()
        self._considered_positions.add(coordinates)

    def get_valid_moves(self, position):
        valid_moves = []
        x, y = position

        knight_moves = [
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ]

        # Iterate through all knight moves
        for move in knight_moves:
            new_x, new_y = x + move[0], y + move[1]

            # Assuming we only allow positions with non-negative coordinates
            if 0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE:
                valid_moves.append((new_x, new_y))

        return valid_moves

    def new_move_positions(self, position):
        valid_moves = self.get_valid_moves(position)

        new_moves = set(valid_moves).difference(self._considered_positions)
        self._considered_positions.update(new_moves)
        return new_moves

    # def build_move_tree(self):
    #     positions = self.new_move_positions(self._root.value)

    #     for value in positions:
    #         self._root.add_child(Node(value))

    #     return self._root

    def build_move_tree(self):
        queue = [self._root]
        count = 0

        while queue:
            count += 1
            current_node = queue.pop(0)
            new_positions = self.new_move_positions(current_node.value)

            for pos in new_positions:
                new_node = Node(pos)
                current_node.add_child(new_node)

                queue.append(new_node)

        return queue

    # def build_move_tree(self):
    #     moves = [self._root]

    #     while moves:
    #         current = moves[0]
    #         position = current.value
    #         new_moves = self.new_move_positions(position)

    #         for move in new_moves:
    #             node = Node(move)
    #             current.add_child(node)
    #             moves.append(node)

    #         moves.pop(0)

    def find_path(self, end_position):
        end_node = self._root.breadth_search(end_position)
        if end_node:
            return self.trace_to_root(end_node)

    def trace_to_root(self, end_node):
        if isinstance(end_node, Node):
            path = []
            current = end_node
            while current:
                path.append(current.value)
                current = current.parent

            # return list(reversed(path))
            return path[::-1]


if __name__ == "__main__":
    finder = KnightPathFinder((0, 0))
    # finder = KnightPathFinder((2, 0))

    print(finder.get_valid_moves((0, 0)))
    print(finder.new_move_positions((0, 0)))

    finder.build_move_tree()
    print(finder._root.children)
    print(finder.find_path((2, 1)))  # => [(0, 0), (2, 1)]
    print(finder.find_path((3, 3)))  # => [(0, 0), (2, 1), (3, 3)]
    print(finder.find_path((6, 2)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
    print(
        finder.find_path((7, 6))
    )  # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
