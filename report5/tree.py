# FROM: https://github.com/dileepnandanam/huffman-coding/blob/master/huff.py

from pprint import pprint as pp

class Fork:  # The node in Huffman tree
    def __init__(self, chars, weight, left=None, right=None):  # optional parameters are None for Leaf nodes
        self.chars = chars
        self.weight = weight

        self.left = left
        self.right = right

    def __add__(self, right):  # combine two nodes to form a parent node
        return (Fork(self.chars + right.chars, self.weight + right.weight, self, right))


class Compressor:

    def __init__(self, source=None):
        if source:
            self.codeTree = self.makeCodeTree(source)
            self.codeTable = self.makeCodeTable(self.codeTree)
            print("Tree optimised for encoding", source, "created")
            print("code table:", self.codeTable)
        else:
            self.codeTree = None
            self.codeTable = None

    def encode(self, string, tree=None):
        tree = self.codeTree

        def encode0(s, node, op):
            if s == '':
                return op
            elif node.left == None:
                return encode0(s[1:], tree, op)
            elif s[0] in node.left.chars:
                return encode0(s, node.left, op + '0')
            else:
                return encode0(s, node.right, op + '1')

        return encode0(string, tree, "")

    def decode(self, string, tree=None):
        if tree == None:
            tree = self.codeTree

        def decode0(s, node, op):
            if s == "":
                return (op + node.chars)
            elif node.left == None:
                return (decode0(s, tree, op + node.chars))
            elif s[0] == '0':
                return (decode0(s[1:], node.left, op))
            else:
                return (decode0(s[1:], node.right, op))

        return (decode0(string, tree, ""))

    def makeCodeTree(self, Representingstring):  # generate tree for a given sample

        def freq(s):
            frq = {}
            for i in s:
                if i in frq:
                    frq[i] = frq[i] + 1
                else:
                    frq[i] = 1

            return (frq)

        nodes = sorted([Fork(i, j) for (i, j) in freq(Representingstring).items()], key=lambda x: x.weight)
        while len(nodes) > 1:
            nodes = sorted(([nodes[0] + nodes[1]] + nodes[2:]), key=lambda x: x.weight)
        return (nodes[0])

    def makeCodeTable(self, codeTree):
        def makeCodeTable0(tree):
            if tree.left == None:
                return [(tree.chars, '')]
            rTable = makeCodeTable0(tree.right)
            lTable = makeCodeTable0(tree.left)
            return [(i, '0' + j) for (i, j) in lTable] + [(i, '1' + j) for (i, j) in rTable]

        codeTable = makeCodeTable0(codeTree)
        codeTable0 = {}
        for (i, j) in codeTable:
            codeTable0[i] = j
        return (codeTable0)

    def quickEncode(self, string, codeTable=None):
        if codeTable == None:
            codeTable = self.codeTable
        for i in string:
            yield codeTable[i]


def test():
    c = Compressor("A Web Simulation of Medical Image Reconstruction and Processing as an Educational Tool\n Abstract\n Background")
    pp(c)
    print(type(c))
test()
