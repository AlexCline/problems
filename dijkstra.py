from priodict import priorityDictionary

def dijkstra(map, start, end):
	if start == end:
		return 0
	if not(map.has_key(start)) or not(map.has_key(end)):
		return -1

	distances = {}
	nodes = {}
	prelim_distances = priorityDictionary()
	prelim_distances[start] = 0
	for vertex in prelim_distances:
		distances[vertex] = prelim_distances[vertex]
		if vertex == end: break

		for edge in map[vertex]:
			dist = distances[vertex] + map[vertex][edge]
			if edge in distances:
				if dist < distances[edge]:
					return Error
			elif edge not in prelim_distances or dist < prelim_distances[edge]:
				prelim_distances[edge] = dist
				nodes[edge] = vertex

	return (distances,nodes)

net = { 's': {'u' : 10, 'x' : 5}, 
	'u': {'v' : 1, 'x' : 2}, 
	'v': {'y' : 4}, 
	'x': {'u' : 3, 'v' : 9, 'y' : 2}, 
	'y': {'s' : 7, 'v' : 6} }

print dijkstra(net, 's', 'y')
