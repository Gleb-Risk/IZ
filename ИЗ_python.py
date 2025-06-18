class Node:
    def __init__(self, color):
        self.color = color
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, colors):
        self.head = None
        self.tail = None

        for color in colors:
            self.append(color)

    def append(self, color):
        node = Node(color)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove_segment(self, start, end):
        prev_node = start.prev
        next_node = end.next

        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        return prev_node  # возвращаем предыдущий узел для проверки новых цепочек


class BallGame:
    def __init__(self, colors):
        self.list = DoublyLinkedList(colors)

    def removal(self):
        removed_count = 0
        current = self.list.head

        while current:
            start = current
            length = 1
            while current.next and current.next.color == current.color:
                current = current.next
                length += 1

            if length >= 3:
                prev_node = self.list.remove_segment(start, current)
                removed_count += length
                current = prev_node  # продолжаем с предыдущего узла
            else:
                current = current.next

        return removed_count

    def play_game(self):
        total_removed = 0
        while True:
            removed = self.removal()
            if removed == 0:
                break
            total_removed += removed
        return total_removed


def main():
    print("   Добро пожаловать в игру:")
    print("           \"Шарики\"")
    print()

    colors = []

    while True:
        line = input("Введите последовательность: <n> <цвет1> <цвет2> ... (цвета от 0 до 9): ").strip()
        try:
            data = list(map(int, line.split()))
        except ValueError:
            print("Ошибка: введите только целые числа.")
            print("Попробуйте ещё раз")
            continue

        if len(data) < 1:
            print("Ошибка: не введено ни одного числа.")
            print("Попробуйте ещё раз")
            continue

        n = data[0]
        colors = data[1:]

        if len(colors) != n:
            print(f"Ошибка: должно быть указано ровно {n} цветов, получено {len(colors)}.")
            print("Попробуйте ещё раз")
            continue

        if any(not (0 <= c <= 9) for c in colors):
            print("Ошибка: цвет должен быть целым числом от 0 до 9.")
            print("Попробуйте ещё раз")
            continue

        break

    game = BallGame(colors)
    destroyed = game.play_game()

    print(f"\nУничтожено шариков: {destroyed}")
    print("Спасибо за игру!")


if __name__ == "__main__":
    main()
