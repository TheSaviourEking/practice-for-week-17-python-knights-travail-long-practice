from tree import Node

BOARD_SIZE = 8


class KnightPathFinder:
    def __init__(self, coordinates):
        # self.x = coordinates[0]
        # self.y = coordinates[1]
        self._root = coordinates
        self._considered_positions = set({self._root})

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

        return set(valid_moves).difference(self._considered_positions)


if __name__ == "__main__":
    finder = KnightPathFinder((0, 0))

    # print(finder.get_valid_moves((0, 0)))
    print(finder.new_move_positions((0, 0)))
