import os

def verify_files(pasta, ficheiro):
    '''
    verifica se o ficheiro e a pasta existem no diretório, e, caso contrário, as cria
    '''
    if not os.path.exists(pasta):
        os.mkdir(pasta)
    if not os.path.exists(ficheiro):
        f = open(ficheiro, "x")

def read_notifications(user_id):
    '''
    recebe o ID do usuário como argumento e lê suas notificações
    '''
    pasta = '.\\databases'
    ficheiro = '.\\databases\\notifications.csv'
    verify_files(pasta, ficheiro)
    f = open(ficheiro, 'r')
    campos = f.readlines()
    for line in campos:
        line_split = line.split(';')
        if line_split[0] == str(user_id):
            notifications = line_split[1]
            list_notifications = notifications.split(',')
            for line in list_notifications:
                list_notif = line.split('-')
                title = list_notif[0]
                description = list_notif[1]
                pasta = '.\\databases'
                new_ficheiro = '.\\databases\\currentnotifications.csv'
                verify_files(pasta, ficheiro)
                file_notif = open(new_ficheiro, 'a')
                file_notif.write(title + ';' + description + '\n')

def clear_notifications():
    ficheiro = '.\\databases\\currentnotifications.csv'
    f = open(ficheiro, 'w')
    f.close()