/* ==========================================================
   SINAPSIS_OS // CONTROLADOR DEL WORKSPACE
   Demo interactiva — 10 Agentes de Negocio
========================================================== */

const AGENTS = [
    {
        id: 'rev',
        name: 'Agente de Inteligencia Financiera',
        sub: 'Analiza tu pipeline, ticket promedio y varianzas diarias para detectar fugas de ingresos.',
        path: 'root@sinapsis-os:~/agents/revenue_intel',
        inputs: [
            { id: 'rev-crm', label: 'CRM / DATA SOURCE', value: 'HubSpot API v3' },
            { id: 'rev-thr', label: 'UMBRAL DE ALERTA (%)', value: '-15%' }
        ],
        lines: [
            '> Conectando a base de datos CRM...',
            '> Analizando 15,204 transacciones históricas...',
            '> Calculando varianza semanal de ingresos...',
            '> Detectando anomalías en el pipeline Q3...'
        ],
        outTemplate: () => `
            <div class="lead-item">
                <h4>⚠️ RIESGO DETECTADO: Ticket Promedio</h4>
                <div class="lead-meta"><span>Venta B2B</span> impactada</div>
                <div class="lead-draft" style="color:#ff4d4d;">
                    El ticket promedio de nuevos clientes cayó un 18% vs el mes anterior. 3 deals en riesgo crítico esta semana (Total: $14,500). Sugerencia: Revisar política de descuentos comerciales.
                </div>
            </div>`
    },
    {
        id: 'gtm',
        name: 'Agente de Prospección B2B',
        sub: 'Despliegue operativo para generación de leads, enriquecimiento de contactos y creación de borradores.',
        path: 'root@sinapsis-os:~/agents/prospeccion_b2b',
        inputs: [
            { id: 'sector', label: 'SECTOR INDUSTRIAL', value: 'Agroindustria y Exportación' },
            { id: 'region', label: 'REGIÓN / CIUDAD', value: 'Lima, Perú' }
        ],
        lines: [
            '> Iniciando crawler web... OK',
            '> Ejecutando parámetros de búsqueda regional...',
            '> Procesando fuentes de datos públicas...',
            '> Enriqueciendo contactos vía Apollo/LinkedIn API...'
        ],
        // The GTM agent will use the real API or fallback to mock
        isRealApi: true
    },
    {
        id: 'tal',
        name: 'Agente Organizador de Talento',
        sub: 'Conectado a tu PM tool, detecta sobrecarga de trabajo y cuellos de botella en tiempo real.',
        path: 'root@sinapsis-os:~/agents/talent_optimizer',
        inputs: [
            { id: 'tal-tool', label: 'PM WORKSPACE', value: 'Asana // Proyectos Q3' },
            { id: 'tal-team', label: 'EQUIPO', value: 'Diseño & Desarrollo' }
        ],
        lines: [
            '> Sincronizando tableros de gestión de proyectos...',
            '> Agregando estimaciones de tiempo por tarea...',
            '> Detectando colaboradores con sobrecarga...',
            '> Cruzando datos con Google Calendar...'
        ],
        outTemplate: () => `
            <div class="lead-item">
                <h4>🔄 OPTIMIZACIÓN REQUERIDA</h4>
                <div class="lead-meta"><span>Asignación de Recursos</span> alerta</div>
                <div class="lead-draft">
                    'Carlos Pérez' tiene 140% de carga asignada para esta semana. 2 proyectos están en riesgo de retraso.
                    Recomendación: Mover la tarea 'Rediseño Home' a 'Ana López' (carga actual: 60%). Moviendo tareas automáticamente...
                </div>
            </div>`
    },
    {
        id: 'pri',
        name: 'Agente de Inteligencia de Precios',
        sub: 'Monitorea competidores y analiza elasticidad para sugerir ajustes de margen.',
        path: 'root@sinapsis-os:~/agents/pricing_intel',
        inputs: [
            { id: 'pri-cat', label: 'CATEGORÍA A MONITOREAR', value: 'Servicios Profesionales' },
            { id: 'pri-comp', label: 'COMPETIDORES', value: 'Top 3 Regionales' }
        ],
        lines: [
            '> Escaneando páginas de precios de competidores...',
            '> Normalizando niveles de servicio del mercado...',
            '> Calculando delta de margen actual vs. mercado...',
            '> Generando recomendación de precios optimizada...'
        ],
        outTemplate: () => `
            <div class="lead-item">
                <h4>💰 RECOMENDACIÓN DE PRECIOS</h4>
                <div class="lead-meta"><span>Margen Potencial</span> detectado</div>
                <div class="lead-draft">
                    Tus precios en 'Consultoría Nivel 1' están 22% por debajo del promedio del mercado. 
                    Simulación: Un aumento del 10% generaría +$4,500/mes de utilidad bruta sin impacto estimado en conversión.
                </div>
            </div>`
    },
    {
        id: 'sup',
        name: 'Agente de Control de Inventario',
        sub: 'Cruza ventas con plazos de proveedores para alertar antes del quiebre de stock.',
        path: 'root@sinapsis-os:~/agents/supply_guard',
        inputs: [
            { id: 'sup-wh', label: 'ALMACÉN / ERP', value: 'Bodega Central (Odoo)' },
            { id: 'sup-lt', label: 'LEAD TIME PROMEDIO', value: '45 días (Importación)' }
        ],
        lines: [
            '> Sincronizando niveles de inventario con ERP...',
            '> Analizando velocidad de ventas — últimos 12 meses...',
            '> Calculando umbrales de stock de seguridad...',
            '> Generando órdenes de compra preventivas...'
        ],
        outTemplate: () => `
            <div class="lead-item">
                <h4>📦 ALERTA DE RUPTURA PREVENTIVA</h4>
                <div class="lead-meta"><span>Stock</span> crítico</div>
                <div class="lead-draft">
                    El SKU 'Motor-AX-500' se agotará en 32 días (velocidad actual: 15/semana). Lead time del proveedor: 45 días.
                    Ruptura proyectada de 13 días. Se ha generado un borrador de Orden de Compra Urgente al proveedor por 200 unidades.
                </div>
            </div>`
    },
    {
        id: 'csm',
        name: 'Agente de Retención de Clientes',
        sub: 'Analiza señales de churn y manda alertas preventivas antes de que el cliente se vaya.',
        path: 'root@sinapsis-os:~/agents/customer_success',
        inputs: [
            { id: 'csm-seg', label: 'SEGMENTO CLIENTES', value: 'Cuentas Enterprise (>$1k/mo)' },
            { id: 'csm-data', label: 'MÉTRICAS', value: 'Uso Plataforma + Tickets Soporte' }
        ],
        lines: [
            '> Analizando telemetría de uso del producto...',
            '> Escaneando sentimiento en tickets de soporte...',
            '> Correlacionando NPS con caída de actividad...',
            '> Identificando cuentas en riesgo de cancelación...'
        ],
        outTemplate: () => `
            <div class="lead-item">
                <h4>🚨 CHURN RISK [ALTO]</h4>
                <div class="lead-meta"><span>Cliente</span> Empresa XYZ Sac</div>
                <div class="lead-draft">
                    Indicadores de riesgo: 0 inicios de sesión en 14 días + 2 tickets abiertos sin resolver.
                    Acción recomendada: Llamada ejecutiva programada. Borrador de email para account manager generado.
                </div>
            </div>`
    },
    {
        id: 'com',
        name: 'Agente de Cumplimiento Legal',
        sub: 'Escanea contratos y genera calendarios ejecutivos de vencimientos y cláusulas de riesgo.',
        path: 'root@sinapsis-os:~/agents/compliance_monitor',
        inputs: [
            { id: 'com-dr', label: 'REPOSITORIO LEGAL', value: '/drive/contratos_2026' },
            { id: 'com-kw', label: 'CLÁUSULAS', value: 'Renovación automática, Exclusividad' }
        ],
        lines: [
            '> Ingiriendo 142 contratos en formato PDF...',
            '> Ejecutando análisis semántico con PLN...',
            '> Extrayendo fechas y cláusulas de responsabilidad...',
            '> Compilando panel de vencimientos críticos...'
        ],
        outTemplate: () => `
            <div class="lead-item">
                <h4>📅 VENCIMIENTO CRÍTICO</h4>
                <div class="lead-meta"><span>Renovación</span> automática</div>
                <div class="lead-draft">
                    Contrato 'Proveedor SaaS A' vence en 45 días. Cláusula detectada: Renovación automática con +15% de aumento si no se cancela 30 días antes.
                    Tienes 15 días para notificar la re-negociación.
                </div>
            </div>`
    },
    {
        id: 'mki',
        name: 'Agente de Monitoreo de Competencia',
        sub: 'Escanea noticias y licitaciones del sector generando un briefing ejecutivo cada lunes.',
        path: 'root@sinapsis-os:~/agents/market_intel',
        inputs: [
            { id: 'mki-kw', label: 'PALABRAS CLAVE', value: 'Licitación, Adjudicación, B2B' },
            { id: 'mki-tr', label: 'TRACKING_ID', value: 'Competidor Alfa, Competidor Beta' }
        ],
        lines: [
            '> Escaneando portales de licitaciones públicas...',
            '> Monitoreando redes sociales de competidores...',
            '> Agregando noticias relevantes del sector...',
            '> Generando briefing ejecutivo semanal...'
        ],
        outTemplate: () => `
            <div class="lead-item">
                <h4>📰 RADAR DE OPORTUNIDADES</h4>
                <div class="lead-meta"><span>Licitación Pública</span> detectada</div>
                <div class="lead-draft">
                    Se publicó una nueva licitación que coincide 92% con tu perfil de servicios (Desarrollo B2B).
                    Plazo de postulación: 14 días. Presupuesto estimado: $450,000. He enviado el pliego técnico a tu correo.
                </div>
            </div>`
    },
    {
        id: 'ops',
        name: 'Agente Automatizador de Operaciones',
        sub: 'El pegamento digital de tu empresa. Conecta herramientas y automatiza el copypaste.',
        path: 'root@sinapsis-os:~/agents/ops_automation',
        inputs: [
            { id: 'ops-in', label: 'TRIGGER', value: 'Nuevo contrato firmado (Docusign)' },
            { id: 'ops-ou', label: 'ACTIONS', value: 'Crear Drive, Slack, Asana, Email' }
        ],
        lines: [
            '> Escuchando trigger de webhook... activo',
            '> Webhook recibido. Procesando payload...',
            '> Ejecutando llamadas a múltiples plataformas...',
            '> Validando consistencia de estado en todos los sistemas...'
        ],
        outTemplate: () => `
            <div class="lead-item">
                <h4>✅ FLUJO DE TRABAJO EJECUTADO</h4>
                <div class="lead-meta"><span>Sin intervención</span> humana</div>
                <div class="lead-draft">
                    Cliente 'Logística Sur' firmado. 
                    - Carpeta de Drive creada.
                    - Canal de Slack #cli-logistica-sur inicializado.
                    - Proyecto Asana creado basado al template 'Onboarding v2'.
                    - Email de bienvenida enviado. (Tiempo humano ahorrado: 45 min)
                </div>
            </div>`
    },
    {
        id: 'cmd',
        name: 'Centro de Comando Ejecutivo',
        sub: 'Recibe señales de todos los agentes y genera el briefing de prioridades diarias.',
        path: 'root@sinapsis-os:~/agents/command_center',
        inputs: [
            { id: 'cmd-src', label: 'DATA SOURCES', value: 'All 9 Agents' },
            { id: 'cmd-out', label: 'OUTPUT CHANNEL', value: 'WhatsApp + Executive Email' }
        ],
        lines: [
            '> Consultando subred de agentes activos...',
            '> Agregando 14 alertas del sistema...',
            '> Priorizando por impacto en ingresos (IA)...',
            '> Transmitiendo briefing ejecutivo de la mañana...'
        ],
        outTemplate: () => `
            <div class="lead-item" style="border-left-color:var(--y);">
                <h4>👑 BRIEFING EJECUTIVO DIARIO</h4>
                <div class="lead-meta"><span style="color:var(--y);">Prioridad</span> Alta</div>
                <div class="lead-draft">
                    Buenos días. Resumen operativo de hoy:
                    1. (Riesgo) Pipeline Q3 cayó 18% vs histórico.
                    2. (Acción) Contrato SaaS vence en 45 días, renegociar ahora.
                    3. (Oportunidad) 12 nuevos leads de perfil Retail generados en frío están listos en tu CRM para contacto.
                </div>
            </div>`
    }
];

