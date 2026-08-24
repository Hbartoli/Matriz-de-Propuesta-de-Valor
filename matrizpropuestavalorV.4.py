import streamlit as st
import pandas as pd

# Configuración de la interfaz
st.set_page_config(page_title="Matriz de Propuesta de Valor Pro v4", layout="wide")

st.title("🎯 Consola de Validación y Viabilidad Financiera de Mercado")
st.subheader("Propuesta de Valor + TAM/SAM/SOM + Unit Economics (CAC/LTV) + Competencia")

# --- CONTROL DEL ESTADO DE LA SESIÓN ---
if "analizado" not in st.session_state:
    st.session_state.analizado = False

def limpiar_formulario():
    st.session_state.analizado = False
    st.session_state.txt_trabajos = ""
    st.session_state.txt_dolores = ""
    st.session_state.txt_alegrias = ""
    st.session_state.txt_productos = ""
    st.session_state.txt_aliviadores = ""
    st.session_state.txt_creadores = ""
    st.session_state.grav_dolor = 1
    st.session_state.rel_alegria = 1
    st.session_state.efec_aliv = 1
    st.session_state.efec_crea = 1
    st.session_state.v1 = False
    st.session_state.v2 = False
    st.session_state.v3 = False
    st.session_state.num_tam = 1000000
    st.session_state.num_sam = 100000
    st.session_state.num_som = 10000
    st.session_state.num_precio = 50.0
    st.session_state.num_mkt = 5000.0
    st.session_state.num_ventas = 3000.0
    st.session_state.num_nuevos = 200
    st.session_state.num_meses = 24
    st.session_state.num_margen = 70.0

# --- PANELES PRINCIPALES (PROPUESTA DE VALOR) ---
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👤 Perfil del Cliente (El Mercado)")
    trabajos = st.text_area("**Trabajos del Cliente (Customer Jobs)**", placeholder="¿Qué tareas intenta resolver?", key="txt_trabajos")
    
    st.divider()
    dolores = st.text_area("**Dolores (Pains)**", placeholder="¿Qué frustraciones o riesgos tiene?", key="txt_dolores")
    gravedad_dolor = st.selectbox(
        "¿Qué tan grave es este dolor?", options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["Insignificante", "Leve", "Moderado", "Frustrante", "Crítico"][x-1], key="grav_dolor"
    )
    
    st.divider()
    alegrias = st.text_area("**Alegrías (Gains)**", placeholder="¿Qué beneficios concretos espera?", key="txt_alegrias")
    relevancia_alegria = st.selectbox(
        "¿Qué tan importante es este beneficio?", options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["Irrelevante", "Secundario", "Deseable", "Muy Necesario", "Esencial"][x-1], key="rel_alegria"
    )

with col2:
    st.markdown("### 📦 Mapa de Valor (Tu Solución)")
    productos = st.text_area("**Productos y Servicios**", placeholder="¿Qué características componen tu oferta?", key="txt_productos")
    
    st.divider()
    aliviadores = st.text_area("**Aliviadores de Dolor (Pain Relievers)**", placeholder="¿Cómo reduces las frustraciones?", key="txt_aliviadores")
    efectividad_aliviador = st.selectbox(
        "¿Qué tan efectivo es tu producto aliviando ese dolor?", options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["No lo alivia", "Mínimo", "Parcial", "Efectivo", "Eliminación Total"][x-1], key="efec_aliv"
    )
    
    st.divider()
    creadores = st.text_area("**Creadores de Alegrías (Gain Creators)**", placeholder="¿Cómo potencias las alegrías?", key="txt_creadores")
    efectividad_creador = st.selectbox(
        "¿Qué tan efectivo es tu producto creando esa alegría?", options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["No aporta", "Insignificante", "Moderado", "Gran Creador", "Supera Expectativas"][x-1], key="efec_crea"
    )

# --- SECCIÓN 1: ESTIMACIÓN DE TAMAÑO DE MERCADO (TAM, SAM, SOM) ---
st.markdown("---")
st.markdown("### 📊 Dimensionamiento del Mercado (Métricas Financieras Anuales)")
st.caption("Define el volumen de clientes potenciales y el precio estimado de tu producto.")

