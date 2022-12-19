import sys
import logging
import networkx as nx
from TrenchLength import getTrenchLength
from RateCards import rateCardA, rateCardB

G = ""
try:
    G = nx.read_graphml('problem.graphml')
except Exception as e:
    print("graphml file error")
    logging.exception(e)
    sys.exit(1)


def calcRateCardA():
    total_rateCard_A = 0
    for node in G.nodes(data=True):
        value = rateCardA()[node[1]["type"]]
        total_rateCard_A += value

    for edge in G.edges(data=True):
        value = rateCardA(edge[2]["length"])[edge[2]["material"]]
        total_rateCard_A += value

    return total_rateCard_A


def calcRateCardB():
    total_rateCard_B = 0
    for node in G.nodes(data=True):
        root = [x for x, y in G.nodes(data=True) if y['type'] == "Cabinet"]
        trenchLength = getTrenchLength(G, root[0], node[0])
        value = rateCardB(1, trenchLength)[node[1]["type"]]
        total_rateCard_B += value

    for edge in G.edges(data=True):
        value = rateCardB(edge[2]["length"])[edge[2]["material"]]
        total_rateCard_B += value

    return total_rateCard_B


print("total_from_rateCard_A", calcRateCardA())
print("total_from_rateCard_B", calcRateCardB())
