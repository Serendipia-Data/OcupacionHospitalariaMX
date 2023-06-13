# HospitalizacionesCOVIDMX

El presente repositorio contiene los datos de capacidad hospitalaria divulgados por la Secretaría de Salud a través del portal de la UNAM
[https://www.gits.igg.unam.mx/red-irag-dashboard/reviewHome#](https://www.gits.igg.unam.mx/red-irag-dashboard/reviewHome#)

# Primera versión de script
Información de ocupación hospitalaria en México, Secretaría de Salud. Obtenidas en su mayoría a través de [CapacidadHospitalariaMX: por @RodrigoZepeda](https://github.com/RodrigoZepeda/CapacidadHospitalariaMX)

## Datos
Los datos descargados están en la carpeta especificada en la linea 18, actualmente la carpeta "Descargas" de tu ordenador. 
```python
folder_of_download = "/Users/yarel/Downloads/"
```

Los datos que descarga son los correspondientes a Ocupación Hospitalaria a nivel estatal y a nivel Unidad Médica ya que la SSa publica los porcentajes con redondeos y no coinciden los cálculos a nivel UM comparando con los totales a nivel Estatal.

[Lee más aqui](https://serendipia.digital/covid-19/datos-sobre-ocupacion-hospitalaria-en-mexico-no-son-replicables/)

También puedes encontrar todos los datos descargados hasta la fecha y los concentrados para su análisis [aquí](https://archivos.serendipiadata.com/ocupacion/)

## Descarga de datos via chromedriver

Si deseas descargar los datos por ti misma, el archivo `descarga_datos.py` contiene el webscrapper para entrar al portal y bajar los datos de manera automática. 

Esta versión de script descarga en memoria cache la última versión de `chromedriver` ([más información](https://chromedriver.chromium.org)). Necesitas conocer la versión de Crome que tienes instalada en tu ordenador y colocar la version en las siguientes lineas:

```python
driver = webdriver.Chrome(ChromeDriverManager(version="91.0.4472.19").install(), options=option)
driver.get("https://www.google.com")
```

donde `driver` es el controlador necesario para la descarga con Chrome. Para seleccionar las fechas de descarga:  `descargar_desde`y `descargar_hasta` son las fechas en formato `año-mes-día`. 

**Ojo** Se recomeinda decargar por rangos cortos de fechas para evitar errores en carga. 


---
Actualizado agosto 2022 por [Marco2309](https://github.com/Marco2309) 💻

Modificado 2021 por [Yarelosa](https://github.com/Yarelosa) 😊
