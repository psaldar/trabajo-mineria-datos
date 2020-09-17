# Proyecto Sistemas de recomendación para un marketplace: modelos con información historica y cold start (productos nuevos)

El proyecto fue ejecutado en AWS en un clúster de EMR m5.xlarge con 4 nodos, se empleó pyspark para el procesamiento y la ejecución de los modelos. 
Únicamente se requirió instalar pandas puesto que el clúster fue configurado con Spark.

Se utilizó el dataset Amazon Customer Reviews  que se encuentra almacenado en un S3 en datos abiertos de Amazon y descrito en https://s3.amazonaws.com/amazon-reviews-pds/readme.html, la metadata de ciertos productos está disponible en http://jmcauley.ucsd.edu/data/amazon/. Esta última es necesaria para extraer características de los productos para el modelo cold start.

El proyecto inicia realizando limpieza y muestreo de los datos. Se ejecutan modelos baseline (media, mediana, media por producto, media por cliente), factores latentes (empleando ALS de pyspark ml) y se adicionan sesgos. Finalmente, se diseñó e implementó un modelo para cold start.

Autores:
- Pablo Saldarriaga
- Nicolás Prieto
- Karen Velásquez
- Ana María Urán
- Victoria Álvarez
