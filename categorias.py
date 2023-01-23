def inserir_categoria(nova_categoria):
    '''
    insere uma nova categoria dada como parâmetro
    '''
    ficheiro = '.\\databases\\categorias.txt'
    f = open(ficheiro, 'a+')
    f.write(nova_categoria + '\n')

def remover_categoria(categoria_selecionada):
    '''
    remove do banco de dados a categoria dada como parâmetro
    '''
    ficheiro = '.\\databases\\categorias.txt'
    f = open(ficheiro, 'r')
    lines = f.readlines()
    j = open(ficheiro, 'w')
    for line in lines:
        if line != categoria_selecionada:
            j.write(line)
