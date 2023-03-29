

class Tree:
    def __init__(self, head, lNode, rNode) -> None:
        self.head = head
        self.lSon = lNode
        self.rSon = rNode

    def print_tree(self, start_indent):
        if(self.head !=None):
            print(self.head)
            print("|")
        if(self.lSon != None):
            #change this
            for i in range (0, start_indent):
                print(" ", end='')
            self.lSon.print_tree(start_indent+1)
        if(self.rSon != None):
            #change this
            for i in range (0, start_indent):
                print(" ", end='')
            self.rSon.print_tree(start_indent+1)

    def append_to_tree(self, node):
        if self.head:
            if node < self.head:
                if self.lSon == None:
                    self.lSon = Tree(node, None, None)
                else:
                    self.lSon.append_to_tree(node)
            else:
                if self.rSon == None:
                    self.rSon = Tree(node, None, None)
                else:
                    self.rSon.append_to_tree(node)
        else:
            self.head = node


    #retrieve max from tree
    def depth_search(self, depth=0, max=0):
        tempMax = max
        if(self.head !=None):
            if tempMax < self.head:
                tempMax = self.head
        if(self.lSon != None):
            tempMax = self.lSon.depth_search(depth, tempMax)
            if tempMax < max:
                tempMax = max
        if(self.rSon != None):
            tempMax = self.rSon.depth_search(depth, tempMax)
            if tempMax < max:
                tempMax = max
        return tempMax
       