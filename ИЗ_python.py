class Node:
    def __init__(self, color):
        self.color = color
        self.prev = None
        self.next = None


class BallGame:
    def __init__(self, colors):
        # Создаем двусвязный список
        self.head = None
        self.tail = None
        for color in colors:
            node = Node(color)
            if not self.head:
                self.head = node
            else:
                self.tail.next = node
                node.prev = self.tail
            self.tail = node

    def removal(self):
        removed_count = 0
        current = self.head

        while current:
            start = current
            length = 1
            while current.next and current.next.color == current.color:
                current = current.next
                length += 1

            if length >= 3:
                # Удалить группу
                prev_node = start.prev
                next_node = current.next

                # Связываем соседей
                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node

                if next_node:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node

                removed_count += length
                # Остаемся на предыдущем узле, чтобы проверить новые цепочки
                current = prev_node
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

    n = None
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


"""
Введите последовательность: <n> <цвет1> <цвет2> ... (цвета от 0 до 9): 10 2 3 4 
Ошибка: должно быть указано ровно 10 цветов, получено 3.
Попробуйте ещё раз...
"""

"""
Введите последовательность: <n> <цвет1> <цвет2> ... (цвета от 0 до 9): 3 12 3 4
Ошибка: цвет должен быть целым числом от 0 до 9.
Попробуйте ещё раз...
"""

"""
Введите последовательность: <n> <цвет1> <цвет2> ... (цвета от 0 до 9): 8 1 1 2 2 2 1 9 3

Уничтожено шариков: 6
Спасибо за игру!
"""

"""
Введите последовательность: <n> <цвет1> <цвет2> ... (цвета от 0 до 9): 
Ошибка: не введено ни одного числа.
Попробуйте ещё раз...
"""

"""
Введите последовательность: <n> <цвет1> <цвет2> ... (цвета от 0 до 9): 5
Ошибка: должно быть указано ровно 5 цветов, получено 0.
Попробуйте ещё раз
"""

"""
Введите последовательность: <n> <цвет1> <цвет2> ... (цвета от 0 до 9): 5 3 3 3 3 1

Уничтожено шариков: 4
Спасибо за игру!
"""
