#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on December 2020

@author: Rodrigo Zepeda
"""


import pandas as pd
import os
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


folder_of_download = "/Users/elledriver/Downloads/"
dia_i = input("Dia1 : ")
mes_i = input("Mes1 : ")
dia_f = input("Dia2 : ")
mes_f = input("Mes2 : ")
if dia_f == '':
    dia_f = dia_i
if mes_f == '':
    mes_f = mes_i
descargar_desde = f"2023-{mes_i}-{dia_i}"
descargar_hasta = f"2023-{mes_f}-{dia_f}"
print('descargar_desde', descargar_desde)
print('descargar_hasta', descargar_hasta)
sleep_first = 20
sleep_time = 50  # Tiempo que tarda la página de la UNAM de cambiar ventana
download_time = 10  # Tiempo que tarda en descargarse el archivo en tu red
option = webdriver.ChromeOptions()
option.add_argument("-incognito")

option.add_experimental_option("prefs", {
    "download.default_directory": folder_of_download,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
})
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=option)
browser.set_window_size(1000, 1000)
browser.get("https://www.gits.igg.unam.mx/red-irag-dashboard/reviewHome#")
# Dar click en entrar
time.sleep(sleep_first)
browser.find_element(By.ID, "enter-button").click()

# Fechas a descargar
fechas_descargar = pd.date_range(
    start=descargar_desde, end=descargar_hasta, freq='D')
fechas_descargar = fechas_descargar.strftime('%Y-%m-%d')
fechas_descargar = fechas_descargar[::-1]

# Impresión de tiempo estimado
print("Tiempo estimado: " + str(len(fechas_descargar) *
      (sleep_time*4 + 4*download_time)/360) + " horas")

# Elementos de resumen, ocupación general, camas y uci
resumen = browser.find_element(
    "xpath", "/html/body/section/section[2]/div[1]/nav/ul/li[1]/a")
hospital = browser.find_element(
    "xpath", "/html/body/section/section[2]/div[1]/nav/ul/li[5]/a")
ventilador = browser.find_element(
    "xpath", "/html/body/section/section[2]/div[1]/nav/ul/li[6]/a")
uci = browser.find_element(
    "xpath", "/html/body/section/section[2]/div[1]/nav/ul/li[7]/a")

# Avance para cuantificar
avance = 0

for fecha_analisis in fechas_descargar:

    print("Descargando " + str(100*avance/len(fechas_descargar)) + "%")
    avance = avance + 1

    # Asegurarnos que estamos en la sección resumen
    resumen.click()
    time.sleep(sleep_first)

    select = Select(browser.find_element(By.ID, "dateSelected"))
    select.select_by_visible_text(fecha_analisis)
    time.sleep(download_time)

    # --------------------------------
    # HOSPITALIZACIONES
    # --------------------------------

    hospital.click()
    time.sleep(sleep_time)

    # --- descarga a nivel unidad médica ---
    browser.find_element(
        "xpath", "/html/body/section/section[2]/div[2]/section/article[2]/article/div[1]/div/div[5]/div/div[1]/button[1]").click()

    newname = "Hospitalizaciones_" + fecha_analisis + "_UM.csv"
    time.sleep(download_time)
    os.rename(os.path.join(folder_of_download, "Sistema de Información de la Red IRAG.csv"),
              os.path.join(folder_of_download, newname))

    # --- descarga a nivel unidad Estatal ---
    browser.find_element(
        "xpath", "/html/body/section/section[2]/div[2]/section/article[2]/article/div[1]/nav/ul/li[1]/a").click()
    time.sleep(sleep_first)
    browser.find_element(
        "xpath", "/html/body/section/section[2]/div[2]/section/article[2]/article/div[1]/div/div[2]/div/div[1]/button[1]").click()

    newname = "Hospitalizaciones_" + fecha_analisis + ".csv"
    time.sleep(download_time)
    os.rename(os.path.join(folder_of_download, "Sistema de Información de la Red IRAG.csv"),
              os.path.join(folder_of_download, newname))

    # --------------------------------
    # VENTILADORES
    # --------------------------------

    ventilador.click()
    time.sleep(sleep_time)

    # --- descarga a nivel unidad médica ---
    browser.find_element(
        "xpath", "/html/body/section/section[2]/div[2]/section/article[2]/article/div[1]/div/div[5]/div/div[1]/button[1]").click()

    newname = "Ventiladores_" + fecha_analisis + "_UM.csv"
    time.sleep(download_time)
    os.rename(os.path.join(folder_of_download, "Sistema de Información de la Red IRAG.csv"),
              os.path.join(folder_of_download, newname))

    # --- descarga a nivel unidad Estatal ---
    browser.find_element(
        "xpath", "/html/body/section/section[2]/div[2]/section/article[2]/article/div[1]/nav/ul/li[1]/a").click()
    time.sleep(sleep_first)
    browser.find_element(
        "xpath", "/html/body/section/section[2]/div[2]/section/article[2]/article/div[1]/div/div[2]/div/div[1]/button[1]").click()

    newname = "Ventiladores_" + fecha_analisis + ".csv"
    time.sleep(download_time)
    os.rename(os.path.join(folder_of_download, "Sistema de Información de la Red IRAG.csv"),
              os.path.join(folder_of_download, newname))

    # --------------------------------
    # UCI
    # --------------------------------

    uci.click()
    time.sleep(sleep_time)

    # --- descarga a nivel unidad médica ---
    browser.find_element(
        "xpath", "/html/body/section/section[2]/div[2]/section/article[2]/article/div[1]/div/div[5]/div/div[1]/button[1]").click()

    newname = "UCI_" + fecha_analisis + "_UM.csv"
    time.sleep(download_time)
    os.rename(os.path.join(folder_of_download, "Sistema de Información de la Red IRAG.csv"),
              os.path.join(folder_of_download, newname))

    # --- descarga a nivel unidad Estatal ---
    browser.find_element(
        "xpath", "/html/body/section/section[2]/div[2]/section/article[2]/article/div[1]/nav/ul/li[1]/a").click()
    time.sleep(sleep_first)
    browser.find_element(
        "xpath", "/html/body/section/section[2]/div[2]/section/article[2]/article/div[1]/div/div[2]/div/div[1]/button[1]").click()

    newname = "UCI_" + fecha_analisis + ".csv"
    time.sleep(download_time)
    os.rename(os.path.join(folder_of_download, "Sistema de Información de la Red IRAG.csv"),
              os.path.join(folder_of_download, newname))

browser.quit()
os.system('say "Descarga de datos finalizada"')
