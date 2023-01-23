def insert_rating(user_id, album_id, rating):
    '''
    insere rating do usuário em um álbum
    '''
    ficheiro = '.\\databases\\ratings.csv'
    f = open(ficheiro, 'a+', encoding='utf-8')
    new_rating = user_id + ';' + album_id + ';' + rating + '\n'
    if verify_if_rating_exists(user_id, album_id) == False:
        f.write(new_rating)
    else:
        g = open(ficheiro, 'r', encoding='utf-8')
        dados = g.readlines()
        i = 0
        for line in dados:
            campos = line.split(';')
            if campos[0] == user_id and campos[1] == album_id:
                h = open(ficheiro, 'w', encoding='utf-8')
                dados[i] = new_rating
                h.writelines(dados)
            else:
                i += 1

        
def verify_if_rating_exists(user_id, album_id):
    '''
    verifica se o usuário já deu rating naquele álbum e retorna um valor booleano
    '''
    ficheiro = '.\\databases\\ratings.csv'
    f = open(ficheiro, 'r', encoding='utf-8')
    dados = f.readlines()
    for line in dados:
        campos = line.split(';')
        if campos[0] == user_id and campos[1] == album_id:
            return True
    return False

def count_ratings(album_id):
    '''
    conta o número total de ratings para um álbum e retorna sua média aritmética
    '''
    people_counter = 0
    rating_counter = 0
    ficheiro = '.\\databases\\ratings.csv'
    f = open(ficheiro, 'r', encoding='utf-8')
    dados = f.readlines()
    for line in dados:
        campos = line.split(';')
        if campos[1] == album_id:
            people_counter += 1
            rating = int(campos[2])
            rating_counter += rating
    media = float(rating_counter / people_counter)
    return media

def update_media(album_id):
    '''
    atualiza a nova média do álbum em ratingalbums
    '''
    rating = count_ratings(album_id)
    ficheiro = '.\\databases\\ratingalbums.csv'
    f = open(ficheiro, 'r', encoding='utf-8')
    dados = f.readlines()
    i = 0
    for line in dados:
        campos = line.split(';')
        if campos[0] == album_id:
            dados[i] = album_id + ';' + str(rating) + '\n'
            g = open(ficheiro, 'w', encoding='utf-8')
            g.writelines(dados)
        else:
            i += 1

def top_5_avaliados():
    '''
    seleciona os 5 álbuns melhores avaliados
    '''
    file = open("databases/ratingalbums.csv", 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    ratingsList = []
    for line in lines:
        split = line.split(";")
        ratings = float(split[1].replace('\n', ''))
        ratingsList.append((ratings, line))

    top_5_ratings = sorted(ratingsList, key=lambda x: x[0], reverse=True)[:5]

    with open("databases/top_5_ratings.txt", "w", encoding="utf=8") as f:
        for rated in top_5_ratings:
            split = rated[1].split(";")
            id_album = split[0]
            rating = split[1]
            f.write(id_album + ";" + rating)

def idsMaisAvaliados():
    '''
    retorna a lista de IDs dos álbuns mais bem avaliados
    '''
    f = open("databases/top_5_ratings.txt")
    lista = f.readlines()
    ids = []
    for linha in lista:
        split = linha.split(";")
        id_album = split[0]
        ids.append(id_album)
    return ids

top_5_avaliados()