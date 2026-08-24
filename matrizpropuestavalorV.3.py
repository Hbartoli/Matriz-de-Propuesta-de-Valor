import streamlit as st
import pandas as pd

# Configuración de la interfaz
st.set_page_config(page_title="Matriz de Propuesta de Valor Pro v3", layout="wide")

st.title("🎯 Consola Avanzada de Validación de Mercado")
st.subheader("Propuesta de Valor + Tamaño de Mercado (TAM/SAM/SOM) + Análisis Competitivo")

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

# --- PANELES PRINCIPALES (PROPUESTA DE VALOR) ---
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👤 Perfil del Cliente (El Mercado)")
    trabajos = st.text_area("**Trabajos del Cliente (Customer Jobs)**", placeholder="¿Qué tareas intenta resolver?", key="txt_trabajos")
    
    st.divider()
    dolores = st.text_area("**Dolores (Pains)**", placeholder="¿Qué frustraciones o riesgos tiene?", key="txt_dolores")
    gravedad_dolor = st.selectbox(
        "¿Qué tan grave es este dolor?", options=,
        format_func=lambda x: f"{x} - " + ["Insignificante", "Leve", "Moderado", "Frustrante", "Crítico"][x-1], key="grav_dolor"
    )
    
    st.divider()
    alegrias = st.text_area("**Alegrías (Gains)**", placeholder="¿Qué beneficios concretos espera?", key="txt_alegrias")
    relevancia_alegria = st.selectbox(
        "¿Qué tan importante es este beneficio?", options=,
        format_func=lambda x: f"{x} - " + ["Irrelevante", "Secundario", "Deseable", "Muy Necesario", "Esencial"][x-1], key="rel_alegria"
    )

with col2:
    st.markdown("### 📦 Mapa de Valor (Tu Solución)")
    productos = st.text_area("**Productos y Servicios**", placeholder="¿Qué características componen tu oferta?", key="txt_productos")
    
    st.divider()
    aliviadores = st.text_area("**Aliviadores de Dolor (Pain Relievers)**", placeholder="¿Cómo reduces las frustraciones?", key="txt_aliviadores")
    efectividad_aliviador = st.selectbox(
        "¿Qué tan efectivo es tu producto aliviando ese dolor?", options=,
        format_func=lambda x: f"{x} - " + ["No lo alivia", "Mínimo", "Parcial", "Efectivo", "Eliminación Total"][x-1], key="efec_aliv"
    )
    
    st.divider()
    creadores = st.text_area("**Creadores de Alegrías (Gain Creators)**", placeholder="¿Cómo potencias las alegrías?", key="txt_creadores")
    efectividad_creador = st.selectbox(
        "¿Qué tan efectivo es tu producto creando esa alegría?", options=,
        format_func=lambda x: f"{x} - " + ["No aporta", "Insignificante", "Moderado", "Gran Creador", "Supera Expectativas"][x-1], key="efec_crea"
    )

# --- SECCIÓN 1: ESTIMACIÓN DE TAMAÑO DE MERCADO (TAM, SAM, SOM) ---
st.markdown("---")
st.markdown("### 📊 Dimensionamiento del Mercado (Métricas Financieras Anuales)")
st.caption("Define el volumen de clientes potenciales y el precio estimado de tu producto para calcular el valor total del mercado.")

c_tam, c_sam, c_som, c_precio = st.columns(4)
with c_tam:
    n_tam = st.number_input("Clientes en TAM (Mercado Total)", min_value=1, value=1000000, step=1000, key="num_tam", help="Total de clientes que necesitan la solución a nivel global o país.")
with c_sam:
    n_sam = st.number_input("Clientes en SAM (Mercado Accesible)", min_value=1, value=100000, step=1000, key="num_sam", help="Fracción del TAM a la que realmente llega tu modelo de negocio y canales.")
