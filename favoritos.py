def likeList(user_id, album_id):
    '''
    insere o ID do álbum nos álbuns favoritos do usuário
    '''
    ficheiro = '.\\databases\\favoritos.csv'
    f = open(ficheiro, 'r')
    campos = f.readlines()
    i = 0
    for line in campos:
        data = line.split(';')
        if data[0] == user_id:
            list_favs = data[1].split(',')
            last_pos = len(list_favs)
            list_favs = list_favs[last_pos-1].replace('\n', '')
            list_favs = list_favs.split(',')
            list_favs.append(album_id)
            if '0\n' in list_favs:
                list_favs.remove('0\n')
            if '0' in list_favs:
                list_favs.remove('0')
            list_to_string = ','.join(map(str, list_favs))
            line = user_id + ';' + list_to_string + '\n'
            campos[i] = line
            j = open(ficheiro, 'w')
            j.writelines(campos)
        else:
            i += 1
    

def insert_new_user_into_favs_database(new_user_id):
    '''
    cria posição na tabela de favoritos ao ter um novo usuário criado
    '''
    new_line = str(new_user_id) + ';' + '0' + '\n'
    ficheiro = '.\\databases\\favoritos.csv'
    f = open(ficheiro, 'r')
    campos = f.readlines()
    i = 0
    for line in campos:
        data = line.split(';')
        position = data[0]
        user_id = int(new_user_id)
        user_id -= 1
        print(position)
        print(user_id)
        if position == str(user_id):
            campos.append(new_line)
            j = open(ficheiro, 'w')
            j.writelines(campos)
        else:
            i+=1