from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ferreira Blas Facundo"
PAGE_ICON = ":wave:"
NAME = "Ferreira Blas Facundo"
DESCRIPTION = """
Data Scientist • Machine Learning • Web scraping • Freelancer • Deep Learning.
"""
EMAIL = "fblasfacundo@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/blasferreira/",
    "GitHub": "https://github.com/BlasFerreira",
    "Twitter": "https://twitter.com/Blasferreirafac",
}

PROJECTS = {
    "🏆 Digit recognizer with deep learning ": "https://blasferreira-tensorflowmnist-main-m6hswf.streamlit.app/",
    "🏆 Extract examples of linguee and PROMT " : "https://webextraction.streamlit.app/",
    "🏆 ship monitoring " : "https://blnqlyx1yu6ubrzt.maps.arcgis.com/apps/dashboards/0f1a827114b04a0d92f4560833e7eb16"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """

- ► Programming Languages: Python, R, and C

- ► Database : SQL, MySQL,CSV.

- ► Libraries and Frameworks:Pandas, NumPy,Request y Beautiful Soup.

- ► Machine Learning :TensorFlow, PyTorch, Scikit Learn y Keras.

- ► Natural Language Processing (NLP): Hugging Face, NLTK, spaCy y Gensim.

- ► Business Intelligence and Visualization: Power BI, Matplotlib y Seaborn.

- ► Cloud Platforms: Azure

- ► Tools and Platforms: Git & GitHub

- ► Development Environments: Visual Studio Code, Jupyter Notebook, Colab

- ► Web Scraping


"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write('\n')
st.write("🚧", "**Data Scientist | freelancer**")
st.write("01/2018 - Present")
st.write(
    """
- ► Web scraping: Data extraction with Python, BeautifulSoup and Scrapy.
- ► Data analysis: Use of Python, R, pandas, NumPy, matplotlib and seaborn for statistical analysis and visualization.
- ► Machine learning models: Model building with TensorFlow, Keras, scikit-learn and traditional algorithms.
- ► Presentation of analysis on web pages: Development of interactive visualizations using Streamlit to create interactive web applications.
- ► Process automation: Automation of tasks using scripts and programming tools.
- ► SQL database management: Database design, queries and data manipulation using MySQL, PostgreSQL and SQL Server.
- ► Azure experience: Use of services such as Azure Machine Learning, Azure Data Factory and Azure Functions for cloud projects.
"""
)

# --- JOB 2
st.write("🚧", "**Data Scientist | Analytics Town**")
st.write("09/2022 - 12/2022")
st.write(
    """
- ► My work gave the company the ability to make more informed and strategic business decisions, based on accurate data analysis.
- ► I am proud to have presented the results in a clear and accessible way, facilitating understanding and effective decision making by the team.
- ► My contribution helped the growth and success of the company, generating higher revenues and strengthening its position in the market.
"""
)

# --- JOB 3
st.write("🚧", "**Electronic Operator | Convex**")
st.write("01/01/2020 - 15/01/2021")
st.write(
    """
- ► Meticulously fabricated Industrial Battery Chargers, ensuring precision and innovation.
"""
)

# --- JOB 4
st.write("🚧", "**Maintenance Technician | Service & Solutions**")
st.write("01/01/2018 - 01/06/2019")
st.write(
    """
- ► Conducted both preventive and corrective maintenance for electrical and IT installations at a Banco Macro branch.
- ► Bolstered operational resilience, ensuring seamless infrastructure functioning.
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
