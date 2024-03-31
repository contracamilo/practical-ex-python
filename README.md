# Proyecto de Patrones de Diseño en Python

## Descripción
Este proyecto es una colección de ejercicios implementados en Python para demostrar el uso de diferentes patrones de diseño de software. Cada patrón se presenta como un subprograma independiente dentro de la estructura del proyecto.

## Patrones de Diseño Implementados
- **Singleton**: Utilizado para gestionar una única instancia de conexión a la base de datos.
- **Abstract Factory**: Implementa una fábrica para crear instituciones públicas y privadas.
- **Adapter**: Proporciona una interfaz para traducir textos entre diferentes idiomas.
- **Decorator**: Permite agregar funcionalidades adicionales a objetos de platos de comida.
- **Observer**: Usado para implementar un sistema de eventos y notificaciones.

## Estructura del Proyecto
```
.
├── README.md
├── abstract_factory
├── adapter
├── decorator
├── main.py
├── observer
├── requirements.txt
└── singleton
    ├── DatabaseConnection.py
    ├── FakeConnect.py
    ├── __init__.py
    └── __pycache__
        ├── DatabaseConnection.cpython-311.pyc
        ├── FakeConnect.cpython-311.pyc
        └── __init__.cpython-311.pyc
```

## Cómo Utilizar
Para ejecutar los ejemplos de cada patrón de diseño, navegue al directorio del patrón correspondiente y ejecute el script Python. Por ejemplo, para el patrón Singleton:

```bash
cd singleton
python database_connection.py
```

## Requisitos
Asegúrese de tener instalado Python 3.6 o superior. Todas las dependencias requeridas se encuentran en `requirements.txt`. Instálelas usando el siguiente comando:

```bash
pip install -r requirements.txt
```

