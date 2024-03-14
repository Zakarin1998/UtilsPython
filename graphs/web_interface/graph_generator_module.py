# graph_module.py
from pymongo import MongoClient
from streamlit_agraph import Node, Edge


def load_graph_data(node_id):
    url = 'mongodb://dbcreator:dbcreator@192.168.10.89:27017/?authMechanism=DEFAULT&authSource=admin'
    client = MongoClient(url)
    db = 'PN_NEW'
    coll = 'AIAAS_PN_network_edge'

    filter_query = {
        '$or': [
            {'_id.source_id': node_id},
            {'_id.target_id': node_id}
        ]
    }
    result = list(client[db][coll].find(filter=filter_query))
    return result


def create_graph(graph_data):
    nodes = []
    nodes_str = []
    edges = []

    for item in graph_data:

        if item['_id']['source_id'] not in nodes_str:
            nodes_str.append(item['_id']['source_id'])

            nodes.append(Node(id=item['_id']['source_id'],
                              label=item['_id']['source_id'],
                              size=20)
                         )

        if item['_id']['target_id'] not in nodes_str:
            nodes_str.append(item['_id']['target_id'])

            nodes.append(Node(id=item['_id']['target_id'],
                              label=item['_id']['target_id'],
                              size=10)
                         )

        edges.append(Edge(source=item['_id']['source_id'],
                          label=f"{item['tot_amount']}, {item['_id']['type']}",
                          target=item['_id']['target_id'],
                          )
                     )

    return nodes, edges
