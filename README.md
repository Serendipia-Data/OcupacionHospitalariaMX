# HospitalizacionesCOVIDMX

El presente repositorio contiene los datos de capacidad hospitalaria divulgados por la Secretaría de Salud a través del portal de la UNAM
[https://www.gits.igg.unam.mx/red-irag-dashboard/reviewHome#](https://www.gits.igg.unam.mx/red-irag-dashboard/reviewHome#)

# Primera versión de script
Información de ocupación hospitalaria en México, Secretaría de Salud. Obtenidas en su mayoría a través de [CapacidadHospitalariaMX: por @RodrigoZepeda](https://github.com/RodrigoZepeda/CapacidadHospitalariaMX)

## Datos
Los datos descargados están en la carpeta especificada en la linea 18, actualmente la carpeta "Descargas" de tu ordenador. 

## Descarga de datos via chromedriver

Si deseas descargar los datos por ti misma, el archivo `descarga_datos.py` contiene el webscrapper para entrar al portal y bajar los datos de manera automática. 

Esta versión de script descarga en memoria cache la última versión de `chromedriver` ([más información](https://chromedriver.chromium.org)). Necesitas conocer la versión de Crome que tienes instalada en tu ordenador y colocar la version en las siguientes lineas:

```python
driver = webdriver.Chrome(ChromeDriverManager(version="91.0.4472.19").install(), options=option)
driver.get("https://www.google.com")
```

donde `driver` es el controlador necesario para la descarga con Chrome. Para seleccionar las fechas de descarga:  `descargar_desde`y `descargar_hasta` son las fechas en formato `año-mes-día`r. 

**Ojo** Se recomeinda decargar por rangos cortos de fechas para evitar errores en carga. 


---
Modificado por [Yarelosa](https://github.com/Yarelosa) 😊
