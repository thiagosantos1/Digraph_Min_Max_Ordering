# Digraph_Min_Max_Ordering
Project designed to find the min_max ordering in digraphs

# Idea
I will use python to create a the new graph H', deriving from graph H. In this new graph, we have the following constraint (x,y) --> (x',y'). This means that x comes before y in the ordering and x' comes before y' as well in the ordering. We do this for all pairs(x,y) in H. Thus, we have to use all combinations to create all pairs. Then, the total of vertices in H' has (N square) - N. Where N is the total number of vertices in H.
