
import mysql.connector # !pip install mysql-connector-python 
from mysql.connector import Error

try: 
    connection = mysql.connector.connect(host='35.208.82.175', 
                                         database='dbgsipp7ucsuwy',
                                         user='uqsnolewgvge8',
                                         password='upgradehub', connection_timeout=180)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)

        cursor = connection.cursor()
        connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    # closing database connection.
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed") 



#Establecemos la conexión
connection = mysql.connector.connect(host='35.208.82.175', database='dbgsipp7ucsuwy', user='uqsnolewgvge8', password='upgradehub', connection_timeout=180000)
#conectamos el cursor, objeto importante para facilitar la ejecución de los comandos necesarios
cursor=connection.cursor()
db_Info = connection.get_server_info()
print("Connected to MySQL database... MySQL Server version on ", db_Info)

# 1.Obtener el listado de todos los productos 
query1 = "select * from PRODUCTO"
cursor.execute(query1)
print(cursor.fetchall())


# 2.Obtener el número de pedido, dni del repartidor y hora de reparto de aquellos pedidos que se toman nota después de las siete de la tarde
query2 =  "select numero, dni_r, hora_rep from PEDIDO where cast(hora_rep AS TIME) > '19:00:00'"
cursor.execute(query2)
print(cursor.fetchall())

# 3. Obtener todos los campos de empleados que cobran entre 900 y 1000 euros.
query3 =  "select * from EMPLEADO where salario between 900 AND 1000"""  
cursor.execute(query3)
print(cursor.fetchall())

# 4.Obtener el número de pedido e importe de aquellos que han sido registrados en el mes de noviembre de 2020 y su importe es mayor a 15 Euros.
query4 = "select Numero, Importe from PEDIDO where Fecha between '2020/1/01' and '2020/11/30' and Importe > 15;"
cursor.execute(query4)
print(cursor.fetchall())

# 5.Obtener por cada dni (con el formato de nombre y no de número ej. Noviembre),la cantidad de pedidos realizados.
query6 =  "select DNI_R, COUNT(*) as cantidad_pedidos from PEDIDO group by DNI_R;"
cursor.execute(query6)
print(cursor.fetchall())

# 6.Obtener por cada mes (con el formato de nombre y no de número ej. Noviembre),la cantidad de pedidos realizados.
query7 =  "select concat(dni, ', ', nombre) as empleado from EMPLEADO where Turno IN ('tarde', 'noche') order by dni;"
cursor.execute(query7)
print(cursor.fetchall())

# 7.Obtener el nombre, código y precio de aquellos productos que superen o igualen la media de todos los precios. Ordenar de mayor a menor precio.
query9 =  "select nombre, codigo, precio from PRODUCTO where precio >= (select avg(precio) from PRODUCTO) order by precio desc;"  
cursor.execute(query9)
print(cursor.fetchall())

# 8.Obtener un listado con el nombre y DNI de los empleados que no han preparado nunca ningún pedido.
query10 =  "select e.nombre, e.dni from EMPLEADO e where e.dni not in (select distinct dni_ep from PEDIDO) order by e.dni;"  
cursor.execute(query10)
print(cursor.fetchall())

# 9.Obtener el código, nombre y precio de los productos(estos dos últimos en el mismo campo)
#que están contenidos en los pedidos que ha tomado nota "Luis" o "María Luisa". 
#Ordena el listado de mayor a menor valor por fecha del pedido
query10 =  "select P.Codigo, concat(P.Nombre, ' ', P.Precio) as Producto, P.Precio from PRODUCTO P JOIN consta C ON P.Codigo = C.Codigo_Pr join PEDIDO Pe ON C.Numero_P = Pe.Numero where Pe.DNI_ETM IN ('11111111Q', '03232323P') order by Pe.Fecha desc;"
cursor.execute(query10)
print(cursor.fetchall())

# 10.Obtener por cada repartidor, su nombre, cantidad de pedidos y el tiempo medio que tardan en entregar los pedidos una vez preparados. 
#Ordenar el listado el tiempo medio que tardan en entregarlos:
query12 =  "select R.Nombre, count(P.Numero) as cantidad_pedidos, avg(TIMESTAMPDIFF(SECOND, P.Hora_pre, P.Hora_rep)) / 60 as tiempo_medio_minutos from REPARTIDOR R JOIN PEDIDO P ON R.DNI = P.DNI_R group by R.DNI order by tiempo_medio_minutos;"  
cursor.execute(query12)
print(cursor.fetchall())

# 11.Obtener un listado obteniendo el código, nombre y el precio de los productos cuyo precios sea el más barato o el más caro de todos
query12 =  "select P.Codigo, P.Nombre, P.Precio from PRODUCTO P where P.Precio = (select min(Precio) from PRODUCTO) OR P.Precio = (select max(Precio) from PRODUCTO);"  
cursor.execute(query12)
print(cursor.fetchall())

# 12.Obtener por cada producto , el nombre y código el número total de pedidos en los que.
#se encuentra teniendo en cuenta que el total de pedidos en los cuales se encuentre sea superior o igual a dos. 
#Ordena el listado de mayor a menor número de productos.
query12 =  "select P.Nombre, P.Codigo, COUNT(C.Numero_P) as total_pedidos from PRODUCTO P JOIN consta C ON P.Codigo = C.Codigo_Pr group by P.Nombre, P.Codigo having count(C.Numero_P) >= 2 order by total_pedidos desc;"  
cursor.execute(query12)
print(cursor.fetchall())

# 13.Mostrar listado de los empleados (código y NSS en la misma columna) que han tomado nota de algún pedido y contienen el producto 
#de código 13 y además el repartidor sea 'Laura'.
query13 =  "select concat(E.DNI, ', ', E.Nss) as Empleado_NSS from EMPLEADO E JOIN PEDIDO P on E.DNI = P.DNI_ETM JOIN consta C ON P.Numero = C.Numero_P where C.Codigo_Pr = '13' and P.DNI_R = '04477744T';"  
cursor.execute(query13)
print(cursor.fetchall())

# 14.Obtener el nombre del producto que es menú junto con el código de los productos 
#que lo componen en aquellos pedidos del mes de septiembre de 2020.0
query14 = "SELECT P.Codigo, P.Nombre, EC.Codigo_P, EC.Codigo_P_compuesto, Pc.Nombre FROM PEDIDO Pe JOIN consta C ON Pe.Numero = C.Numero_P JOIN PRODUCTO P ON C.Codigo_Pr = P.Codigo JOIN esta_compuesto EC ON P.Codigo = EC.Codigo_P JOIN PRODUCTO Pc ON EC.Codigo_P_compuesto = Pc.Codigo WHERE Pe.Fecha BETWEEN '2020-09-01' AND '2020-09-30';"
cursor.execute(query14)
print(cursor.fetchall())


