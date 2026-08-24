import streamlit as st
import pandas as pd

# Configuración de la interfaz
st.set_page_config(page_title="Matriz de Propuesta de Valor Pro v2", layout="wide")

st.title("🎯 Matriz de Propuesta de Valor Inteligente")
st.subheader("Consola de diagnóstico cuantitativo y validación de hipótesis de mercado")

# --- CONTROL DEL ESTADO DE LA SESIÓN (Limpieza de campos) ---
if "analizado" not in st.session_state:
    st.session_state.analizado = False

# Función para resetear todos los campos del formulario utilizando sus llaves (keys)
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

# --- FORMULARIO PRINCIPAL DE ENTRADA ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👤 Perfil del Cliente (El Mercado)")
    trabajos = st.text_area(
        "**Trabajos del Cliente (Customer Jobs)**", 
        placeholder="¿Qué tareas, necesidades o problemas intenta resolver el cliente?",
        key="txt_trabajos"
    )
    
    st.divider()
    dolores = st.text_area(
        "**Dolores (Pains)**", 
        placeholder="¿Qué frustraciones, obstáculos o riesgos teme el cliente?",
        key="txt_dolores"
    )
    gravedad_dolor = st.selectbox(
        "¿Qué tan grave es este dolor para el cliente?",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["Insignificante", "Leve", "Moderado", "Frustrante", "Crítico"][x-1],
        key="grav_dolor"
    )
    
    st.divider()
    alegrias = st.text_area(
        "**Alegrías (Gains)**", 
        placeholder="¿Qué beneficios o resultados positivos espera obtener el cliente?",
        key="txt_alegrias"
    )
    relevancia_alegria = st.selectbox(
        "¿Qué tan importante es este beneficio para el cliente?",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["Irrelevante", "Secundario", "Deseable", "Muy Necesario", "Esencial"][x-1],
        key="rel_alegria"
    )

with col2:
    st.markdown("### 📦 Mapa de Valor (Tu Solución)")
    productos = st.text_area(
        "**Productos y Servicios**", 
        placeholder="¿Qué características u ofertas componen tu solución?",
        key="txt_productos"
    )
    
    st.divider()
    aliviadores = st.text_area(
        "**Aliviadores de Dolor (Pain Relievers)**", 
        placeholder="¿Cómo tu producto elimina o reduce las frustraciones descritas a la izquierda?",
        key="txt_aliviadores"
    )
    efectividad_aliviador = st.selectbox(
        "¿Qué tan efectivo es tu producto aliviando ese dolor?",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["No lo alivia", "Mínimo", "Parcial", "Efectivo", "Eliminación Total"][x-1],
        key="efec_aliv"
    )
    
    st.divider()
    creadores = st.text_area(
        "**Creadores de Alegrías (Gain Creators)**", 
        placeholder="¿Cómo tu solución potencia o genera las alegrías que el cliente espera?",
        key="txt_creadores"
    )
    efectividad_creador = st.selectbox(
        "¿Qué tan efectivo es tu producto creando esa alegría?",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - " + ["No aporta", "Insignificante", "Moderado", "Gran Creador", "Supera Expectativas"][x-1],
        key="efec_crea"
    )

st.divider()

# --- VALIDACIÓN AVANZADA EN EL MERCADO (Lean Startup Check) ---
st.markdown("### 🔍 Checklist de Validación en el Mundo Real")
st.caption("Responde con honestidad si ya has verificado estas hipótesis fuera de tu oficina.")
v1 = st.checkbox("¿Has hablado con al menos 10 clientes potenciales que confirmen que este dolor es real?", key="v1")
v2 = st.checkbox("¿El cliente está buscando activamente o pagando por soluciones alternativas actualmente?", key="v2")
v3 = st.checkbox("¿Has presentado un prototipo o MVP y los clientes han mostrado intención de compra?", key="v3")

st.divider()

# --- BOTONES DE CONTROL DE LA APLICACIÓN ---
btn_col1, btn_col2, _ = st.columns([2, 2, 5])
with btn_col1:
    activar_analisis = st.button("📊 Evaluar Ajuste y Generar Reporte", type="primary")
with btn_col2:
    st.button("🗑️ Limpiar Formulario", on_click=limpiar_formulario)

if activar_analisis:
    if not (trabajos and dolores and alegrias and productos and aliviadores and creadores):
        st.warning("⚠️ Por favor, completa todos los campos de texto antes de generar el reporte.")
        st.session_state.analizado = False
    else:
        st.session_state.analizado = True

