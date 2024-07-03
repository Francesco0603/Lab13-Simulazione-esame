import copy

from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.avvistamenti = DAO.getSights()
        self.stati = DAO.getStates()
        self.archi = DAO.getArchi()
        self.stateMap = {}
        self.anni = []
        self.forme = []
        self.distMap = {}
        self.grafo = nx.Graph()


    def creaGrafo(self,anno,forma):
        for s in self.stati:
            self.stateMap[s.__hash__()] = s
            self.grafo.add_node(s.__hash__())
        for e in self.archi:
            self.grafo.add_edge(e[0],e[1],weight=DAO.getPeso(anno,forma,e[0],e[1])[0])
        print(self.grafo.number_of_nodes())
        print(self.grafo.number_of_edges())
    def cercaPercorso(self):
        self.dMax = 0
        self.bestPercorso = []
        self.ricorsione([],0,0)
        return self.dMax, self.bestPercorso
    def ricorsione(self,parziale,peso,distanza):
        if len(parziale) == 0:
            for n in self.grafo.nodes:
                parziale.append(n)
                self.ricorsione(parziale,peso,distanza)
                parziale.pop()
        else:
            if self.dMax < distanza:
                self.dMax = distanza
                self.bestPercorso = copy.deepcopy(parziale)
                print(self.dMax)
                print(parziale)
            for n in self.grafo.neighbors(parziale[-1]):
                if n in parziale:
                    continue
                if len(parziale) != 1 and self.grafo[parziale[-2]][parziale[-1]]["weight"] <= self.grafo[parziale[-1]][n]["weight"]:
                    continue
                peso += self.grafo[parziale[-1]][n]["weight"]
                distanza += DAO.getDistanza(parziale[-1],n)[0]
                self.distMap[(parziale[-1],n)] = DAO.getDistanza(parziale[-1],n)[0]
                parziale.append(n)
                print(distanza)
                self.ricorsione(parziale, peso, distanza)
                parziale.pop()
                peso -= self.grafo[parziale[-1]][n]["weight"]
                distanza -= self.distMap[(parziale[-1],n)]





