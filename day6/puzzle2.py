import numpy
  
from collections import defaultdict 
import sys 
  
file = open("C:/Users/Pierre/Documents/AdventCode2019/inputs/day6.txt","r")
input = file.read().splitlines()

def list_planets(input):
    planets_list=[]
    for orbit in input:
        planets=orbit.split(")")
        for planet in planets:
            if not(planet in planets_list):
                planets_list += [planet]
    return planets_list

def list_orbits(input):

    planets_list = list_planets(input)
    orbits_list = [[] for _ in range(len(planets_list))]

    for orbit in input:
        planets=orbit.split(")")
        orbits_list[planets_list.index(planets[0])] += [planets[1]]
        orbits_list[planets_list.index(planets[1])] += [planets[0]]

        # print(planets)

    return planets_list,orbits_list

def count_orbits(input):
    planets_list,orbits_list = list_orbits(input)
    orbits_count = [0]*len(planets_list)
    for k,orbiters in enumerate(orbits_list):
        orbits_count[k] = len(orbiters)
    return planets_list, orbits_list, orbits_count

def terminal_recursive(planets_list, orbits_list, planet, result):
    if orbits_list[planets_list.index(planet)]==[]:
        return result
    else:
        current_orbits = orbits_list[planets_list.index(planet)]
        new_result = result
        for k in range(len(current_orbits)):
            subplanet = current_orbits[k]
            # print(subplanet)
            new_result = 1 + terminal_recursive(planets_list, orbits_list, subplanet, new_result)
        return(new_result)



def count_all_orbits(input, planet):
    planets_list, orbits_list, _ = count_orbits(input)
    result = terminal_recursive(planets_list, orbits_list, planet, 0)
    return result

# print(list_orbits(input)[1])
# print(count_all_orbits(input, "C"))

def shortest_path(planets_list, orbits_list, planetStart, planetEnd):
    if planetStart==planetEnd:
        return 0
    else:
        return 1 + min([shortest_path(planets_list, orbits_list, planetStart, subplanet) for subplanet in orbits_list[planets_list.index(planetStart)] ])

# planets_list, orbits_list, _ = count_orbits(input)
# print(shortest_path(planets_list, orbits_list, "YOU", "SAN"))

# A Python program for Dijkstra's shortest  
# path algorithm for adjacency 
# list representation of graph 

class Heap(): 
  
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
  
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
  
    # A utility function to swap two nodes  
    # of min heap. Needed for min heapify 
    def swapMinHeapNode(self,a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    # A standard function to heapify at given idx 
    # This function also updates position of nodes  
    # when they are swapped.Position is needed  
    # for decreaseKey() 
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2*idx + 1
        right = 2*idx + 2
  
        if left < self.size and self.array[left][1] < self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right 
  
        # The nodes to be swapped in min  
        # heap if idx is not smallest 
        if smallest != idx: 
  
            # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
  
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest) 
  
    # Standard function to extract minimum  
    # node from heap 
    def extractMin(self): 
  
        # Return NULL wif heap is empty 
        if self.isEmpty() == True: 
            return
  
        # Store the root node 
        root = self.array[0] 
  
        # Replace root node with last node 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
  
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        # Reduce heap size and heapify root 
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
  
        # Get the index of v in  heap array 
  
        i = self.pos[v] 
  
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is  
        # not hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]: 
  
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)//2 ) 
  
            # move to parent index 
            i = (i - 1) // 2; 
  
    # A utility function to check if a given  
    # vertex 'v' is in min heap or not 
    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
  
  
def printArr(dist, n, i): 
    print("Vertex\tDistance from source")
    print("%d\t\t%d" % (i,dist[i]-2) )
  
  
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = defaultdict(list) 
  
    # Adds an edge to an undirected graph 
    def addEdge(self, src, dest, weight): 
  
        # Add an edge from src to dest.  A new node  
        # is added to the adjacency list of src. The  
        # node is added at the beginning. The first  
        # element of the node has the destination  
        # and the second elements has the weight 
        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode) 
  
        # Since graph is undirected, add an edge  
        # from dest to src also 
        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode) 
  
    # The main function that calulates distances  
    # of shortest paths from src to all vertices.  
    # It is a O(ELogV) function 
    def dijkstra(self, src, k): 
  
        V = self.V  # Get the number of vertices in graph 
        dist = []   # dist values used to pick minimum  
                    # weight edge in cut 
  
        # minHeap represents set E 
        minHeap = Heap() 
  
        #  Initialize min heap with all vertices.  
        # dist value of all vertices 
        for v in range(V): 
            dist.append(sys.maxsize) 
            minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
            minHeap.pos.append(v) 
  
        # Make dist value of src vertex as 0 so  
        # that it is extracted first 
        minHeap.pos[src] = src 
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src]) 
  
        # Initially size of min heap is equal to V 
        minHeap.size = V; 
  
        # In the following loop, min heap contains all nodes 
        # whose shortest distance is not yet finalized. 
        while minHeap.isEmpty() == False: 
  
            # Extract the vertex with minimum distance value 
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0] 
  
            # Traverse through all adjacent vertices of  
            # u (the extracted vertex) and update their  
            # distance values 
            for pCrawl in self.graph[u]: 
  
                v = pCrawl[0] 
  
                # If shortest distance to v is not finalized  
                # yet, and distance to v through u is less  
                # than its previously calculated distance 
                if minHeap.isInMinHeap(v) and dist[u] != sys.maxsize and pCrawl[1] + dist[u] < dist[v]: 
                        dist[v] = pCrawl[1] + dist[u] 
  
                        # update distance value  
                        # in min heap also 
                        minHeap.decreaseKey(v, dist[v]) 

        printArr(dist,V,k) 
  
  
# Driver program to test the above functions 

planets = list_planets(input)
graph = Graph(len(planets))
for orbit in input:
    tempplanets=orbit.split(")")
    graph.addEdge(planets.index(tempplanets[0]),planets.index(tempplanets[1]),1)

graph.dijkstra(planets.index("SAN"), planets.index("YOU"))

# The Djikstra code is contributed by Divyanshu Mehta, Thank you very much 