let currentAgentId = 'gtm';

function renderSidebar() {
    const list = document.getElementById('agent-list');
    list.innerHTML = '';
    AGENTS.forEach((a, idx) => {
        const item = document.createElement('div');
        item.className = 'sb-item' + (a.id === currentAgentId ? ' active' : '');
        item.innerHTML = `${String(idx+1).padStart(2,'0')} // ${a.name}`;
        item.onclick = () => loadAgent(a.id);
        list.appendChild(item);
    });
}

function loadAgent(id) {
    currentAgentId = id;
    renderSidebar(); // Update active state
    
    const agent = AGENTS.find(a => a.id === id);
    
    // Update headers
    document.getElementById('ws-title').textContent = agent.name;
    document.getElementById('ws-sub').textContent = agent.sub;
    document.getElementById('ws-path').textContent = agent.path;
    
    // Build inputs
    const inputsHtml = agent.inputs.map(inp => `
        <div class="input-group">
            <label>${inp.label}</label>
            <input type="text" id="${inp.id}" value="${inp.value}">
        </div>
    `).join('');
    document.getElementById('ws-inputs').innerHTML = inputsHtml;
    
    // Build loader terminal lines
    const loaderHtml = agent.lines.map((l, i) => {
        const showCursor = i === agent.lines.length - 1 ? '<span class="cursor"></span>' : '';
        return `<div class="m-line"><span>></span> ${l.replace('> ','')} ${showCursor}</div>`;
    }).join('');
    document.getElementById('loader').innerHTML = loaderHtml;
    
    // Reset state
    document.getElementById('results').style.display = 'none';
    const btn = document.getElementById('run-agent');
    btn.style.display = 'inline-flex';
    btn.textContent = '$ EXECUTE_AGENT SEQUENCE';
}

