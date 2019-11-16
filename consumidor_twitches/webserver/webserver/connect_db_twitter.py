import mysql.connector 
from webserver.settings import BD_INFO

dict_tabela_campos = {
    'twitters': '*', # Nome da tabela : Campos da tabela , LIMIT
}

dict_tabela_update = {
    'TB_INFO_POD': '*', # Nome da tabela : Campos da tabela , LIMIT
}


QUERY_CONSULTA_TWITTER = "SELECT {campos} from {tabela} LIMIT {LIMIT}"
QUERY_INSERT_REGISTER = "INSERT INTO {tabela} (nome_pod) VALUES ('{campos}')"

def conecta_com_mysql(host: str, database: str, user: str, password: str):
    """
        Connecta com um DB MySql
    """
    try:
        connection = mysql.connector.connect(host=host,
                                            database=database,
                                            user=user,
                                            password=password)
    
        
        if connection.is_connected():
            return connection
    except Exception as erro:
        print("OPS: {}".format(erro))    
    return None
    
def obtem_lista_twitches(connection, numero_informacoes: int):
    # Lista de constantes que criara o arquivo de constantes.
    lista_twitches = []
    if connection is not None and connection.is_connected():

        # Abre cursor para query
        cursor = connection.cursor()

        for tabela, campos in dict_tabela_campos.items():
            # Realiza query para obter as informacoes desejadas do BD
            cursor.execute(QUERY_CONSULTA_TWITTER.format(campos=campos, tabela=tabela,LIMIT=numero_informacoes))
            # Obtem a lista onde cada elemento é uma linha do BD
            dados = cursor.fetchall()


            # Adicionamos à nossa lista de informacoes
            lista_twitches.append(dados)


        # Realiza insert no banco dedados avisando que realizou uma requisição
        cursor.execute(QUERY_INSERT_REGISTER.format(campos="os.environ['HOSTNAME']", tabela='TB_INFO_POD'))

        # Fecha conexao com o banco
        cursor.close()
        connection.close()
    
    return lista_twitches


def obtem_dados_twitter(numero_informacoes: int = 500):
    # Gera conexao:
    connection = conecta_com_mysql(host=BD_INFO['HOST'], database=BD_INFO['NAME'], user=BD_INFO['USER'], password=BD_INFO['PASSWORD'])
    
    return obtem_lista_twitches(connection, numero_informacoes=numero_informacoes)[0]