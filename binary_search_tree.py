from collections import deque


class BinarySearchTree:
    """Binary Search Tree implementation."""

    class TreeNode:
        """Node structure for the Binary Search Tree."""

        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    def __init__(self):
        """Initialize an empty Binary Search Tree."""
        self.root = None

    def insert(self, key):
        """
        Insert a key into the Binary Search Tree.

        Args:
            key: The key to insert into the tree.
        """
        def insert_node(node, key):
            if node is None:
                return self.TreeNode(key), True
            else:
                if key < node.val:
                    node.left, success = insert_node(node.left, key)
                elif key > node.val:
                    node.right, success = insert_node(node.right, key)
                else:
                    success = False
            return node, success

        self.root, success = insert_node(self.root, key)
        return success

    def delete(self, key):
        """
        Delete a key from the Binary Search Tree.

        Args:
            key: The key to delete from the tree.
        """
        def delete_node(root, key):
            if root is None:
                return root
            if key < root.val:
                root.left = delete_node(root.left, key)
            elif key > root.val:
                root.right = delete_node(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                temp = self.min_value_node(root.right)
                root.val = temp.val
                root.right = delete_node(root.right, temp.val)
            return root

        return delete_node(self.root, key)

    def min_value_node(self, node):
        """
        Find the node with the minimum value in the subtree rooted at the given node.

        Args:
            node: The root node of the subtree.

        Returns:
            The node with the minimum value in the subtree.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        """
        Search for a key in the Binary Search Tree.

        Args:
            key: The key to search for.

        Returns:
            The node containing the key if found, otherwise None.
        """
        def search_node(root, key):
            if root is None or root.val == key:
                return root
            if root.val < key:
                return search_node(root.right, key)
            return search_node(root.left, key)

        return search_node(self.root, key)

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the Binary Search Tree.

        Returns:
            A list containing the keys in sorted order.
        """
        def inorder(root):
            result = []
            if root:
                result += inorder(root.left)
                result.append(root.val)
                result += inorder(root.right)
            return result

        return inorder(self.root)

    def preorder_traversal(self):
        """
        Perform a preorder traversal of the Binary Search Tree.

        Returns:
            A list containing the keys in preorder traversal order.
        """
        def preorder(root):
            result = []
            if root:
                result.append(root.val)
                result += preorder(root.left)
                result += preorder(root.right)
            return result

        return preorder(self.root)

    def postorder_traversal(self):
        """
        Perform a postorder traversal of the Binary Search Tree.

        Returns:
            A list containing the keys in postorder traversal order.
        """
        def postorder(root):
            result = []
            if root:
                result += postorder(root.left)
                result += postorder(root.right)
                result.append(root.val)
            return result

        return postorder(self.root)

    def left_rotate(self):
        """Perform a left rotation on the Binary Search Tree."""
        def rotate(node):
            new_root = node.right
            node.right = new_root.left
            new_root.left = node
            return new_root

        self.root = rotate(self.root)

    def right_rotate(self):
        """Perform a right rotation on the Binary Search Tree."""
        def rotate(node):
            new_root = node.left
            node.left = new_root.right
            new_root.right = node
            return new_root

        self.root = rotate(self.root)

    def bfs(start, end):
        """
        Find the shortest path from start to end in a graph.

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

    def dfs(self, graph, node, visited=[]):
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
                self.dfs(graph, neighbor, visited)

        return visited
