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
