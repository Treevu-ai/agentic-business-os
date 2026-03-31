import json

class CompanyScraper:
    def __init__(self, sector, region, max_companies=50):
        self.sector = sector
        self.region = region
        self.max_companies = max_companies

    def get_companies(self):
        """
        Simulates a web search for companies in the given sector and region.
        In a real scenario, this would use a search API or a scraping tool.
        """
        # Simulated results based on real patterns
        simulated_data = [
            {"nombre": f"{self.sector.capitalize()} Soluciones SAC", "web": f"{self.sector}soluciones.pe", "ciudad": self.region, "telefono": "987654321"},
            {"nombre": f"Grupo {self.sector.capitalize()} Perú", "web": f"grupo{self.sector}.com.pe", "ciudad": self.region, "telefono": "912345678"},
            {"nombre": f"{self.sector.capitalize()} Innova E.I.R.L.", "web": f"{self.sector}innova.pe", "ciudad": self.region, "telefono": "955443322"},
            {"nombre": f"Logística {self.sector.capitalize()} S.A.", "web": f"logistica{self.sector}.pe", "ciudad": self.region, "telefono": "944332211"},
            {"nombre": f"{self.sector.capitalize()} Digital Lab", "web": f"{self.sector}digital.pe", "ciudad": self.region, "telefono": "933221100"},
        ]
        return simulated_data[:self.max_companies]