# --- RENDERIZADO DE RESULTADOS ---
if st.session_state.analizado:
    st.success("✅ ¡Reporte Estratégico Generado Exitosamente!")
    
    # Cálculos analíticos de encaje
    puntuacion_dolor = min(100, int((efectividad_aliviador / gravedad_dolor) * 100)) if gravedad_dolor > 0 else 0
    puntuacion_alegria = min(100, int((efectividad_creador / relevancia_alegria) * 100)) if relevancia_alegria > 0 else 0
    
    # Penalización del índice de ajuste si no hay validación real en la calle (Checklist)
    validaciones_completadas = sum([v1, v2, v3])
    bono_validacion = validaciones_completadas * 5  # Máximo 15% de confianza por validación práctica
    
    encaje_base = int((puntuacion_dolor + puntuacion_alegria) / 2)
    encaje_total = min(100, encaje_base + bono_validacion) if encaje_base >= 40 else encaje_base

    # Mostrar métricas numéricas principales
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Encaje de Alivio de Dolores", value=f"{puntuacion_dolor}%")
    m2.metric(label="Encaje de Creación de Alegrías", value=f"{puntuacion_alegria}%")
    m3.metric(label="Índice de Ajuste de Mercado Total (Fit)", value=f"{encaje_total}%", delta=f"+{bono_validacion}% por Validación" if bono_validacion > 0 else None)
    
    # --- GRÁFICO DE BARRAS COMPARATIVO ---
    st.subheader("📊 Comparativa Cuantitativa: Mercado vs. Producto")
    
    # Crear estructura de datos limpia para graficar en Streamlit de forma nativa
    chart_data = pd.DataFrame({
        "Métrica": ["Dolor (Severidad)", "Aliviador (Efecto)", "Alegría (Relevancia)", "Creador (Efecto)"],
        "Puntuación (1-5)": [gravedad_dolor, efectividad_aliviador, relevancia_alegria, efectividad_creador]
    })
    # Transformamos el índice para un correcto renderizado del gráfico de barras horizontal
    chart_data = chart_data.set_index("Métrica")
    st.bar_chart(chart_data)

    # Diagnóstico comercial automatizado y personalizado
    st.subheader("💡 Diagnóstico del Mercado y Próximos Pasos")
    
    if encaje_total >= 85 and validaciones_completadas >= 2:
        st.balloons()
        st.success("**Ajuste Producto-Mercado Sólido (Luz Verde):** Tu propuesta de valor coincide matemáticamente con las urgencias del cliente y además cuentas con respaldo experimental en la calle. Es hora de acelerar el desarrollo o escalar ventas.")
    elif encaje_total >= 60:
        st.warning("**Ajuste de Escritorio o Teórico (Precaución):** Tu lógica matemática interna tiene buen sentido, pero necesitas salir al mercado a validar más hipótesis. Si tus checkboxes de validación están vacíos, recuerda que una buena idea en papel no garantiza compras reales.")
    else:
        st.error("**Ajuste Deficiente (Pivote Urgente):** Estás diseñando soluciones para dolores irrelevantes o tu producto no tiene la fuerza necesaria para curar las frustraciones descritas. Detén el desarrollo actual y reentrevista a tu segmento de clientes.")

    # --- EXPORTACIÓN DE ARCHIVO COMPLETO ---
    datos_matriz = {
        "Concepto de Negocio": [
            "Trabajos del Cliente", "Dolores del Cliente", "Alegrías del Cliente", 
            "Productos/Servicios", "Aliviadores de Dolor", "Creadores de Alegrías",
            "Entrevistas realizadas", "Análisis de competencia", "Pruebas de MVP",
            "Resultado: Ajuste de Dolores", "Resultado: Ajuste de Alegrías", "Índice de Ajuste Comercial Final"
        ],
        "Detalle Registrado": [
            trabajos, dolores, alegrias, productos, aliviadores, creadores,
            "Sí" if v1 else "No", "Sí" if v2 else "No", "Sí" if v3 else "No",
            f"{puntuacion_dolor}%", f"{puntuacion_alegria}%", f"{encaje_total}%"
        ]
    }
    
    df_export = pd.DataFrame(datos_matriz)
    csv_data = df_export.to_csv(index=False).encode('utf-8')
    
    st.write("") 
    st.download_button(
        label="📥 Descargar Reporte y Matriz Completa (CSV)",
        data=csv_data,
        file_name="reporte_propuesta_valor_avanzado.csv",
        mime="text/csv",
    )
