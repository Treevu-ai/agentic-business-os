from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from orchestrator import TreevuOrchestrator
import uvicorn

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class LeadGenRequest(BaseModel):
    sector: str
    region: str = "Lima"
    max_companies: int = 5

@app.get("/")
def read_root():
    return {"message": "SINAPSIS Agentic OS API Running"}

@app.post("/api/generate-leads")
async def generate_leads(request: LeadGenRequest):
    try:
        orchestrator = TreevuOrchestrator(request.sector, request.region, request.max_companies)
        result = orchestrator.run()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
