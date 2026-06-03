"""
Approach: Given a graph, we have to clone the graph i.e make a new instance of each node and set a graph of those nodes.
This is exactly like the deep copy we made in linked list of "Copy List with Random Pointer"
But there, just iterating straight through the next nodes guarentee that we have made visited and made copy of each node
But it's not the same for graphs which are acyclic. Such graphs are not connected in a loop. 
For eg:
A-B-C
|
D

Here, suppose we went to B from A. Now there is no way we reach D
Also if:
A--B
|  |
|--C
D

Here though we go to B from A, there is still a chance of going to D from C. But what if we go to A isntead?
(choosing where to go based on the first neighbor)

That's why we have to make sure that we go to each of the neighbors of a node straight from that node. 
This is why we have to setup a extra data structure for this purpose such as a stack or a recursion.
"""

#With Stack
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None
    cpyMap = {node: Node(node.val)}
    stack = [node]
    while stack:
        curr = stack.pop()
        for neighbor in curr.neighbors:
            if neighbor not in cpyMap:
                cpyMap[neighbor] = Node(neighbor.val)
                stack.append(neighbor)
            cpyMap[curr].neighbors.append(cpyMap[neighbor])
    return cpyMap[node]


#With Recursion
cpyMap = {}
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None
    if node in self.cpyMap:
        return self.cpyMap[node] 
    self.cpyMap[node] = Node(node.val)
    for neighbor in node.neighbors:
        neighborNode = self.cloneGraph(neighbor)
        self.cpyMap[node].neighbors.append(neighborNode)
    return self.cpyMap[node]
