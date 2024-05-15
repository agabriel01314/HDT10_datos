#se pusieron 2 codigos similares, el que no esta comentado es el que funciona de mejor manera con el .txt llamado
#logistica la cuestion es que no se en que me para no validarme de forma correcta los puntos a calificar
#aparte de siempre marcarme error en la lineas 33 a 39 por los verices.index 
#el segundo codigo que esta comentado no funciona pero no entiendo el porque no funciona y queria ver si me lo 
#me lo podian explicar ya que en ese codigo pedi ayuda de chatgpt para ver que me fallaba y no me decia nada
#aparte pedi ayuda a otras personas y no me lograban decir el porque de sus errore, asi que me gustaria ver 
#si me lo pueden ecplicar ustedes
import Graph

def read_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        vertices = [line.split()[0] for line in lines]
        graph_obj = Graph.Graph(len(vertices))
        city_to_index = {city: i for i, city in enumerate(vertices)}
        for line in lines:
            city1, city2, time_normal, time_rain, time_snow, time_storm = line.strip().split()
            if city1 in city_to_index and city2 in city_to_index:
                u = city_to_index[city1]
                v = city_to_index[city2]
                graph_obj.add_edge(u, v, int(time_normal))
                graph_obj.add_edge(v, u, int(time_normal))
        return graph_obj, vertices

def main():
    graph_obj, vertices = read_graph_from_file('logistica.txt')
    graph_obj.floyd_warshall()
    print("Matriz de Adyacencia:")
    graph_obj.print_matrix()
    return graph_obj, vertices

while True:
    print("\nOpciones:")
    print("1. Calcular ruta más corta entre dos ciudades")
    print("2. Calcular centro del grafo")
    print("3. Modificar grafo")
    print("4. Finalizar programa")
    option = input("Ingrese una opción: ")

    if option == '1':
        city1 = input("Ingrese ciudad origen: ")
        city2 = input("Ingrese ciudad destino: ")
        graph_obj, vertices = main()
        shortest_path = graph_obj.get_shortest_path(vertices.index(city1), vertices.index(city2))
        print("Ruta más corta:", ' -> '.join(shortest_path))

    elif option == '2':
        graph_obj, vertices = main()
        center = graph_obj.get_center()
        print("Centro del grafo:", vertices[center])

    elif option == '3':
        graph_obj, vertices = main()
        print("Modificar grafo:")
        print("a. Interrupción de tráfico entre dos ciudades")
        print("b. Establecer conexión entre dos ciudades")
        print("c. Indicar clima entre dos ciudades")
        suboption = input("Ingrese una opción: ")

        if suboption == 'a':
            city1 = input("Ingrese ciudad 1: ")
            city2 = input("Ingrese ciudad 2: ")
            graph_obj.add_edge(vertices.index(city1), vertices.index(city2), float('inf'))
            graph_obj.add_edge(vertices.index(city2), vertices.index(city1), float('inf'))

        elif suboption == 'b':
            city1 = input("Ingrese ciudad 1: ")
            city2 = input("Ingrese ciudad 2: ")
            time_normal = int(input("Ingrese tiempo con clima normal: "))
            graph_obj.add_edge(vertices.index(city1), vertices.index(city2), time_normal)
            graph_obj.add_edge(vertices.index(city2), vertices.index(city1), time_normal)

        elif suboption == 'c':
            city1 = input("Ingrese ciudad 1: ")
            city2 = input("Ingrese ciudad 2: ")
            climate = input("Ingrese clima (normal, lluvia, nieve, tormenta): ")
            if climate == 'lluvia':
                time= int(input("Ingrese tiempo con lluvia: "))
            elif climate == 'nieve':
                time = int(input("Ingrese tiempo con nieve: "))
            elif climate == 'tormenta':
                time = int(input("Ingrese tiempo con tormenta: "))
            else:
                time = int(input("Ingrese tiempo con clima normal: "))
            graph_obj.add_edge(vertices.index(city1), vertices.index(city2), time)
            graph_obj.add_edge(vertices.index(city2), vertices.index(city1), time)

        graph_obj.floyd_warshall()

    elif option == '4':
        break

if __name__ == "__main__":
    main()


"""
import Graph 
def read_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        vertices = [line.split()[0] for line in lines]
        graph_obj = Graph(len(vertices))
        city_to_index = {city: i for i, city in enumerate(vertices)}
        for line in lines:
            city1, city2, time_normal, time_rain, time_snow, time_storm = line.strip().split()
            u = city_to_index[city1]
            v = city_to_index[city2]
            graph_obj.add_edge(u, v, int(time_normal))
            graph_obj.add_edge(v, u, int(time_normal))
        return graph_obj

def main():
    graph_obj = read_graph_from_file('logistica.txt')
    graph_obj.floyd_warshall()
    print("Matriz de Adyacencia:")
    graph_obj.print_matrix()

while True:
    print("\nOpciones:")
    print("1. Calcular ruta más corta entre dos ciudades")
    print("2. Calcular centro del grafo")
    print("3. Modificar grafo")
    print("4. Finalizar programa")
    option = input("Ingrese una opción: ")

    if option == '1':
        city1 = input("Ingrese ciudad origen: ")
        city2 = input("Ingrese ciudad destino: ")
        shortest_path = graph_obj.get_shortest_path(vertices.index(city1), vertices.index(city2))
        print("Ruta más corta:", ' -> '.join(shortest_path))

    elif option == '2':
        center = graph_obj.get_center()
        print("Centro del grafo:", vertices[center])

    elif option == '3':
        print("Modificar grafo:")
        print("a. Interrupción de tráfico entre dos ciudades")
        print("b. Establecer conexión entre dos ciudades")
        print("c. Indicar clima entre dos ciudades")
        suboption = input("Ingrese una opción: ")

        if suboption == 'a':
            city1 = input("Ingrese ciudad 1: ")
            city2 = input("Ingrese ciudad 2: ")
            graph_obj.add_edge(vertices.index(city1), vertices.index(city2), float('inf'))
            graph_obj.add_edge(vertices.index(city2), vertices.index(city1), float('inf'))

        elif suboption == 'b':
            city1 = input("Ingrese ciudad 1: ")
            city2 = input("Ingrese ciudad 2: ")
            time_normal = int(input("Ingrese tiempo con clima normal: "))
            graph_obj.add_edge(vertices.index(city1), vertices.index(city2), time_normal)
            graph_obj.add_edge(vertices.index(city2), vertices.index(city1), time_normal)

        elif suboption == 'c':
            city1 = input("Ingrese ciudad 1: ")
            city2 = input("Ingrese ciudad 2: ")
            climate = input("Ingrese clima (normal, lluvia, nieve, tormenta): ")
            if climate == 'lluvia':
                time = int(input("Ingrese tiempo con lluvia: "))
            elif climate == 'nieve':
                time = int(input("Ingrese tiempo con nieve: "))
            elif climate == 'tormenta':
                time = int(input("Ingrese tiempo con tormenta: "))
            else:
                time = int(input("Ingrese tiempo con clima normal: "))
            graph_obj.add_edge(vertices.index(city1), vertices.index(city2), time)
            graph_obj.add_edge(vertices.index(city2), vertices.index(city1), time)

        graph_obj.floyd_warshall()

    elif option == '4':
        break

if __name__ == "__main__":
    main()
"""