with c_som:
    n_som = st.number_input("Clientes en SOM (Mercado Capturable)", min_value=1, value=10000, step=100, key="num_som", help="Tus objetivos reales de venta para los primeros 12-24 meses.")
with c_precio:
    precio_anual = st.number_input("Precio/Ingreso promedio anual por cliente ($)", min_value=0.1, value=50.0, step=5.0, key="num_precio", help="Cuánto dinero te pagará un cliente promedio a lo largo de un año.")

# --- SECCIÓN 2: TABLA INTERACTIVA DE COMPETENCIA ---
st.markdown("---")
st.markdown("### ⚔️ Matriz de Competitividad Directa")
st.caption("Asigna una calificación del 1 (Muy Malo) al 5 (Excelente) para evaluar cómo se comporta tu negocio frente a la competencia.")

# Usamos st.data_editor para permitir edición en tiempo real de la tabla interactiva
tabla_competencia_inicial = pd.DataFrame([
    {"Característica / Criterio": "Precio / Accesibilidad", "Tu Proyecto": 4, "Competidor 1": 3, "Competidor 2": 5, "Competidor 3": 2},
    {"Característica / Criterio": "Efectividad Resolviendo el Dolor", "Tu Proyecto": 5, "Competidor 1": 2, "Competidor 2": 3, "Competidor 3": 4},
    {"Característica / Criterio": "Experiencia de Usuario (Diseño)", "Tu Proyecto": 4, "Competidor 1": 4, "Competidor 2": 2, "Competidor 3": 3},
    {"Característica / Criterio": "Tecnología / Innovación", "Tu Proyecto": 5, "Competidor 1": 3, "Competidor 2": 1, "Competidor 3": 4},
])

df_competencia = st.data_editor(
    tabla_competencia_inicial,
    num_rows="dynamic", # Permite al usuario añadir filas personalizadas (ej. características específicas)
    use_container_width=True,
    key="tabla_editor"
)

# --- SECCIÓN 3: CHECKLIST LEAN ---
st.markdown("---")
st.markdown("### 🔍 Validación Experimental")
v1 = st.checkbox("¿Has hablado con al menos 10 clientes potenciales reales?", key="v1")
v2 = st.checkbox("¿Los clientes ya gastan dinero o tiempo en alternativas?", key="v2")
v3 = st.checkbox("¿Has validado el precio o un prototipo funcional con el mercado?", key="v3")

st.markdown("---")
btn_col1, btn_col2, _ = st.columns()
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

