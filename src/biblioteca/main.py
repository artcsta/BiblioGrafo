from biblioteca.grafo import Grafo
from biblioteca.digrafo import Digrafo
from tabulate import tabulate
import time

def ler_grafo(path):
    arestas = []
    arquivo = open(path, 'r')
    for linha in arquivo: #passa por todas linhas no arquivo
        if linha.startswith('a'): # por padrão, no documento, cada linha começa com 'a'
            _, v1, v2, peso = linha.split() # ignora o 'a' e atribui os valores a v1,v2 e peso
            arestas.append((int(v1), int(v2), float(peso)))
    return arestas

def formatar_dicionario(tempo_inicial, tempo_final):
    print("Vértice | Inicio | Término")
    print("-" * 30)
    for vertice in sorted(tempo_inicial.keys()):
        print(f"{vertice:^7} | {tempo_inicial[vertice]:^10} | {tempo_final[vertice]:^7}")

def formatar_saida_bf(distancias, caminhos, pais):
    # Cria uma lista de listas para a tabela
    tabela = []
    for vertice in distancias.keys():
        linha = [
            vertice,
            distancias[vertice],
            " -> ".join(map(str, caminhos[vertice])),
            pais[vertice]
        ]
        tabela.append(linha)

    # Define o cabeçalho da tabela
    cabecalho = ["Vértice", "Distância Mínima", "Caminho", "Pai"]

    # Imprime a tabela
    print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))

if __name__ == "__main__":

#     while True:
#         num = int(input("Quer usar grafo(1) ou digrafo(2)? \n\n"))
#         if(num==1):
#             #g = grafo()
#             break
#         elif(num==2):
#             #g = digrafo()
#             break
#         else:
#             print("1 ou 2")
    inicio = time.time()

    arestas = ler_grafo("../USA-road-d.NY.gr")
    #arestas = ler_grafo("../grafoTeste.txt")
    #arestas = ler_grafo("../grafoTeste2.txt")

    i = 0



    #g = Grafo()
    g = Digrafo()
    for aresta in arestas:
        g.adicionarAresta(aresta[0], aresta[1], aresta[2])

    # prints das funções

    # print(g.m())
    # print(g.viz(1))
    # print(g.d(1))
    # print(g.w(1,2))
    # print(g.count)
    # dist,caminho,paibf = g.bf(1)
    # print(dist)
    # print(paibf)
    #formatar_saida_bf(dist,caminho,pai)


    # maior_distancia, vertice = g.vertice_mais_distante(129)
    # print(maior_distancia)
    # print(vertice)


    # ciclos = g.busca_ciclo(i)
    # for aresta in ciclos:
    #     for vertice, vizinho, peso in aresta:
    #         print(vertice,vizinho,peso)

    # caminho = g.busca_caminho(1,20)
    # for origem, destino, peso in caminho:
    #     print(origem, destino, peso)


    # print(g.viz(1))
    # pi, distancia = g.bfs(1)
    # print(pi)
    # print(distancia)
    # pai,distancia = g.djikstra(1)
    # print(distancia)
    # print(pai)

    # inicioTempo,finalTempo,pai = g.dfs(1)
    # formatar_dicionario(inicioTempo, finalTempo)
    # print("*****PAI*******")
    # print(pai)


    # vertice_maior, d2 = g.maxd()
    # print(vertice_maior,d2)
    # print(g.viz(140961))

    # vertice_menor, d1 = g.mind()
    # print(vertice_menor,d1)


    fim = time.time()
    print(fim-inicio)