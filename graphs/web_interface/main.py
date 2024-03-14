# main.py
import streamlit as st
from graph_module import load_graph_data, create_graph
from streamlit_agraph import agraph, Config, Node, Edge

def main():
    st.title("Visualizzazione Grafo")
    node_id = st.text_input("Inserisci l'ID del nodo:")
    if st.button("GENERA GRAFO"):
        # Carica dati utili (restituisce lista)
        graph_data = load_graph_data(node_id)

        nodes, edges = create_graph(graph_data)

        config = Config(width=750,
                        height=950,
                        directed=True,
                        physics=False,
                        hierarchical=False
                        )

        return_value = agraph(nodes=nodes,
                              edges=edges,
                              config=config)

if __name__ == "__main__":
    main()
