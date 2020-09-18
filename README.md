## Trabajo final - Proyecto Sistemas de recomendación para un marketplace: modelos con información historica y cold start (productos nuevos)
============================================================================

### "Minería de datos para grandes volúmenes de información"

Pablo A. Saldarriaga<sup>1</sup>, Nicolás Prieto<sup>1</sup>, Karen Velásquez<sup>1</sup>, Ana María Urán<sup>1</sup>, Victoria Álvarez<sup>1</sup>

<sup>1</sup> Maestría en Ciencia de Datos, Universidad EAFIT, Medellín, Colombia

## Descripción


El proyecto relacionado en este repositorio corresponde a la creación de sistemas de recomendación para el Marketplace de Amazon utilizando información histórica disponible de los reviews de diferentes productos asociados a diferentes usuarios, además de metadata propia de los productos. De esta forma, en este repositorio se pueden encontrar los códigos y programas utilizados en el desarrollo del proyecto.

Dado que se está enfrentando un problema de Big Data (debido a las altas dimensiones de la información disponible para la creación de sistemas de recomendación), el proyecto fue realizado utilizando los servicios de la nube de Amazon, utilizando una cuenta de AWS educate. De forma particular, el servicio que se utilizó fue tanto un clúster de EMR m5.xlarge con 4 nodos para realizar el procesamiento de la información y creación de los modelos utilizando pyspark. Por lo tanto, el notebook asociado al desarrollo del trabajo (archivo Entrega_final/Trabajo-entrega-mineria-datos.ipynb) fue ejecutado en la nube de Amazon para la obtención de los resultados. Ya que por la configuración del clúster se contaba con el kernel de pyspark, adicional a las librerías que este trae, se requirió instalar únicamente la librería panda que fue utilizada en algunos de los pasos de análisis.

Respecto a la información necesaria para ejecutar el trabajo, se utilizó el dataset Amazon Customer Reviews que se encuentra almacenado en un bucket de S3 en datos abiertos de Amazon (se puede encontrar su descripción en https://s3.amazonaws.com/amazon-reviews-pds/readme.html), además de la metadata de ciertos productos está disponible en http://jmcauley.ucsd.edu/data/amazon/. Este último conjunto de información es necesario para extraer características de los productos para el modelo cold start. Se menciona que si bien se utilizó la información de la metadata para la creación del modelo Cold Star, el archivo descargado fue procesado y almacenado en varios archivos csv que fueron cargados en un bucket de S3 (para realizar este proceso, se tiene el archivo Entrega_final/Split_metadata.py que toma el archivo comprimido de la metadata, y extrae solo columnas de interés y realiza la partición en archivos csv con no más de 1.5 millones de registros), así, para obtener los archivos csv sin necesidad de ejecutar el script, se pueden descargar del siguiente link de google drive: https://drive.google.com/drive/folders/1O6wwpSUKFIQKHggYhkF8QGcDWeE1vccx?usp=sharing

El desarrollo de la entrega final inicia realizando limpieza y muestreo de los datos, posteriormente ejecuta modelos baseline (media, mediana, media por producto, media por cliente), factores latentes (empleando ALS de pyspark ml) y se adicionan sesgos. Finalmente, se diseñó e implementó un modelo para cold start.

Adicionalmente, en este repositorio en la carpeta “Anteproyecto”, se pueden encontrar el notebook que presenta la viabilidad de la creación de un sistema de recomendación, para esto se sacó una muestra de los reviews de una categoría de producto y se construyó el sistema. Para ejecutar este notebook, se puede descargar la información ya filtrada del siguiente link de Google drive: https://drive.google.com/drive/folders/1Obo2lWQBfDTinmSyPAddNiOzT2BXZnvP?usp=sharing

En la carpeta Documentos se pueden encontrar los archivos en PDF entregados en este proyecto.

