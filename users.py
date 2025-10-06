import mysql.connector
import bcrypt

mydb = mysql.connector.connect(
    host="localhost",
    port=3308,
    user="root",
    password='root',
    database='dados'
)

def ver_usuario():
    mycursor = mydb.cursor()
    result = []

    sql = "SELECT * FROM usuarios"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        result.append(x)
    return result
    

def ver_usuario_id(id):
    mycursor = mydb.cursor()

    sql = "SELECT * FROM usuarios WHERE id = %s"
    val = id,

    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    for x in myresult:
        return x

def criar_usuario(name, senha):
    mycursor = mydb.cursor()

    senha_codigo = senha.encode('utf-8')
    senha_hash = bcrypt.hashpw(senha_codigo, bcrypt.gensalt()).decode('utf-8')
    
    sql = "INSERT INTO usuarios (name, senha) VALUES (%s, %s)"
    val = (name, senha_hash)
    
    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        return {"mensagem": "Usuario Já cadastrado!"}

    return {"mensagem": "Usuario criado com sucesso!"}


def login(name, senha):
    mycursor = mydb.cursor()

    query = "SELECT * FROM usuarios WHERE name = %s"
    val = (name,)

    mycursor.execute(query, val)
    myresult = mycursor.fetchone()

    if myresult is None:
        return {"mensagem": "Usuário não localizado"}

    else:
        senha_codigo = myresult[2].encode('utf-8')
        senha_digitada = senha.encode('utf-8')

        if bcrypt.checkpw(senha_digitada, senha_codigo):
            return {"mensagem": "logado com sucesso"}
        
        else:
            return {"mensagem": "ERRO! senha errada!"}

        




    
        

