# 1. 전위순회
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])  # 좌
        preorder(tree[root][1])  # 우

# 2. 중위순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0])   # 좌
        print(root, end='')
        inorder(tree[root][1])   # 우

# 3. 후위순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

# 메인
n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()