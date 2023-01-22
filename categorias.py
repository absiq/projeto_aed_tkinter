def inserir_categoria(nova_categoria):
    '''
    insere uma nova categoria dada como parâmetro
    '''
    ficheiro = '.\\databases\\categorias.txt'
    f = open(ficheiro, 'a+')
    f.seek(0)
    data = f.read(100)
    if len(data) > 0:
        f.write("\n")
    f.write(nova_categoria)

def remover_categoria(categoria_selecionada):
    '''
    remove do banco de dados a categoria dada como parâmetro
    '''
    ficheiro = '.\\databases\\categorias.txt'
    f = open(ficheiro, 'r')
    lines = f.readlines()
    j = open(ficheiro, 'w')
    for line in lines:
        if line.strip('\n') != categoria_selecionada:
            j.write(line)
