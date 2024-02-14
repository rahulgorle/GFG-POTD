class Solution:
    def criticalConnections(self, v, adj):
        # Function to find critical connections in a graph
        
        def Articulation_Point(u):
            # Function to find Articulation Point and critical connections
            
            low[u]=time[0]
            disc[u]=time[0]
            time[0]+=1
            visited[u]=True
            for v in adj[u]:
                if visited[v]==False:
                    parent[v]=u
                    Articulation_Point(v)
                    
                    low[u]=min(low[u],low[v])
                    
                    if low[v]>disc[u]:
                        ans.append(sorted([u,v]))
                        
                elif parent[u]!=v:
                    low[u]=min(low[u],disc[v])
        
        
        
        ans=[]
        
        # Initializing low, disc, parent, time, and visited arrays
        low=[sys.maxsize for i in range(v)]
        disc=[sys.maxsize for i in range(v)]
        parent=[-1 for i in range(v)]
        time=[0]
        visited=[False for i in range(v)]
        
        # Calling Articulation_Point function for each unvisited vertex
        for i in range(v):
            if visited[i]==False:
                Articulation_Point(i)
        
    
        return sorted(ans)
