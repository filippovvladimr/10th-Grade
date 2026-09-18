from collections import Counter
import heapq
text = "A" * 10 + "E" * 8 + "C" * 6 + "B" * 4 + "D" * 4


def get_frequencies(text):
    return Counter(text)


freq_table = get_frequencies(text)


class Node:
    def __init__(self, freq, symbol=None, left=None, right=None, order=0):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.order = order

    def __lt__(self, other): #нужен для heapq
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.order < other.order


order_counter = 0


nodes = []
for char, freq in freq_table.items():
    order_counter += 1
    nodes.append(Node(freq=freq, symbol=char, order=order_counter))

heapq.heapify(nodes)


while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    order_counter += 1
    parent = Node(
        freq=left.freq + right.freq,
        symbol=None,
        left=left,
        right=right,
        order=order_counter,
    )
    heapq.heappush(nodes, parent)

root = nodes[0]


codes = {}


def get_codes(node, current_code=""):
    if node is None:
        return
    if node.symbol is not None:
        codes[node.symbol] = current_code
        return
    get_codes(node.left, current_code + "0")
    get_codes(node.right, current_code + "1")


get_codes(root)

# Выводим букву и её код
for char in sorted(codes):
    print(f"{codes[char]}")
