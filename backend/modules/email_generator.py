class EmailGenerator:
    def __init__(self):
        pass

    def generate_draft(self, contact_name, company_name, sector):
        """
        Generates a personalized email draft using an LLM-style prompt pattern.
        """
        subject = f"Propuesta de Eficiencia Agéntica para {company_name}"
        body = f"""Hola {contact_name},

He estado analizando el sector de {sector} en Perú y he identificado que empresas como {company_name} podrían capturar un margen adicional mediante la automatización de decisiones operativas.

En SINAPSIS INNOVADORA ayudamos a implementar el 'Agentic Business OS', un sistema que reduce la carga manual y acelera el crecimiento.

¿Te interesaría una sesión de diagnóstico de 15 minutos para ver el potencial en vuestra operación?

Saludos,
El Agentic Bot de Sinapsis"""
        
        return subject, body
