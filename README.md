# Simple stochastic block model

The function stochastic_block_model in sbm.py creates a network adjacency matrix from a stochastic block model and community labelled node list:

```python
import sbm
import time
import random as rn
import networkx as nx
import matplotlib.pyplot as plt

num_communities = 3
num_nodes = 30
community_labels = [rn.randrange(num_communities) for _ in range(num_nodes)]
p_matrix = [
  [.7, .1, .1],
  [.1, .7, .1],
  [.1, .1, .7],
]

adj_matrix = stochastic_block_model(p_matrix, community_labels)
g = nx.from_numpy_matrix(adj_matrix)
nx.draw(g, pos=nx.spring_layout(g), cmap=plt.get_cmap('Pastel2'), with_labels=True, node_color=community_labels)
```

## Sample output 1
![Sample 1](https://github.com/faisalnsour/stochastic-block-model/blob/test-branch/sbm-sample1.png)

## Sample output 2
![Sample 2](https://github.com/faisalnsour/stochastic-block-model/blob/test-branch/sbm-sample2.png)