c_tam, c_sam, c_som, c_precio = st.columns(4)
with c_tam:
    n_tam = st.number_input("Clientes en TAM (Mercado Total)", min_value=1, value=1000000, step=1000, key="num_tam")
with c_sam:
    n_sam = st.number_input("Clientes en SAM (Mercado Accesible)", min_value=1, value=100000, step=1000, key="num_sam")
with c_som:
    n_som = st.number_input("Clientes en SOM (Mercado Capturable)", min_value=1, value=10000, step=100, key="num_som")
with c_precio:
    precio_anual = st.number_input("Precio/Ingreso promedio anual por cliente ($)", min_value=0.1, value=50.0, step=5.0, key="num_precio")

# --- NUEVA SECCIÓN: UNIT ECONOMICS (CAC / LTV) ---
st.markdown("---")
st.markdown("### 💸 Viabilidad Económica (Cálculo de CAC y LTV)")
st.caption("Ingresa tus estimaciones operativas mensuales o por campaña para determinar la salud financiera de cada cliente capturado.")

cc1, cc2, cc3, cc4, cc5 = st.columns(5)
with cc1:
    gasto_mkt = st.number_input("Gasto en Marketing ($)", min_value=0.0, value=5000.0, step=500.0, key="num_mkt", help="Inversión en publicidad, anuncios, software de mkt, etc.")
with cc2:
    gasto_ventas = st.number_input("Gasto en Ventas ($)", min_value=0.0, value=3000.0, step=200.0, key="num_ventas", help="Comisiones, salarios del equipo comercial o herramientas de venta.")
with cc3:
    clientes_nuevos = st.number_input("Clientes Nuevos Capturados", min_value=1, value=200, step=10, key="num_nuevos", help="Total de clientes reales obtenidos gracias a esa inversión.")
with cc4:
    meses_vida = st.number_input("Permanencia Media (Meses)", min_value=1, value=24, step=1, key="num_meses", help="¿Cuántos meses se queda consumiendo tu producto un cliente promedio antes de irse?")
with cc5:
    margen_bruto = st.number_input("Margen Bruto (%)", min_value=1.0, max_value=100.0, value=70.0, step=5.0, key="num_margen", help="Porcentaje de ganancia libre tras restar los costos directos de entregar el producto.")

# --- SECCIÓN 2: TABLA INTERACTIVA DE COMPETENCIA ---
st.markdown("---")
st.markdown("### ⚔️ Matriz de Competitividad Directa")

tabla_competencia_inicial = pd.DataFrame([
    {"Característica / Criterio": "Precio / Accesibilidad", "Tu Proyecto": 4, "Competidor 1": 3, "Competidor 2": 5, "Competidor 3": 2},
    {"Característica / Criterio": "Efectividad Resolviendo el Dolor", "Tu Proyecto": 5, "Competidor 1": 2, "Competidor 2": 3, "Competidor 3": 4},
    {"Característica / Criterio": "Experiencia de Usuario (Diseño)", "Tu Proyecto": 4, "Competidor 1": 4, "Competidor 2": 2, "Competidor 3": 3},
    {"Característica / Criterio": "Tecnología / Innovación", "Tu Proyecto": 5, "Competidor 1": 3, "Competidor 2": 1, "Competidor 3": 4},
])

df_competencia = st.data_editor(tabla_competencia_inicial, num_rows="dynamic", use_container_width=True, key="tabla_editor")

# --- SECCIÓN 3: CHECKLIST LEAN ---
st.markdown("---")
st.markdown("### 🔍 Validación Experimental")
v1 = st.checkbox("¿Has hablado con al menos 10 clientes potenciales reales?", key="v1")
v2 = st.checkbox("¿Los clientes ya gastan dinero o tiempo en alternativas?", key="v2")
v3 = st.checkbox("¿Has validado el precio o un prototipo funcional con el mercado?", key="v3")

