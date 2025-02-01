import psycopg2
class postgres:
    def __init__ (self, database, user, password, host, port):

        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port


    def crear_conexion (self):

        # si bien es cierto que crear la conexión es sencillo, es importante controlar los posibles errores que pudieran existir cuando realicemos estas conexiones
        try:
            connection = psycopg2.connect(
                database= self.database, # la base de datos con la que queremos trabajar
                user= self.user, # el usuario que tenemos 
                password= self.password,
                host= self.host,
                port= self.port)

            self.connection = connection

        except OperationalError as e:
            # Manejo de errores comunes
            if e.pgcode == errorcodes.INVALID_PASSWORD:
                print("Contraseña inválida.")
                
            elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
                print("Error de conexión.")
            else:
                print(f"Ocurrió un error: {e}")
        


    def cerrar_conexion(self):

        connection = self.crear_conexion()
        self.connection.close()

    def query_creacion(self, query):
        self.crear_conexion()
        connection = self.connection
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            cursor.close()
        except Exception as error:
            print(f"Ocurrió un error: {error}")

        self.cerrar_conexion()



    def query_insercion (self, tabla, df):
        self.crear_conexion()
        connection = self.connection
        cursor = connection.cursor()
        cols = ', '.join(df.columns)
        s = ['%s' for i in range(len(df.columns))]
        values = ', '.join(s)
        query = f'''INSERT INTO "{tabla}" ({cols}) VALUES ({values})'''
        lista_tuplas = df.to_numpy().tolist()
        try:
        # Ejecutamos nuestras queries
            cursor.executemany(query, lista_tuplas)
            connection.commit()
            #Mostramos el número de registros insertados
            print(cursor.rowcount, 'registros insertados')
            # Ejecutamos nuestra query
            cursor.close()
        #Si la query no es exitosa que nos indique el error pertiente
        except cursor.connector.Error as err:
                print(err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)
        cursor.close()
        self.cerrar_conexion()
        
