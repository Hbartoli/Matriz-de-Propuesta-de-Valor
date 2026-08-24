import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Matriz de Propuesta de Valor Pro", layout="wide")

st.title("🎯 Matriz de Propuesta de Valor Avanzada")
st.subheader("Evalúa cuantitativa y cualitativamente el encaje de tu Producto-Mercado")

# Inicializar estados de la sesión para persistencia de datos
if "analizado" not in st.session_state:
    st.session_state.analizado = False

# Dividir la interfaz en dos columnas visuales
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👤 Perfil del Cliente")
    trabajos = st.text_area(
        "**Trabajos del Cliente (Customer Jobs)**", 
        placeholder="¿Qué tareas o necesidades intenta resolver tu cliente en su día a día?"
    )
    
    st.divider()
    dolores = st.text_area(
        "**Dolores (Pains)**", 
        placeholder="¿Qué le frustra, le molesta o qué riesgos teme el cliente?"
    )
    gravedad_dolor = st.selectbox(
        "¿Qué tan grave es este dolor para el cliente?",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["Insignificante", "Leve", "Moderado", "Frustrante", "Crítico/Insoportable"][x-1],
        key="grav_dolor"
    )
    
    st.divider()
    alegrias = st.text_area(
        "**Alegrías (Gains)**", 
        placeholder="¿Qué resultados concretos o beneficios espera obtener el cliente?"
    )
    relevancia_alegria = st.selectbox(
        "¿Qué tan importante es este beneficio para el cliente?",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["Irrelevante", "Secundario", "Deseable", "Muy Necesario", "Esencial/Vital"][x-1],
        key="rel_alegria"
    )

with col2:
    st.markdown("### 📦 Mapa de Valor (Tu Producto)")
    productos = st.text_area(
        "**Productos y Servicios**", 
        placeholder="¿Qué vendes u ofreces específicamente para ayudar al cliente?"
    )
    
    st.divider()
    aliviadores = st.text_area(
        "**Aliviadores de Dolor (Pain Relievers)**", 
        placeholder="¿Cómo tu producto mitiga las frustraciones y dolores descritos a la izquierda?"
    )
    efectividad_aliviador = st.selectbox(
        "¿Qué tan efectivo es tu producto aliviando ese dolor?",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["No lo alivia", "Alivio mínimo", "Alivio parcial", "Alivio efectivo", "Elimina el dolor por completo"][x-1],
        key="efec_aliv"
    )
    
    st.divider()
    creadores = st.text_area(
        "**Creadores de Alegrías (Gain Creators)**", 
        placeholder="¿Cómo tu solución potencia las alegrías y beneficios que el cliente espera?"
    )
    efectividad_creador = st.selectbox(
        "¿Qué tan efectivo es tu producto creando esa alegría?",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["No aporta valor", "Aporte insignificante", "Aporte moderado", "Gran creador de valor", "Supera todas las expectativas"][x-1],
        key="efec_crea"
    )

st.divider()

# Botón principal de análisis
if st.button("📊 Evaluar Ajuste y Generar Reporte", type="primary"):
    if not (trabajos and dolores and alegrias and productos and aliviadores and creadores):
        st.warning("⚠️ Por favor, completa todos los campos de texto antes de evaluar.")
        st.session_state.analizado = False
    else:
        st.session_state.analizado = True

# Si ya se hizo clic y los datos son válidos, renderizamos los resultados y descargas
if st.session_state.analizado:
    st.success("✅ ¡Análisis Cuantitativo Generado!")
    
    # Cálculos matemáticos del encaje
    # El encaje perfecto ocurre cuando la efectividad de la solución empata o supera la intensidad del mercado
    puntuacion_dolor = min(100, int((efectividad_aliviador / gravedad_dolor) * 100)) if gravedad_dolor > 0 else 0
    puntuacion_alegria = min(100, int((efectividad_creador / relevancia_alegria) * 100)) if relevancia_alegria > 0 else 0
    encaje_total = int((puntuacion_dolor + puntuacion_alegria) / 2)
    
    # Mostrar métricas visuales
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Encaje de Alivio de Dolores", value=f"{puntuacion_dolor}%")
    m2.metric(label="Encaje de Creación de Alegrías", value=f"{puntuacion_alegria}%")
    m3.metric(label="Índice de Ajuste Total (Fit)", value=f"{encaje_total}%")
    
    # Diagnóstico automático basado en los puntajes
    st.subheader("💡 Diagnóstico del Mercado")
    if encaje_total >= 85:
        st.balloons()
        st.success("**Encaje Excelente:** Tu propuesta de valor está sumamente alineada con dolores reales y críticos del mercado. Tienes luz verde para proceder a prototipar o vender.")
    elif encaje_total >= 50:
        st.warning("**Encaje Moderado:** Resuelves problemas del cliente, pero tal vez estás sobrevalorando tu solución o enfocándote en dolores muy leves. Intenta pivotar o ajustar las características clave.")
    else:
        st.error("**Encaje Débil:** Cuidado. Estás construyendo algo que el mercado no considera urgente ni valioso. Revisa tus hipótesis antes de gastar presupuesto.")

    # --- SISTEMA DE EXPORTACIÓN A CSV ---
    # Creación del DataFrame con los datos actuales
    datos_matriz = {
        "Elemento de la Matriz": [
            "Trabajos del Cliente", 
            "Dolores del Cliente", 
            "Alegrías del Cliente", 
            "Productos y Servicios", 
            "Aliviadores de Dolor", 
            "Creadores de Alegrías",
            "Métrica: Ajuste de Dolores",
            "Métrica: Ajuste de Alegrías",
            "Métrica: Índice de Ajuste Total"
        ],
        "Detalle / Descripción": [
            trabajos, dolores, alegrias, productos, aliviadores, creadores, 
            f"{puntuacion_dolor}%", f"{puntuacion_alegria}%", f"{encaje_total}%"
        ],
        "Puntuación de Importancia (1-5)": [None, gravedad_dolor, relevancia_alegria, None, None, None, None, None, None],
        "Puntuación de Solución (1-5)": [None, None, None, None, efectividad_aliviador, efectividad_creador, None, None, None]
    }
    
    df = pd.DataFrame(datos_matriz)
    csv_data = df.to_csv(index=False).encode('utf-8')
    
    st.write("") # Espaciador gráfico
    # Botón nativo para descargar el archivo CSV sin recargar la página
    st.download_button(
        label="📥 Descargar Matriz en Formato CSV",
        data=csv_data,
        file_name="matriz_propuesta_valor.csv",
        mime="text/csv",
    )
