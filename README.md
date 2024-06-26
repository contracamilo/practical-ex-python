# ACTIVIDAD 4: Taller: Ejercicios prácticos en Phyton

## Descripción
Este proyecto es una colección de ejercicios implementados en Python para demostrar el uso de diferentes patrones de diseño de software. Cada patrón se presenta como un subprograma independiente dentro de la estructura del proyecto.

## Patrones de Diseño Implementados
- **Singleton**:  Se implemento un ejemplo para gestionar una única instancia de conexión a la base de datos.
- **Abstract Factory**:  Se implemento una fábrica para crear instituciones públicas y privadas.
- **Adapter**: Proporciona una interfaz para traducir textos entre diferentes idiomas.
- **Decorator**: Se creo funcionalidad que permite crear Helados y controlar los topings y salsas aplicados.
- **Observer**: Se implemento un ejemplo que notifica sobre cambios de precios en un producto

## Estructura del Proyecto
```
.
├── README.md
├── abstract_factory
│   ├── CreateInstitutionInterfaces.py
│   ├── Institution.py
│   ├── __init__.py
├── adapter
│   ├── TranslationInterface.py
│   ├── TranslatorAdapter.py
│   ├── __init__.py
├── decorator
│   ├── IceCream.py
│   ├── IceCreamDecorators.py
│   ├── __init__.py
├── main.py
├── observer
│   ├── Observer.py
│   ├── PriceAlert.py
│   ├── Product.py
│   ├── Subject.py
│   ├── __init__.py
│   └── helpers.py
├── requirements.txt
└── singleton
    ├── DatabaseConnection.py
    ├── FakeConnect.py
    ├── __init__.py
```

## Cómo Utilizar
Ejecute el main.py y siga las instrucciones del menu en la consola.

<img width="495" alt="Screenshot 2024-03-31 at 4 59 42 PM" src="https://github.com/contracamilo/practical-ex-python/assets/27745159/69bbeef4-6a76-4438-9eac-7fa37e6c06ff">

## Requisitos
Asegúrese de tener instalado Python 3.6 o superior. Todas las dependencias requeridas se encuentran en `requirements.txt`. Instálelas usando el siguiente comando:

```bash
pip install -r requirements.txt
```

