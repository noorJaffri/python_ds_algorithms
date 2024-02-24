from binary_search_tree import BinarySearchTree

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

    # Example usage of BFS
    start_room = 'A'
    end_room = 'F'
    print("\nShortest path from room", start_room, "to room",
          end_room, ":", bst.bfs(start_room, end_room))

    # Example usage of DFS
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    start_node = 'A'
    print("\nDFS traversal starting from node",
          start_node, ":", bst.dfs(graph, start_node))
