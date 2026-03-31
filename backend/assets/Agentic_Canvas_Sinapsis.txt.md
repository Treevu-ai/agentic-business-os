# 🧬 Agentic Canvas: Pasos del Workshop

FASE 1: Identificación del Proceso (50 min)

Paso 1.1 — Listar procesos candidatos (8 min)
- Escribir 3 post-its con procesos dolorosos
- Clasificar cada uno: 🔴 Crítico | 🟡 Frecuente | 🟢 Tedioso

Paso 1.2 — Votación grupal (12 min)
- Pegar los 9 post-its en la pared
- Votar: 2 votos por persona
- Seleccionar el ganador por votos

Paso 1.3 — Validación (5 min)
- Verificar: ¿Ocurre ≥1 vez al día o ≥5 a la semana?
- Verificar: ¿Es 80% repetitivo?
- Verificar: ¿Consume >3 horas/semana o genera errores >$500/mes?

Paso 1.4 — Completar Canvas Fase 1 (25 min)

Campo | Tu respuesta
Nombre | 
Frecuencia | 
Interacción Humana | 

---

FASE 2: Deconstrucción Lógica (55 min)

Paso 2.1 — Definir Trigger (10 min)
- ¿Qué evento inicia el proceso? (email, webhook, schedule, cambio en base de datos)
- Describir condición exacta del trigger

Tu Trigger | 
Tipo | 
Condición específica | 

Paso 2.2 — Mapear Herramientas (10 min)
- ¿De dónde LEE el agente?
- ¿Dónde ESCRIBE el agente?
- ¿Qué formato tienen los datos?

Tu Herramienta | 
Lee de | 
Escribe en | 
Formato datos | 

Paso 2.3 — Diseñar Filtro de IA (10 min)
- Convertir decisión humana en regla binaria
- Máximo 2-3 condiciones

SI _________________________________________________
Y __________________________________________________
ENTONCES ___________________________________________

SI NO SI ____________________________________________
ENTONCES ___________________________________________

SI NINGUNA __________________________________________
ENTONCES ___________________________________________

Paso 2.4 — Storyboard del flujo (25 min)
- Dibujar 3-6 pasos del proceso
- Cada paso = trigger → herramienta → filtro → acción

---

BREAK (15 min)

---

FASE 3: Diseñando el Agente (50 min)

Paso 3.1 — Definir Identidad (5 min)

Elemento | Tu respuesta
Nombre del Agente | 
Rol funcional (1 oración) | 
Tono (3 adjetivos) | 
Avatar mental | 

Paso 3.2 — Escribir Instrucción 1: Rol y Contexto (4 min)

Eres [Nombre], [rol funcional].
Tu propósito es [objetivo en una oración].

CONTEXTO DE NEGOCIO:
• Trabajas en [empresa/industria]
• Tus usuarios son [quién se beneficia]
• El proceso ocurre [frecuencia]
• Actualmente consume [tiempo] y genera [problema]

HERRAMIENTAS:
• Recibes información de: [trigger + herramienta]
• Consultas datos en: [herramientas]
• Ejecutas acciones en: [herramientas]

RESTRICCIÓN:
• Tú NO haces: [límites]
• Tú SÍ haces: [responsabilidad]

Paso 3.3 — Escribir Instrucción 2: Lógica de Decisión (4 min)

CUANDO [trigger específico], SIGUE ESTE PROTOCOLO:

PASO 1: EXTRACCIÓN
• Obtén: [lista datos obligatorios]
• Si falta alguno: [acción]

PASO 2: CONSULTA
• Busca en [herramienta] usando [campo clave]
• Si no encuentras: [acción alternativa]

PASO 3: EVALUACIÓN
• Aplica: [copiar Filtro de IA de Fase 2]

PASO 4: EJECUCIÓN
• Si [Condición A]: [Acción 1], [Acción 2]
• Si [Condición B]: [Acción 3], [Acción 4]
• Si [duda]: [escalación]

Paso 3.4 — Escribir Instrucción 3: Output y Formato (4 min)

PARA CADA EJECUCIÓN, GENERA:

1. RESUMEN INTERNO (logs):
   • Proceso: [nombre]
   • Trigger: [fecha/hora + ID]
   • Decisión: [A/B/C]
   • Confianza: [Alta/Media/Baja]

2. OUTPUT PRINCIPAL:
   • Formato: [Email/JSON/Nota/Ticket]
   • Destinatario: [quién]
   • Contenido obligatorio: [elementos]
   • Tono: [descripción]

3. NOTIFICACIÓN SECUNDARIA (si aplica):
   • A: [stakeholder]
   • Cuándo: [inmediato/diario/excepción]
   • Formato: [breve/alerta/dashboard]

REGLAS:
• Siempre verifica [X] antes de completar
• Nunca [acción prohibida]
• En caso de error: [protocolo]

Paso 3.5 — Peer Review (12 min)
- Intercambiar prompts con compañero
- Evaluar con rúbrica:
  - ¿Rol claro?
  - ¿Herramientas listadas?
  - ¿Trigger específico?
  - ¿Filtro binario?
  - ¿Acciones concretas?
  - ¿Output medible?
  - ¿Tono definido?

Paso 3.6 — Iteración (6 min)
- Ajustar según feedback recibido
- Revisar coherencia con Canvas Fase 2

---

CIERRE: Compromiso de Acción (10 min)

Paso C.1 — Presentación 60 segundos
1. "Automatizamos [proceso] — ahorra [X horas/semana]"
2. "Nuestro agente se llama [nombre], es [rol]"
3. "Esta semana construimos [componente específico]"

Paso C.2 — Entregable
- Foto del Canvas completo (3 fases)
- Fecha de primera prueba: ___________
- Responsable: ___________

---
*Sinapsis OS // Workshop Material*
