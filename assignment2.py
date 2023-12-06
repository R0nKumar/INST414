import requests
import networkx as nx

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

names = ['marijuana', 'cannabis', 'pot', 'weed', 'herb', 'greeen', 'ganja', 'bud', 'grass', 'mary jane', 'dope', 'reefer', 'joint', 'spliff', 'blunt', 'tree', 'chronic', 'devils lettuce', 'kush', 'skunk', 'hydro', 'wacky tobaccy', 'hash', 'cabbage', 'puff', 'cheeba', 'doobie', 'twist', 'Bob Hope', 'sticky icky', 'acapulca gold', 'blue dream', 'purple haze', 'sative', 'indica', 'edibles', 'thc', '420', 'pot browniies', 'mary warner', 'scooby snacks', 'jamaican gold', 'cannabutter', 'giggle smoke', 'wake and bake', 'moon rocks']

headers = {
	"X-RapidAPI-Key": "6f4292c6b1msh05d7557a0fa4342p1985f0jsnf625956c6df6",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}


g = nx.Graph()

for name in names:
    querystring = {"term": name}
    response = requests.get(url, headers=headers, params=querystring).json()['list']
    
    authors = []
    test = []

    for entry in response:
        authors.append(entry['author'])

    for author1 in authors:
        for author2 in authors:
            if author1 != author2:
                current_weight = g.get_edge_data(author1, author2, default={"weight":0})["weight"]
                g.add_edge(author1, author2, weight=current_weight+1)


top_k = 10
centrality_degree = nx.degree_centrality(g)
for u in sorted(centrality_degree, key=centrality_degree.get, reverse=True)[:top_k]:
    print(u, g.nodes[u], centrality_degree[u])