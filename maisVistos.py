
def maisVistos():
    """
    seleciona os 5 albuns mais vistos da aplicacao
    """
    file = open("pop.txt", 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    viewsList = []
    for line in lines:
        split = line.split(";")
        views = int(split[-2])
        viewsList.append((views, line))

    top_5_views = sorted(viewsList, key=lambda x: x[0], reverse=True)[:5]

    for view in top_5_views:
        split = view[1].split(";")
        id_album = split[0]
        img_album = split[1]
        nome_album = split[2]
        nome_artista = split[3]
        visualizacoes = split[10]
        print(id_album + ";" + img_album  + ";" + nome_album +";" + nome_artista+ ";" + visualizacoes)

    with open("top_5_views.txt", "w", encoding="utf-8") as file:
        for view in top_5_views:
            split = view[1].split(";")
            id_album = split[0]
            img_album = split[1]
            nome_album = split[2]
            nome_artista = split[3]
            visualizacoes = split[10]
            file.write(id_album + ";" + img_album  + ";" + nome_album + ";" + nome_artista + ";" + visualizacoes + '\n')


maisVistos()