st.markdown("---")
btn_col1, btn_col2, _ = st.columns(3)
with btn_col1:
    activar_analisis = st.button("📊 Ejecutar Diagnóstico Integral", type="primary")
with btn_col2:
    st.button("🗑️ Limpiar Formulario", on_click=limpiar_formulario)

if activar_analisis:
    if not (trabajos and dolores and alegrias and productos and aliviadores and creadores):
        st.warning("⚠️ Completa los campos obligatorios de la propuesta de valor antes de continuar.")
        st.session_state.analizado = False
    elif n_som > n_sam or n_sam > n_tam:
        st.error("⚠️ Error de lógica en mercado: El SOM no puede ser mayor al SAM, ni el SAM mayor al TAM.")
        st.session_state.analizado = False
    else:
        st.session_state.analizado = True

# --- DESPLIEGUE DEL INFORME CONSOLIDADO ---
if st.session_state.analizado:
    st.success("✅ ¡Diagnóstico de Negocios de Alta Fidelidad Generado!")
    
    # 1. Cálculos de Ajuste de Propuesta de Valor
    puntuacion_dolor = min(100, int((efectividad_aliviador / gravedad_dolor) * 100)) if gravedad_dolor > 0 else 0
    puntuacion_alegria = min(100, int((efectividad_creador / relevancia_alegria) * 100)) if relevancia_alegria > 0 else 0
    validaciones = sum([v1, v2, v3])
    bono_validacion = validaciones * 5
    encaje_base = int((puntuacion_dolor + puntuacion_alegria) / 2)
    encaje_total = min(100, encaje_base + bono_validacion) if encaje_base >= 40 else encaje_base

    # 2. Cálculos Financieros del Mercado
    valor_tam = n_tam * precio_anual
    valor_sam = n_sam * precio_anual
    valor_som = n_som * precio_anual

    # 3. NUEVOS CÁLCULOS: UNIT ECONOMICS (CAC, LTV, Relación)
    # CAC = (Inversión Mkt + Inversión Ventas) / Clientes Nuevos
    cac_calculado = (gasto_mkt + gasto_ventas) / clientes_nuevos
    # Ingreso mensual estimado = Precio anual / 12 meses
    ingreso_mensual = precio_anual / 12
    # LTV = Ingreso Mensual * Meses de Vida * % Margen Bruto
    ltv_calculado = ingreso_mensual * meses_vida * (margen_bruto / 100)
    # Relación LTV a CAC
    relacion_ltv_cac = ltv_calculado / cac_calculado if cac_calculado > 0 else 0

    # MÓDULO VISUAL DE MÉTRICAS
    st.markdown("#### 📐 Estado del Encaje y Viabilidad")
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Encaje de Dolores", value=f"{puntuacion_dolor}%")
    m2.metric(label="Encaje de Alegrías", value=f"{puntuacion_alegria}%")
    m3.metric(label="Ajuste de Mercado Total (Fit)", value=f"{encaje_total}%")

    st.markdown("#### 💰 Potencial Financiero del Mercado")
    f1, f2, f3 = st.columns(3)
    f1.metric(label="TAM (Mercado Máximo)", value=f"${valor_tam:,.2f}")
    f2.metric(label="SAM (Mercado Objetivo)", value=f"${valor_sam:,.2f}")
    f3.metric(label="SOM (Captura Anual)", value=f"${valor_som:,.2f}")

    # RENDIMIENTO FINANCIERO DEL CLIENTE (CAC/LTV)
    st.markdown("#### 🔄 Métricas Unitarias por Cliente (Unit Economics)")
    u1, u2, u3 = st.columns(3)
    u1.metric(
        label="CAC (Costo de Adquisición)", 
        value=f"${cac_calculado:,.2f}", 
        help="Te cuesta esto traer un cliente."
    )
    u2.metric(
        label="LTV (Valor de Vida Útil)", 
        value=f"${ltv_calculado:,.2f}", 
        help="Esto te deja de ganancia neta un cliente a lo largo de su ciclo de vida."
    )
    u3.metric(
        label="Relación LTV / CAC", 
        value=f"{relacion_ltv_cac:.2f}x", 
        delta="Saludable (> 3x)" if relacion_ltv_cac >= 3 else "Peligro (< 3x)", 
        delta_color="normal" if relacion_ltv_cac >= 3 else "inverse"
    )

    # Gráficos combinados
    st.subheader("📈 Análisis de Mercado y Unit Economics")
    g1, g2 = st.columns(2)
    with g1:
        st.caption("Volumen de Ingresos por Capa de Mercado ($)")
        mercado_chart_data = pd.DataFrame({
            "Capa de Mercado": ["TAM", "SAM", "SOM"], 
            "Ingresos ($)": [valor_tam, valor_sam, valor_som]
        }).set_index("Capa de Mercado")
        st.bar_chart(mercado_chart_data)
        
    with g2:
        st.caption("Comparativa de Costo de Captura vs Retorno Neto ($)")
        economics_chart_data = pd.DataFrame({
            "Métrica Financiera": ["CAC (Inversión)", "LTV (Retorno Neto)"], 
            "Monto ($)": [cac_calculado, ltv_calculado]
        }).set_index("Métrica Financiera")
        st.bar_chart(economics_chart_data)

    # 4. Análisis Competitivo
    st.subheader("🏆 Resultados del Análisis Competitivo")
    try:
        promedios = df_competencia.mean(numeric_only=True)
        lider = promedios.idxmax()
        puntaje_lider = promedios.max()
        st.info(f"💡 **Evaluación Competitiva:** El líder según tus calificaciones es **{lider}** con un promedio de **{puntaje_lider:.2f}/5**.")
    except Exception:
        st.caption("Registra valores numéricos en la competencia para calcular promedios.")

    # Diagnóstico Final Integrado con CAC/LTV
    st.subheader("💡 Dictamen Comercial e Indicaciones Técnicas")
    
    if encaje_total >= 80 and relacion_ltv_cac >= 3.0 and valor_som >= 50000:
        st.balloons()
        st.success("**Negocio Altamente Escalable (Luz Verde):** Tu propuesta tiene un encaje sólido, tus *Unit Economics* son excelentes (el LTV triplica o supera al CAC) y el volumen de mercado sustenta la operación. Tienes un modelo apto para presentar ante inversores.")
    elif relacion_ltv_cac < 3.0:
        st.error("**Foco de Alerta en Unit Economics (Inviabilidad Comercial):** Aunque tu producto resuelva problemas, estás gastando demasiado en adquirir clientes (`CAC`) para la poca ganancia neta (`LTV`) que te dejan en su ciclo de vida. Necesitas reducir costos de conversión o subir los precios/retención urgentemente.")
    elif encaje_total >= 50:
        st.warning("**Ajuste Incompleto o Mercado Limitado:** Tu propuesta funciona, pero tus volúmenes financieros son ajustados. Revisa tus canales de captación para ver si puedes mejorar tu presencia en el SAM.")
    else:
        st.error("**Proyecto en Zona de Riesgo:** El encaje de valor es muy bajo o los números generales no sustentan el negocio.")

    # --- EXPORTACIÓN GENERAL ---
    csv_propuesta = pd.DataFrame({
        "Métrica General": ["Ajuste Total %", "Valor TAM $", "Valor SAM $", "Valor SOM $", "Costo Adquisición (CAC)", "Valor de Vida (LTV)", "Ratio LTV/CAC"],
        "Resultado": [f"{encaje_total}%", f"${valor_tam:,.2f}", f"${valor_sam:,.2f}", f"${valor_som:,.2f}", f"${cac_calculado:,.2f}", f"${ltv_calculado:,.2f}", f"{relacion_ltv_cac:.2f}x"]
    })
    
    csv_data = csv_propuesta.to_csv(index=False).encode('utf-8')
    st.write("")
    st.download_button(
        label="📥 Descargar Reporte de Negocio Consolidado (CSV)",
        data=csv_data,
        file_name="reporte_financiero_matriz.csv",
        mime="text/csv",
    )
