# 📘 PREGUNTAS_Y_RESPUESTAS_FUNDAMENTOS_GENERAL

---

## 🐍 0. ¿Qué es Python?

Python es un lenguaje tipado, pero usa **tipado dinámico**, lo que significa que no tienes que declarar los tipos de variables — Python los determina en tiempo de ejecución.

---

### 🔐 0.1 Existen objetos inmutables y mutables — ¿qué son?

En Python, algunos objetos son mutables y otros son inmutables.

| Tipo | ¿Se puede cambiar? | Ejemplos |
|------|-------------------|----------|
| 🔒 **Inmutable** | ❌ No | `int`, `float`, `string`, `tuple`, `bool` |
| 🔓 **Mutable** | ✅ Sí | `list`, `dict`, `set` |

**Diferencia simple:**
- **Inmutable** = no puedes modificar el objeto en sí (si lo "cambias", Python crea un nuevo objeto)
- **Mutable** = puedes modificar el objeto en su lugar (no se crea un nuevo objeto)

---

### ⚙️ 0.2 ¿Qué es una función?

Una función es un bloque de código reutilizable que recibe una entrada, realiza alguna lógica y devuelve una salida.

---

## 🗄️ 1. ¿Qué es SQL (Structured Query Language)?

SQL (Structured Query Language) es un lenguaje usado para almacenar, recuperar y gestionar datos en bases de datos relacionales. Te permite consultar datos, actualizarlos y organizarlos usando tablas.

---

### 📋 1.2 ¿Cuál es la diferencia entre DDL y DML?

| Categoría | Nombre Completo | Propósito | Comandos |
|-----------|-----------------|-----------|----------|
| 🏗️ **DDL** | Data Definition Language | Definir/cambiar estructura | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| 📝 **DML** | Data Manipulation Language | Trabajar con datos | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |

---

### 📊 1.3 ¿Qué es una agregación?

Una agregación (en SQL o ingeniería de datos) es una operación que combina múltiples filas en un solo resultado aplicando una función.

| Función | Descripción |
|---------|-------------|
| `SUM()` | Suma valores |
| `COUNT()` | Cuenta filas |
| `AVG()` | Promedio |
| `MAX()` / `MIN()` | Valor más alto o más bajo |

---

### 🔧 1.4 Otros tipos de operaciones

| Operación | Descripción | Palabras clave |
|-----------|-------------|----------------|
| 🔍 **Filtrado** | Selecciona solo las filas que quieres | `WHERE`, `HAVING` |
| 🔗 **Joins** | Combina datos de múltiples tablas | `INNER`, `LEFT`, `RIGHT`, `FULL` |
| 📊 **Ordenamiento** | Ordena los resultados | `ORDER BY` |
| 📦 **Agrupamiento** | Agrupa filas para agregaciones | `GROUP BY` |
| 🪟 **Window Functions** | Cálculos sobre conjuntos de filas | `OVER()` |
| ➕ **Operaciones de Conjunto** | Combina resultados de queries | `UNION`, `INTERSECT`, `EXCEPT` |
| 🔄 **Subqueries** | Queries dentro de otros queries | `(SELECT ...)` |

```sql
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

---

## 🌊 2. ¿Cuál es la diferencia entre Delta Lake y Data Lake?

| Característica | 🌊 Data Lake | 🔺 Delta Lake |
|----------------|--------------|---------------|
| **Definición** | Almacenamiento grande para todo tipo de datos | Data lake mejorado con confiabilidad |
| **Calidad de Datos** | ❌ Sin garantías | ✅ Aplicación de esquema |
| **Transacciones ACID** | ❌ No | ✅ Sí |
| **Time Travel** | ❌ No | ✅ Sí (historial de versiones) |
| **Updates/Deletes** | ❌ Difícil | ✅ Fácil |

**Analogía simple:**
- 🏠 **Data Lake** = Una gran bodega donde puedes poner cualquier cosa
- 🏢 **Delta Lake** = La misma bodega pero con organización, etiquetas, seguridad y seguimiento

---

## ⚡ 3. ¿Qué es Spark?

Apache Spark es un framework rápido y de código abierto usado para procesar grandes cantidades de datos a través de muchas máquinas.

| Capacidad | Descripción |
|-----------|-------------|
| 📊 **Batch Processing** | Procesa grandes datasets |
| 🌊 **Streaming** | Procesamiento de datos en tiempo real |
| 🗃️ **SQL** | Consulta datos con Spark SQL |
| 🤖 **ML** | Machine learning con MLlib |

**¿Por qué es popular Spark?**

| Ventaja | Descripción |
|---------|-------------|
| 🚀 **Velocidad** | 100x más rápido que Hadoop MapReduce (en memoria) |
| 🐍 **Fácil de Usar** | Soporte para Python, SQL, Scala, Java |
| 📈 **Escalable** | Desde laptop hasta miles de servidores |

> 💡 **¿Por qué Spark es más rápido que MapReduce?**
> 
> - **Hadoop MapReduce** escribe resultados intermedios a HDFS (disco) después de cada etapa map y reduce. Esto lo hace más lento pero muy tolerante a fallos.
> - **Apache Spark** almacena la mayoría de los datos intermedios en memoria (RAM) usando RDDs, lo que lo hace mucho más rápido que MapReduce.

---

## 📦 4. ¿Qué es un RDD?

Un **RDD** (Resilient Distributed Dataset) es la estructura de datos básica en Apache Spark. Representa una colección de datos tolerante a fallos dividida entre muchas máquinas.

| Propiedad | Descripción |
|-----------|-------------|
| 🔒 **Inmutable** | No puede cambiar una vez creado |
| 💾 **En Memoria** | Procesamiento rápido |
| 🌐 **Distribuido** | Dividido entre máquinas |
| 🔄 **Tolerante a Fallos** | Auto-recuperación vía lineage |

---

### ⚖️ 4.1 ¿Cuál es la diferencia entre RDD y DataFrame?

| Aspecto | 📦 RDD | 📊 DataFrame |
|---------|--------|--------------|
| **Nivel** | Bajo nivel | Alto nivel |
| **Esquema** | ❌ Sin esquema | ✅ Tiene esquema |
| **Optimización** | ❌ Manual | ✅ Optimizador Catalyst |
| **Facilidad de Uso** | Complejo | Fácil (similar a SQL) |
| **Rendimiento** | Bueno | Mejor (optimizado) |
| **Mejor Para** | Datos no estructurados | Datos estructurados |

---

### 🔄 4.2 ¿Cuál es la diferencia entre Transformaciones y Acciones en Spark?

En Spark, las operaciones sobre RDDs/DataFrames se dividen en dos categorías:

| Aspecto | 🔄 Transformaciones | ▶️ Acciones |
|---------|---------------------|-------------|
| **Ejecución** | Lazy (no se ejecutan inmediatamente) | Eager (dispara la ejecución) |
| **Retorna** | Nuevo RDD/DataFrame | Resultado al driver o almacenamiento |
| **Ejemplos** | `map`, `filter`, `select`, `groupBy`, `join` | `collect`, `count`, `show`, `write`, `take` |
| **DAG** | Construye el plan de ejecución | Ejecuta el DAG |

**🔄 Transformaciones (Lazy):**
- Crean un nuevo RDD/DataFrame a partir de uno existente
- No se ejecutan hasta que se llama una acción
- Construyen el **DAG (Directed Acyclic Graph)** de operaciones

```python
# Estas son transformaciones - ¡nada se ejecuta aún!
df_filtered = df.filter(df["age"] > 25)
df_selected = df_filtered.select("name", "salary")
df_grouped = df_selected.groupBy("name").sum("salary")
```

**▶️ Acciones (Eager):**
- Disparan la ejecución de todas las transformaciones
- Devuelven resultados al driver o escriben al almacenamiento

```python
# Esta es una acción - ¡AHORA todas las transformaciones se ejecutan!
df_grouped.show()        # Acción: muestra resultados
df_grouped.count()       # Acción: devuelve número de filas
df_grouped.collect()     # Acción: devuelve todos los datos al driver
df_grouped.write.parquet("output/")  # Acción: escribe al almacenamiento
```

> 💡 **¿Por qué Evaluación Lazy?**
> 
> Spark usa evaluación lazy porque permite al **Catalyst Optimizer** analizar el DAG completo y optimizar el plan de ejecución antes de ejecutar. Esto lleva a:
> - **Mejor rendimiento:** Combina múltiples operaciones en menos pasos
> - **Menor I/O:** Evita escrituras intermedias innecesarias
> - **Optimización:** Predicate pushdown, column pruning, reordenamiento de joins

| Tipo de Transformación | Descripción | Ejemplos |
|------------------------|-------------|----------|
| **Narrow** | Cada partición depende de una partición padre | `map`, `filter`, `select` |
| **Wide** | Las particiones dependen de múltiples particiones padre (shuffle) | `groupBy`, `join`, `repartition` |

> 🎯 **Tip de Entrevista:** "Entiendo que las transformaciones son lazy y construyen el DAG, mientras que las acciones disparan la ejecución. Por esto puedo encadenar muchas transformaciones sin problemas de rendimiento - Spark optimiza todo el plan antes de ejecutar. También conozco la diferencia entre transformaciones narrow y wide, lo que me ayuda a entender cuándo ocurren shuffles."

---

## 📨 5. ¿Qué es Apache Kafka?

Apache Kafka es una plataforma de streaming distribuida usada para mover datos entre sistemas en tiempo real.

| Componente | Descripción |
|------------|-------------|
| 📤 **Producer** | Envía mensajes a Kafka |
| 📁 **Topic** | Categoría/stream de mensajes |
| 📊 **Partition** | Subdivisión para paralelismo |
| 📥 **Consumer** | Lee mensajes de Kafka |
| 👥 **Consumer Group** | Equipo de consumers |
| 🔢 **Offset** | Rastreador de posición de mensaje |

**Usado para:**
- Pipelines de datos en tiempo real
- Sistemas event-driven
- Streaming de logs/métricas
- Comunicación de microservicios
- ETL streaming

---

### 🔄 5.1 ¿Cómo funciona Kafka?

**Flujo:** `Producer → Topic/Partitions → Consumer Group`

**Garantías de Kafka:**

| Garantía | Descripción |
|----------|-------------|
| 🚀 **Alto Throughput** | Millones de mensajes/segundo |
| 💾 **Durabilidad** | Mensajes almacenados en disco |
| 📈 **Escalabilidad** | Escalado horizontal |
| 📊 **Ordenamiento** | Garantizado dentro de partición |
| 🔄 **Tolerancia a Fallos** | Replicación entre brokers |

---

### ⚖️ 5.2 Kafka vs Pub/Sub Tradicional

| Característica | 📨 Kafka | 📢 Pub/Sub Tradicional (SNS/RabbitMQ) |
|----------------|----------|---------------------------------------|
| **Almacenamiento de Mensajes** | ✅ Persistido (días/semanas) | ❌ Se pierde después de entrega |
| **Replay** | ✅ Puede re-leer mensajes | ❌ No es posible |
| **Ordenamiento** | ✅ Garantizado (por partición) | ⚠️ Mejor esfuerzo |
| **Throughput** | 🚀 Muy alto | 📊 Moderado |

> 💡 **En palabras simples:**
> 
> "Con Kafka, puedo almacenar mensajes por días y leerlos de nuevo si lo necesito. Siempre llegan en orden. Es como un video grabado que puedo volver a ver cuando quiera.
> 
> Con Pub/Sub tradicional, una vez que un mensaje se entrega, desaparece para siempre. No puedo reproducirlo. Es como una llamada telefónica - si la pierdo, está perdida."

---

# 🔵 PREGUNTAS_Y_RESPUESTAS_FUNDAMENTOS_GCP

---

## 📊 0. ¿Qué es BigQuery?

BigQuery es el **data warehouse serverless** de Google Cloud usado para almacenar y analizar grandes cantidades de datos muy rápidamente usando SQL.

| Característica | Descripción |
|----------------|-------------|
| 📊 **Escala** | Terabytes a Petabytes |
| ⚡ **Velocidad** | Segundos para queries complejos |
| 🗃️ **Interfaz** | SQL estándar |
| 💰 **Precios** | Pago por query o tarifa plana |
| 🔧 **Gestión** | Cero infraestructura |

---

## 🎼 1. ¿Qué es Cloud Composer?

Cloud Composer es la versión gestionada de **Apache Airflow** de Google Cloud.

| Capacidad | Descripción |
|-----------|-------------|
| 📊 **DAGs** | Define workflows como Directed Acyclic Graphs |
| ⏰ **Scheduling** | Programación tipo cron |
| 🔄 **Dependencias** | Ordenamiento de tareas y reintentos |
| 🔗 **Integraciones** | BigQuery, Dataflow, Dataproc, GCS, APIs |
| 📈 **Monitoreo** | UI web para seguimiento |

---

## 📦 2. ¿Qué es Cloud Storage (GCS)?

Cloud Storage es un servicio que te permite guardar datos en internet en lugar de en hardware físico.

| Clase de Almacenamiento | Caso de Uso | Costo |
|-------------------------|-------------|-------|
| 🔥 **Standard** | Acceso frecuente | 💰💰💰 |
| 🌡️ **Nearline** | Acceso mensual | 💰💰 |
| ❄️ **Coldline** | Acceso trimestral | 💰 |
| 🧊 **Archive** | Acceso anual | 💵 |

---

## 🐳 3. ¿Qué es Cloud Run?

Cloud Run es un servicio de Google Cloud que te permite ejecutar **aplicaciones containerizadas** de forma serverless.

| Qué Puedes Ejecutar | Ejemplo |
|---------------------|---------|
| 🔌 APIs | Endpoints REST/GraphQL |
| 🌐 Web Apps | Aplicaciones frontend |
| 🔧 Microservicios | Servicios de lógica de negocio |
| ⚙️ Jobs en Segundo Plano | Tareas de procesamiento de datos |

---

## 🔐 4. ¿Qué es Secret Manager?

Secret Manager te permite guardar tus secretos en la nube de forma segura y acceder a ellos solo cuando los necesitas.

| Almacena | Ejemplos |
|----------|----------|
| 🔑 Contraseñas | Credenciales de base de datos |
| 🎫 API Keys | Claves de servicios de terceros |
| 🎟️ Tokens | OAuth, tokens JWT |
| 📜 Certificados | Certificados SSL/TLS |

---

## 👤 5. ¿Qué es IAM?

IAM (Identity and Access Management) es el sistema que controla **quién puede acceder a qué** en un entorno cloud.

| Componente | Descripción |
|------------|-------------|
| 👤 **Users** | Identidades humanas |
| 🤖 **Service Accounts** | Identidades de aplicaciones |
| 🎭 **Roles** | Colecciones de permisos |
| 🔒 **Policies** | Vinculaciones de roles a recursos |

---

## ⚡ 6. ¿Qué es Bigtable?

Bigtable es la **base de datos NoSQL** de Google Cloud diseñada para grandes cantidades de datos con baja latencia.

| Mejor Para | Ejemplo |
|------------|---------|
| ⏱️ Series temporales | Métricas, datos de sensores |
| 📱 IoT | Telemetría de dispositivos |
| 💹 Financiero | Precios de acciones, transacciones |
| 🎯 Recomendaciones | Preferencias de usuarios |

> 💡 **Casos de Uso en palabras simples:**
> 
> "Uso Bigtable cuando necesito almacenar miles de millones de filas y leerlas muy rápido. Por ejemplo:
> - **Series temporales:** Almaceno métricas del servidor cada segundo y consulto la última hora instantáneamente.
> - **IoT:** Recolecto datos de miles de sensores y analizo patrones en tiempo real.
> - **Financiero:** Rastrea cada cambio de precio de acciones y recupero datos históricos en milisegundos.
> - **Recomendaciones:** Almaceno comportamiento del usuario para sugerir productos o contenido rápidamente."

---

## 🌍 7. ¿Qué es Cloud Spanner?

Cloud Spanner es la **base de datos SQL globalmente escalable** y completamente gestionada de Google Cloud.

| Característica | Descripción |
|----------------|-------------|
| 🌍 **Global** | Replicación multi-región |
| 🔒 **Consistente** | Garantías ACID fuertes |
| 📈 **Escalable** | Escalado horizontal |
| 🗃️ **SQL** | Interfaz SQL estándar |

**Casos de uso:** Apps financieras, e-commerce global, sistemas de inventario, backends de gaming.

### ⚖️ Bigtable vs Cloud Spanner - ¿Cuál es la diferencia?

| Característica | ⚡ Bigtable | 🌍 Cloud Spanner |
|----------------|-------------|------------------|
| **Tipo** | NoSQL (key-value) | SQL (relacional) |
| **Esquema** | Sin esquema | Esquema estructurado |
| **Lenguaje de Query** | Sin SQL, solo búsquedas por key | Soporte SQL completo |
| **Consistencia** | Eventualmente consistente | Transacciones ACID fuertes |
| **Joins** | ❌ No soportado | ✅ Soportado |
| **Mejor Para** | Alto throughput, lecturas simples | Queries complejos, transacciones |

> 💡 **¿Cuándo uso cada uno?**
> 
> "Elijo entre Bigtable y Cloud Spanner según mis necesidades de datos:
> - **Bigtable:** Lo uso cuando tengo cantidades masivas de datos con patrones de acceso simples. Por ejemplo, almaceno datos de series temporales donde solo leo por row key - no necesito queries complejos. Es extremadamente rápido para búsquedas de una sola key.
> - **Cloud Spanner:** Lo uso cuando necesito características SQL como JOINs y transacciones entre múltiples filas. Por ejemplo, una app bancaria donde necesito transferir dinero entre cuentas de forma atómica - no puedo permitir inconsistencia.
> 
> Regla simple: Si necesito SQL y transacciones → Spanner. Si necesito velocidad y escala con búsquedas simples → Bigtable."

---

## ⚖️ 8. Dataflow vs Dataproc vs BigQuery

| Servicio | Tipo | Mejor Para | Serverless |
|----------|------|------------|------------|
| 🌊 **Dataflow** | Procesamiento | ETL Streaming/Batch | ✅ Sí |
| 🔥 **Dataproc** | Procesamiento | Jobs Spark/Hadoop | ❌ Clusters gestionados |
| 🔵 **BigQuery** | Analítica | Queries SQL, BI | ✅ Sí |

> 💡 **¿Cuándo uso cada uno?**
> 
> "Elijo según lo que necesito hacer:
> - **Dataflow:** Lo uso cuando necesito procesar datos en streaming en tiempo real o ejecutar pipelines ETL batch. No gestiono servidores - escala automáticamente.
> - **Dataproc:** Lo uso cuando tengo código Spark o Hadoop existente y quiero ejecutarlo en la nube. Gestiono clusters pero GCP maneja la infraestructura.
> - **BigQuery:** Lo uso cuando quiero analizar datos que ya están almacenados. Solo escribo queries SQL y obtengo resultados en segundos - no necesito pipelines de procesamiento."

---

### 🔧 8.1 ¿Cómo configuras un cluster de Dataproc?

> 💡 **¿Has configurado un cluster de Dataproc antes?**
> 
> "Sí, he configurado muchos clusters de Dataproc para diferentes cargas de trabajo. Así es como abordo la configuración del cluster:"

**Parámetros Clave de Configuración:**

| Parámetro | Descripción | Mi Recomendación |
|-----------|-------------|------------------|
| 🖥️ **Master Node** | Coordina workers, ejecuta driver | `n1-standard-4` para la mayoría de jobs |
| 👷 **Worker Nodes** | Ejecutan tareas Spark | Empezar con 2-4, escalar según datos |
| 📊 **Machine Type** | CPU/Memoria por nodo | `n1-standard-4` a `n1-highmem-16` |
| 💾 **Disk Size** | Almacenamiento local por nodo | 100-500 GB SSD |
| 🔄 **Preemptible Workers** | Más baratos, pueden ser reclamados | Usar para jobs batch tolerantes a fallos |
| 📦 **Image Version** | Versiones de Spark/Hadoop | `2.1-debian11` (Spark 3.3+) |

**Ejemplo: Crear un Cluster Dataproc (gcloud CLI)**

```bash
gcloud dataproc clusters create my-spark-cluster \
    --region=us-central1 \
    --zone=us-central1-a \
    --master-machine-type=n1-standard-4 \
    --master-boot-disk-size=100GB \
    --num-workers=2 \
    --worker-machine-type=n1-standard-4 \
    --worker-boot-disk-size=100GB \
    --num-secondary-workers=2 \
    --secondary-worker-type=preemptible \
    --image-version=2.1-debian11 \
    --initialization-actions=gs://my-bucket/init-scripts/install-packages.sh \
    --properties=spark:spark.executor.memory=4g,spark:spark.driver.memory=2g \
    --optional-components=JUPYTER,ANACONDA \
    --enable-component-gateway
