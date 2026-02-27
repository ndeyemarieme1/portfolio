import streamlit as st
st.set_page_config(page_title="Portfolio Mariéme", layout="wide")

# ===== SIDEBAR =====
# Photo
st.sidebar.image("image/photo_marieme.jpeg", width=150)

st.sidebar.title("Ndéye Mariéme MBAYE")

st.sidebar.markdown("""
Étudiante en 2ème année de Géomatique  
Dakar, Sénégal  

Email : ndeyemariemem21@email.com  
LinkedIn : [Voir mon profil LinkedIn](https://linkedin.com/in/ndeye-marieme-mbaye)  
GitHub : [Voir mes projets GitHub](https://github.com/ndeyemarieme1)
""")

# ===== PAGE PRINCIPALE =====

st.title("Portfolio")

# Présentation
st.header("Présentation")

st.write("""
Je suis étudiante en deuxième année de Géomatique.
Je m’intéresse particulièrement à l’analyse spatiale, 
la cartographie numérique et le traitement des données géospatiales.
Mon objectif est de développer des solutions numériques 
dans le domaine des Systèmes d’Information Géographique.
""")

# Compétences
st.header("Compétences")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Compétences techniques")
    st.write("""
    - Python
    - Streamlit
    - ArcGIS
    - QGIS
    - Analyse spatiale
    - Cartographie thématique
    - Word
    - Power point
    - Excel
    - SQL
    - PostgreSQL
    - Manipulation de données
    - Structuration de bases de données
    """)

with col2:
    st.subheader("Compétences académiques")
    st.write("""
    - Hydrologie
    - Géodynamique interne
    - Roches et processus sédimentaires
    - Cartographie
    """)

# Expériences
st.header("Expériences professionnelles")

st.subheader("Stage - DGPRE")
st.write("""
- Traitement et organisation des données hydrologiques
- Production de cartes thématiques
- Appui à l’analyse spatiale
""")

st.subheader("Stage - Ministère des Transports - Kaolack")
st.write("""
- Collecte et structuration des données territoriales
- Contribution à l’analyse spatiale
""")

# Projets
st.header("Projets réalisés")

st.write("""
- Réalisation de cartes thématiques sous QGIS
- Analyse hydrologique sous ArcMap
- Développement d’un portfolio avec Streamlit
- Etude académiqe portant sur l'évaluation de la couverture spatiale des infrastructures sanitaires dans la commune de kaolack

""")

st.header("Rapports & Documents")

with open("document/Rapport de stage.docx", "rb") as file:
    st.download_button(
        label="📄 Télécharger mon rapport de stage",
        data=file,
        file_name="Rapport_de_stage_Marieme.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
with open("document/Rapport du travail.docx", "rb") as file:
    st.download_button(
        label="📄 Télécharger mon rapport du travail",
        data=file,
        file_name="Rapport_du_travail_Marieme.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

