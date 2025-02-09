# SGE-BLOC2 
José G. Fernández DAM1B

## CONEXIÓN A UNA BASA DE DATOS

![llamada_conn](bloc2_JOSEGFERNANDEZ/img/1-llamada_conexion.png)

### Se está realizando una conexión a una base de datos PostgreSQL usando la librería psycopg2. En el código, la función connection_db() establece la conexión con la base de datos the_bear utilizando los parámetros proporcionados y devuelve el objeto conn, que representa dicha conexión. El print(conn) muestra que la conexión se ha establecido correctamente (closed: 0) y que se cierra satisfactoriamente (closed: 1).

### Previamente se ha iniciado PostgreSQL a través de Docker, creado un entorno virtual con Python 3.10, instalado la librería psycopg2 para la conexión con PostgreSQL y pandas para gestionar los datos de la base de datos, incluyendo la carga de un archivo CSV.

## CREACIÓN E INSERCIÓN EN UNA BASE DE DATOS

![create-able](bloc2_JOSEGFERNANDEZ/img/2-create_tables.png)

### Se descargan los datos en formato CSV y se procede a insertarlos en la base de datos.

### Primer paso, se utiliza un archivo llamado create_table para crear una tabla vacía siguiendo el formato del archivo CSV. En este archivo, se define la función create_table(), que establece una conexión con PostgreSQL y ejecuta una consulta SQL para crear una tabla llamada clientes.

### Se guardan los cambios y se cierran la conexión y el cursor. El cursor, en psycopg2, es un objeto que permite ejecutar consultas SQL dentro de una conexión, funcionando como el intermediario entre Python y la base de datos. Se establece la conexión (cursor = conn.cursor()) y se ejecuta la creación de la tabla con cursor.execute(sql_clients).

![csvtodict](bloc2_JOSEGFERNANDEZ/img/3-csvtodict.png)

### Con el archivo csv_to_dict, se transforma la información del CSV en formato diccionario, un tipo de dato en el que Python almacena información en pares clave-valor. Esto facilita la organización y el acceso a los datos.

### Los datos se envían a la base de datos mediante d_t_bdb-send_data_to_db.

![dicttodb](bloc2_JOSEGFERNANDEZ/img/4-dicttodb.png)

![vista-tabla-pgadmin](bloc2_JOSEGFERNANDEZ/img/5-vista-tabla-pgadmin.png)

### El último paso de la inserción de datos consiste en insertar la información del diccionario en cada columna correspondiente, es decir, agregar los valores en los distintos campos existentes, como nombre, dirección, teléfono, etc.

### Una vez completada la inserción, se guardan los cambios y se cierra la conexión. Se recibe un mensaje de confirmación: "Process finished with exit code 0", que indica que el proceso se ha ejecutado correctamente.

## CREAR REGISTROS

![create_registre](bloc2_JOSEGFERNANDEZ/img/6-create_registre.png)

### Aquí vemos cómo el código del archivo create_registre crea una nueva entrada en la base de datos.

### Se establece la conexión con cursor = conn.cursor(), se define el formato de la consulta (sql_create) y los valores a insertar (values) y se ejecuta la inserción con cursor.execute(sql_create, values).

### Al finalizar, se muestra el código 0 indicando que el registro se ha realizado correctamente. Se ha establecido la conexión, se han insertado los datos y se ha cerrado la conexión con la base de datos.

![tabla-Clientes-new](bloc2_JOSEGFERNANDEZ/img/8-tabla-clientes-new.png)

### Aquí se muestra el resultado en la base de datos,donde se han insertado correctamente los datos.

### Para realizar esta inserción en la tabla, también es necesario modificar el archivo main para que llame a la función cr.create_reg(). El código ejecuta esta función dentro del archivo create_registre.py.

## MÉTODOS PARA EXTRAER INFORMACIÓN

![read-registre](bloc2_JOSEGFERNANDEZ/img/9-read_registre.png)

### En la imagen se observa cómo primero se establece una conexión con la base de datos mediante conn y luego se inicializa cursor para ejecutar consultas SQL.

### Se ejecuta la consulta sql_read, que recupera todos los datos (con el uso de *) de la tabla clientes. El uso de cursor.fetchall() obtiene todas las filas devueltas por la consulta. Los resultados se muestran en pantalla mediante print().

![read-registre1](bloc2_JOSEGFERNANDEZ/img/10-read_registre1a.png)

### Aquí se muestra cómo se ha realizado una consulta específica al índice 4, que corresponde al id_cliente 5 (Alba).

### Aquí se muestra la información del teléfono de Alba, que se encuentra en la fila con índice 4 de la base de datos. Dentro de esta fila, el dato está ubicado en la columna 2, donde se almacenan los números de teléfono.

### El valor se estructura como un array dentro de otro array, lo que significa que los datos están organizados en una estructura anidada.

![read-registre2](bloc2_JOSEGFERNANDEZ/img/11-read_registre2.png)

### Aquí màs resultados de consultas

![read-registre3](bloc2_JOSEGFERNANDEZ/img/12-read_registre3.png)

### En esta búsqueda, se utiliza un bucle for para recorrer todas las columnas de la base de datos. Con el for y el salto de línea (\n), los datos se muestran de manera clara y organizada.

### Primero se llama a la función del archivo read_registre y luego se ejecuta con rr.read_reg().

## EDITAR INFORMACIÓN

### Se ha cambiado el código de main.py para poder hacer la llamada de update_registre. 

![main-up](bloc2_JOSEGFERNANDEZ/img/12A-main_up.png)

### Usaremos las tres primeras filas para hacer algunos cambios.

![tabla](bloc2_JOSEGFERNANDEZ/img/13-tabla.png)

### Cambiaremos el número de teléfono

![update-registre](bloc2_JOSEGFERNANDEZ/img/14-update_registre1.png)

![tabla-up](bloc2_JOSEGFERNANDEZ/img/14-up_registre1.png)

### Cambiaremos el nombre

![up-nombre](bloc2_JOSEGFERNANDEZ/img/15-up_nombre.png)

![up-nombre1](bloc2_JOSEGFERNANDEZ/img/15-up_nombre1.png)

## BORRAR INFORMACIÓN

### Volveremos a modificar main.py

![delete_main](bloc2_JOSEGFERNANDEZ/img/16-delete_main.png)

### Escribimos el código al archivo delete_registre.py

![delete_nombre](bloc2_JOSEGFERNANDEZ/img/16-delete_nombre.png)

### Así quedara la base de datos despues de eliminar los tres registros.

![delete_table](bloc2_JOSEGFERNANDEZ/img/16-detete_table.png)

