## 📊 Calculadora en Python

Este proyecto es una calculadora básica desarrollada en Python, pensada como ejemplo práctico para implementar Integración Continua (CI) usando Jenkins. Incluye operaciones matemáticas fundamentales y pruebas unitarias para verificar su correcto funcionamiento.

# ✨ Funcionalidades

✅ Suma

✅ Resta

✅ Multiplicación

✅ División (incluye manejo de división por cero)

# ▶️ Cómo Usar

Para ejecutar la calculadora desde la terminal:

```bash
python3 calculadora.py
```

# 🧪 Ejecutar Pruebas

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

# ⚙️ Configuración del Pipeline en Jenkins

Paso 1: Crear el Proyecto
En Jenkins, crea un nuevo proyecto del tipo Pipeline.

Copia el contenido del archivo Jenkinsfile en la sección de definición del pipeline.

Guarda y aplica los cambios.

Paso 2: Webhook desde GitHub
Payload URL: http://<TU_IP_O_DOMINIO>:8080/github-webhook/

Content type: application/json

Eventos: Solo push

# 🔍 Comprobación de Fallos

Puedes probar el sistema introduciendo errores intencionales en operaciones.py para confirmar que Jenkins detecta correctamente los fallos en la ejecución de las pruebas.

