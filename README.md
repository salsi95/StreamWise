# StreamWise

StreamWise es un sistema de recomendación de películas, series y videojuegos basado en el análisis de su argumento y otros metadatos. Utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) y aprendizaje automático para ofrecer recomendaciones personalizadas.

## Características

- Recomendación basada en el argumento: Análisis de la sinopsis con NLP.

- Metadatos adicionales: Consideración de género, actores, directores y guionistas.

- Base de datos relacional: Gestión eficiente de la información.

- Interfaz intuitiva: Posibilidad de futuras implementaciones en web o app.

## Instalación

### Clona el repositorio:
```python
git clone https://github.com/salsi95/StreamWise.git 
```


### Accede al directorio del proyecto:
```python
cd StreamWise
```

### Crea un entorno virtual (opcional pero recomendado):
```python
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### Instala las dependencias:
```python

pip install -r requirements.txt
```

## Uso

### Ejecuta el script principal:

python main.py

### Sigue las instrucciones en pantalla para ingresar un título y obtener recomendaciones.

## Tecnologías utilizadas

- Python

- NLTK / SpaCy (Procesamiento de Lenguaje Natural)

- Pandas y NumPy (Manejo de datos)

- PostgreSQL (Base de datos)

- Selenium (Scraping de datos)

## Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

Realiza un fork del repositorio.

Crea una nueva rama:
```python
git checkout -b feature-nueva-funcionalidad
```

Realiza tus cambios y haz commit:
```python

git commit -m "Añadir nueva funcionalidad"
```

Envía un pull request.