// Setup initial
renderSidebar();
loadAgent('gtm');

// Execution Logic
document.getElementById('run-agent').addEventListener('click', async () => {
    const agent = AGENTS.find(a => a.id === currentAgentId);
    const btn = document.getElementById('run-agent');
    const loader = document.getElementById('loader');
    const resultsDiv = document.getElementById('results');
    const leadsList = document.getElementById('leads-list');
    
    btn.style.display = 'none';
    resultsDiv.style.display = 'none';
    loader.style.display = 'block';
    
    // Terminal Animation
    const lines = loader.querySelectorAll('.m-line');
    lines.forEach(l => l.style.opacity = '0');
    
    await new Promise(r => setTimeout(r, 200));
    if(lines[0]) lines[0].style.opacity = '1';
    
    await new Promise(r => setTimeout(r, 800));
    if(lines[1]) lines[1].style.opacity = '1';
    
    await new Promise(r => setTimeout(r, 1500));
    if(lines[2]) lines[2].style.opacity = '1';
    
    await new Promise(r => setTimeout(r, 1200));
    if(lines[3]) lines[3].style.opacity = '1';
    
    // Execution
    if (agent.isRealApi) {
        // Fallback for real GTM API
        const sector = document.getElementById('sector') ? document.getElementById('sector').value : 'General';
        const region = document.getElementById('region') ? document.getElementById('region').value : 'Lima';
        
        try {
            const resp = await fetch('http://localhost:8000/api/generate-leads', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ sector, region, max_companies: 2 })
            });
            
            if (resp.ok) {
                const res = await resp.json();
                leadsList.innerHTML = res.data.map(lead => `
                    <div class="lead-item">
                        <h4>🏢 ${lead.empresa}</h4>
                        <div class="lead-meta"><span>${lead.cargo}</span> ${lead.nombre_contacto}</div>
                        <div class="lead-email">${lead.email} | ${lead.web}</div>
                        <div class="lead-draft">${lead.borrador_cuerpo.substring(0, 150)}...</div>
                    </div>
                `).join('');
            } else {
                throw new Error('Local API not running');
            }
        } catch (e) {
            // Fallback mock if backend offline
            leadsList.innerHTML = `
                <div class="lead-item">
                    <h4>🏢 Agrocorp SAC</h4>
                    <div class="lead-meta"><span>Gerente Comercial</span> Luis Tapia</div>
                    <div class="lead-email">luis.tapia@agrocorpsac.fake | www.agrocorpsac.fake</div>
                    <div class="lead-draft">Hola Luis, noté el crecimiento de Agrocorp y preparé un análisis...</div>
                </div>`;
        }
    } else {
        // Mock output for non-GTM agents
        await new Promise(r => setTimeout(r, 800)); // extra delay
        leadsList.innerHTML = agent.outTemplate();
    }
    
    // Done
    loader.style.display = 'none';
    resultsDiv.style.display = 'block';
    
    btn.style.display = 'inline-flex';
    btn.textContent = '$ RE_EXECUTE SEQUENCE';
});
