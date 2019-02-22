def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()

def postorder(self):
    if self.rightChild:
        self.rightChild.postorder()
    if self.leftChild:
        self.leftChild.postorder()
    print(self.key)

def inorder(self):
    if self.leftChild:
        self.leftChild.inorder()
    print(self.key)
    if self.rightChild:
        self.rightChild.inorder()

