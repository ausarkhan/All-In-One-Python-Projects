"""
GraphRAG Implementation using Llama-Index and NetworkX
Issue #103 for king04aman/All-In-One-Python-Projects
"""
import networkx as nx
from llama_index.core import KnowledgeGraphIndex, SimpleNodeParser, QueryEngine
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Example documents
DOCUMENTS = [
    "Alice is a data scientist. She works at Acme Corp.",
    "Bob is a software engineer. He collaborates with Alice on ML projects.",
    "Acme Corp is a tech company based in New York."
]

# Step 1: Parse documents into nodes
parser = SimpleNodeParser()
nodes = parser.get_nodes_from_documents(DOCUMENTS)

# Step 2: Build Knowledge Graph Index
kg_index = KnowledgeGraphIndex(nodes)

# Step 3: Create Query Engine (using OpenAI LLM and embeddings)
llm = OpenAI(model="gpt-3.5-turbo")
embed_model = OpenAIEmbedding(model="text-embedding-ada-002")
query_engine = QueryEngine(kg_index, llm=llm, embed_model=embed_model)

# Step 4: Example query
query = "Who works at Acme Corp?"
response = query_engine.query(query)
print("Query:", query)
print("Response:", response)

# Step 5: Visualize Knowledge Graph
G = nx.Graph()
for node in nodes:
    for rel in node.relationships:
        G.add_edge(node.entity, rel.entity, label=rel.type)

nx.write_gml(G, "knowledge_graph.gml")
print("Knowledge graph saved as knowledge_graph.gml")
