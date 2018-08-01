package bfs;

import java.util.ArrayList;
class DirectedGraphNode {
    public int label;
    public ArrayList<DirectedGraphNode> neighbors;
    DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
};