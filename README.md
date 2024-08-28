# GalacticShooter
# Mi Juego en Python

¡Bienvenido a mi proyecto de juego en Python! Este juego está desarrollado utilizando Pygame y algunas otras dependencias que se detallan a continuación. Sigue las instrucciones para clonar el repositorio e instalar todas las dependencias necesarias para ejecutar el juego.

## Requisitos

- Python 3.6 o superior
- Pip (administrador de paquetes de Python)

## Instalación

Sigue estos pasos para clonar el repositorio e instalar las dependencias necesarias:

1. **Clonar el repositorio:**

   Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:

   ```bash
   git clone https://github.com/JulioMarquezH/GalacticShooter.git
   ```

2. **Crear y activar un entorno virtual (opcional, pero recomendado):**

    - Crear un entorno virtual te ayudará a mantener las dependencias de tu proyecto separadas de otras dependencias en tu sistema. Puedes crear y activar un entorno virtual con los siguientes comandos:

    - En sistemas Unix o MacOS:
       ```bash
        python3 -m venv venv
        source venv/bin/activate
       ```

    - En Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3. **Instalar las dependencias:**

    - Una vez que estés en el directorio del proyecto y hayas activado el entorno virtual (si decidiste crear uno), instala las dependencias utilizando pip:
        ```bash
        pip install -r requirements.txt
        ```

4. **Ejecutar el juego:**
    - Después de instalar las dependencias, puedes ejecutar el juego con el siguiente comando:
        ```bash
        python index.py
        ```

## Modos de Juego

Al iniciar el juego, se te presentará una opción para elegir entre dos modalidades de juego:

1. **Un Jugador**: Controla un solo personaje y enfrenta a los enemigos mientras avanzas por el nivel.
2. **Dos Jugadores**: Dos jugadores pueden jugar en el mismo dispositivo, controlando cada uno a su propio personaje y cooperando para derrotar a los enemigos.

### Controles del Juego

- **Jugador 1**:
  - **Moverse**: Usa las teclas **W** (arriba), **A** (izquierda), **S** (abajo), **D** (derecha).
  - **Atacar**: Presiona la tecla **Espacio** para atacar.

- **Jugador 2**:
  - **Moverse**: Usa las teclas de flecha **↑** (arriba), **←** (izquierda), **↓** (abajo), **→** (derecha).
  - **Atacar**: Presiona la tecla **-** (guión) para atacar.

### Reglas del Juego

- Cada jugador comienza con **3 vidas**.
- Los jugadores pierden una vida cada vez que chocan con un enemigo.
- El juego termina cuando ambos jugadores han perdido todas sus vidas.

¡Buena suerte y diviértete jugando!
