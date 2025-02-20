from queue import LifoQueue, Queue
import heapq

class Grafo:
    def __init__(self):
        self.lista_de_adjacencia = {} # usamos um vertice como chave
        self.lista_de_arestas = set()
        self.ciclo_check = False # para função recursiva que busca ciclos
        #self.count = 0

    def adicionarVertice(self,vertice):
        if vertice not in self.lista_de_adjacencia:
            self.lista_de_adjacencia[vertice] = []

    def adicionarAresta(self, u, v, peso=1):
        # note que não preciso adicionar o v, já que pela forma que o documento está, ele passará por todos vertices
        # e portanto o u já bastará
        self.adicionarVertice(u)
        self.lista_de_adjacencia[u].append((v, peso))
        self.lista_de_arestas.add((u,v,peso))

        # o grafo representa tanto a ida quanto a volta para todos os vertices, portanto sendo representado de maneira
        # não direcional, dessa forma só quero colocar uma vez na lista de aresta, sem duplicata, por ser não direcional
        # 1->2 seria o mesmo que 2->1
        #if u<v:
            # tmp = len(self.lista_de_arestas) serve para contar quantas arestas tem duplicadas caso utiliza um set()
            #self.lista_de_arestas.add((u,v,peso))
            # if len(self.lista_de_arestas) == tmp:
            #     self.count +=1

    # #retorna o numero de arestas do grafo
    # def m(self):
    #     count = 0
    #     for chave in self.lista_de_adjacencia:
    #        for tupla in self.lista_de_adjacencia[chave]:
    #            count += 1
    #     return count

    # retorna o numero de vertices do grafo
    def n(self):
        return len(self.lista_de_adjacencia)

    # retorna o numero de arestas no grafo
    def m(self):
        return len(self.lista_de_arestas)

    #retorna a lista de vizinhos do vertice
    def viz(self,vertice):
        return self.lista_de_adjacencia[vertice]

    # retorna o peso da aresta, a tupla seria (vertice,peso)
    def w(self,vertice1,vertice2):
        for tupla in self.lista_de_adjacencia[vertice1]:
            if tupla[0] == vertice2:
                return tupla[1] # peso
        return 0 # esse vertice1 nao tem esse vizinho

    # retorna o grau do vertice
    def d(self, vertice):
        return len(self.lista_de_adjacencia[vertice])

    # retorna o menor grau do grafo
    def mind(self):
        menor_grau = self.d(1) # pego o grau do vertice 1 para iniciar
        menor_vertice = 1
        for i in self.lista_de_adjacencia:
            grau = self.d(i) # utilizo a nossa outra funçao para calcular o grau
            if grau < menor_grau:
                menor_grau = grau
                menor_vertice = i
        return menor_vertice,menor_grau

    # retorna o maior grau do grafo, quase igual a função do menor, mudando apenas a comparação
    def maxd(self):
        maior_grau = 0
        menor_vertice = 1
        for i in self.lista_de_adjacencia:
            grau = self.d(i)
            if grau > maior_grau:
                maior_grau = grau
                menor_vertice = i
        return menor_vertice,maior_grau

    def dfs(self, inicio):
        visitados = set()  # conjunto para armazenar os vértices visitados
        pilha = LifoQueue()  # pilha que irá processar os vertices

        tempo_inicial = {}
        tempo_final = {}
        pai = {} # chave = cada vertice, contendo o valor pai
        tempo = 1  # contador de tempo

        # nossa pilha irá receber uma tupla, (vertice,indice do vizinho que ainda não foi visitado)
        # é necessário pois precisamos ter um controle em relação a quando um vertice foi de fato processado por completo
        # e assim podermos atribuir o tempo final corretamente
        # normalmente feito com cores, mas por ser uma pilha, e não uma recursão, achei mais facil assim
        pilha.put((inicio,0))
        visitados.add(inicio) # marca o vértice inicial como visitado
        tempo_inicial[inicio] = tempo
        tempo += 1
        pai[inicio] = None  # vértice inicial não tem pai

        while not pilha.empty():
            vertice, indice_vizinho = pilha.get()  # pega o vértice e o indice do próximo vizinho a ser processado
            vizinhos = self.lista_de_adjacencia[vertice] # todos vizinhos do vértice

            if indice_vizinho < len(vizinhos): # checa se o indice atual do vértice é menor que o tamanho da lista
                vizinho, _ = vizinhos[indice_vizinho]
                pilha.put((vertice,indice_vizinho+1))

                # importante pois o vizinho já pode ter sido visitado, exemplo: pai do vértice já que o grafo é não direcional
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    tempo_inicial[vizinho] = tempo
                    tempo += 1
                    # só queremos considerar o vértice antecessor ao caminho
                    if vizinho not in pai:
                        pai[vizinho] = vertice # vizinho recebe vértice antecessor a ele como pai

                    pilha.put((vizinho,0))
            else: # se não for menor é por que o vértice já foi totalmente processador e colocar o tempo final
                tempo_final[vertice] = tempo
                tempo += 1

        return tempo_inicial, tempo_final, pai

    #Bellman-Ford
    # se for representar a lista de arestas como uma aresta (v1,v2,peso) representando tanto a ida quanto
    # a volta, lembre-se de adicionar mais um if, checando a volta.
    # Se tiver duas arestas para representar uma aresta não direcional(ida e volta) mantenha assim
    def bf(self,vertice_inicial):
        #coloco todas distancias do vertice para todos outros como infinitas
        distancias = {vertice: float('inf') for vertice in self.lista_de_adjacencia}
        distancias[vertice_inicial] = 0
        # para armazenar os caminhos minimos
        caminhos = {vertice: [] for vertice in self.lista_de_adjacencia}
        caminhos[vertice_inicial] = [vertice_inicial]
        #antecessor de cada vértice no caminho minimo
        pai = {vertice: None for vertice in self.lista_de_adjacencia}

        # relaxando arestas
        for _ in range(self.n()-1):
            atualizou = False
            for u,v,peso in self.lista_de_arestas:
                # distancia de origem até u + peso de(u,v) tem que ser menor que distancia da origem a v
                if distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso
                    caminhos[v] = caminhos[u] + [v]
                    pai[v] = u
                    print(u,v,peso)
                    atualizou = True
            if not atualizou: # nessa iteração não houve atualizações nas distancias
                break

        # verificando ciclos de valores negativos: se isso é encontrado sempre será possivel fazer relaxamento
        # pois sempre dará para encurtar a distancia entre um vértice e outro
        for u,v,peso in self.lista_de_arestas:
            if distancias[v] > distancias[u] + peso:
                return False # encontrou um ciclo negativo pois foi possivel fazer mais relaxamentos
            # não encontrou ciclo negativo

        return distancias, caminhos, pai

    #função para realizar djikstra
    def djikstra(self, origem):
        if origem not in self.lista_de_adjacencia:  # verifica se o vertice esta na lista
            print("Erro: vertice não encontrado")
            return
        distancias = {vertice: float('inf') for vertice in self.lista_de_adjacencia} # esse distancias representa a distancia minima
        pai = {vertice: None for vertice in self.lista_de_adjacencia}

        distancias[origem] = 0

        filadeprioridade = [(0.0, origem)]

        while filadeprioridade:  # vai percorrendo enquanto tiver valor na fila de prioridade
            distatual, verticeatual = heapq.heappop(filadeprioridade)  # remove o menor elemento da fila

            if distatual > distancias[verticeatual]:
                continue

            for vizinho,peso in self.lista_de_adjacencia[verticeatual]:
                if distancias[vizinho] > distancias[verticeatual] + peso:  # verifica se é a menor distancia total
                    distancias[vizinho] = distancias[verticeatual] + peso  # atualiza a distancia
                    pai[vizinho] = verticeatual  # atualiza o pai do vértice
                    heapq.heappush(filadeprioridade, (distancias[vizinho], vizinho))  # adiciona à fila

        return pai, distancias

    #função para realizar bfs
    def bfs(self, origem):
        if origem not in self.lista_de_adjacencia:
            print("Erro: vertice não encontrado")
            return

        distancia = {vertice: float('inf') for vertice in self.lista_de_adjacencia}  # Distâncias(infinitas)
        pai = {vertice: None for vertice in self.lista_de_adjacencia}  # começa sem predecessor
        distancia[origem] = 0
        fila = Queue()
        verticesvisitados = set()  # set pra não ter duplicado

        fila.put(origem)  # adiciona a partir de onde começa a busca
        verticesvisitados.add(origem)  # origem já foi visitada

        while not fila.empty():
            verticeatual = fila.get()
            for vizinho, _ in self.lista_de_adjacencia[verticeatual]:  # vai pegando cada vizinho
                if vizinho not in verticesvisitados:  # se o vertice não tiver sido visitado
                    distancia[vizinho] = distancia[verticeatual] + 1  # +1 de distancia a partir da origem
                    pai[vizinho] = verticeatual  # verticeatual se torna pai do vizinho
                    verticesvisitados.add(vizinho)
                    fila.put(vizinho)  # vizinho pra fila de prioridade

        return pai, distancia


    def vertice_mais_distante(self,vertice):
        dist,_,_ = self.bf(vertice) # lista das distancias a partir de um vértice, usando bellman ford
        maior_distancia = -float('inf')
        vertice_maior = None
        for vertice in dist:
            if dist[vertice] > maior_distancia and dist[vertice] != float('inf'): # comparo a distancia dos vértices
                maior_distancia = dist[vertice]
                vertice_maior = vertice

        return maior_distancia,vertice_maior # retorno maior distancia e o vértice mais distante da minha origem

    def busca_caminho(self,origem,tamanho_minimo):
        # irei fazer uma função interna pois a chamada da função recursiva é simples demais pra separar
        def dfs_caminho(vertice,caminho_atual, arestas_atual):
            # checa para cada chamada se o resultado atual corresponde ao criterio de arestas minimas
            # se não atender a isso, não vai retornar o caminho de arestas_atual e portanto continuará para uma nova origem
            # se retornar cai na checagem if resultado(não for nulo) retorna o resultado e pronto
            if len(arestas_atual) >= tamanho_minimo:
                return arestas_atual
            for vizinho, peso in self.lista_de_adjacencia[vertice]:
                if vizinho not in caminho_atual: # não posso ter ciclos
                    nova_aresta = (vertice,vizinho,peso) #formato a aresta para retornar bonitinho no print
                    resultado = dfs_caminho(vizinho,caminho_atual + [vizinho], arestas_atual + [nova_aresta])
                    if resultado: # se o resultado(caminho não tiver vazio) retorna o caminho
                        return resultado
            return None
        return dfs_caminho(origem, [origem], []) # faz a chamada para a recursão

    # função base para a chamada do dfs_ciclo, inicia a recursão
    def busca_ciclo(self,tamanho_minimo):
        # inicia todos os visitados com o status("cor") 0, nenhum foi visitado ou processado
        visitados = {vertice: 0 for vertice in self.lista_de_adjacencia}
        ciclos = []
        ciclos_arestas = []
        #caso seja um grafo conexo só usaremos o primeiro vértice
        for vertice in self.lista_de_adjacencia:
            if visitados[vertice] == 0:
                # vertice de inicio, lista de visitados e a "cor", lista para armazenar caminho, lista para armazenar
                # ciclo e o tamanho minimo do ciclo que queremos retornar
                self.dfs_ciclo(vertice,visitados,[],ciclos,tamanho_minimo)
            if self.ciclo_check: break

        # função para formatar as arestas de maneira correta para retornar a aresta, e não o vértice
        for ciclo_vertices in ciclos:
            ciclo_arestas = []
            for i in range(len(ciclo_vertices) - 1):
                origem = ciclo_vertices[i]
                destino = ciclo_vertices[i + 1]
                # Procura o peso da aresta entre origem e destino
                for v, p in self.lista_de_adjacencia[origem]:
                    if v == destino:
                        ciclo_arestas.append((origem, destino, p))
                        break
            ciclos_arestas.append(ciclo_arestas)
        return ciclos_arestas

    def dfs_ciclo(self, vertice, visitados, caminho_atual,ciclos,tamanho_minimo):
        # Marca o vértice como visitado (1)
        visitados[vertice] = 1
        caminho_atual.append(vertice)

        # itera sobre os vizinhos do vértice atual
        for vizinho, _ in self.lista_de_adjacencia[vertice]: # ignoro o peso da aresta
            if self.ciclo_check: break
            if visitados.get(vizinho, 0) == 1: # significa que ele já foi visitado alguma vez, portanto ciclo!
                ciclo = caminho_atual[caminho_atual.index(vizinho):] + [vizinho]  # faço slicing da primeira ocorrencia do vizinho até esta
                if len(ciclo) - 1 >= tamanho_minimo: # número de vértices no ciclo - 1 é o número de arestas
                    ciclos.append(ciclo)
                    self.ciclo_check = True # quero apenas um ciclo do tamanho requerido, portanto paro tudo
                    return
            elif visitados.get(vizinho, 0) == 0:
                visitados[vizinho] = 0
                self.dfs_ciclo(vizinho, visitados,caminho_atual,ciclos,tamanho_minimo) # chamo a recursão

        # marco vértice como totalmente visitado
        visitados[vertice] = 2
        caminho_atual.pop()  # removo o ultimo elemento do caminho

