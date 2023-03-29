from tree import *
from minimax import *
from gui import *
from game import *

def tree_init():
    tree = Tree(None, None, None)

def tree_instanciation():
    print("Tree 1: ")
    tree = Tree(3, None, None)
    tree.print_tree(1)

    print("Tree 2: ")
    tree2 = Tree(3, None, Tree(4, None, None))
    tree2.print_tree(2)

    print("Tree 3: ")
    tree3 = Tree(3, Tree(2, None, Tree(5, None, None)), Tree(4, None, None))
    tree3.print_tree(3)

def tree_max_depth_search():
    print("Search 1: ")
    tree = Tree(3, None, None)
    print(tree.depth_search())

    print("Search 2: ")
    tree2 = Tree(4, None, Tree(3, None, None))
    print(tree2.depth_search())

    print("Search 3: ")
    tree3 = Tree(3, Tree(2, None, Tree(5, None, None)), Tree(4, None, None))
    print(tree3.depth_search())

def appending_to_tree():
    print("append 1: ")
    tree = Tree(None, None, None)
    tree.append_to_tree(1)
    tree.print_tree(1)

    print("append 2: ")
    tree = Tree(3, None, None)
    tree.append_to_tree(1)
    tree.print_tree(1)

    print("append 3: ")
    tree = Tree(3, Tree(2, None, None), Tree(3, None, None))
    tree.append_to_tree(2)
    tree.append_to_tree(5)
    tree.print_tree(1)

def minimax_init():
    minimax = Minimax()

def gui_init():
    gui = Gui()

def board_init():
    board = Game()

tree_init()
minimax_init()
gui_init()
tree_instanciation()
tree_max_depth_search()
appending_to_tree()
board_init()