```

**Ejemplo: Crear un Cluster Dataproc (Terraform)**

```hcl
resource "google_dataproc_cluster" "spark_cluster" {
  name   = "my-spark-cluster"
  region = "us-central1"

  cluster_config {
    master_config {
      num_instances = 1
      machine_type  = "n1-standard-4"
      disk_config {
        boot_disk_size_gb = 100
        boot_disk_type    = "pd-ssd"
      }
    }

    worker_config {
      num_instances = 2
      machine_type  = "n1-standard-4"
      disk_config {
        boot_disk_size_gb = 100
        boot_disk_type    = "pd-ssd"
      }
    }

    preemptible_worker_config {
      num_instances = 2
    }

    software_config {
      image_version = "2.1-debian11"
      override_properties = {
        "spark:spark.executor.memory" = "4g"
        "spark:spark.driver.memory"   = "2g"
      }
    }

    gce_cluster_config {
      zone        = "us-central1-a"
      subnetwork  = google_compute_subnetwork.default.id
      service_account = google_service_account.dataproc.email
    }
  }
}
```

**Enviar un Job de Spark:**

```bash
gcloud dataproc jobs submit pyspark gs://my-bucket/jobs/my_spark_job.py \
    --cluster=my-spark-cluster \
    --region=us-central1 \
    --properties=spark.executor.instances=4,spark.executor.memory=4g \
    -- --input=gs://my-bucket/data/input/ --output=gs://my-bucket/data/output/
