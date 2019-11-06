import mysql.connector 

dict_tabela_campos = {
    '': '', # Nome da tabela : Campos da tabela 
}
QUERY_CONSULTA_TWITTER = "SELECT {campos} from {tabela}"

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
    
def obtem_lista_twitches(connection):
    # Lista de constantes que criara o arquivo de constantes.
    lista_twitches = []
    if connection is not None and connection.is_connected():

        # Abre cursor para query
        cursor = connection.cursor()

        for tabela, campos in dict_tabela_campos.items():
            # Realiza query para obter as informacoes desejadas do BD
            cursor.execute(QUERY_CONSULTA_TWITTER.format(campos=campos, tabela=tabela))
            # Obtem a lista onde cada elemento é uma linha do BD
            dados = cursor.fetchall()
            # Adicionamos à nossa lista de informacoes
            lista_twitches.append(dados)

        # Fecha conexao com o banco
        cursor.close()
        connection.close()
    
    return lista_twitches
