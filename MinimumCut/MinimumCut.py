'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''
#import networkx as nx
#import matplotlib.pyplot as plt
import random
import os
# remove edge '1' 



class Graph:
    '''this class implements a graph data structure using an adjacency list representation'''
    '''the graph is represented by a list of vertices and a list of edges
    where the keys are the vertices and the values are lists of
    the vertices that are adjacent to the key vertex, no parallel edges are allowed'''
    def __init__(self, edges = list() , lut = list()) -> None:
        self.edges = edges
        self.lut = lut
        self.vertices = set(lut)
        
    def add_vertex_edges(self, vertex :str, edges : list):
        '''add a vertex to the graph'''
        pass
            
    def contract_edge(self,edge_index : int) -> int:
        lut_temp = self.lut.copy()
        edges_temp = self.edges.copy()
        node1 = lut_temp.pop(edge_index)
        node2 = edges_temp.pop(edge_index)
        
        for index in range(0,len(lut_temp)-1):
            if lut_temp[index] == node1 or lut_temp[index] == node2:
                lut_temp[index] = node1 + '-' + node2
            if edges_temp[index] == node1 or edges_temp[index] == node2:
                edges_temp[index] = node1 + '-' + node2
        self_loops_counter = 0
        for lut_index in range(0,len(lut_temp)-1):
            if edges_temp[lut_index] == lut_temp[lut_index]:
               self_loops_counter += 1
                
        self.edges = edges_temp
        self.lut = lut_temp
        self.vertices = set(self.lut)
        return self_loops_counter
    def minimum_cut(self):
        '''return the minimum cut of the graph'''
        len_vertices = len(self.vertices)
        len_edges = len(self.edges)
        while (len_vertices) != 2:
            edge_index = random.randint(0,(len_edges)-1)
            self_loops = self.contract_edge(edge_index)
            len_vertices = len(self.vertices)
            len_edges = len(self.edges)
            print(len_vertices)
            
        return len(self.edges)//2 - self_loops//2 
def main():
    '''read graph from file and contstruct a graph object'''
    graph = Graph()
    read_edges = list()
    read_lut = list()
    
    # read input files 
    input_files = [file for file in os.listdir('.') if ('input' in file)]
    output_files = [file.replace('input','output') for file in input_files ]
    results_valid = list()
    results_min_cut = list()
    #for file in input_files:
    base_dir = os.getcwd()
    mincut_folder = 'MinimumCut'
    mincut_folder = ''
    file = 'input_random_9_25.txt'
    file = os.path.join(base_dir,mincut_folder,file)
    print("input ",file)
    with open(file) as f:
            for line in f:
                line = line.split()
                for index, element in enumerate(line):
                    if index == 0:
                        for edge in range(0,len(line[1:])): 
                            read_lut.append(element)
                    else:
                        read_edges.append(element)
                        
    cuts = list()
    for run in range(2):
            test_graph = Graph(read_edges,read_lut)
            cuts.append((test_graph.minimum_cut()))
    with open(file.replace('input','output')) as f:
        for line in f:
            results_valid.append(line[0])
    print("Difference in the Results: ",min(cuts)-int(line[0]))
    results_min_cut.append(min(cuts))
        
        
        
       
    
if __name__ == "__main__":
    main()