```

**Mis Mejores Prácticas de Configuración:**

| Práctica | Por qué |
|----------|---------|
| 🔄 **Usar preemptible workers** | 60-80% ahorro en costos para jobs batch |
| 📊 **Dimensionar correctamente** | Empezar pequeño, monitorear, luego escalar |
| ⏱️ **Configurar idle timeout** | Auto-eliminar clusters después de X minutos de inactividad |
| 🔧 **Usar initialization actions** | Instalar paquetes personalizados al crear cluster |
| 📦 **Almacenar datos en GCS** | Separar almacenamiento de cómputo para flexibilidad |
| 🏷️ **Agregar labels** | Rastrear costos por proyecto/equipo/ambiente |

> 🎯 **Tip de Entrevista:** "Configuro clusters de Dataproc según los requisitos de la carga de trabajo. Para desarrollo, uso clusters pequeños con preemptible workers. Para producción, uso workers dedicados con auto-scaling. Siempre separo almacenamiento (GCS) de cómputo para poder eliminar clusters cuando terminan los jobs y ahorrar costos. También uso Terraform para Infrastructure as Code para asegurar deployments reproducibles."

---

# 🟠 PREGUNTAS_Y_RESPUESTAS_FUNDAMENTOS_AWS

---

## 📊 0. Amazon Redshift (≈ BigQuery)

Amazon Redshift es el data warehouse en la nube de AWS usado para almacenar y analizar datasets masivos con SQL.

| Característica | Descripción |
|----------------|-------------|
| 📊 **Escala** | Petabytes de datos |
| ⚡ **Velocidad** | Almacenamiento columnar, queries paralelos |
| 🗃️ **Interfaz** | SQL compatible con PostgreSQL |
| 💰 **Precios** | On-demand o Reservado |
| 🆕 **Serverless** | Redshift Serverless disponible |

---

## 🎼 1. Amazon MWAA (≈ Cloud Composer)

Amazon MWAA es el servicio gestionado de Apache Airflow de AWS.

| Característica | Descripción |
|----------------|-------------|
| 📊 **DAGs** | Misma estructura de DAG de Airflow |
| 🔗 **Integraciones** | Redshift, Glue, EMR, S3, Lambda |
| 📈 **Monitoreo** | CloudWatch + UI de Airflow |
| 🔧 **Gestión** | AWS maneja la infraestructura |

---

## 📦 2. Amazon S3 (≈ Cloud Storage)

Amazon S3 es el servicio de almacenamiento de objetos en la nube de AWS.

| Clase de Almacenamiento | Caso de Uso | Costo |
|-------------------------|-------------|-------|
| 🔥 **Standard** | Acceso frecuente | 💰💰💰 |
| 🌡️ **Standard-IA** | Acceso infrecuente | 💰💰 |
| ❄️ **Glacier** | Archivo (minutos para recuperar) | 💰 |
| 🧊 **Glacier Deep** | Archivo a largo plazo (horas) | 💵 |

---

## 🐳 3. AWS Fargate & Lambda (≈ Cloud Run)

| Servicio | Tipo | Mejor Para |
|----------|------|------------|
| 🐳 **Fargate** | Contenedores serverless | Servicios de larga duración, APIs |
| ⚡ **Lambda** | Funciones serverless | Event-driven, tareas cortas |

---

## 🔐 4. AWS Secrets Manager (≈ Secret Manager)

Almacena de forma segura y **rota secretos automáticamente**.

| Característica | Descripción |
|----------------|-------------|
| 🔑 **Almacenamiento** | Contraseñas, API keys, tokens |
| 🔄 **Rotación** | Rotación automática de secretos |
| 🔗 **Integración** | RDS, Redshift, Lambda |

---

## 👤 5. AWS IAM (≈ GCP IAM)

| Componente | Descripción |
|------------|-------------|
| 👤 **Users** | Identidades humanas |
| 🎭 **Roles** | Asumidos por servicios/usuarios |
| 📜 **Policies** | Documentos JSON de permisos |
| 👥 **Groups** | Colecciones de usuarios |

---

## ⚡ 6. Amazon DynamoDB (≈ Bigtable)

Amazon DynamoDB es la **base de datos NoSQL** de alto rendimiento de AWS.

| Característica | Descripción |
|----------------|-------------|
| ⚡ **Latencia** | Milisegundos de un solo dígito |
| 📈 **Escala** | Throughput ilimitado |
| 🌍 **Global** | Global Tables para multi-región |
| 💰 **Precios** | On-demand o Provisioned |

> 💡 **Casos de Uso en palabras simples:**
> 
> "Uso DynamoDB cuando necesito lecturas/escrituras súper rápidas a cualquier escala. Por ejemplo:
> - **Gaming:** Almaceno sesiones de jugadores y leaderboards con actualizaciones instantáneas.
> - **E-commerce:** Manejo carritos de compra y perfiles de usuario para millones de usuarios.
> - **Apps móviles:** Almaceno datos de usuario que se sincronizan entre dispositivos en tiempo real.
> - **Ad tech:** Sirvo anuncios personalizados en milisegundos basándome en comportamiento del usuario."

---

## 🌍 7. Amazon Aurora Global (≈ Cloud Spanner)

| Característica | Aurora Global | DynamoDB Global Tables |
|----------------|---------------|------------------------|
| **Tipo** | SQL (MySQL/PostgreSQL) | NoSQL |
| **Consistencia** | Fuerte | Eventual |
| **Escala** | Replicación global | Replicación global |
| **Mejor Para** | Apps SQL tradicionales | Workloads key-value |

> 💡 **Casos de Uso en palabras simples:**
> 
> "Elijo entre Aurora Global y DynamoDB Global Tables según mis necesidades:
> - **Aurora Global:** Lo uso cuando necesito queries SQL y transacciones ACID globalmente. Por ejemplo, apps bancarias donde necesito consistencia fuerte para transferencias de dinero.
> - **DynamoDB Global Tables:** Lo uso cuando necesito búsquedas key-value rápidas globalmente. Por ejemplo, una app de gaming donde necesito leer perfiles de usuario rápidamente, y la consistencia eventual está bien."

---

## ⚖️ 8. Servicios de Procesamiento AWS

| Servicio GCP | Equivalente AWS | Tipo |
|--------------|-----------------|------|
| 🌊 **Dataflow** | AWS Glue / Kinesis | ETL, Streaming |
| 🔥 **Dataproc** | Amazon EMR | Spark/Hadoop |
| 🔵 **BigQuery** | Amazon Redshift | Data Warehouse |

### 🔥 ¿Qué es Amazon EMR?

Amazon EMR (Elastic MapReduce) es la **plataforma de big data gestionada** de AWS para ejecutar Spark, Hadoop, Hive y otros frameworks.

| Característica | Descripción |
|----------------|-------------|
| 🔧 **Frameworks** | Spark, Hadoop, Hive, Presto, Flink |
| 📈 **Escala** | Clusters con auto-scaling |
| 💰 **Precios** | Pago por hora de cluster |
| 🗃️ **Almacenamiento** | S3, HDFS, o EBS |

> 💡 **¿Cuándo uso EMR?**
> 
> "Uso Amazon EMR cuando:
> - Tengo **jobs Spark o Hadoop existentes** y quiero ejecutarlos en AWS.
> - Necesito control total sobre la configuración del cluster y software instalado.
> - Quiero ejecutar workloads de **Hive, Presto, o Flink** - no solo Spark.
> 
> Por ejemplo, migro mis jobs Spark on-premise a EMR sin reescribir código. Solo subo mis JARs, configuro el cluster y ejecuto."

### 🔧 ¿Cómo configuras un cluster de Amazon EMR?

> 💡 **¿Has configurado un cluster EMR antes?**
> 
> "Sí, he configurado clusters EMR para varias cargas de trabajo de Spark y Hadoop. Así es como abordo la configuración de EMR:"

**Parámetros Clave de Configuración:**

| Parámetro | Descripción | Mi Recomendación |
|-----------|-------------|------------------|
| 🖥️ **Master Node** | Coordina el cluster, ejecuta YARN | `m5.xlarge` para la mayoría de jobs |
| 👷 **Core Nodes** | Almacenan datos HDFS, ejecutan tareas | 2-4 nodos, escalar según datos |
| 📊 **Task Nodes** | Solo ejecutan tareas (sin HDFS) | Usar Spot instances para ahorrar costos |
| 💾 **Instance Type** | CPU/Memoria por nodo | `m5.xlarge` a `r5.4xlarge` |
| 📦 **Release Label** | Versión de EMR (Spark/Hadoop) | `emr-6.10.0` (Spark 3.3+) |
| 🔄 **Spot Instances** | Más baratas, pueden ser interrumpidas | Usar para task nodes en jobs batch |

**Ejemplo: Crear un Cluster EMR (AWS CLI)**

```bash
aws emr create-cluster \
    --name "my-spark-cluster" \
    --release-label emr-6.10.0 \
    --applications Name=Spark Name=Hadoop Name=Hive \
    --instance-groups '[
        {
            "InstanceGroupType": "MASTER",
            "InstanceCount": 1,
            "InstanceType": "m5.xlarge",
            "Name": "Master"
        },
        {
            "InstanceGroupType": "CORE",
            "InstanceCount": 2,
            "InstanceType": "m5.xlarge",
            "Name": "Core"
        },
        {
            "InstanceGroupType": "TASK",
            "InstanceCount": 2,
            "InstanceType": "m5.xlarge",
            "Market": "SPOT",
            "Name": "Task"
        }
    ]' \
    --ec2-attributes KeyName=my-key,SubnetId=subnet-xxxxx \
    --use-default-roles \
    --log-uri s3://my-bucket/emr-logs/ \
    --configurations '[
        {
            "Classification": "spark-defaults",
            "Properties": {
                "spark.executor.memory": "4g",
                "spark.driver.memory": "2g",
                "spark.executor.instances": "4"
            }
        }
    ]' \
    --bootstrap-actions Path=s3://my-bucket/bootstrap/install-packages.sh,Name=InstallPackages \
    --auto-terminate \
    --steps '[
        {
            "Type": "Spark",
            "Name": "My Spark Job",
            "ActionOnFailure": "TERMINATE_CLUSTER",
            "Args": ["--deploy-mode", "cluster", "s3://my-bucket/jobs/my_spark_job.py"]
        }
    ]'
```

**Ejemplo: Crear un Cluster EMR (Terraform)**

```hcl
resource "aws_emr_cluster" "spark_cluster" {
  name          = "my-spark-cluster"
  release_label = "emr-6.10.0"
  applications  = ["Spark", "Hadoop", "Hive"]
  
  service_role = aws_iam_role.emr_service.arn
  
  ec2_attributes {
    subnet_id                         = aws_subnet.main.id
    emr_managed_master_security_group = aws_security_group.emr_master.id
    emr_managed_slave_security_group  = aws_security_group.emr_slave.id
    instance_profile                  = aws_iam_instance_profile.emr_ec2.arn
    key_name                          = "my-key"
  }

  master_instance_group {
    instance_type  = "m5.xlarge"
    instance_count = 1
    ebs_config {
      size = 100
      type = "gp3"
    }
  }

  core_instance_group {
    instance_type  = "m5.xlarge"
    instance_count = 2
    ebs_config {
      size = 100
      type = "gp3"
    }
  }

  configurations_json = jsonencode([
    {
      Classification = "spark-defaults"
      Properties = {
        "spark.executor.memory"    = "4g"
        "spark.driver.memory"      = "2g"
        "spark.executor.instances" = "4"
      }
    }
  ])

  log_uri = "s3://my-bucket/emr-logs/"

  tags = {
    Environment = "production"
    Project     = "data-platform"
  }
}
```

**Enviar un Job de Spark a EMR:**

```bash
# Agregar step a cluster en ejecución
aws emr add-steps \
    --cluster-id j-XXXXXXXXXXXXX \
    --steps Type=Spark,Name="My Spark Job",ActionOnFailure=CONTINUE,\
