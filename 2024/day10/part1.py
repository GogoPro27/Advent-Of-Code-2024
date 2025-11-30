from read import read_file

class Node:
    def __init__(self, value: int,pos:tuple[int,int]):
        self.value = value
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.matrix_pos = pos

    def set_up(self, node: 'Node'):
        self.up = node

    def set_down(self, node: 'Node'):
        self.down = node

    def set_left(self, node: 'Node'):
        self.left = node

    def set_right(self, node: 'Node'):
        self.right = node


def dfs(start: Node, visited=None):
    if visited is None:
        visited = set()

    if start is None or start in visited:
        return

    # Mark the node as visited
    visited.add(start)
    # print(start.value)  # Process the node (e.g., print its value)

    # Recursively visit neighbors
    for neighbor in (start.up, start.down, start.left, start.right):
        if neighbor and neighbor not in visited and neighbor.value-start.value==1:
            dfs(neighbor, visited)

    return [v.value for v in visited].count(9)

def main():
    lines = read_file("./puzzle_input.txt")
    lines = [line.strip() for line in lines]
    # [print(line) for line in lines]
    node_dic = {}
    for i in range(0,len(lines)):
        for j in range(0,len(lines[0])):
            node = node_dic.setdefault((i,j),Node(int(lines[i][j]),(i,j)))
            if i-1 in range(len(lines)):
                node_up = node_dic.setdefault((i-1,j),Node(int(lines[i-1][j]),(i-1,j)))
                node.set_up(node_up)
            if i+1 in range(len(lines)):
                node_down = node_dic.setdefault((i+1,j),Node(int(lines[i+1][j]),(i+1,j)))
                node.set_down(node_down)
            if j-1 in range(len(lines[0])):
                node_left = node_dic.setdefault((i,j-1),Node(int(lines[i][j-1]),(i,j-1)))
                node.set_left(node_left)
            if j+1 in range(len(lines[0])):
                node_right = node_dic.setdefault((i,j+1),Node(int(lines[i][j+1]),(i,j+1)))
                node.set_right(node_right)
    total_sum=0
    for i in range(0,len(lines)):
        for j in range(0,len(lines[0])):
            if lines[i][j]=='0':
                total_sum+=dfs(node_dic[(i,j)],set())
    print(total_sum)








if __name__ == "__main__":
    main()