import psycopg2 as ps

postgre={"host":"localhost","dbname":"PythonSql","user":"postgres","password":"M12587410@s"}

conexao=ps.connect(**postgre)

class Db_comandos:
    @staticmethod
    def consulta(email,senha):
        comando=f"""select email,senha from usuarios where email='{email}' and senha='{senha}'
        """
        cursor=conexao.cursor()
        cursor.execute(comando)
        conexao.commit()
        result=cursor.fetchall()

        try:
            usuario_db=result[0][0]
            senha_usuario_db=result[0][1]  
        except(IndexError):
            usuario_db=None
            senha_usuario_db=None
        else:
            if(email==usuario_db and senha==senha_usuario_db):
                return True
            else:
                return False

                
                
            
                

    
      

    













