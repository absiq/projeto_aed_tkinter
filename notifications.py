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


def insert_new_user_into_notification_database(new_user_id):
    '''
    cria posição na tabela de notificações ao ter um novo usuário criado
    '''
    new_line = str(new_user_id) + ';' + "'0'-'0','0'-'0','0'-'0','0'-'0'" + '\n'
    ficheiro = '.\\databases\\notifications.csv'
    f = open(ficheiro, 'r')
    campos = f.readlines()
    i = 0
    for line in campos:
        data = line.split(';')
        position = data[0]
        user_id = int(new_user_id)
        user_id -= 1
        if position == str(user_id):
            campos.append(new_line)
            j = open(ficheiro, 'w')
            j.writelines(campos)
        else:
            i+=1



def create_notification(user_id, title, text):
    '''
    insere notificação para o usuário do ID do parâmetro
    '''
    pasta = '.\\databases'
    ficheiro = '.\\databases\\notifications.csv'
    verify_files(pasta, ficheiro)
    f = open(ficheiro, 'r')
    campos = f.readlines()
    f.close()
    i = 0
    for line in campos:
        data = line.split(';')
        if data[0] == user_id:
            new_notifications = []
            notifications = data[1].split(',')
            latest_notification = notifications[0]
            second_notification = notifications[1]
            third_notification = notifications[2]
            new_notification = "'{0}'-'{1}'" .format(title, text)
            new_notifications.insert(0, new_notification)
            new_notifications.insert(1, latest_notification)
            new_notifications.insert(2, second_notification)
            new_notifications.insert(3, third_notification)
            list_to_string = ','.join(map(str, new_notifications))
            line = user_id + ';' + list_to_string + '\n'
            campos[i] = line
            j = open(ficheiro, 'w')
            j.writelines(campos)
        else:
            i += 1 
        
