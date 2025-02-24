import networkx as nx
import matplotlib.pyplot as plt

def generate_graph(df, wallet):
    G = nx.DiGraph()

    # Add transactions to the graph
    for _, row in df.iterrows():
        sender, receiver, value = row["from"], row["to"], row["value"]
        G.add_edge(sender, receiver, weight=value)

    plt.figure(figsize=(16, 12))  # Increase figure size for clarity
    pos = nx.spring_layout(G, k=0.9, seed=42)  # Adjust node spacing to reduce clutter

    # Shorten Ethereum addresses for clarity
    labels = {node: node[:6] + "..." + node[-4:] for node in G.nodes()}
    
    # Draw graph with improved spacing
    nx.draw(G, pos, with_labels=True, labels=labels, node_color="skyblue", edge_color="gray",
            node_size=2800, font_size=10, font_weight="bold", alpha=0.9)

    # Add transaction values as edge labels
    edge_labels = {(u, v): f"{d['weight']:.4f} ETH" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, alpha=0.8, bbox=dict(facecolor="white", alpha=0.7))

    plt.title(f"ETH Transaction Flow for {wallet[:6]}...{wallet[-4:]}", fontsize=16)
    plt.savefig("flow_diagram.png", dpi=300, bbox_inches="tight")
    return "flow_diagram.png"
