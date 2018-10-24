class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

node10=TreeNode(10)
node9=TreeNode(9)
node20=TreeNode(20)
node15=TreeNode(15)
node35=TreeNode(35)

# tree
root=node10
root.left=node9
root.right=node20
node20.left=node15
node20.right=node35

#先序遍历  先访问根节点，然后访问左节点，最后访问右节点(根->左->右)
print("先序遍历")
def b_serch(treeNode):
    if not treeNode is None:
        print(str(treeNode.val)+"->",end='')
        b_serch(treeNode.left)
        b_serch(treeNode.right)

b_serch(root)
print()

#中序遍历  先访问左节点，然后访问根节点，最后访问右节点(左->根->右)
print("中序遍历")
def c_serch(treeNode):
    if not treeNode is None:
        c_serch(treeNode.left)
        print(str(treeNode.val)+"->" ,end='')
        c_serch(treeNode.right)
    
c_serch(root)
print()


#后序遍历  先访问左节点，然后访问右节点，最后访问根节点(左->右->根)
print("后序遍历")
def a_serch(treeNode):
    if not treeNode is None:
        a_serch(treeNode.left)
        a_serch(treeNode.right)
        print(str(treeNode.val)+"->" ,end='')
    
a_serch(root)
print()

# 二叉查找树(binary search tree)
# 定义：当前根节点的左边全部比根节点小，当前根节点的右边全部比根节点大。
# 往往我们动态创建二叉树都是创建二叉查找树

def create_binary_search_tree(treeNode,val):

    if(val<treeNode.val):
        if treeNode.left is None:
            treeNode.left=TreeNode(val)
        else:
            create_binary_search_tree(treeNode.left,val)
    
    if(val>treeNode.val):
        if treeNode.right is None:
            treeNode.right=TreeNode(val)
        else:
            create_binary_search_tree(treeNode.right,val)

def create_binary_search_tree_while(treeNode,val):
    root=treeNode
    while root is not None:
        if val<root.val:
            if root.left is None:
                root.left=TreeNode(val)
                return
            else:
                root=treeNode.left
        
        if val>root.val:
            if root.right is None:
                root.right=TreeNode(val)
                return
            else:
                root=treeNode.right

l=[3,2,1,4,5]
root=TreeNode(3)
for val in l[1:5]:
    create_binary_search_tree_while(root,val)

print (root)
print()
print (b_serch(root))
print()
print (c_serch(root))
print()

# 查询二叉树深度 
# 查询树的深度我们可以这样想：左边的子树和右边的字数比，谁大就返回谁，那么再接上根节点+1就可以了

def getHeight(treeNode):
    if treeNode is None:
        return 0
    
    leftHeight=getHeight(treeNode.left)
    rightHeight=getHeight(treeNode.right)

    return max(leftHeight,rightHeight)+1

print("树的深度是："+str(getHeight(root)))
print()

# 查询树的最大值
# 从上面先序遍历二叉查找树的时候，细心的同学可能会发现：中序遍历二叉查找树得到的结果是排好顺序的～
# 那么，如果我们的二叉树不是二叉查找树，我们要怎么查询他的最大值呢？

def getMaxVal(treeNode):
    if treeNode.left is None and treeNode.right is None:
        return treeNode.val
    if treeNode.left is None:
        return getMaxVal(treeNode.right)
    if treeNode.right is None:
        return getMaxVal(treeNode.left)
    return max(getMaxVal(treeNode.right),getMaxVal(treeNode.left))

def getMaxVal2(treeNode):
    if treeNode is None:
        return 0
    return max(getMaxVal(treeNode.right),getMaxVal(treeNode.left),treeNode.val)

print("最大值是："+str(getMaxVal(root)))
print("最大值2是："+str(getMaxVal2(root)))
print()