Args=[--deploy-mode,cluster,--executor-memory,4g,s3://my-bucket/jobs/my_spark_job.py]

# O usar spark-submit directamente en el cluster
spark-submit \
    --deploy-mode cluster \
    --master yarn \
    --executor-memory 4g \
    --num-executors 4 \
    s3://my-bucket/jobs/my_spark_job.py \
    --input s3://my-bucket/data/input/ \
    --output s3://my-bucket/data/output/
```

**Mis Mejores Prácticas de Configuración:**

| Práctica | Por qué |
|----------|---------|
| 🔄 **Usar Spot para Task nodes** | 60-90% ahorro en costos, sin pérdida de datos si se interrumpe |
| 📊 **Usar Core nodes para HDFS** | Almacenamiento estable, usar instancias On-Demand |
| ⏱️ **Auto-terminate** | Eliminar cluster después de que complete el job |
| 🔧 **Bootstrap actions** | Instalar paquetes personalizados al crear cluster |
| 📦 **Almacenar datos en S3** | Separar almacenamiento de cómputo |
| 🏷️ **Usar tags** | Rastrear costos por proyecto/equipo/ambiente |
| 📝 **Habilitar logging** | Enviar logs a S3 para debugging |

**Comparación EMR vs Dataproc:**

| Característica | 🔥 Dataproc (GCP) | 🔥 EMR (AWS) |
|----------------|-------------------|--------------|
| **Tiempo de Inicio** | ~90 segundos | ~5-10 minutos |
| **Spot/Preemptible** | Preemptible workers | Spot instances |
| **Almacenamiento** | GCS | S3 / HDFS |
| **Precios** | Por segundo | Por segundo |
| **Opción Serverless** | Dataproc Serverless | EMR Serverless |
| **Integración Notebook** | Jupyter vía Component | EMR Studio |

> 🎯 **Tip de Entrevista:** "Configuro clusters EMR según los requisitos de la carga de trabajo. Para optimización de costos, uso Spot instances para Task nodes ya que no almacenan datos HDFS y pueden ser interrumpidos de forma segura. Siempre uso auto-termination para jobs batch y almaceno datos en S3 para separar almacenamiento de cómputo. Para Infrastructure as Code, uso Terraform para versionar mis configuraciones de cluster y asegurar deployments reproducibles entre ambientes."

### 🌊 ¿Funciona Apache Beam en AWS como Dataflow?

| Runner | Plataforma | Descripción |
|--------|------------|-------------|
| 🌊 **Dataflow Runner** | GCP | Nativo, completamente gestionado |
| 🔥 **Spark Runner** | EMR / Dataproc | Ejecutar Beam en clusters Spark |
| 🌀 **Flink Runner** | EMR / Kinesis Data Analytics | Ejecutar Beam en Flink |

> 💡 **En palabras simples:**
> 
> "Apache Beam es el **código que escribo**, y el runner es **donde se ejecuta**:
> - En **GCP**, uso Dataflow Runner - es nativo y serverless.
> - En **AWS**, puedo ejecutar mi código Beam en **EMR usando Spark Runner** o **Flink Runner**. No es serverless como Dataflow, pero mi código Beam funciona igual.
> 
> Así que sí, puedo escribir pipelines Beam una vez y ejecutarlos tanto en GCP (Dataflow) como en AWS (EMR con Spark/Flink). Ese es el poder de Beam - escribe una vez, ejecuta en cualquier lugar!"

### 🔄 AWS Glue vs Kinesis - ¿Cuál es la diferencia?

| Característica | 🔧 AWS Glue | 🌊 Kinesis |
|----------------|-------------|------------|
| **Propósito** | ETL (Extract, Transform, Load) | Streaming en tiempo real |
| **Tipo de Datos** | Datos batch | Streams continuos |
| **Latencia** | Minutos a horas | Milisegundos a segundos |
| **Caso de Uso** | Data warehousing, data lakes | Dashboards en vivo, alertas |

> 💡 **¿Cuándo uso cada uno?**
> 
> "Elijo entre Glue y Kinesis según el timing:
> - **AWS Glue:** Lo uso cuando necesito mover y transformar datos en batches. Por ejemplo, cada noche extraigo datos de bases de datos, los transformo y los cargo en Redshift.
> - **Kinesis:** Lo uso cuando necesito procesar datos a medida que llegan. Por ejemplo, hago streaming de datos de clickstream desde mi sitio web y analizo el comportamiento del usuario en tiempo real.
> 
> A veces uso ambos juntos: Kinesis captura eventos en tiempo real, y Glue los procesa en batches para almacenamiento a largo plazo."

---

# 🎯 PREGUNTAS_Y_RESPUESTAS_PREPARACION_ENTREVISTA

> **Nota:** Las respuestas a continuación están basadas en experiencia personal. Cada Data Engineer tiene un background diferente, así que adapta estas respuestas para reflejar tu propio camino.
> 
> 📋 **Esta sección incluye:** Criterios de Evaluación Senior + Preguntas y Respuestas de Entrevista (Q1-Q30)

---

## 🎯 ¿Qué evalúan las empresas para Senior Data Engineer?

| Área | Qué Evalúan |
|------|-------------|
| 📚 **Fundamentos** | SQL avanzado (CTEs, window functions, rendimiento), Python productivo, testing |
| 🔄 **Data Pipelines** | Spark/dbt/Airflow, orquestación, particiones/clustering, manejo de fallos |
| 🏗️ **Arquitectura & Cloud** | Modelado de datos (3NF/OLAP/OBT), patrones CDC, costo y rendimiento en BigQuery/Redshift |
| ✅ **Confiabilidad** | SLAs/SLOs, monitoreo, calidad de datos (checks/expectations), versionado & IaC |

> 💡 **Cómo me preparo para entrevistas Senior:**
> 
> "Cuando entrevisto para roles Senior, me enfoco en estas 4 áreas:
> 
> - **Fundamentos:** Practico SQL avanzado - CTEs para legibilidad, window functions para rankings y totales acumulados, y optimización de queries. Escribo Python limpio con testing apropiado y manejo de errores.
> 
> - **Data Pipelines:** Puedo explicar mis jobs de Spark, modelos de dbt, y DAGs de Airflow en detalle. Sé por qué particiono por fecha, por qué hago clustering por ciertas columnas, y cómo manejo fallos con reintentos y dead-letter queues.
> 
> - **Arquitectura:** Entiendo diferentes modelos de datos - cuándo usar 3NF vs star schema vs One Big Table. Conozco patrones CDC para sincronización de datos en tiempo real. Puedo discutir optimización de costos en BigQuery (particionado, clustering, slot reservations) o Redshift (distribution keys, sort keys).
> 
> - **Confiabilidad:** Defino SLAs con stakeholders, configuro monitoreo y alertas, implemento checks de calidad de datos, y uso Infrastructure as Code (Terraform) para deployments reproducibles.
> 
> La clave a nivel Senior no es solo saber CÓMO hacer las cosas, sino POR QUÉ tomas ciertas decisiones y CUÁNDO usar cada enfoque."

---

## 🟢 SECCIÓN 1 — Background y Experiencia Técnica (Q1-Q9)

---

### 🖥️ Q1. Experiencia con Spark On-Premise vs Cloud

| Ambiente | Experiencia |
|----------|-------------|
| 🏢 **On-Premise** | Clusters Hadoop/YARN, gestión de recursos, tuning |
| ☁️ **Cloud** | Dataproc (GCP), EMR (AWS), escalado simplificado |

> ✅ Cómodo con ambos ambientes, entendiendo deployment, optimización y diferencias de costo.

> 💡 **Mi experiencia en palabras simples:**
> 
> "**On-Premise:** Gestioné clusters Hadoop con YARN. Tenía que configurar manualmente memoria, CPU y executors. Cuando un job fallaba, revisaba logs en múltiples nodos. Escalar significaba comprar nuevos servidores y esperar semanas. Pasé mucho tiempo tuneando shuffle partitions, asignación de memoria y arreglando errores de out-of-memory.
> 
> **Cloud:** Ahora uso Dataproc o EMR. Levanto un cluster en minutos, ejecuto mi job y lo elimino. Auto-scaling agrega workers cuando los necesito. No me preocupo por hardware - solo me enfoco en mi código Spark. Si necesito más poder, cambio el tipo de máquina y reinicio.
> 
> **Diferencias clave que noté:**
> - **Costo:** On-premise = costo fijo (comprar servidores). Cloud = pago por uso (puede ser más barato o más caro dependiendo del uso).
> - **Velocidad:** On-premise = semanas para escalar. Cloud = minutos para escalar.
> - **Control:** On-premise = control total pero más responsabilidad. Cloud = menos control pero menos mantenimiento.
> - **Tuning:** El mismo tuning de Spark aplica a ambos, pero cloud me da más flexibilidad para experimentar rápidamente."

---

### 🗄️ Q2. Experiencia con Bases de Datos Enterprise (Oracle & SQL Server)

| Base de Datos | Experiencia |
|---------------|-------------|
| 🟥 **Oracle** | ETL con PL/SQL, particionado, integración GoldenGate/CDC |
| 🟦 **SQL Server** | Optimización de SSIS (SQL Server Integration Services), Always On AG, stored procedures |

| Patrón de Integración | Herramientas Usadas |
|-----------------------|---------------------|
| 📤 CDC a Cloud | Datastream, AWS DMS, Debezium |
| 🔄 Rutinas ETL | PL/SQL, SSIS, stored procedures |
| 📊 Integración BI | Views, stored procedures para Spark/herramientas BI |

> 💡 **Mi experiencia en palabras simples:**
> 
> "**Oracle:** Escribí procedimientos PL/SQL para jobs ETL que corrían cada noche. Usé particionado para manejar tablas grandes - por ejemplo, particionando por fecha para que los queries solo escaneen datos relevantes. Configuré GoldenGate para CDC (Change Data Capture) en tiempo real para replicar datos a nuestro data lake sin impactar producción.
> 
> **SQL Server:** Construí paquetes SSIS para integración de datos - extrayendo de múltiples fuentes, transformando y cargando al warehouse. Configuré Always On Availability Groups para alta disponibilidad. Optimicé stored procedures que las herramientas BI llamaban directamente.
> 
> **Cómo integro bases de datos enterprise con cloud moderno:**
> - **CDC a Cloud:** Uso Datastream (GCP), AWS DMS, o Debezium para capturar cambios en tiempo real y streamearlos a BigQuery, Redshift, o data lakes. De esta forma, no necesito jobs batch pesados - los datos fluyen continuamente.
> - **Rutinas ETL:** A veces mantengo jobs PL/SQL o SSIS existentes porque funcionan bien. No reescribo todo - solo conecto su salida a almacenamiento cloud.
> - **Integración BI:** Creo views y stored procedures que Spark o herramientas BI pueden consultar. Esto da a los analistas una interfaz limpia sin exponer estructuras de tabla complejas."

---

### ⚡ Q3. Funciones Serverless en Data Engineering

| Caso de Uso | Implementación |
|-------------|----------------|
| 📋 Validación de Esquema | Validar al llegar el archivo |
| 🏷️ Enriquecimiento de Metadata | Agregar tags y contexto |
| 🔔 Trigger Downstream | Iniciar jobs Spark, enviar notificaciones |
| 🔌 Integración API | Conectar servicios externos |

> 💡 **Mi experiencia en palabras simples:**
> 
> "Uso funciones serverless (Cloud Functions, Lambda) para tareas ligeras que no necesitan un job Spark completo:
> 
> - **Validación de Esquema:** Cuando un archivo llega a GCS o S3, mi función se dispara automáticamente. Verifica si el archivo tiene las columnas y tipos de datos correctos. Si la validación falla, muevo el archivo a una carpeta de error y envío una alerta.
> 
> - **Enriquecimiento de Metadata:** Agrego metadata como timestamp de procesamiento, sistema fuente y tamaño de archivo a cada registro antes de que vaya al data lake. Esto ayuda con debugging y auditoría después.
> 
> - **Trigger Downstream:** Después de que un archivo es validado, mi función inicia un job de Dataproc o envía un mensaje a Pub/Sub. Esto crea un pipeline event-driven sin intervención manual.
> 
> - **Integración API:** Llamo APIs externas para enriquecer datos - por ejemplo, obtener tasas de cambio de moneda o geocodificar direcciones. Las funciones son perfectas porque escalan automáticamente y solo pago cuando se ejecutan."

---

### 🎼 Q4. Experiencia con Herramientas de Orquestación

| Herramienta | Cloud | Experiencia |
|-------------|-------|-------------|
| 🎼 **Airflow/Composer** | GCP | DAGs, orquestación batch/streaming |
| 🎼 **MWAA** | AWS | Mismas capacidades de Airflow |
| ⚙️ **Step Functions** | AWS | Workflows event-driven |
| 🏭 **Data Factory** | Azure | Orquestación de pipelines |

> 💡 **Mi experiencia en palabras simples:**
> 
> "Uso herramientas de orquestación para programar y coordinar mis pipelines de datos:
> 
> - **Airflow/Composer (GCP):** Esta es mi herramienta principal. Escribo DAGs (Directed Acyclic Graphs) en Python para definir dependencias de tareas. Por ejemplo: extraer datos → validar → transformar → cargar → enviar notificación. Si un paso falla, Airflow lo reintenta y me alerta. Uso Composer porque es gestionado - no me preocupo por la infraestructura de Airflow.
> 
> - **MWAA (AWS):** Igual que Composer pero en AWS. Mis DAGs de Airflow funcionan en ambos con cambios mínimos. Solo actualizo las conexiones y operadores (ej. GCS a S3, BigQuery a Redshift).
> 
> - **Step Functions (AWS):** Lo uso para workflows event-driven. A diferencia de Airflow (programado), Step Functions reaccionan a eventos inmediatamente. Por ejemplo, cuando llega un archivo, dispara un Lambda, luego otro Lambda, luego un job de EMR - todo definido como una máquina de estados.
> 
> - **Data Factory (Azure):** Concepto similar pero nativo de Azure. Lo he usado para orquestar pipelines que mueven datos entre SQL Server on-premise y Azure Synapse.
> 
> **¿Cuándo elijo cada uno?**
> - Pipelines batch complejos con muchas dependencias → Airflow/Composer/MWAA
> - Reacciones event-driven en tiempo real → Step Functions
> - Ecosistema Azure → Data Factory"

---

### 📊 Q5. Dataform y Herramientas de Transformación SQL

| Herramienta | Cloud | Propósito |
|-------------|-------|-----------|
| 📊 **Dataform** | GCP | Transformaciones SQL en BigQuery |
| 🔧 **dbt (data build tool)** | AWS/GCP | Transformaciones SQL (funciona con Redshift, BigQuery, Snowflake) |

> 💡 **Mi experiencia en palabras simples:**
> 
> "Uso Dataform y herramientas similares para transformar datos **dentro** del warehouse usando SQL:
> 
> - **Dataform (GCP):** Escribo modelos SQL que transforman datos raw en tablas limpias en BigQuery. Dataform maneja dependencias - si tabla A depende de tabla B, ejecuta B primero. También escribo tests para validar calidad de datos (ej. sin nulls en columnas clave). Es como 'control de versiones para transformaciones SQL'.
> 
> - **dbt (AWS):** Mismo concepto que Dataform pero lo uso con Redshift en AWS. La sintaxis es casi idéntica a Dataform, así que cambiar entre ellos es fácil.
> 
> **Dataform vs Herramientas de Orquestación - ¿Cuál es la diferencia?**
> - **Airflow/Step Functions:** Orquestan jobs *externos* (Spark, APIs, movimientos de archivos)
> - **Dataform/dbt:** Transforman datos *dentro* del warehouse solo con SQL
> 
> A menudo uso ambos juntos: Airflow dispara el job de Dataform/dbt, que luego ejecuta todas mis transformaciones SQL en el orden correcto."

---

### 🎤 Q6. Cuéntame sobre tu background como Data Engineer.

| Aspecto | Mi Experiencia |
|---------|----------------|
| ☁️ **Plataformas Cloud** | GCP & AWS |
| 🏗️ **Arquitectura** | Data lakes, pipelines en tiempo real, sistemas de analítica |
| 🔧 **Herramientas** | Airflow, Dataform, Lambda, Cloud Functions, Kinesis, Kafka |
| 🆕 **Enfoque Reciente** | Generative AI: RAG, agentes inteligentes, sistemas de monitoreo |

> 💡 **Cómo respondo esto:**
> 
> "Soy un Data Engineer con experiencia en GCP y AWS. He construido data lakes desde cero, diseñado pipelines de streaming en tiempo real, y creado sistemas de analítica que soportan decisiones de negocio. Mis herramientas diarias incluyen Airflow para orquestación, Dataform para transformaciones SQL, y funciones serverless para procesamiento ligero. Recientemente, me he enfocado en Generative AI - construyendo sistemas RAG y agentes inteligentes que combinan data engineering tradicional con capacidades modernas de IA."

---

### 🛠️ Q7. ¿Qué herramientas usas diariamente?

| Categoría | Herramientas |
|-----------|--------------|
| 📊 **Data Warehouses** | BigQuery, Redshift |
| 🔄 **ETL/ELT** | Dataform, dbt |
| 🎼 **Orquestación** | Airflow, Cloud Composer, MWAA |
| ⚡ **Serverless** | Cloud Functions, Lambda |
| 📦 **Almacenamiento** | S3, GCS |
| 📨 **Streaming** | Kafka, Kinesis |
| 🤖 **AI/ML** | Vertex AI, AutoML |
| 🔧 **DevOps** | GitHub, Cloud Build, Docker |
| 🆕 **GenAI** | LangGraph, Agent Builder, ADK |

> 💡 **Cómo respondo esto:**
> 
> "Cada día trabajo con BigQuery o Redshift para analítica - escribiendo SQL, optimizando queries y gestionando tablas. Uso Dataform o dbt para transformar datos raw en modelos limpios. Airflow es mi herramienta principal para programar y orquestar pipelines. Para tareas ligeras, uso Cloud Functions o Lambda - se disparan automáticamente cuando llegan archivos. Almaceno todo en S3 o GCS. Cuando necesito procesamiento en tiempo real, uso Kafka o Kinesis. Recientemente, he estado usando LangGraph y Agent Builder para crear soluciones de datos impulsadas por IA."

---

### 🏭 Q8. ¿En qué industrias has trabajado?

| Industria | Área de Enfoque |
|-----------|-----------------|
| 📊 **Marketing Analytics** | Rendimiento de campañas, atribución |
| 📞 **Operaciones de Call Center** | Insights de clientes, sentimiento |
| 📈 **Business Intelligence** | Dashboards, reportes |
| 🤖 **Desarrollo de AI Agents** | IA conversacional, automatización |
| ☁️ **Automatización Cloud** | Infraestructura, DevOps |

> 💡 **Cómo respondo esto:**
> 
> "He trabajado en varias industrias. En Marketing Analytics, construí pipelines que rastrean rendimiento de campañas a través de múltiples plataformas de ads - ayudando a marketers a entender ROI y atribución. En Operaciones de Call Center, analicé interacciones de clientes para extraer insights sobre sentimiento y problemas comunes. También he construido sistemas de Business Intelligence - creando dashboards y reportes que ejecutivos usan para toma de decisiones. Recientemente, he estado desarrollando AI Agents para interfaces conversacionales y automatizando infraestructura cloud."

---

### 🎓 Q9. ¿Qué certificaciones tienes?

| Certificación | Proveedor | Estado |
|---------------|-----------|--------|
| 🔵 **Professional Data Engineer** | Google Cloud | ✅ Certificado |
| 🤖 **Generative AI Leader** | Google Cloud | ✅ Certificado |
| 🌐 **Inglés B2** | Cambridge/TOEFL | ✅ Certificado |
| 📚 **Skills Boost Training** | Google Cloud | ✅ Completado |

> 💡 **Cómo respondo esto:**
> 
> "Soy Professional Data Engineer certificado por Google Cloud - esta certificación valida mis habilidades en diseño y construcción de sistemas de procesamiento de datos en GCP. También tengo la certificación de Generative AI Leader, que cubre sistemas RAG, prompt engineering y AI agents. Completé entrenamiento extensivo a través de Google Cloud Skills Boost. Mi inglés tiene certificación B2, lo que me permite comunicarme efectivamente en equipos internacionales."

---

## 🟡 SECCIÓN 2 — Preguntas Intermedias (Q10-Q13)

---

### 📊 Q10. Describe un pipeline ETL típico que hayas construido.

```
FUENTES DE DATOS → INGESTA → TRANSFORMACIÓN → SALIDA
─────────────────────────────────────────────────────
• Google Ads     • APIs           • Dataform        • Dashboards
• Meta           • S3/GCS         • BigQuery SQL    • Tiempo real
• TikTok         • Validación     • Airflow         • Alertas
• LinkedIn       • Cloud Build    • CI/CD           • Reportes
• X (Twitter)
```

> 💡 **Cómo respondo esto:**
> 
> "Construí un pipeline de marketing analytics que extrae datos de múltiples plataformas de ads - Google Ads, Meta, TikTok, LinkedIn y X. Cada día, mi pipeline llama a sus APIs para extraer datos de campañas. Los datos raw llegan a GCS, luego Cloud Functions validan el esquema. Si la validación pasa, Dataform transforma los datos - limpiando, uniendo y calculando métricas. Airflow orquesta todo el flujo y envía alertas si algo falla. Las tablas finales alimentan dashboards donde los marketers rastrean rendimiento de campañas en casi tiempo real."

---

### ✅ Q11. ¿Cómo aseguras la calidad de datos?

| Tipo de Validación | Implementación | Impacto |
|--------------------|----------------|---------|
| 🔍 **Null Checks** | Automatizado después de ingesta | Captura datos faltantes |
| 📐 **Schema Drift** | Comparar esperado vs actual | Prevenir cambios que rompen |
| ⏰ **Políticas de Freshness** | Alertar sobre datos viejos | Asegurar oportunidad |
| 📊 **Alertas de Threshold** | Detección de anomalías | Capturar outliers |
| 🔄 **Reconciliación** | Comparar contra APIs fuente | Asegurar completitud |

> 📈 **Resultado:** Reducción de fallos en pipeline de marketing en **60%**.

> 💡 **Cómo respondo esto:**
> 
> "La calidad de datos es crítica en mis pipelines. Primero, ejecuto null checks justo después de la ingesta - si columnas clave están vacías, el pipeline se detiene y me alerta. Segundo, detecto schema drift comparando datos entrantes contra esquemas esperados - esto nos salvó muchas veces cuando las APIs cambiaron sin aviso. Tercero, configuro políticas de freshness - si los datos son más viejos de lo esperado, recibo una alerta. Cuarto, uso alertas de threshold para detección de anomalías - si las métricas suben o bajan súbitamente, algo podría estar mal. Finalmente, reconcilio nuestros datos contra las APIs fuente para asegurar que no perdimos ningún registro. Estas prácticas redujeron nuestros fallos de pipeline en 60%."

---

### ⚡ Q12. ¿Cómo optimizas el rendimiento de BigQuery o Redshift?

| Optimización | BigQuery | Redshift |
|--------------|----------|----------|
| 📅 **Particionado** | Por fecha/timestamp | Por columna de fecha |
| 🎯 **Clustering** | Por columnas de alta cardinalidad | Sort keys |
| 📊 **Materialized Views** | ✅ Soportado | ✅ Soportado |
| 🔍 **Query Pruning** | Filtrado de predicados | Predicate pushdown |
| 🏗️ **Distribution** | N/A | Estrategia DISTKEY |
| ❌ **Evitar** | SELECT * | SELECT * |

> ⚡ **Resultado:** Tiempos de query reducidos de **minutos a segundos**.

> 💡 **Cómo respondo esto:**
> 
> "Optimizo BigQuery y Redshift usando varias técnicas. Primero, particionado - siempre particiono por fecha para que los queries solo escaneen datos relevantes. Un query para 'últimos 7 días' escanea 7 particiones en lugar de toda la tabla. Segundo, clustering (BigQuery) o sort keys (Redshift) - hago clustering por columnas frecuentemente usadas en cláusulas WHERE. Tercero, creo materialized views para agregaciones complejas que se consultan frecuentemente. Cuarto, nunca uso SELECT * - solo selecciono las columnas que necesito. En Redshift, también elijo la distribution key correcta para minimizar shuffling de datos. Estas optimizaciones redujeron tiempos de query de minutos a segundos."

---

### 🌊 Q13. Cuéntame sobre tu experiencia con streaming en tiempo real.

| Plataforma | Caso de Uso | Características |
|------------|-------------|-----------------|
| 📨 **Kinesis** | Eventos de clientes, tracking de marketing | Nativo de AWS, auto-scaling |
| 📨 **Kafka** | Pipelines event-driven | Alto throughput, replay |

> 💡 **Cómo respondo esto:**
> 
> "He trabajado con Kinesis y Kafka para streaming en tiempo real. Con Kinesis, construí un pipeline que captura eventos de clientes desde nuestro sitio web - clicks, page views, envíos de formularios. Los datos fluyen a Kinesis, Lambda los procesa, y en segundos están disponibles para análisis. Con Kafka, construí pipelines event-driven donde múltiples consumers leen de los mismos topics. La ventaja clave de Kafka es replay - si algo sale mal, puedo reprocesar mensajes desde cualquier punto en el tiempo. Elijo Kinesis cuando estoy completamente en AWS y necesito simplicidad. Elijo Kafka cuando necesito alto throughput, capacidades de replay, o escenarios multi-consumer."

---

## 🔴 SECCIÓN 3 — Preguntas Avanzadas Senior (Q14-Q20)

---

### 🏗️ Q14. Describe cómo diseñas una arquitectura de datos cloud escalable.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ARQUITECTURA DE DATOS ESCALABLE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  INGESTA     →    ALMACENAMIENTO   →    CÓMPUTO      →    SEMÁNTICA         │
│  ──────────       ───────────────       ───────           ─────────         │
│  • APIs           • Zona Raw            • Dataform        • Capa BI         │
│  • Streaming      • (S3/GCS)            • Spark           • Modelos ML      │
│  • Batch          • Staging             • Airflow         • APIs            │
│  • CDC            • Modelado                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│  TRANSVERSAL: CI/CD | Monitoreo | Logging | Alertas | Gestión de Costos     │
└─────────────────────────────────────────────────────────────────────────────┘
```

> 💡 **Cómo respondo esto:**
> 
> "Diseño arquitecturas de datos en capas. Primero, la capa de Ingesta - extraigo datos de APIs, fuentes streaming, archivos batch, y CDC desde bases de datos. Todos los datos raw llegan a una Zona Raw (S3/GCS) - nunca modifico datos fuente. Segundo, la capa de Almacenamiento con zonas staging y modeladas. Tercero, la capa de Cómputo donde Dataform/dbt transforma datos y Spark maneja procesamiento pesado. Finalmente, la capa Semántica expone datos limpios a herramientas BI y modelos ML.
> 
> A través de todas las capas, implemento CI/CD para deployments, monitoreo para salud del pipeline, logging para debugging, alertas para fallos, y gestión de costos para evitar sorpresas. Esta arquitectura escala porque cada capa puede escalar independientemente."

---

### 🤖 Q15. ¿Cómo abordas el diseño de sistemas RAG?

| Componente | Implementación |
|------------|----------------|
| ✂️ **Chunking** | Optimizado para tipo de contenido (marketing, soporte) |
| 🔢 **Embeddings** | Modelos tuneados para el dominio |
| 🗃️ **Vector Store** | Vertex Matching Engine, Supabase, Pinecone |
| 🔀 **Context Routing** | Clasificación de queries + cadenas de retrieval |
| 🛡️ **Fallbacks** | Respuestas basadas en reglas, filtros de seguridad |
| 📊 **Evaluación** | Tests de regresión, scores de similitud |

> 💡 **Cómo respondo esto:**
> 
> "Cuando diseño sistemas RAG, empiezo con la estrategia de chunking - optimizo el tamaño de chunk según el tipo de contenido. El contenido de marketing necesita chunking diferente que la documentación técnica. Luego elijo modelos de embeddings - a veces los fine-tuneo para nuestro dominio. Para almacenamiento vectorial, uso Vertex Matching Engine en GCP o Pinecone para multi-cloud. Implemento context routing para clasificar queries y elegir la estrategia de retrieval correcta. Siempre agrego fallbacks para cuando el retrieval falla. Finalmente, configuro evaluación con tests de regresión y scores de similitud para asegurar calidad en el tiempo."

---

### 🤖 Q16. Explica cómo construyes agentes de IA inteligentes.

| Paso | Descripción | Herramientas |
|------|-------------|--------------|
| 1️⃣ **Persona** | Definir comportamiento del sistema y restricciones | Prompt engineering |
| 2️⃣ **Tools** | Búsqueda, memoria, retrieval, acciones de API | LangGraph, ADK |
| 3️⃣ **Conversación** | Lógica multi-turno | Gestión de estado |
| 4️⃣ **Fallbacks** | Manejo de errores, escalación | Filtros de seguridad |
| 5️⃣ **Monitoreo** | Confiabilidad, consistencia de marca | Logging, métricas |
| 6️⃣ **Evaluación** | Tests A/B, regresión | Testing automatizado |

> 💡 **Cómo respondo esto:**
> 
> "Construyo agentes de IA en 6 pasos. Primero, defino la persona - qué debe hacer el agente y qué restricciones tiene. Segundo, le doy tools - búsqueda, memoria, retrieval, y acciones de API usando LangGraph o ADK. Tercero, implemento lógica de conversación para interacciones multi-turno con gestión de estado apropiada. Cuarto, agrego fallbacks para cuando las cosas salen mal - manejo de errores y escalación a humanos. Quinto, configuro monitoreo para rastrear confiabilidad y asegurar consistencia de marca. Finalmente, creo pipelines de evaluación con tests A/B y testing de regresión para medir calidad."

---

### 🔔 Q17. ¿Cómo diseñas sistemas de alertas y monitoreo?

| Tipo de Alerta | Trigger | Canal | Prioridad |
|----------------|---------|-------|-----------|
| 📈 **Keyword Spikes** | Volumen > threshold | Slack | 🟡 Media |
| 😠 **Anomalía de Sentimiento** | Negativo > 2σ | PagerDuty | 🔴 Alta |
| 🤖 **Detección de Spam** | Patrón match | Slack | 🟡 Media |
| 📊 **Caída de Rendimiento** | Métricas bajan | Email | 🟠 Alta |
| ⏰ **Freshness de Datos** | Stale > 2 horas | PagerDuty | 🔴 Crítica |

> 💡 **Cómo respondo esto:**
> 
> "Diseño alertas basadas en prioridad y urgencia. Para issues críticos como freshness de datos (stale > 2 horas), uso PagerDuty para despertar a alguien si es necesario. Para issues de alta prioridad como anomalías de sentimiento, también uso PagerDuty pero con diferentes reglas de escalación. Para prioridad media como keyword spikes, Slack es suficiente - el equipo lo ve durante horario de trabajo. Siempre defino thresholds claros y evito fatiga de alertas tuneando la sensibilidad. Cada alerta incluye contexto: qué pasó, por qué importa, y cómo investigar."

---

### 💪 Q18. Describe un problema desafiante y cómo lo resolviste.

| Fase | Descripción |
|------|-------------|
| 🔴 **Problema** | Pipeline de marketing se rompía por cambios de schema en APIs de terceros |
| 🔍 **Causa Raíz** | Sin validación de schema, transformaciones frágiles |

| Solución | Implementación |
|----------|----------------|
| 📐 **Detección de Schema** | Inferencia automática de schema en ingesta |
| 🔔 **Alertas de Drift** | Notificar cambios de schema |
| 🔄 **Auto-Reparación** | Transformaciones flexibles |
| ✅ **Validación** | Checks pre-carga |

> 📈 **Resultado:** Reducción de fallos en **60%**, reportes estabilizados.

> 💡 **Cómo respondo esto:**
> 
> "Uno de mis mayores desafíos fue cuando nuestro pipeline de marketing seguía rompiéndose aleatoriamente. Después de investigar, encontré la causa raíz: las APIs de terceros (Google Ads, Meta) a veces cambiaban sus schemas de respuesta sin aviso. Nuestras transformaciones eran frágiles - cualquier campo nuevo o eliminado causaba fallos.
> 
> Lo resolví implementando detección automática de schema. Cuando llegan datos, mi pipeline infiere el schema y lo compara contra el esperado. Si hay drift, recibo una alerta inmediatamente pero el pipeline no se rompe - maneja el cambio graciosamente. También hice las transformaciones más flexibles usando funciones COALESCE y TRY_CAST.
> 
> ¿El resultado? Los fallos de pipeline cayeron en 60%, y cuando los schemas cambian, lo sé instantáneamente en lugar de descubrirlo cuando los dashboards se rompen."

---

### ☁️ Q19. ¿Cómo manejas arquitecturas multi-cloud?

| Capa | GCP | AWS | Abstracción |
|------|-----|-----|-------------|
| 📦 **Almacenamiento** | GCS | S3 | Paths unificados |
| ⚡ **Cómputo** | Cloud Functions | Lambda | Mismos patrones de código |
| 📊 **Analítica** | BigQuery | Redshift | SQL estándar |
| 🎼 **Orquestación** | Composer | MWAA | DAGs de Airflow |
| 📝 **Logging** | Cloud Logging | CloudWatch | Formato unificado |

> 💡 **Cómo respondo esto:**
> 
> "Manejo multi-cloud creando capas de abstracción. Para almacenamiento, uso patrones de path unificados - al código no le importa si es S3 o GCS. Para cómputo, escribo Cloud Functions y Lambda con los mismos patrones - la lógica es idéntica, solo cambian los triggers. Para analítica, uso SQL estándar que funciona tanto en BigQuery como Redshift. Para orquestación, uso Airflow - los mismos DAGs corren en Composer (GCP) o MWAA (AWS) con cambios mínimos. Para logging, uso formato unificado para poder analizar logs de ambos clouds en un solo lugar. Este enfoque me permite mover workloads entre clouds sin reescribir todo."

---

### 🤖 Q20. ¿Cómo has combinado Data Engineering + Generative AI?

| Integración | Descripción |
|-------------|-------------|
| 🔍 **Pipelines RAG** | BigQuery/vector stores como backend de retrieval |
| 🤖 **AI Agents** | Ejecutar workflows de datos automáticamente |
| 📈 **Predictivo** | Vertex AI, AutoML para forecasting |
| 💡 **Insights** | Insights automatizados de clientes, alineación de brand voice |

> 💡 **Cómo respondo esto:**
> 
> "He estado combinando Data Engineering con Generative AI de varias formas. Primero, pipelines RAG - uso BigQuery y vector stores como backend de retrieval. Mis pipelines de datos preparan e indexan documentos para que la IA pueda recuperar contexto relevante. Segundo, AI Agents - construyo agentes que pueden ejecutar workflows de datos automáticamente, como disparar DAGs de Airflow o consultar BigQuery basándose en solicitudes en lenguaje natural. Tercero, analítica predictiva - uso Vertex AI y AutoML para construir modelos de forecasting, con mis pipelines preparando los datos de entrenamiento. Cuarto, insights automatizados - uso LLMs para analizar datos de clientes y generar resúmenes, siempre asegurando alineación con brand voice."

---

## 🟣 SECCIÓN 4 — Preguntas Comportamentales (Q21-Q25)

---

### 👨‍🏫 Q21. ¿Cómo mentorizas a ingenieros junior?

| Método | Descripción |
|--------|-------------|
| 📚 **Materiales de Onboarding** | Documentación estructurada para nuevos |
| 🖥️ **Sesiones Prácticas** | Pair programming, live coding |
| 📋 **Mejores Prácticas** | Estándares y guidelines definidos |
| 🔍 **Code Reviews** | Feedback educativo, no solo aprobación |

> 💡 **Cómo respondo esto:**
> 
> "Creo en la mentoría estructurada. Cuando un junior se une, empiezo con documentación de onboarding - diagramas de arquitectura, patrones comunes, y 'cómo hacemos las cosas aquí'. Luego hago sesiones prácticas donde hacemos pair programming en tareas reales. No solo arreglo su código - explico por qué hacemos las cosas de cierta manera.
> 
> Creé una guía de mejores prácticas cubriendo estilo SQL, patrones de Airflow, y manejo de errores. Durante code reviews, me enfoco en enseñar, no solo aprobar. Hago preguntas como '¿Qué pasa si esto falla?' o '¿Cómo escalaría esto?' Esto los ayuda a pensar como ingenieros senior.
> 
> El resultado es que los juniors se vuelven productivos más rápido y desarrollan buenos hábitos desde el día uno."

---

### 🤝 Q22. ¿Cómo manejas la colaboración cross-funcional?

| Equipo | Tipo de Colaboración |
|--------|---------------------|
| 🤖 **MLEs** | Integración de modelos, feature engineering |
| 🧪 **QA** | Estrategias de testing, validación de datos |
| 📋 **PMs** | Requisitos, priorización |
| 💼 **Negocio** | Traducir necesidades a soluciones técnicas |

> 💡 **Cómo respondo esto:**
> 
> "Trabajo de cerca con diferentes equipos cada día. Con ML Engineers, colaboro en feature engineering - preparo los datos que necesitan para modelos y ayudo a integrar sus predicciones de vuelta en nuestros pipelines. Con QA, definimos estrategias de testing y reglas de validación de datos juntos.
> 
> Con Product Managers, traduzco requisitos de negocio en especificaciones técnicas. Los ayudo a entender qué es factible y cuánto toman las cosas. Con stakeholders de Negocio, soy el traductor - me dicen qué insights necesitan, y yo descubro cómo obtener los datos ahí.
> 
> La clave es comunicación. Evito jerga técnica con personas no técnicas y me enfoco en resultados: 'Esto te dará reportes diarios en lugar de semanales' en vez de 'Implementaré un patrón ETL incremental.'"

---

### 📚 Q23. ¿Cómo te mantienes actualizado?

| Método | Plataforma | Enfoque |
|--------|------------|---------|
| 🎓 **Cursos** | Google Cloud Skills Boost | Cloud & AI |
| 🔧 **Open Source** | Contribuciones en GitHub | Habilidades prácticas |
| 📺 **Enseñanza** | Streams en vivo en Twitch | Compartir con comunidad |
| 🛠️ **Proyectos** | Builds personales | Aprendizaje práctico |

> 💡 **Cómo respondo esto:**
> 
> "Me mantengo actualizado a través de múltiples canales. Tomo cursos en Google Cloud Skills Boost para aprender nuevas features de cloud y AI. Contribuyo a proyectos open source en GitHub - esto me obliga a leer código de otras personas y aprender nuevos patrones. También enseño en streams en vivo de Twitch - explicar conceptos a otros me ayuda a entenderlos mejor. Finalmente, construyo proyectos personales para experimentar con nuevas tecnologías antes de usarlas en el trabajo."

---

### 💪 Q24. ¿Cuál ha sido el proyecto más desafiante?

| Fase | Descripción |
|------|-------------|
| 🎯 **Proyecto** | Plataforma de marketing analytics en tiempo real |
| 🔧 **Desafío** | 5+ APIs con diferentes schemas, rate limits, auth |
| ⚠️ **Problemas** | Consistencia de datos, fallos de API, updates en tiempo real, costos |

| Componente de Solución | Implementación |
|------------------------|----------------|
| 🛡️ **Manejo de Errores** | Lógica robusta de retry y fallback |
| 📐 **Normalización de Schema** | Modelo de datos unificado |
| 📊 **Carga Incremental** | Updates eficientes de datos |
| 🔔 **Monitoreo** | Alertas de anomalías antes del impacto |

> 💡 **Cómo respondo esto:**
> 
> "Mi proyecto más desafiante fue construir una plataforma de marketing analytics en tiempo real que extraía datos de 5+ APIs - Google Ads, Meta, TikTok, LinkedIn, X. Cada API tenía diferentes schemas, rate limits, y métodos de autenticación. Los desafíos eran consistencia de datos entre fuentes, manejar fallos de API graciosamente, proveer updates en tiempo real, y controlar costos.
> 
> Lo resolví implementando manejo robusto de errores con retries y fallbacks, normalizando schemas en un modelo de datos unificado, usando carga incremental para ser eficiente, y configurando monitoreo para detectar anomalías antes de que impactaran reportes. El resultado fue una plataforma confiable de la que los marketers ahora dependen diariamente."

---

### 🎯 Q25. ¿Qué buscas en un nuevo rol?

| Buscando | Descripción |
|----------|-------------|
| 🚀 **Desafío** | Problemas de Data & AI a escala |
| ☁️ **Tecnología** | Arquitecturas cloud-native modernas |
| 👥 **Equipo** | Colegas talentosos y colaborativos |
| 📚 **Crecimiento** | Aprendizaje y compartir conocimiento |

> 💡 **Cómo respondo esto:**
> 
> "Busco un rol donde pueda resolver problemas desafiantes de data y AI a escala. Quiero trabajar con arquitecturas cloud-native modernas - no sistemas legacy. Valoro un equipo de colegas talentosos y colaborativos que se empujen mutuamente a crecer. Más importante, quiero oportunidades de aprendizaje continuo y una cultura de compartir conocimiento. Me emocionan los roles que combinan Data Engineering tradicional con Generative AI - ahí es donde veo el futuro de nuestro campo."

---

## ⚫ SECCIÓN 5 — Experto: Preguntas Senior DE + AI (Q26-Q30)

---

### 🤖 Q26. ¿Cuál es tu enfoque para arquitecturas multi-agente?

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA MULTI-AGENTE                          │
├─────────────────────────────────────────────────────────────────────┤
│    ┌──────────┐     ┌──────────────┐     ┌──────────┐              │
│    │ Agente A │◄───►│   ROUTER /   │◄───►│ Agente B │              │
│    │(Investig)│     │  ARBITRADOR  │     │(Escritor)│              │
│    └──────────┘     └──────────────┘     └──────────┘              │
│         │                  │                  │                     │
│         └──────────────────┼──────────────────┘                     │
│                            ▼                                        │
│                   ┌──────────────┐                                  │
│                   │CAPA MEMORIA  │                                  │
│                   │  COMPARTIDA  │                                  │
│                   └──────────────┘                                  │
└─────────────────────────────────────────────────────────────────────┘
```

| Componente | Propósito |
|------------|-----------|
| 🎭 **Roles Especializados** | Cada agente tiene responsabilidad distinta |
| 🔧 **Interacciones Tool** | Agentes usan tools para acciones |
| 🧠 **Memoria Compartida** | Persistencia de estado entre agentes |
| 🔀 **Lógica de Routing** | Dirigir queries al agente correcto |

> 💡 **Cómo respondo esto:**
> 
> "Diseño sistemas multi-agente con roles especializados. Cada agente tiene una responsabilidad - por ejemplo, Agente A investiga, Agente B escribe. Un router o arbitrador decide qué agente maneja cada query. Todos los agentes comparten una capa de memoria para tener contexto sobre la conversación. Uso tools para que los agentes tomen acciones - búsqueda, consultar bases de datos, llamar APIs. La clave es separación clara de concerns y lógica de routing robusta. Implemento esto usando LangGraph, que me permite definir workflows de agentes complejos como máquinas de estado."

---

### 📊 Q27. ¿Cómo mides la calidad de sistemas RAG o agentes?

| Métrica | Descripción | Objetivo |
|---------|-------------|----------|
| 🎯 **Precisión de Retrieval** | Docs relevantes recuperados | > 90% |
| 📝 **Relevancia de Contexto** | Contexto coincide con query | > 85% |
| 🚫 **Tasa de Alucinación** | Información falsa | < 5% |
| 🔄 **Consistencia Multi-turno** | Conversaciones coherentes | > 95% |
| 🎤 **Alineación Brand Voice** | Coincide con tono de marca | Revisión manual |
| 🔧 **Éxito de Ejecución de Tools** | Tools funcionan correctamente | > 99% |
| ⏱️ **Latencia de Respuesta** | Tiempo para responder | < 2s |

> 💡 **Cómo respondo esto:**
> 
> "Mido calidad de RAG y agentes con métricas específicas. Precisión de retrieval - ¿estamos recuperando documentos relevantes? Objetivo >90%. Relevancia de contexto - ¿el contexto coincide con el query? Objetivo >85%. Tasa de alucinación - ¿la IA está inventando cosas? Objetivo <5%. Consistencia multi-turno - ¿las conversaciones son coherentes entre turnos? Objetivo >95%. Para ejecución de tools, espero >99% tasa de éxito. Latencia de respuesta debe ser <2s. Alineación de brand voice requiere revisión manual - muestreo respuestas semanalmente para asegurar que coincidan con nuestro tono. Ejecuto tests de regresión antes de cada deployment para capturar regresiones de calidad."

---

### 🔒 Q28. ¿Cómo manejas gobernanza de datos y compliance?

| Área | Implementación |
|------|----------------|
| 📊 **Lineage** | Rastrear origen de datos y transformaciones |
| 🔐 **Seguridad** | Enmascarado a nivel columna, encriptación |
| 👤 **Control de Acceso** | IAM con privilegio mínimo |
| 📝 **Documentación** | Ownership de datos, políticas de retención |
| 🛡️ **Compliance** | Detección automatizada de datos personales sensibles (emails, teléfonos, IDs) |

> 💡 **Cómo respondo esto:**
> 
> "La gobernanza de datos está integrada en mis pipelines desde el día uno. Implemento rastreo de lineage para saber de dónde viene cada pieza de datos y cómo se transforma. Para seguridad, uso enmascarado a nivel columna para campos sensibles y encriptación en reposo y en tránsito. El control de acceso sigue privilegio mínimo - los usuarios solo ven lo que necesitan. Documento ownership de datos y políticas de retención para cada dataset. Para compliance, ejecuto escaneos automatizados para detectar datos personales sensibles como emails, números de teléfono e IDs - si algo aparece donde no debería, recibo una alerta inmediatamente."

---

### 💰 Q29. ¿Cómo abordas la optimización de costos?

| Estrategia | Implementación | Ahorros |
|------------|----------------|---------|
| 📅 **Particionado** | Query solo datos necesarios | 50-80% |
| 🗄️ **Políticas Lifecycle** | Hot → Cold → Archive | 40-70% |
| 📊 **Right-sizing** | Ajustar cómputo a workload | 20-40% |
| 💵 **Spot Instances** | Usar preemptible para batch | 60-90% |
| 🔔 **Alertas de Costo** | Monitorear anomalías | Preventivo |

> 💡 **Cómo respondo esto:**
> 
> "La optimización de costos es un proceso continuo. Particionado es la mayor ganancia - al particionar tablas por fecha, los queries escanean solo particiones relevantes, ahorrando 50-80% en costos de query. Implemento políticas de lifecycle para mover datos de hot (SSD) a cold (HDD) a archive (Glacier/Coldline), ahorrando 40-70%. Hago right-sizing de cómputo - si un job corre bien en n1-standard-4, no uso n1-standard-16. Para jobs batch, uso instancias spot/preemptible que cuestan 60-90% menos. Finalmente, configuro alertas de costo para capturar anomalías antes de que se conviertan en facturas grandes. Estas prácticas han ahorrado miles de dólares mensualmente."

---

### 🏗️ Q30. ¿Cuál es tu experiencia con data mesh?

| Principio | Implementación |
|-----------|----------------|
| 🏢 **Ownership de Dominio** | Equipos son dueños de sus productos de datos |
| 📦 **Data as Product** | Métricas de calidad, documentación, SLAs |
| 🛠️ **Plataforma Self-Serve** | Equipos publican/consumen independientemente |
| 🏛️ **Gobernanza Federada** | Estándares con autonomía |

> 💡 **Cómo respondo esto:**
> 
> "He implementado principios de data mesh en organizaciones transicionando de equipos de datos centralizados. La clave es ownership de dominio - cada equipo es dueño de sus productos de datos, no un equipo central. Ayudo a los equipos a tratar los datos como producto con métricas de calidad, documentación y SLAs. Construyo plataformas self-serve donde los equipos pueden publicar y consumir datos independientemente. La gobernanza es federada - definimos estándares a nivel compañía (naming, seguridad), pero los equipos tienen autonomía en implementación. El resultado es entrega de datos más rápida porque los equipos no esperan por un equipo central, mientras mantienen calidad y consistencia."

---

# 🎯 SECCIÓN 5.1 — Portafolio de Proyectos Clave

> **Propósito:** Proyectos reales para referenciar en entrevistas.

---

## 📊 Resumen de Proyectos

| # | Proyecto | Cloud | Categoría | Resultado Clave |
|---|----------|-------|-----------|-----------------|
| 1️⃣ | **CDP (Customer Data Platform)** | 🔵 GCP | Plataforma de Datos | 5M+ perfiles unificados, 25% reducción CAC |
| 1️⃣B | **CDP (Customer Data Platform)** | 🟠 AWS | Plataforma de Datos | 50M+ eventos/día, compliance de seguridad y privacidad |
| 2️⃣ | **Sistema de Alertas Tiempo Real** | 🔵 GCP | Monitoreo | < 5 min latencia de alerta, 40% ahorro de costos |
| 2️⃣B | **Sistema de Alertas Tiempo Real** | 🟠 AWS | Monitoreo | < 5 min latencia de alerta, 40% ahorro de costos |
| 3️⃣ | **Sistema de Insights Multi-Modal** | 🔵 GCP | AI/Analytics | 70% menos revisión manual, 18% mejora ROAS |
| 3️⃣B | **Sistema de Insights Multi-Modal** | 🟠 AWS | AI/Analytics | 70% menos revisión manual, 18% mejora ROAS |
| 4️⃣ | **Framework de Gobernanza** | 🔵 GCP | Gobernanza | 65% menos incidentes, 30% ahorro de costos |
| 4️⃣B | **Framework de Gobernanza** | 🟠 AWS | Gobernanza | 65% menos incidentes, 30% ahorro de costos |
| 5️⃣ | **Arquitectura de Pipelines AI-Driven** | 🔵 GCP | Arquitectura | 80% desarrollo de features más rápido |
| 5️⃣B | **Arquitectura de Pipelines AI-Driven** | 🟠 AWS | Arquitectura | 80% desarrollo de features más rápido |
| 6️⃣ | **Agentes de Marketing Analyst AI** | 🔵 GCP | GenAI | Insights automatizados, análisis manual reducido |
| 6️⃣B | **Agentes de Marketing Analyst AI** | 🟠 AWS | GenAI | Insights automatizados, análisis manual reducido |
| 7️⃣ | **Sistemas RAG & Multi-Agente** | 🔵 GCP | GenAI | Búsqueda grounded, workflows inteligentes |
| 7️⃣B | **Sistemas RAG & Multi-Agente** | 🟠 AWS | GenAI | Búsqueda grounded, workflows inteligentes |
| 8️⃣ | **Sistemas de Alertas y Predictivos** | 🔵 GCP | ML/Monitoreo | Alertas proactivas, analítica predictiva |
| 8️⃣B | **Sistemas de Alertas y Predictivos** | 🟠 AWS | ML/Monitoreo | Alertas proactivas, analítica predictiva |
| 9️⃣ | **Arquitectura de Datos AI-Native** | 🔵 GCP | Arquitectura | Infraestructura lista para ML |
| 9️⃣B | **Arquitectura de Datos AI-Native** | 🟠 AWS | Arquitectura | Infraestructura lista para ML |

---

## 🎯 Proyecto 1: Customer Data Platform (CDP) — GCP

### 📋 Resumen

| Aspecto | Detalles |
|---------|----------|
| 🔴 **Problema** | Datos de clientes fragmentados en 8+ sistemas |
| 🎯 **Objetivo** | Vista unificada para personalización, reducir CAC |
| ☁️ **Cloud** | Google Cloud Platform |

### 💬 Mi Experiencia (Cómo lo explicaría en una entrevista)

> *"En este proyecto, fui responsable de construir una Customer Data Platform desde cero. El equipo de marketing tenía datos de clientes dispersos en 8 sistemas diferentes — CRM, analytics del sitio web, eventos de app móvil, plataformas de ads como Google Ads y Meta, e incluso logs de call center. Nadie tenía una vista unificada del cliente.*
>
> *Empecé extrayendo datos de Supermetrics y las diferentes APIs de plataformas de ads usando **BigQuery Data Transfers** — este es un servicio nativo de GCP que automáticamente programa y carga datos desde fuentes como Google Ads, Google Analytics, y conectores de terceros como Supermetrics directamente a BigQuery. Para eventos en tiempo real del sitio web y app móvil, configuré Pub/Sub para capturar todo a medida que sucedía. Luego usé Dataproc con Spark Structured Streaming para procesar los datos de streaming y realizar identity resolution — básicamente emparejando usuarios entre sistemas usando email, números de teléfono y device IDs.*
>
> *Todos los datos procesados llegaron a BigQuery, que particioné por fecha y clusterizé por customer_id para rendimiento óptimo de queries. Construí la capa de transformación con Dataform, creando un modelo de datos limpio con capas staging, intermediate y mart. Todo el pipeline fue orquestado con Cloud Composer ejecutando refreshes diarios.*
>
> *Para activación, conecté los perfiles unificados a Vertex AI para construir modelos de propensión — prediciendo qué clientes era probable que convirtieran. Estas predicciones se retroalimentaron a Google Ads y Meta para targeting de audiencias. El resultado final fue 5 millones de perfiles unificados y una reducción del 25% en costo de adquisición de clientes."*

### 🏗️ Arquitectura

```
FUENTES DE DATOS → INGESTA → PROCESAMIENTO → ALMACENAMIENTO → ACTIVACIÓN
──────────────────────────────────────────────────────────────────────────
[CRM]          BQ Data Transfers  Dataproc      BigQuery     Vertex AI
[Website]  ──► Pub/Sub        ──► (Spark)   ──► GCS      ──► Looker
[Mobile]       Cloud Functions    Dataform                   Ad APIs
[Ads]
[Call Center]
               └──── Cloud Composer (Airflow) Orquestación ────┘
```

### 🔧 Implementación Técnica

| Capa | Componentes | Detalles |
|------|-------------|----------|
| 📥 **Ingesta** | BigQuery Data Transfers, Pub/Sub | Supermetrics/ads vía Data Transfers, tiempo real vía Pub/Sub |
| ⚙️ **Procesamiento** | Dataproc (Spark), Dataform | Identity resolution, transformaciones |
| 💾 **Almacenamiento** | BigQuery, GCS | Particionado por fecha, clusterizado por customer_id |
| 🔗 **Identidad** | Matching personalizado | Email, teléfono, device IDs |
| 🎯 **Activación** | Vertex AI, APIs | Modelos de propensión, sync de audiencias |
| 🎼 **Orquestación** | Cloud Composer | Refreshes diarios, reentrenamiento ML |

### 📈 Resultados

| Métrica | Resultado |
|---------|-----------|
| 👥 **Perfiles Unificados** | 5M+ de 8 fuentes de datos |
| 💰 **Reducción CAC** | 25% mejora |
| ⚡ **Procesamiento de Eventos** | 10K eventos/segundo |
| ⏱️ **Latencia** | Vista 360° en < 15 minutos |

---

## 🎯 Proyecto 1B: Customer Data Platform (CDP) — AWS

### 📋 Resumen

| Aspecto | Detalles |
|---------|----------|
| 🔴 **Problema** | Misma necesidad de negocio, infraestructura AWS |
| 🎯 **Objetivo** | Vista unificada del cliente, compliance-first |
| ☁️ **Cloud** | Amazon Web Services |

### 💬 Mi Experiencia (Cómo lo explicaría en una entrevista)

> *"En este proyecto, fui responsable de construir una Customer Data Platform desde cero en AWS. El equipo de marketing tenía datos de clientes dispersos en 8 sistemas diferentes — CRM, analytics del sitio web, eventos de app móvil, plataformas de ads como Google Ads y Meta, e incluso logs de call center. Nadie tenía una vista unificada del cliente.*
>
> *A diferencia de GCP que tiene BigQuery Data Transfers como servicio nativo, AWS no tiene un equivalente directo para fuentes de datos de marketing. Así que para extraer datos de Supermetrics y APIs de plataformas de ads, usé **Fivetran** (una herramienta ELT de terceros) que conecta con 150+ fuentes y carga datos directamente en S3 y Redshift. Alternativamente, para algunas fuentes usé **AWS AppFlow** para integraciones SaaS como Salesforce y Google Analytics, y **funciones Lambda** disparadas por EventBridge para extracciones de APIs personalizadas donde Fivetran/AppFlow no tenían conectores. Para eventos en tiempo real del sitio web y app móvil, configuré Kinesis Data Streams para capturar todo a medida que sucedía, y configuré Kinesis Firehose para entregar automáticamente los datos a S3 en formato Parquet. Luego usé AWS Glue con Spark para procesar los datos y realizar identity resolution — básicamente emparejando usuarios entre sistemas usando email, números de teléfono y device IDs.*
>
> *Todos los datos procesados llegaron a S3 organizado como data lake con capas Bronze, Silver y Gold — datos raw en Bronze, datos limpios en Silver, y agregaciones listas para negocio en Gold. Para la capa de warehouse, usé Redshift Serverless que particioné por fecha y usé distribution keys en customer_id para rendimiento óptimo de queries. También configuré Redshift Spectrum para consultar el data lake de S3 directamente sin mover datos.*
>
> *La capa de transformación fue construida con scripts SQL personalizados y jobs de Glue, creando un modelo de datos limpio con capas staging, intermediate y mart. Todo el pipeline fue orquestado con MWAA (Managed Airflow) ejecutando refreshes diarios.*
>
> *Para activación, conecté los perfiles unificados a SageMaker para construir modelos de propensión — prediciendo qué clientes era probable que convirtieran. Estas predicciones se retroalimentaron a Google Ads y Meta para targeting de audiencias. Lake Formation manejó todo el control de acceso — podía controlar quién ve qué datos a nivel columna, como ocultar direcciones de email de ciertos equipos. El resultado final fue más de 50 millones de eventos procesados diariamente y el mismo impacto de negocio: perfiles de clientes unificados y costos de adquisición reducidos."*

### 🏗️ Arquitectura

```
FUENTES DE DATOS → INGESTA → PROCESAMIENTO → ALMACENAMIENTO → ACTIVACIÓN
──────────────────────────────────────────────────────────────────────────
[CRM]          Fivetran/AppFlow   Glue/EMR      Redshift    SageMaker
[Website]  ──► Kinesis        ──► Step      ──► S3 Lake ──► QuickSight
[Mobile]       Lambda             Functions                  Ad APIs
[Ads]          EventBridge
[Call Center]
               └──── MWAA (Managed Airflow) Orquestación ────┘
```

### 🟠 Patrones Específicos de AWS

| Patrón | Servicio | Propósito |
|--------|----------|-----------|
| 📥 **Ingesta de Datos** | Fivetran / AppFlow / Lambda | Sin Data Transfers nativo como GCP |
| 📤 Auto-delivery | Kinesis Firehose | Entrega a S3 + transformación |
| 🔒 Gobernanza | Lake Formation | Control de acceso centralizado |
| 🔍 Queries ad-hoc | Athena | Query S3 directamente |
| 🔗 S3 desde Redshift | Redshift Spectrum | Tablas externas |

> 💡 **GCP vs AWS Ingesta de Datos:**
> 
> | Aspecto | 🔵 GCP | 🟠 AWS |
> |---------|--------|--------|
> | **Servicio Nativo** | BigQuery Data Transfers | ❌ Sin equivalente directo |
> | **Datos de Marketing** | Conector Supermetrics | Fivetran, Stitch, Airbyte |
> | **Fuentes SaaS** | Data Transfers | AWS AppFlow (fuentes limitadas) |
> | **APIs Personalizadas** | Cloud Functions | Lambda + EventBridge |
> 
> *"AWS no tiene un servicio de Data Transfer nativo como GCP. Para fuentes de datos de marketing como Supermetrics, Google Ads y Meta, uso herramientas ELT de terceros como Fivetran o Airbyte. Para fuentes SaaS como Salesforce, AWS AppFlow funciona bien. Para APIs personalizadas sin conectores, construyo funciones Lambda disparadas por EventBridge en un schedule."*

### 📈 Resultados

| Métrica | Resultado |
|---------|-----------|
| ⚡ **Eventos/Día** | 50M+ con latencia sub-segundo |
| 💰 **Modelo de Costos** | Redshift Serverless (pago por query) |
| 🔗 **Data Sharing** | AWS Data Exchange |
| 🔒 **Compliance** | Auditorías de seguridad + leyes de privacidad vía Lake Formation |

---

## 💡 Cómo Presentar Proyectos en Entrevistas

### 🌟 Usa el Método STAR

| Letra | Significado | Enfoque |
|-------|-------------|---------|
| **S** | Situación | Problema de negocio |
| **T** | Tarea | Tu responsabilidad |
| **A** | Acción | Decisiones técnicas |
| **R** | Resultado | Impacto cuantificado |

### 📝 Ejemplo de Respuesta

> *"En mi proyecto CDP, la **situación** era que marketing tenía datos de clientes fragmentados en 8 sistemas. Mi **tarea** fue diseñar una plataforma de datos unificada. **Arquitecté** una solución usando BigQuery para almacenamiento, Dataproc con Spark para identity resolution en streaming, y Vertex AI para modelos de propensión. El **resultado** fue 5M+ perfiles unificados y una reducción del 25% en costo de adquisición de clientes."*

---

# ❓ SECCIÓN 6 — Preguntas para Hacer al Entrevistador

---

## 📋 Resumen de Preguntas

| # | Pregunta | Propósito |
|---|----------|-----------|
| 1️⃣ | Día típico | Entender balance de trabajo |
| 2️⃣ | Mayores desafíos | Insight de madurez de datos |
| 3️⃣ | Enfoque de calidad de datos | Madurez de prácticas |
| 4️⃣ | Stack tecnológico | Herramientas y evolución |
| 5️⃣ | Métricas de éxito | Claridad de expectativas |
| 6️⃣ | Oportunidades de aprendizaje | Potencial de crecimiento |
| 7️⃣ | Colaboración ML/AI | Integración de equipos |
| 8️⃣ | Proceso CI/CD | Madurez de ingeniería |
| 9️⃣ | Onboarding | Nivel de organización |
| 🔟 | Por qué está abierta la posición | Entender contexto |

---

### 1️⃣ ¿Cómo es un día típico para este rol?

| Buscar | Banderas Rojas |
|--------|----------------|
| ✅ Estructura clara | ❌ "Cada día es diferente" |
| ✅ Tiempo para trabajo profundo | ❌ Exceso de reuniones |
| ✅ On-call definido | ❌ Firefighting constante |

---

### 2️⃣ ¿Cuáles son los mayores desafíos de datos?

| Buenas Señales | Banderas Rojas |
|----------------|----------------|
| ✅ Desafíos específicos | ❌ Respuestas vagas |
| ✅ Planes para abordarlos | ❌ Negación de problemas |
| ✅ Enfoque en escala/calidad | ❌ Lista abrumadora sin abordar |

---

### 3️⃣ ¿Cómo aborda el equipo la calidad de datos?

| Buscar | Banderas Rojas |
|--------|----------------|
| ✅ Testing automatizado | ❌ "Estamos trabajando en eso" (sin plan) |
| ✅ Data contracts | ❌ "Los analistas manejan eso" |
| ✅ Ownership claro | ❌ Sin awareness de compliance |

---

### 4️⃣ ¿Cuál es el stack tecnológico?

| Buenas Señales | Banderas Rojas |
|----------------|----------------|
| ✅ Stack moderno | ❌ Desactualizado sin planes de upgrade |
| ✅ Disposición a evolucionar | ❌ Churn constante |
| ✅ Presupuesto para herramientas | ❌ Sin estabilidad |

---

### 5️⃣ ¿Cómo miden el éxito?

| Buenas Señales | Banderas Rojas |
|----------------|----------------|
| ✅ OKRs/KPIs claros | ❌ "Solo mantener las cosas funcionando" |
| ✅ Métricas de uptime de pipeline | ❌ Sin métricas claras |
| ✅ Objetivos de freshness de datos | ❌ Puramente subjetivo |

---

### 6️⃣ ¿Qué oportunidades de aprendizaje y crecimiento hay?

| Buenas Señales | Banderas Rojas |
|----------------|----------------|
| ✅ Presupuesto de training | ❌ "Estamos muy ocupados" |
| ✅ Asistencia a conferencias | ❌ Sin career ladder |
| ✅ Ejemplos de promoción | ❌ Sin mentoría |

---

### 7️⃣ ¿Cómo colabora el equipo con equipos de ML/AI?

| Buenas Señales | Banderas Rojas |
|----------------|----------------|
| ✅ Infraestructura compartida | ❌ Equipos en silos |
| ✅ Feature stores | ❌ "Ellos hacen lo suyo" |
| ✅ Prácticas MLOps | ❌ Fricción entre equipos |

---

### 8️⃣ ¿Cómo es el proceso de CI/CD?

| Buenas Señales | Banderas Rojas |
|----------------|----------------|
| ✅ CI/CD automatizado | ❌ Deployments manuales |
| ✅ Deployments frecuentes | ❌ Sin testing |
| ✅ Infrastructure as code | ❌ "Deploy cuando esté listo" |

---

### 9️⃣ ¿Cómo es el onboarding?

| Buenas Señales | Banderas Rojas |
|----------------|----------------|
| ✅ Plan 30/60/90 días | ❌ "Ya lo descubrirás" |
| ✅ Buddy/mentor asignado | ❌ Sin documentación |
| ✅ Documentación de calidad | ❌ Nadar o hundirse |

---

### 🔟 ¿Por qué está abierta esta posición?

| Buenas Señales | Banderas Rojas |
|----------------|----------------|
| ✅ Expansión del equipo | ❌ Alta rotación |
| ✅ Nueva iniciativa | ❌ Respuestas vagas |
| ✅ Proyectos de crecimiento | ❌ Persona anterior "se fue de repente" |

---

## 💡 Tips Pro para Hacer Preguntas

| Tip | Por qué |
|-----|---------|
| 🎯 **Elegir 3-4 preguntas** | No abrumar; ajustar al flujo de conversación |
| 📝 **Tomar notas** | Muestra seriedad; ayuda a comparar ofertas |
| 🔍 **Hacer follow-ups** | "¿Puedes dar un ejemplo?" profundiza respuestas |
| 👥 **Adaptar al entrevistador** | Preguntas técnicas para ingenieros, cultura para managers |
| 💰 **Guardar salario para HR** | Evitar en rondas tempranas |

---