# --- DESPLIEGUE DEL INFORME CONSOLIDAD ---
if st.session_state.analizado:
    st.success("✅ ¡Diagnóstico de Negocios de Alta Fidelidad Generado!")
    
    # 1. Cálculos de Ajuste de Propuesta de Valor
    puntuacion_dolor = min(100, int((efectividad_aliviador / gravedad_dolor) * 100)) if gravedad_dolor > 0 else 0
    puntuacion_alegria = min(100, int((efectividad_creador / relevancia_alegria) * 100)) if relevancia_alegria > 0 else 0
    validaciones = sum([v1, v2, v3])
    bono_validacion = validaciones * 5
    encaje_base = int((puntuacion_dolor + puntuacion_alegria) / 2)
    encaje_total = min(100, encaje_base + bono_validacion) if encaje_base >= 40 else encaje_base

    # 2. Cálculos Financieros del Mercado (Volumen * Precio)
    valor_tam = n_tam * precio_anual
    valor_sam = n_sam * precio_anual
    valor_som = n_som * precio_anual

    # Render de métricas en columnas (Fila 1: Ajuste | Fila 2: Finanzas)
    st.markdown("#### 📐 Estado del Encaje y Viabilidad")
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Encaje de Dolores", value=f"{puntuacion_dolor}%")
    m2.metric(label="Encaje de Alegrías", value=f"{puntuacion_alegria}%")
    m3.metric(label="Ajuste de Mercado Total (Fit)", value=f"{encaje_total}%")

    st.markdown("#### 💰 Potencial Financiero del Mercado (USD / Moneda Local)")
    f1, f2, f3 = st.columns(3)
    f1.metric(label="TAM (Mercado Máximo Teórico)", value=f"${valor_tam:,.2f}")
    f2.metric(label="SAM (Tu Mercado Objetivo)", value=f"${valor_sam:,.2f}")
    f3.metric(label="SOM (Tu Captura Inmediata Anual)", value=f"${valor_som:,.2f}")

    # Gráfico de Barras del Tamaño de Mercado
    st.subheader("📈 Proyección del Volumen de Ingresos por Capa de Mercado")
    mercado_chart_data = pd.DataFrame({
        "Capa de Mercado": ["TAM (Total)", "SAM (Accesible)", "SOM (Capturable)"],
        "Ingresos Potenciales ($)": [valor_tam, valor_sam, valor_som]
    }).set_index("Capa de Mercado")
    st.bar_chart(mercado_chart_data)

    # 3. Análisis Competitivo Basado en el Editor de Datos
    st.subheader("🏆 Resultados del Análisis Competitivo")
    try:
        # Calcular el puntaje promedio de cada columna numérico
        promedios = df_competencia.mean(numeric_only=True)
        
        # Encontrar quién lidera el mercado según la matriz armada por el usuario
        lider = promedios.idxmax()
        puntaje_lider = promedios.max()
        
        st.info(f"💡 **Evaluación Competitiva:** El promedio de calificaciones indica que el líder de la comparativa es **{lider}** con un rendimiento promedio de **{puntaje_lider:.2f}/5**. Revisa en qué criterios quedaste por debajo para fortalecer tus barreras de entrada.")
    except Exception:
        st.caption("Registra valores numéricos en la tabla competitiva para calcular promedios automáticos.")

    # Diagnóstico Final Integrado
    st.subheader("💡 Dictamen Comercial e Indicaciones Técnicas")
    if encaje_total >= 80 and valor_som >= 50000:
        st.balloons()
        st.success("**Propuesta de Alta Viabilidad:** Cuentas con un encaje sólido en el papel, un mercado capturable (SOM) monetariamente atractivo y validación en marcha. El proyecto califica para iniciar fases operativas intensivas.")
        elif encaje_total >= 50:
        st.warning("**Ajuste Incompleto o Mercado Limitado:** Tu propuesta resuelve problemas, pero el volumen financiero de tu SOM es ajustado o tu validación es baja. Considera optimizar tu estrategia de precios o expandir los canales de distribución para elevar tu SAM.")
    else:
        st.error("**Proyecto en Zona de Riesgo:** El encaje de valor es muy bajo o los números del mercado no sustentan la operación de la empresa. No escales gastos; necesitas redefinir el dolor principal del cliente.")

    # --- EXPORTACIÓN GENERAL ---
    # Convertimos los dos marcos de datos principales para unificarlos en la descarga
    csv_propuesta = pd.DataFrame({
        "Métrica General": [
            "Ajuste Total %", 
            "Valor TAM $", 
            "Valor SAM $", 
            "Valor SOM $", 
            "Validaciones (0-3)"
        ],
        "Resultado": [
            f"{encaje_total}%", 
            f"${valor_tam:,.2f}", 
            f"${valor_sam:,.2f}", 
            f"${valor_som:,.2f}", 
            validaciones
        ]
    })
    
    # Codificación de los datos a CSV
    csv_data = csv_propuesta.to_csv(index=False).encode('utf-8')
    
    st.write("") # Espaciador gráfico
    
    # Botón de descarga interactivo de Streamlit
    st.download_button(
        label="📥 Descargar Reporte Consolidado (CSV)",
        data=csv_data,
        file_name="reporte_estrategico_completo.csv",
        mime="text/csv",
    )
