## TFG_Roberto_Jimenez_delaTorre
En este proyecto se encuentra el código del trabajo fin de grado sobre el desarrollo de un sistema de evaluación de riesgos ante ciberataques en tiempo real mediante el uso de ontologías y tecnologías Big Data.
## Componentes requeridos para la instalación:
1. Python 3.9.13
2. Protégé 5.6.1
3. Librería de Owlready2 de Python.
4. Librería de CSV de Python.
## Archivos del proyecto:
1. Sistemas basados en python para ejecutar las ontologías, uno distinto por cada ontología.
2. Archivos CSV necesarios para cada ontologia con sus respectivos individuos.
3. Archivos OWL que contienen la estructura de cada ontología.
## Procedimiento de ejecución del código:
1. Importamos el proyecto en cualquier entorno de desarrollo integrado(IDE), en este caso se está utilizando Visual Studio Code. 
2. Abrimos una terminal de comandos dentro de la ruta del proyecto.
3. Ejecutamos el comando 'python ontologia_basica.py' si queremos ejecutar la ontología básica.
4. Ejecutamos el comando 'python ontologia_compleja.py' si queremos ejecutar la ontología compleja.
5. Se puede comprobar que se devuelve por pantalla un print con el tiempo final de ejecucción en segundos.Además, para cada activo se muestra su nivel de riesgo   inicial, el valor de todos los impactos que recibe y su nivel de riesgo final, el cual se obtiene mediante la suma de los dos valores previamente mencionados.
6. Cada script de python guarda toda la información en el archivo **ontología_basica_tfg.owl** para la **ontologia_tfg.owl** y en el archivo **ontologia_compleja_tfg.owl** para la **ontologia_tfg_2.owl**. Si accedemos a esos archivos desde Protégé podemos comprobar como se han cargado y clasificado todos los individuos con sus diferentes reglas de razonamiento. 
