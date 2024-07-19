# Configuración de MySQL
$MYSQL_USER = "root"
$MYSQL_PASSWORD = "root"
$MYSQL_HOST = "localhost"
$MYSQL_PORT = "3306"
$DATABASE = "eventra"

# Crear base de datos
$CREATE_DB_QUERY = "CREATE DATABASE IF NOT EXISTS $DATABASE;"
mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -h $MYSQL_HOST -P $MYSQL_PORT -e "$CREATE_DB_QUERY"

# Realizar migraciones de la base de datos
python manage.py makemigrations
python manage.py migrate

# Ejecutar las consultas SQL
$USE_DB_QUERY = "USE $DATABASE;"
$INSERT_ADMIN_QUERY = "INSERT INTO EventraApp_typeofuser (description) VALUES ('Admin');"
$INSERT_USER_QUERY = "INSERT INTO EventraApp_typeofuser (description) VALUES ('User');"

mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -h $MYSQL_HOST -P $MYSQL_PORT -e "$USE_DB_QUERY $INSERT_ADMIN_QUERY"
mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -h $MYSQL_HOST -P $MYSQL_PORT -e "$USE_DB_QUERY $INSERT_USER_QUERY"

# Iniciar el servidor de Django
python manage.py runserver
