class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_binary_tree(input_list):
    node_dict = {}

    # 주어진 리스트를 순회하면서 노드를 생성하고 딕셔너리에 저장합니다.
    for item in input_list:
        values = item.split()  # 각 항목을 분리하여 값을 가져옵니다.
        parent_value, left_value, right_value = values

        # 부모 노드 생성 또는 가져오기
        if parent_value not in node_dict:
            parent_node = TreeNode(parent_value)
            node_dict[parent_value] = parent_node
        else:
            parent_node = node_dict[parent_value]

        # 왼쪽 자식 노드 생성 또는 가져오기
        if left_value != '.':
            left_node = TreeNode(left_value)
            parent_node.left = left_node
            node_dict[left_value] = left_node

        # 오른쪽 자식 노드 생성 또는 가져오기
        if right_value != '.':
            right_node = TreeNode(right_value)
            parent_node.right = right_node
            node_dict[right_value] = right_node

    # 루트 노드 반환
    return node_dict['A']


def preorder_traversal(node):
    if node is not None:
        print(node.value, end='')
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end='')
        inorder_traversal(node.right)


def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end='')


if __name__ == "__main__":
    N = int(input())
    inputs = []
    for i in range(N):
        char = input()
        inputs.append(char)

    root = create_binary_tree(inputs)
    print(inputs)

    preorder_traversal(root)
    print("")
    inorder_traversal(root)
    print("")
    postorder_traversal(root)
