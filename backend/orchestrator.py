import pandas as pd
import os
from modules.scraper import CompanyScraper
from modules.enricher import ContactEnricher
from modules.email_generator import EmailGenerator

class TreevuOrchestrator:
    def __init__(self, sector, region="Lima", max_companies=5):
        self.sector = sector
        self.region = region
        self.max_companies = max_companies
        self.leads = []
        
    def run(self):
        print(f"Iniciando flujo para {self.sector} en {self.region}...")
        
        # 1. Scraping
        scraper = CompanyScraper(self.sector, self.region, self.max_companies)
        companies = scraper.get_companies()
        
        # 2. Enrichment & Generation
        enricher = ContactEnricher()
        email_gen = EmailGenerator()
        
        for co in companies:
            contacts = enricher.enrich_company(co["nombre"], co["web"])
            if not contacts:
                contacts = [{"nombre": "N/A", "cargo": "Gerente de RRHH (Genérico)", "email": ""}]
            
            for contact in contacts:
                asunto, cuerpo = "", ""
                if contact["email"]:
                    asunto, cuerpo = email_gen.generate_draft(contact["nombre"], co["nombre"], self.sector)
                
                self.leads.append({
                    "sector": self.sector,
                    "empresa": co["nombre"],
                    "web": co["web"],
                    "ciudad_region": co["ciudad"],
                    "telefono": co["telefono"],
                    "nombre_contacto": contact["nombre"],
                    "cargo": contact["cargo"],
                    "email": contact["email"],
                    "fuente_datos": "Google / Web Corporativa",
                    "borrador_asunto": asunto,
                    "borrador_cuerpo": cuerpo
                })
        
        # 3. Export to CSV in a temporary directory or known output path
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        output_file = os.path.join(output_dir, f"leads_{self.sector}_{self.region}.csv")
        df = pd.DataFrame(self.leads)
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        return {
            "status": "success",
            "file": output_file,
            "count": len(self.leads),
            "data": self.leads
        }

if __name__ == "__main__":
    orchestrator = TreevuOrchestrator("tech", "Lima", 2)
    print(orchestrator.run())
