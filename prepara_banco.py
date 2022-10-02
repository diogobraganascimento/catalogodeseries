import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash


print('Conectando...')
try:
      conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

# Exclui o banco existente
cursor.execute("DROP DATABASE IF EXISTS `catalogodeseries`;")

# Cria o banco
cursor.execute("CREATE DATABASE `catalogodeseries`;")

# Selecionando a tabela
cursor.execute("USE `catalogodeseries`;")

# Criando tabelas
TABLES = {}
TABLES['Series'] = ('''
      CREATE TABLE `series` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `categoria` varchar(20) NOT NULL,
      `plataforma` varchar(30) NOT NULL,
      `resumo` varchar(250) NOT NULL,
      `c_etaria` int(2) NOT NULL,
      `nota` int(1),
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `nome` varchar(20) NOT NULL,
      `nickname` varchar(8) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print(f'Criando tabela {tabela_nome}', end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# Inserindo usuários
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
      ("Diogo Braga", "dbn", generate_password_hash("123456").decode('utf-8')),
      ("Paula Braga", "paula", generate_password_hash("adorogatos").decode('utf-8')),
      ("Aquiles Alves", "quilao", generate_password_hash("minecraft").decode('utf-8')),
]

cursor.executemany(usuario_sql, usuarios)
cursor.execute('select * from catalogodeseries.usuarios')

print(' -------------  Usuários  --------------- ')
for user in cursor.fetchall():
      print(user[1])


# Inserindo series
serie_sql = 'INSERT INTO series (nome, categoria, plataforma, resumo, c_etaria, nota) VALUES (%s, %s, %s, %s, %s, %s)'
series = [
      ("Hanna", "Drama, Ação", "Prime Video", "Um suspence bem elaborado e um drama sobre o amadurecimento.", "18", "5"),
      ("The Good Doctor - O Bom Doutor", "Drama, Médico", "Globoplay", "Um jovem médico com autismo começa a trabalhar em um famoso hospital.", "12", "4"),
      ("Jujutsu Kaisen", "Shõnen", "Crunchyroll", "O jovem Okkotsu ganha o controle de um espirito extremamente poderoso.", "12", "5")
]
cursor.executemany(serie_sql, series)

cursor.execute('select * from catalogodeseries.series')
print(' -------------  Series  --------------- ')
for serie in cursor.fetchall():
      print(serie[1])






# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
