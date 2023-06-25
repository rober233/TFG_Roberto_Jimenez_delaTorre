## TFG_Roberto_Jimenez_delaTorre
En este proyecto se encuentra el código del trabajo fin de grado sobre el desarrollo de un sistema de evaluación de riesgos ante ciberataques en tiempo real mediante el uso de ontologías y tecnologías Big Data.
## Componentes requeridos para la instalación:
1. Python 3.9.13
2. Protégé 5.6.1
3. Librería de Owlready2 de Python.
4. Librería de CSV de Python.
5. Anaconda 3.0
6. Librería sklearn.
7. Librería pandas.
8. Librería pyplot.
## Archivos del proyecto:
1.	Sistemas basados en Python para ejecutar las ontologías, uno distinto por cada ontología y método de ejecución **‘ontologia_basica.py’** y **‘ontologia_basica_multi.py’** para la **‘ontologia_tfg.owl’** y **‘ontologia_compleja.py’** y **‘ontologia_compleja_multi.py’** para la **‘ontologia_tfg_2.owl’**.
2.	Archivos CSV necesarios para cada ontología con sus respectivos individuos **‘activos.csv’**, **‘Datos_TFG_Basica.csv’** y **‘Datos_TFG_Compleja.csv’**.
3.	Archivos OWL que contienen la estructura de cada ontología **‘ontologia_tfg.owl’** y **‘ontologia_tfg_2.owl’**.
4.	Carpeta con los archivos necesarios para la selección de características, un archivo CSV con el dataset **‘seleccion_caracteristicas.csv’** y un archivo Python **‘seleccion_caracteristicas_TFG.py’** con el modelo RF. 
## Procedimiento de ejecución del código para la selección de características:
1. Importamos el proyecto en cualquier entorno de desarrollo integrado(IDE), en este caso se está utilizando Spyder.
2. Abrimos una terminal de comandos dentro de la ruta del proyecto.
3. Ejecutamos el comando '**python seleccion_caracteristicas_TFG.py**' para ejecutar el modelo de machine learning Random Forest.
4. Se puede comprobar el resultado en el terminal, donde aparecerá un gráfico con la importancia de cada característica.
## Procedimiento de ejecución del código para las ontologías:
1. Importamos el proyecto en cualquier entorno de desarrollo integrado(IDE), en este caso se está utilizando Visual Studio Code. 
3. Abrimos una terminal de comandos dentro de la ruta del proyecto.
4. Ejecutamos el comando '**python ontologia_basica.py**' si queremos ejecutar la ontología básica con el método íntegro y '**python ontologia_basica_multi.py**' para ejecutar el método por multiprocesado.
5. Ejecutamos el comando '**python ontologia_compleja.py**' si queremos ejecutar la ontología compleja con el método íntegro y '**python ontologia_complejo_multi.py**' para ejecutar el método por multiprocesado.
6. Se puede comprobar que se devuelve por pantalla un print con el tiempo final de ejecución en segundos.Además, para cada activo se muestra su nivel de riesgo   inicial, el valor de todos los impactos que recibe y su nivel de riesgo final, el cual se obtiene mediante la suma de los dos valores previamente mencionados.
7. Cada script de python guarda toda la información en el archivo **ontología_basica_tfg.owl** para la **ontologia_tfg.owl** y en el archivo **ontologia_compleja_tfg.owl** para la **ontologia_tfg_2.owl**. Si accedemos a esos archivos desde Protégé podemos comprobar como se han cargado y clasificado todos los individuos con sus diferentes reglas de razonamiento. 
