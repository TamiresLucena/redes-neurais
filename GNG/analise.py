from gng import GrowingNeuralGas
from sklearn import datasets, metrics
import networkx as nx
import random

__authors__ = 'Adrien Guille'
__email__ = 'adrien.guille@univ-lyon2.fr'


def evaluate_on_digits():
    # digits = datasets.load_iris()
    #digits = datasets.load_wine()
    digits = datasets.load_breast_cancer()

    data = digits.data
    target = digits.target
    gng = GrowingNeuralGas(data)
    gng.fit_network(e_b=0.05, e_n=0.006, a_max=10, l=20, a=0.5, d=0.995, passes=15, plot_evolution=False)
    clustered_data = gng.cluster_data()
    print('Found %d clusters.' % nx.number_connected_components(gng.network))
    target_infered = []
    for observation, cluster in clustered_data:
        target_infered.append(cluster)
    homogeneity = metrics.homogeneity_score(target, target_infered)
    print(homogeneity)
    gng.plot_clusters(gng.reduce_dimension(gng.cluster_data()))

if __name__ == '__main__':
    evaluate_on_digits()
