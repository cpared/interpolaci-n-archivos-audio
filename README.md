# Interpolación de Datos de Audio

Este proyecto implementa un flujo completo para la generación, carga, interpolación y visualización de datos de audio con huecos en las muestras. Utiliza bibliotecas como NumPy, Matplotlib y SciPy para el procesamiento y visualización.

## Descripción

El objetivo principal de este programa es simular un archivo de datos de audio con valores ausentes (representados como `NaN`) y aplicar técnicas de interpolación para estimar los valores faltantes. Esto es útil en aplicaciones donde la recuperación de señales incompletas es crítica.

### Funcionalidades Principales

1. **Generación de Datos**: Crea un archivo CSV con una onda senoidal, introduciendo huecos simulados en un rango de muestras.
2. **Carga de Datos**: Lee el archivo generado y procesa los valores utilizando una grilla personalizada para redondear los valores.
3. **Interpolación**: Estima los valores faltantes mediante métodos de interpolación como:
   - Lineal
   - Polinómica
   - Spline
4. **Visualización**: Grafica los datos originales e interpolados para evaluar el resultado.

---

## Uso 

1. Ejecute el programa principal:

```python
python main.py
```

2. El programa generará un archivo CSV `(audio_data.csv)` con las muestras y amplitudes de una onda senoidal.

3. A continuación, se le solicitará seleccionar un método de interpolación:

    * 1 para interpolación lineal
    * 2 para interpolación polinómica
    * 3 para interpolación spline

4. Finalmente, se mostrará un gráfico comparando los valores originales con los interpolados.

![alt text](<Screenshot from 2024-11-19 00-14-05.png>)


---

## Requisitos

- Python 3.7+
- Bibliotecas:
  - `numpy`
  - `matplotlib`
  - `scipy`

Para instalar las bibliotecas necesarias, ejecute:

```bash
pip install numpy matplotlib scipy
```

## Bibliografia

https://recoverit.wondershare.es/audio-repair/what-is-dithering-audio.html#:~:text=Conocer%20la%20interpolaci%C3%B3n%20es%20importante,por%20un%20error%20de%20cuantificaci%C3%B3n.

---

## Créditos
Este proyecto fue desarrollado para demostrar técnicas de recuperación de datos en señales incompletas mediante interpolación. El concepto de grilla fue adaptado de un modelo proporcionado por la cátedra de la materia Modelacion Numerica de la Universidad de Buenos Aires.