import streamlit as st

from agente import crear_agente_tutor

st.set_page_config(
    page_title="Agente Tutor de IA",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Agente Tutor de Inteligencia Artificial")

st.write(
    "Escribe un tema, selecciona tu nivel y el agente lo explicará "
    "con un ejemplo y una pregunta de evaluación."
)

nivel = st.selectbox(
    "Selecciona el nivel del estudiante",
    ["Principiante", "Intermedio", "Avanzado"],
)

tema = st.text_input(
    "Tema que deseas aprender",
    placeholder="Ejemplo: aprendizaje supervisado",
)

if st.button("Explicar tema", type="primary"):
    if not tema.strip():
        st.warning("Escribe un tema antes de continuar.")
    else:
        mensaje = f"""
        Tema: {tema}
        Nivel: {nivel}
        """
        with st.spinner("El agente tutor está pensando..."):
            try:
                agente = crear_agente_tutor()
                respuesta = agente.run(mensaje)
                st.markdown(respuesta.content)
            except Exception as e:
                st.error(f"Error al conectar con Groq: {e}")
                st.info(
                    "Verifica que la clave de API de Groq sea correcta."
                )
