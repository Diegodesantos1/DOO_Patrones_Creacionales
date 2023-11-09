<h1 align="center">Patrones Creacionales</h1>

En este [repositorio](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales) queda resuelta la práctica de los Patrones Creacionales.

<h2 align="center">Análisis Modular de las Activaciones del SAMUR-Protección Civil en Madrid con Abstract Factory</h2>

El SAMUR-Protección Civil es el servicio de atención a urgencias y emergencias sanitarias extrahospitalarias en el municipio de Madrid. Su labor es esencial para garantizar la seguridad y el bienestar de los ciudadanos en situaciones de emergencia. A lo largo del año, el SAMUR lleva a cabo múltiples "activaciones" en respuesta a diversas situaciones, desde accidentes de tráfico hasta emergencias médicas.

La ciudad de Madrid, en su compromiso con la transparencia y la apertura de datos, publica un registro detallado de estas activaciones en formato CSV. Este registro incluye información como la fecha, hora, tipo de emergencia, y otros detalles relevantes de cada activación.

<h3 align="center">Objetivos</h3>

***

Tu tarea es desarrollar un programa en Python que haga uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos. En específico:

Lectura de Datos: Acceda y lea el archivo CSV directamente desde el enlace proporcionado: Activaciones del SAMUR-Protección Civil.
Modelado de Datos: Modela y estructura la información para su análisis.

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/558ded3c-702a-4e70-889c-2c09b851176b)


Abstract Factory: Diseña un "Abstract Factory" que permita crear diferentes tipos de análisis o representaciones de los datos. Por ejemplo:
Cada fábrica debe tener al menos dos productos concretos (e.g., histograma de activaciones por tipo de emergencia, gráfico de barras de activaciones por mes).
Una fábrica que genere análisis estadísticos (media, moda, mediana).

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/73e0650d-cde0-4759-84c8-f0ec923689a4)

Una fábrica que produzca visualizaciones gráficas (histogramas, gráficos de barras).

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/f9ccf586-8026-4f63-9dde-5b473b3eac2b)


Análisis y Representación: Utiliza las fábricas creadas para generar distintos análisis y representaciones de los datos. Muestra la media de activaciones por día, y un histograma de las activaciones


![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/265a259d-bc9b-43c7-953c-aebf1b03942c)

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/d53d9ca2-26b6-450c-835e-0851d7e8b28c)


***

<h2 align="center">Sistema Integral de Creación y Gestión de Pizzas Gourmet con Almacenamiento en CSV utilizando el Patrón Builder</h2>

***

La reconocida cadena de pizzerías gourmet "Delizioso" ha decidido lanzar una plataforma digital para permitir a sus clientes diseñar y personalizar sus pizzas al máximo detalle. Esta pizzería es conocida por su meticulosidad y su vasto menú de ingredientes, técnicas de cocción y presentaciones. Además de la personalización, "Delizioso" busca almacenar cada pizza diseñada por sus clientes en un archivo CSV para análisis posterior, recomendaciones personalizadas y marketing dirigido.

<h3 align="center">Características a considerar</h3>

***

Tipo de masa: Variedades premium desde masas delgadas hasta masas fermentadas por 48 horas, con opciones de ingredientes especiales.
Salsa base: Desde salsas clásicas hasta salsas de autor, incluyendo opciones veganas y de edición limitada.
Ingredientes principales: Una gama que abarca desde ingredientes locales hasta importados de especialidad, todos categorizados por su origen, tipo y rareza.
Técnicas de cocción: Diversidad que abarca desde hornos tradicionales hasta técnicas modernas de cocina molecular.
Presentación: Opciones que van desde estilos clásicos hasta presentaciones que son verdaderas obras de arte.
Maridajes recomendados: Una base de datos con cientos de opciones de vinos, cervezas y cocteles, con recomendaciones basadas en las elecciones de los ingredientes de la pizza.
Extras y finalizaciones: Desde bordes especiales hasta acabados con ingredientes gourmet como trufas y caviar.

<h3 align="center">Objetivos</h3>

***

Diseñar un sistema que permita a los clientes construir su pizza paso a paso utilizando el patrón Builder.

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/f1758382-2015-4fa4-a858-e205cdf085bd)

Asegurar que cada elección sea validada para ser compatible con las selecciones previas del cliente.
Desarrollar una interfaz de usuario amigable que guíe al cliente en el proceso de creación, ofreciendo información relevante sobre cada elección y facilitando la toma de decisiones.

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/25a64ff0-5801-4bac-9e15-c8de6da4819f)

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/ea72bc07-06c0-402b-82db-d42c5c3008eb)

Incorporar un sistema de recomendaciones que sugiera ingredientes, técnicas y maridajes basados en las elecciones previas del cliente.

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/3952a0d1-b80e-4daa-8f7b-9f7de4bfa965)


Desarrollar un módulo que guarde cada pizza personalizada en un archivo CSV, almacenando cada detalle, desde los ingredientes hasta el maridaje recomendado.

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/4159f326-7a5d-4209-826a-ff4cb555133a)

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/407fea3f-1002-4310-ab96-f592ebd15313)

Crear una funcionalidad que lea del archivo CSV y pueda reconstruir la pizza para su visualización, edición o reorden.

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/e03ed533-6a57-42b6-9ee6-2609ec27c981)

Garantizar la flexibilidad del sistema para futuras adiciones o modificaciones, ya que la pizzería está en constante innovación.

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/1dba4560-4c03-475b-9b83-2b9decae4910)

Implementar medidas de seguridad para garantizar la integridad de los datos almacenados y la privacidad de las elecciones de los clientes.

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/ffa7e371-a012-4d30-b588-868e24410778)

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/6be4ea7c-0dfa-456e-a518-ac40de28fe21)

Ahora iniciamos sesión con el nuevo usuario y contraseña:

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/56f04263-fe84-4869-9926-dd55d4bab9eb)

Y nos lleva a la web mostrando nuestro nombre de usuario:

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/60f8c4a0-8497-42b2-bbe1-1053f6540d5f)

Para el admin:

![image](https://github.com/Diegodesantos1/DOO_Patrones_Creacionales/assets/91721855/9f45f7a6-383a-4cd3-a936-f834ffbadd1c)


Al final del ejercicio, el estudiante deberá justificar el uso del patrón Builder y explicar cómo se logra la robustez y adaptabilidad del sistema, destacando las ventajas de su diseño frente a otros posibles enfoques.

*EL patrón builder...*
