class ContactEnricher:
    def __init__(self):
        pass

    def enrich_company(self, company_name, website):
        """
        Simulates finding contacts (HR, Finance, Operations) for a company.
        In production, this would query LinkedIn, Apollo, or company websites.
        """
        # Simulated enrichment logic
        contacts = [
            {"nombre": "Carlos Rodríguez", "cargo": "Gerente de Operaciones", "email": f"carlos.rodriguez@{website}"},
            {"nombre": "María Paz", "cargo": "Directora de Finanzas", "email": f"m.paz@{website}"}
        ]
        return contacts
