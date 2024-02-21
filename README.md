# Globaltek Technical Test
Este repositorio contiene las soluciones de una serie de ejercicios provisionados por Globaltek. No se utilizó ningún paquete de terceros o bibliotecas externas, solo el módulo __sys__ integrado con Python.

## Archivos Incluidos
1. Ejercicio 1: [`ejercicio1.py`](/exercise1.py)
   - Escriba una función que retorne la suma de una serie de X número repetido hasta el n-ésimo término
2. Ejercicio 2: [`ejercicio2.py`](/exercise2.py)
   - Escriba una función que retorne en una lista de salida, solo aquellos números de una lista de entrada que satisfagan las siguientes condiciones:
     1. El número debe ser divisible por cinco.
     2. Si el número es mayor que 600, no se incluye en la salida.
     3. Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado.
3. Ejercicio 3: [`ejercicio3.py`](/exercise3.py)
   - Dada una lista de cualquier longitud de entrada, escriba una función para agrupar los elementos similares en una matriz de salida (no importa el orden).
4. Ejercicio 4: [`ejercicio4.py`](/exercise4.py)
   - En un negocio reciben periódicamente productos para la venta, se requiere desarrollar un programa de consola (o terminal) que cumpla con los siguientes requerimientos:
     1. Se requiere organizar el inventario en los siguientes grupos: **dairy**, **cleaning** y **grain**
     2. Cada grupo tiene que estar asociado a un elemento de otra lista que almacena las existencias de ese grupo en la misma posición, como en el siguiente ejemplo:
        ```python
        dairy_products = ["Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
        dairy_stock = [28, 36, 50]
        ```
        En donde, por ejemplo, el producto del grupo dairy “Alta Dena Milk” tiene una existencia de 36 unidades.
     3. Para un producto entrante, se debe poder registrar en el sistema: el nombre del producto, la cantidad y el grupo al que pertenece.
     4. Si el producto no existe en la lista, se debe agregar al final con su cantidad entrante, pero si existe se debe actualizar el número de existencias sumando la nueva cantidad.
     5. El programa debe permitir visualizar todo el inventario de productos y existencias. <br> <br>
        Ejemplo de menú de inicio del programa: <br>
        ![image](https://github.com/Gabenx/GlobaltekTechnicalTest/assets/70778743/1e7dcae8-2b63-49fb-8d74-6401c0007978) <br><br>
        Ejemplo de Reporte de Inventario: <br>
        ![image](https://github.com/Gabenx/GlobaltekTechnicalTest/assets/70778743/c7cff80e-b822-4c61-8742-78184b48849f)

## Uso 

1. Clone el repositorio a su máquina local utilizando el siguiente comando:
   ```bash
   git clone https://github.com/Gabenx/GlobaltekTechnicalTest.git
   ```
2. Abra el directorio clonado utilizando una herramienta como Visual Studio Code
3. Abra y pruebe cada programa .py según corresponda, siguiendo las siguientes instrucciones:
   * Para el caso del [`ejercicio1.py`](/exercise1.py) se debe utilizar el siguiente comando en la terminal:
     ```python
     python exercise1.py num rep
     ```
     En donde __num__ corresponde al número a sumar y __rep__ a la cantidad de repeticiones, por ejemplo:
     ```python
     python exercise1.py 3 5
     ```
     Tendría un resultado de 37035.
     
   * Para los ejercicios [`ejercicio2.py`](/exercise2.py) y [`ejercicio3.py`](/exercise3.py) se debe utilizar uno de los siguientes comandos en la terminal según corresponda:
     ```python
     python exercise2.py
     ```
     ```python
     python exercise3.py
     ```
     Y al momento de introducir los números que conformarán la lista, es necesario separarlos por un espacio, como se muestra en la imagen: <br>
     ![image](https://github.com/Gabenx/GlobaltekTechnicalTest/assets/70778743/0d744c01-d93b-4b34-89c0-2c1494c76dbc)

   *Para el ejercicio [`ejercicio4.py`](/exercise4.py) se debe utilizar el siguiente comando:
    ```python
     python exercise4.py
     ```
    A partir de allí, se podrá interactuar con el menú provisionado normalmente.

## Licencia
  [MIT](https://choosealicense.com/licenses/mit/)
    
    
