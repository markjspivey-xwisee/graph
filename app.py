
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.edges = []

class Edge:
    def __init__(self, node_from, node_to, weight=None):
        self.node_from = node_from
        self.node_to = node_to
        self.weight = weight

# In-memory store
nodes = {}
edges = {}
next_node_id = 1
next_edge_id = 1

@app.route('/')
def index():
    return render_template('nodes.html', nodes=nodes)

@app.route('/node/<int:node_id>')
def node(node_id):
    return render_template('node.html', node=nodes.get(node_id))

@app.route('/edge/<int:edge_id>')
def edge(edge_id):
    return render_template('edge.html', edge=edges.get(edge_id))

@app.route('/node/add', methods=['POST'])
def add_node():
    global next_node_id
    data = request.form.get('data')
    nodes[next_node_id] = Node(next_node_id, data)
    next_node_id += 1
    return redirect(url_for('index'))

@app.route('/edge/add', methods=['POST'])
def add_edge():
    global next_edge_id
    node_from = int(request.form.get('node_from'))
    node_to = int(request.form.get('node_to'))
    weight = request.form.get('weight')
    edges[next_edge_id] = Edge(node_from, node_to, weight)
    next_edge_id += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
