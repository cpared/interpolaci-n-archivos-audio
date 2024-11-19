import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import time

MAX_SAMPLES = 100
DEC = 7
FRECUENCY = 20
FILE_NAME = "audio_data.csv"

# Funcion de grilla de la catedra
def grilla(n, t):
    if (n == 0):
       n_en_grilla = 0
    elif (t == 0):
        n_en_grilla = n
    else:
        n_signo = np.sign(n)
        n_abs = np.abs(n)
        corrimiento = np.log10(n_abs)
        corrimiento = np.fix(corrimiento) + 1
        n_en_grilla = n_abs + 0.5 * 10 ** (corrimiento - t)
        n_en_grilla = np.fix(n_en_grilla * 10 ** (t - corrimiento))
        n_en_grilla = n_signo * n_en_grilla * 10 ** (corrimiento - t)
    
    return n_en_grilla    

def generate_audio_file():
    """
        Genera un archivo CSV con una onda senoidal con valores nulos
        para simular huecos en la señal.

        La cantidad de muestras generadas está dada por la variable MAX_SAMPLES
        y la frecuencia de la onda senoidal está dada por la variable FRECUENCY.
    """
    samples = np.arange(MAX_SAMPLES)
    amplitudes = np.sin(2 * np.pi * samples / FRECUENCY)

    # Introducir valores nulos para simular huecos
    amplitudes[10:30] = np.nan

    # Guardar como archivo CSV
    with open(FILE_NAME, "w") as f:
        f.write("Sample,Amplitude\n")  # Header
        for sample, amplitude in zip(samples, amplitudes):
            f.write(f"{sample},{amplitude}\n")

def load_audio_file():
    """
        Carga el archivo CSV generado con la función generate_audio_file
        y retorna dos listas: samples y amplitudes.

        PRE CONDICION: El archivo debe tener la estructura 'Sample,Amplitude' en la primera línea.

        Retorna:
        - samples: Lista de muestras.
        - amplitudes: Lista de amplitudes.
    """
    samples = []
    amplitudes = []
    with open(FILE_NAME, "r") as file:
        next(file)  # Omitir el header
        for line in file:
            sample, amplitude = line.strip().split(',')
            g_amplitude = grilla(float(amplitude), DEC)  # Aplico la grilla de la cátedra
            samples.append(int(sample))
            amplitudes.append(float(g_amplitude))
    return samples, amplitudes

def interpolate(samples, amplitudes, kind):
    """
        Realiza una interpolación sobre los valores de amplitudes. Imprime el tiempo de ejecución.

        POST CONDICION: Se modifican los valores interpolados en amplitudes.

        Parámetros:
        - samples: Lista de muestras.
        - amplitudes: Lista de amplitudes.
        - kind: Tipo de interpolación a realizar. Puede ser 'linear', 'quadratic' o 'cubic'.

    """
    start_time = time.time()
    valid_samples, valid_amplitudes = get_valid_values(samples, amplitudes)

    # Crear la función de interpolación
    interp_func = interp1d(valid_samples, valid_amplitudes, kind=kind, fill_value="extrapolate")

    for i in range(len(amplitudes)):
        if np.isnan(amplitudes[i]):
            amplitudes[i] = interp_func(samples[i])

    print(f"--- {time.time() - start_time} seconds ---")

def get_valid_values(samples, amplitudes):
    """
        Retorna las muestras y amplitudes válidas (no nulas).

        Parámetros:
        - samples: Lista de muestras.
        - amplitudes: Lista de amplitudes.
    """
    valid_samples = [s for s, a in zip(samples, amplitudes) if not np.isnan(a)]
    valid_amplitudes = [a for a in amplitudes if not np.isnan(a)]
    return valid_samples, valid_amplitudes

def request_interpolation_method(samples, amplitudes):
    """
        Solicita al usuario el método de interpolación a utilizar.

        Parámetros:
        - samples: Lista de muestras.
        - amplitudes: Lista de amplitudes.
    """
    print("Seleccione el método de interpolación:")
    print("1. Lineal")
    print("2. Polinómica")
    print("3. Spline")
    method = input("Ingrese el número correspondiente al método: ")

    if method == '1':
        interpolate(samples, amplitudes, kind='linear')
        return "Interpolación lineal"
    elif method == '2':
        interpolate(samples, amplitudes, kind='quadratic')
        return "Interpolación polinómica"
    elif method == '3':
        interpolate(samples, amplitudes, kind='cubic')
        return "Interpolación spline"
    else:
        print("Método no válido")
        return "Interpolación no realizada"
    
def print_results(samples, amplitudes, text):
    """
        Grafica los datos interpolados.

        Parámetros:
        - samples: Lista de muestras.
        - amplitudes: Lista de amplitudes.
        - text: Texto a mostrar en el título del gráfico.
    """

    plt.plot(samples, amplitudes, '-x')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.title(text)
    plt.legend(['Original', 'Interpolado'], loc='lower right')
    plt.grid()
    plt.show()

def main():
    # Generar y cargar datos
    generate_audio_file()
    samples, amplitudes = load_audio_file()

    # Graficar los datos originales
    plt.plot(samples, amplitudes, 'o')

    # Aplico Interpolación
    text = request_interpolation_method(samples, amplitudes)

    # Graficar los datos interpolados
    print_results(samples, amplitudes, text)

main()
