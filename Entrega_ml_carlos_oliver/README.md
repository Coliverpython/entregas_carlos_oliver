# Predicción de Retrasos en Transacciones

Este repositorio contiene el código para predecir los días de retraso en transacciones utilizando diferentes técnicas de preprocesamiento de datos y modelos de machine learning.

## Descripción

El objetivo de este proyecto es procesar un conjunto de datos de transacciones, limpiarlos, realizar un análisis exploratorio de datos y construir modelos de machine learning para predecir el tiempo de retraso de las transacciones. El código incluye pasos para la limpieza de datos, ingeniería de características, entrenamiento de modelos y evaluación de los mismos.

## Estructura del Repositorio

- `preprocesamiento.py`: Código para la limpieza y transformación de los datos.
- `entrenamiento_modelos.py`: Código para el entrenamiento y evaluación de los modelos.
- `predicciones.py`: Código para realizar predicciones con el modelo entrenado.
- `label_encoders.pkl`: Archivo que guarda los `LabelEncoders` usados en el preprocesamiento.
- `scaler.pkl`: Archivo que guarda el `MinMaxScaler` usado en el preprocesamiento.
- `best_model.pkl`: Archivo que guarda el mejor modelo entrenado.

## Dependencias

Asegúrate de tener instaladas las siguientes librerías antes de ejecutar el código:

```sh
pip install pandas numpy scikit-learn joblib matplotlib seaborn xgboost lightgbm
```

## Uso

### Preprocesamiento de Datos

El archivo `preprocesamiento.py` contiene el código necesario para limpiar y transformar los datos de entrada. Aquí se detallan algunos de los pasos realizados:

1. **Conversión de Fechas**: Convertir las columnas `estimate_arrival_date` y `complete_date` a formato de fecha desde enteros.
2. **Cálculo de Retrasos**: Calcular el tiempo de retraso entre `complete_date` y `estimate_arrival_date`.
3. **Filtrado de Datos**: Eliminar valores atípicos basados en un rango razonable de tiempo de retraso (1 a 30 días).
4. **Eliminación de Columnas Innecesarias**: Eliminar columnas que no son relevantes para el modelo.
5. **Codificación de Variables Categóricas**: Usar `LabelEncoder` para transformar las variables categóricas.
6. **Escalado de Variables Numéricas**: Aplicar `MinMaxScaler` para normalizar las variables numéricas.

### Entrenamiento de Modelos

El archivo `entrenamiento_modelos.py` incluye el código para entrenar y evaluar diferentes modelos de machine learning:

1. **División de Datos**: Dividir los datos en conjuntos de entrenamiento y prueba.
2. **Definición de Modelos y Parámetros**: Configurar un `Pipeline` y usar `GridSearchCV` para encontrar los mejores parámetros.
3. **Entrenamiento y Evaluación**: Entrenar los modelos y evaluar su precisión.
4. **Guardado del Mejor Modelo**: Guardar el mejor modelo encontrado con `joblib`.

### Predicción

El archivo `predicciones.py` proporciona un ejemplo de cómo usar el modelo entrenado para hacer predicciones en nuevos datos:

1. **Cargar el Modelo**: Cargar el modelo guardado desde `best_model.pkl`.
2. **Preparar los Datos**: Crear un `DataFrame` con los datos nuevos para la predicción.
3. **Realizar Predicciones**: Usar el modelo para predecir los días de retraso.

## Ejecución

### Preprocesamiento

```sh
python preprocesamiento.py
```

### Entrenamiento de Modelos

```sh
python entrenamiento_modelos.py
```

### Predicción

```sh
python predicciones.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor realiza un fork del repositorio, crea una nueva rama con tus cambios y envía un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

Este README proporciona una guía clara sobre cómo usar y contribuir a este proyecto, y resume el flujo de trabajo y los archivos principales involucrados en el procesamiento y predicción de retrasos en transacciones.