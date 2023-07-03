import requests
import json

url = 'http://127.0.0.1:10000'
#url = 'https://mail-gpt-automation.onrender.com/'
  # Cambia esto a la URL de tu API si no es esta
data = {

    "content": """
    

Contactar cgutierrez.infor@gmail.com www.linkedin.com/in/ cristiangutierrez-ds (LinkedIn) github.com/cristian-data-science (Personal) Aptitudes principales Resolución de problemas Capacidad de análisis Visualización de datos Certifications Escuela de Data Science e Inteligencia Artificial Google Data Analytics Certificate Querying Data with Transact-SQLCristian Gutierrez Business Analyst en Patagonia | Máster en Data Science y Big Data | Optimizando negocios a través de la tecnología Chile Extracto Ingeniero de sistemas apasionado por el data science y la inteligencia artificial, con experiencia en análisis de datos, automatización de procesos y reportería interactiva. Mis principales objetivos son seguir desarrollando mis habilidades técnicas para ser un científico de datos de primer nivel y utilizar mis conocimientos para contribuir al desarrollo de soluciones sostenibles tanto para el negocio como para nuestro hogar, el planeta tierra. Estoy constantemente buscando nuevas oportunidades de aprendizaje y desarrollo en mi área, y me encanta colaborar con otros profesionales para enfrentar retos y lograr resultados excepcionales Experiencia Patagonia 3 años 10 meses Business analyst & functional support diciembre de 2020 - Present  (2 años 8 meses) Región Metropolitana de Santiago, Chile System and Data Support julio de 2020 - noviembre de 2020  (5 meses) Región Metropolitana de Santiago, Chile System Analyst enero de 2020 - junio de 2020  (6 meses) Región Metropolitana de Santiago, Chile Information Technology Executive octubre de 2019 - diciembre de 2019  (3 meses) Región Metropolitana de Santiago, Chile   Page 1 of 2    Educación IEBS Business School Máster en Data Science y Big Data   · (noviembre de 2022 - noviembre de

CIISA Diplomado, Ciberseguridad Aplicada  · (mayo de 2019 - febrero de 2020) Duoc UC Ingeniería, Redes y Telecomunicaciones  · (2015 - 2018)   Page 2 of 2




"""
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers, auth=('make_ia_auto', '3%6%7dJFDS511'))

print(response.status_code)  # Debería imprimir 200 si todo salió bien
print(response.json())  # Imprime la respuesta de la API
