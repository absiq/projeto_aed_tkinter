def leitura_comentarios(album_id):
    '''
    retorna a lista de comentários do ID do álbum
    '''
    ficheiro = '.\\databases\\comentarios.csv'
    f = open(ficheiro, 'r', encoding='utf-8')
    campos = f.readlines()
    comments = []
    for line in campos:
        data = line.split(';')
        if data[0] == album_id:
            list_comments = data[1].split(',')
            for comment in list_comments:
                comment_field = comment.split('-')
                new_line = comment_field[0] + ':' + ' ' + comment_field[1] + '\n'
                comments.append(new_line)
    return comments

def inserir_comentario(username, comment, album_id):
    '''
    insere um comentário do usuário no respectivo álbum do id dado
    '''
    ficheiro = '.\\databases\\comentarios.csv'
    f = open(ficheiro, 'r', encoding='utf-8')
    campos = f.readlines()
    i = 0
    for line in campos:
        data = line.split(';')
        if data[0] == album_id:
            previous_comments = []
            without_n = data[1].replace('\n', '')
            previous_comments.append(without_n)
            new_comment = '{0}-{1}\n' .format(username, comment)
            previous_comments.append(new_comment)
            new_comments = ','.join(map(str, previous_comments))
            campos[i] = album_id + ';' + new_comments
            print(campos[i])
            arquivo = open(ficheiro, 'w', encoding='utf-8')
            arquivo.writelines(campos)
        else:
            i += 1