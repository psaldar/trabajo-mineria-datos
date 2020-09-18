## Trabajo final - Sistemas de recomendación para un marketplace: modelos con información histórica y cold start (productos nuevos)
============================================================================

### "Minería de datos para grandes volúmenes de información"

Pablo A. Saldarriaga<sup>1</sup>, Nicolás Prieto<sup>1</sup>, Karen Velásquez<sup>1</sup>, Ana María Urán<sup>1</sup>, Victoria Álvarez<sup>1</sup>

<sup>1</sup> Maestría en Ciencia de los Datos y Analítica, Universidad EAFIT, Medellín, Colombia

## Descripción


El proyecto relacionado en este repositorio corresponde a la creación de sistemas de recomendación para el Marketplace de Amazon, los cuales se crean a través del uso de información histórica de los reviews de diferentes productos asociados a diferentes usuarios, además de tener en cuenta características propias de los productos. De esta forma, en este repositorio se pueden encontrar los códigos, archivos y programas relacionados con el desarrollo del proyecto.

Dado que se está enfrentando un problema de Big Data (debido a las altas dimensiones de la información disponible para la creación de sistemas de recomendación), el proyecto fue realizado utilizando los servicios de la nube de Amazon, usando una cuenta de AWS educate. De forma particular, el servicio que se utilizó para realizar el procesamiento de la información y la creación de los modelos utilizando pyspark fue un clúster de EMR con 4 nodos m5.xlarge. Por lo tanto, el notebook asociado al desarrollo del trabajo (el cual se encuentra en la carpeta "Entrega_final" y se llama "Trabajo-entrega-mineria-datos.ipynb") fue ejecutado en la nube de Amazon para la obtención de los resultados. Debido a que la configuración del clúster de EMR contaba con el kernel de pyspark y traía algunas librerías preinstaladas, únicamente se requirió instalar la librería pandas (1.1.2), la cual fue utilizada en algunos de los pasos de análisis.

El desarrollo de la entrega final inicia realizando limpieza y muestreo de los datos, posteriormente ejecuta modelos baseline (media, mediana, media por producto, media por cliente), factores latentes (empleando ALS de pyspark ml) y se adicionan sesgos. Finalmente, se diseña e implementa un modelo para los casos de cold start. Todo este procedimiento se puede ver en el notebook final anteriormente mencionado.

Respecto a la información necesaria para ejecutar el trabajo, se utilizó el dataset Amazon Customer Reviews que se encuentra almacenado en un bucket de S3 en datos abiertos de Amazon (se puede encontrar su descripción en https://s3.amazonaws.com/amazon-reviews-pds/readme.html), además de la metadata de ciertos productos que está disponible en http://jmcauley.ucsd.edu/data/amazon/. Este último conjunto de información es necesario para extraer características de los productos, la cual es consumida por el modelo que se usa en cold start. Se menciona que, si bien se utilizó la información de la metadata para la creación del modelo para los casos de cold start, esta información fue descargada, procesada y almacenada en varios archivos csv que fueron cargados en un bucket de S3 (para realizar este proceso, se usó el archivo "Split_metadata.py" de la carpeta "Entrega_final", el cual toma el archivo comprimido de la metadata y extrae solo columnas de interés y realiza la partición de los datos en archivos csv con no más de 1.5 millones de registros cada uno). Para obtener estos archivos csv sin necesidad de ejecutar el script, se puede usar el siguiente link de Google drive: https://drive.google.com/drive/folders/1O6wwpSUKFIQKHggYhkF8QGcDWeE1vccx?usp=sharing



Adicionalmente, en este repositorio en la carpeta “Anteproyecto”, se puede encontrar el notebook que presenta la viabilidad de la creación de un sistema de recomendación para este caso, el cual usa una muestra que contiene solo los reviews de una categoría de producto y con esto se evaluó el sistema. Para ejecutar este notebook, se puede descargar la muestra que se utilizó del siguiente link de Google drive: https://drive.google.com/drive/folders/1Obo2lWQBfDTinmSyPAddNiOzT2BXZnvP?usp=sharing

En la carpeta "Documentos" se pueden encontrar los archivos en PDF entregados en este proyecto.

