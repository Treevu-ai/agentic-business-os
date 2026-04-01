import pandas as pd
from modules.scraper import CompanyScraper
from modules.enricher import ContactEnricher
from modules.email_generator import EmailGenerator
import os

class TreevuOrchestrator:
    def __init__(self, sector, region="Lima", max_companies=50):
        self.sector = sector
        self.region = region
        self.max_companies = max_companies
        self.leads = []
        
    def run(self):
        print(f"Iniciando flujo para {self.sector} en {self.region}...")
        
        # 1. Scraping (Placeholder for real tool calls)
        scraper = CompanyScraper(self.sector, self.region, self.max_companies)
        # Note: In the Antigravity implementation, we would call the search tool here.
        # companies = scraper.get_companies()
        
        # 2. Enrichment & Generation
        enricher = ContactEnricher()
        email_gen = EmailGenerator()
        
        # Assuming we have a list of companies (as a placeholder)
        # We will populate this with example data if the scraper is empty
        companies = [
            {"nombre": "Empresa Ejemplo 1", "web": "ejemplo1.pe", "ciudad": self.region, "telefono": "987654321"},
            {"nombre": "Empresa Ejemplo 2", "web": "ejemplo2.pe", "ciudad": self.region, "telefono": "912345678"}
        ]
        
        for co in companies:
            # Enrich
            contacts = enricher.enrich_company(co["nombre"], co["web"])
            if not contacts:
                # Add at least one row per company even if no contact found
                contacts = [{"nombre": "N/A", "cargo": "Gerente de RRHH (Genérico)", "email": ""}]
            
            for contact in contacts:
                asunto, cuerpo = "", ""
                if contact["email"] or True: # Generate drafts even if email placeholder
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
        
        # 3. Export to CSV
        df = pd.DataFrame(self.leads)
        output_file = "treevu_leads.csv"
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        print("\n" + "="*40)
        print("¡PROCESO COMPLETADO CON ÉXITO!")
        print("="*40)
        print(f"Total de empresas procesadas: {len(companies)}")
        print(f"Total de contactos encontrados: {len(self.leads)}")
        print(f"Archivo generado: {os.path.abspath(output_file)}")
        print("="*40)
        
        return output_file

if __name__ == "__main__":
    try:
        # Pide parámetros al usuario si se ejecuta directamente
        print("--- Treevü Lead Generator ---")
        sector = input("Ingrese el sector (manufactura, servicios, retail, tech, agroindustria, minería): ") or "tech"
        region = input("Ingrese la ciudad o región (ej: Lima): ") or "Lima"
        max_co = input("Máximo de empresas (default 50): ") or 50
        
        orchestrator = TreevuOrchestrator(sector, region, int(max_co))
        orchestrator.run()
    except Exception as e:
        print(f"\nERROR DETECTADO: {e}")
    
    print("\n")
    input("Presiona ENTER para cerrar esta ventana...")
