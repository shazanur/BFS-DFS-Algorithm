import streamlit as st

# --- Title ---
st.title("Breadth First Search (BFS) and Depth First Search (DFS) Visualization")
st.markdown("Select a starting node and choose which algorithm to run.")

# --- Display image ---
st.image("LabReport_BSD2513_#1.jpg", caption="Graph Representation", use_container_width=True)

# --- Define graph based on your uploaded image ---
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'G', 'E'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['G','F']
}

# --- BFS Function ---
def bfs(graph, start_node):
    visited = []
    queue = []
    traversal_order = []

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        traversal_order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    return traversal_order


# --- DFS Function ---
def dfs(graph, start_node, visited=None, traversal_order=None):
    if visited is None:
        visited = []
    if traversal_order is None:
        traversal_order = []

    visited.append(start_node)
    traversal_order.append(start_node)

    for neighbour in graph[start_node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, traversal_order)
    
    return traversal_order


# Dropdown for starting node
start_node = st.selectbox("Select Starting Node:", list(graph.keys()))

# Choose algorithm
algorithm = st.radio("Select Algorithm:", ("Breadth First Search (BFS)", "Depth First Search (DFS)"))

# Run button
if st.button("Run Algorithm"):
    if algorithm == "Breadth First Search (BFS)":
        order = bfs(graph, start_node)
        st.write("BFS Traversal Order:")
        st.success(" → ".join(order))
    else:
        order = dfs(graph, start_node)
        st.write("DFS Traversal Order:")
        st.info(" → ".join(order))
