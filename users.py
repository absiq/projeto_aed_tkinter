import os

def verify_files(pasta, ficheiro):
    '''
    verifica se o ficheiro e a pasta existem no diretório, e, caso contrário, as cria
    '''
    if not os.path.exists(pasta):
        os.mkdir(pasta)
    if not os.path.exists(ficheiro):
        f = open(ficheiro, "x")

def data_exists_in_utilizadores(ficheiro, linha):
    '''
    verifica se a linha de dados já se encontra no banco de dados e retorna um valor booleano
    '''
    f = open(ficheiro, 'r')
    dados = f.readlines()
    f.close()
    linha_split = linha.split(',')
    for i in dados:
        i_split = i.split(',')
        if linha_split[1] == i_split[1]: # verificação de email
            print('verificação de email não passou')
            return True
        elif linha_split[2] == i_split[2]: # verificação de username
            print('verificação de username não passou')
            return True
    return False

def valida_tamanho_password(password):
    '''
    valida o tamanho da password e retorna falso se tiver menos que 8 caracteres
    '''
    if len(password) < 8:
        return False
    else:
        return True

def valida_email(email):
    '''
    realiza as validações do campo de e-mail
    '''
    if email.count('@') > 0:
        return True
    else:
        return False

def valida_campo_sem_virgula(*args):
    '''
    realiza a validação do campo e retorna falso se houver uma vírgula
    '''
    for i in args:
        if i.count(',') > 0:
            return False
        else:
         return True

def cria_id_user():
    last_id = 0
    count_id = 0
    ficheiro = '.\\databases\\users.csv'
    f = open(ficheiro, 'r')
    dados = f.readlines()
    for i in dados:
        line_split = i.split(',')
        if int(line_split[0]) > last_id:
            last_id = int(line_split[0])
    count_id = last_id + 1
    return count_id



def submit_register(nome, email, username, password):
    '''
    registra os dados no banco após passar por validações
    '''
    pasta = '.\\databases'
    ficheiro = '.\\databases\\users.csv'
    verify_files(pasta, ficheiro)
    line = '{0},{1},{2},{3}' .format(nome, email, username, password)
    if data_exists_in_utilizadores(ficheiro, line) == True:
        print('Os dados já existem no banco de dados')
    elif valida_campo_sem_virgula(nome, email, username, password) == False:
        print('Os campos não podem conter vírgulas')
    elif valida_tamanho_password(password) == False:
        print('A password precisa ter mais que 8 caracteres')
    elif valida_email(email) == False:
        print('O e-mail inserido é inválido')
    else:
        f = open(ficheiro, 'a')
        count_id = cria_id_user()
        default_bio = 'Adicione um texto na tua bio ao editar o perfil'
        default_profile_pic = 'avatarnone.png'
        register = str(count_id) + ',' + line + ',' + default_profile_pic + default_bio + '\n'
        f.write(register)
        print('Dado inserido com sucesso')

def atualiza_sessao(dado):
    '''
    recebe a linha de dados do utilizador e guarda em arquivo que indica o utilizador da sessão atual
    '''
    pasta = '.\\ databases'
    ficheiro = '.\\databases\\currentsession.csv'
    verify_files(pasta, ficheiro)
    f = open(ficheiro, 'w')
    f.write(dado)
    f.close()

def verify_login(ficheiro, username, password):
    '''
    verifica se o username e a password se encontra, no banco de dados e retorna um valor booleano
    '''
    f = open(ficheiro, 'r')
    dados = f.readlines()
    for i in dados:
        line_split = i.split(',')
        if username == line_split[3]: # verificação de username
            password = password.replace('\n', '')
            if password == line_split[4]: # verificação de senha
                atualiza_sessao(i)
                return True
    return False

def submit_login(username, password):
    '''
    retorna um valor booleano e realiza o login após passar por todas as validações
    '''
    pasta = '.\\databases'
    ficheiro = '.\\databases\\users.csv'
    verify_files(pasta, ficheiro)
    password = password + '\n'
    if verify_login(ficheiro, username, password) == True:
        return True ## O login foi realizado com sucesso
    else:
        return False ## O login não foi realizado pois houve erro

def logout_user():
    pasta = '.\\ databases'
    ficheiro = '.\\databases\\currentsession.csv'
    verify_files(pasta, ficheiro)
    f = open(ficheiro, 'w')
    f.write('')
    f.close()

def retrieve_current_user_data():
    '''
    busca os dados do usuário logado
    '''
    pasta = '.\\databases'
    ficheiro = '.\\databases\\currentsession.csv'
    verify_files(pasta, ficheiro)
    f = open(ficheiro, 'r')
    campos = f.readline()
    campos_split = campos.split(',')
    user_id = campos_split[0]
    name = campos_split[1]
    username = campos_split[3]
    icon = campos_split[5]
    bio = campos_split[6].replace('\n', '')
    return name, username, icon, bio, user_id

def edit_user_data(new_name, new_username, new_bio):
    '''
    edita os dados do usuário logado
    '''
    name, username, icon, bio, user_id = retrieve_current_user_data()
    ficheiro = '.\\databases\\users.csv'
    f = open(ficheiro, 'r+')
    dados = f.readlines()
    i = 0
    for line in dados:
        line_split = line.split(',')
        line_id = line_split[0]
        past_name = line_split[1]
        past_email = line_split[2]
        past_username = line_split[3]
        past_password = line_split[4]
        past_icon = line_split[5]
        past_bio = line_split[6].replace('\n', '')
        new_data = [line_id, past_name, past_email, past_username, past_password, past_icon, past_bio]
        if line_id == user_id:
            if new_name != '':
                new_data[1] = new_name
            if new_username != '':
                new_data[3] = new_username
            if new_bio != '':
                print(new_bio)
                new_data[6] = new_bio
            list_to_string = ','.join(map(str, new_data))
            dados[i] = list_to_string + '\n'
            # f.truncate(0) 
            f.writelines(dados)
        else:
            i += 1
            
