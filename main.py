from binary_search_tree import BinarySearchTree
from collections import deque


def bfs(start, end):
    """
    Find the shortest path from start to end in a graph using Breadth-First Search (BFS).

    Args:
        start (str): The starting node.
        end (str): The ending node.

    Returns:
        list: The shortest path from start to end.
    """
    rooms = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C', 'F'],
        'F': ['E']
    }
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in rooms[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))


def dfs(graph, node, visited=[]):
    """
    Perform Depth-First Search (DFS) traversal on a graph.

    Args:
        graph (dict): The graph represented as an adjacency list.
        node (str): The starting node for DFS.
        visited (list, optional): A list to track visited nodes. Defaults to [].

    Returns:
        list: The visited nodes in DFS order.
    """
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

    return visited


if __name__ == "__main__":
    # Example usage of BinarySearchTree
    bst = BinarySearchTree()
    keys = [5, 3, 7, 1, 4, 6, 8]
    for key in keys:
        success = bst.insert(key)
        if success:
            print(f"Insertion of {key} successful.")
        else:
            print(f"Insertion of {key} failed. Key already exists.")

    print("\nPerforming inorder traversal of the Binary Search Tree...")
    print("Inorder Traversal:", bst.inorder_traversal())

    print("\nPerforming preorder traversal of the Binary Search Tree...")
    print("Preorder Traversal:", bst.preorder_traversal())

    print("\nPerforming postorder traversal of the Binary Search Tree...")
    print("Postorder Traversal:", bst.postorder_traversal())

    # Example usage of deleting a node
    key_to_delete = 3
    deleted = bst.delete(key_to_delete)
    if deleted:
        print(f"\nDeletion of {key_to_delete} successful.")
    else:
        print(f"\nDeletion of {key_to_delete} failed. Key not found.")

    # Example usage of searching for a node
    key_to_search = 7
    node = bst.search(key_to_search)
    if node:
        print(f"\nFound node with key {key_to_search}.")
    else:
        print(f"\nNode with key {key_to_search} not found.")

    # Example usage of left rotation
    print("\nPerforming left rotation on the Binary Search Tree...")
    bst.left_rotate()
    print("Inorder Traversal after left rotation:", bst.inorder_traversal())

    # Example usage of right rotation
    print("\nPerforming right rotation on the Binary Search Tree...")
    bst.right_rotate()
    print("Inorder Traversal after right rotation:", bst.inorder_traversal())
