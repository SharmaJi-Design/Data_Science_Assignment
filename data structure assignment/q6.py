# Graph (Using defaultdict from collections)
from collections import defaultdict

graph = defaultdict(list)

graph['A'].append('B')
graph['A'].append('C')
graph['B'].append('D')

print(dict(graph))