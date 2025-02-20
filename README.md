Biblioteca de grafos feita para disciplica de Teoria dos grafos na UECE, semestre 2024.2

a) G.n: Retorna o número de vértices do grafo.

b) G.m: Retorna o número de arestas do grafo.

c) G.viz(v): Retorna a vizinhança do vértice v, ou seja, os vértices adjacentes a v.

d) G.d(v): Retorna o grau do vértice v, ou seja, o número de arestas incidentes a v.

e) G.w(uv): Retorna o peso da aresta uv.

f) G.mind: Retorna o menor grau presente no grafo.

g) G.maxd: Retorna o maior grau presente no grafo.

h) G.bfs(v): Executa uma busca em largura (BFS) a partir do vértice v e retorna duas listas
com os atributos "d" e "pi" correspondentes aos vértices. A lista "d" representa a
distância entre cada vértice e v, e a lista "pi" armazena o vértice predecessor no
caminho de v até cada vértice.

i) G.dfs(v): Executa uma busca em profundidade (DFS) a partir do vértice v e retorna três
listas com os atributos "pi", "v.ini" e "v.fim". A lista "pi" armazena o vértice predecessor
na árvore de busca, a lista "v.ini" indica o tempo de início da visita a cada vértice, e a
lista "v.fim" indica o tempo de término da visita a cada vértice.

j) G.bf(v): Executa o algoritmo de Bellman-Ford a partir do vértice v como origem. Retorna
duas listas com os atributos "d" e "pi". A lista "d" representa as distâncias mínimas entre
v e cada vértice, e a lista "pi" armazena o vértice predecessor no caminho mínimo de v
até cada vértice.

k) G.djikstra(v): Executa o algoritmo de Dijkstra a partir do vértice v como origem. Retorna
duas listas com os atributos "d" e "pi". A lista "d" representa as distâncias mínimas entre
v e cada vértice, e a lista "pi" armazena o vértice predecessor no caminho mínimo de v
até cada vértice.Requisitos
