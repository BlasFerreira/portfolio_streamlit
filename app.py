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


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ 3 years of web scraping experience
- ✔️ 4 months of comprehensive strategic data analysis service
- ✔️ Good understanding of statistical principles and their respective applications
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming Language: Python, SQL, R, C.
- 📊 Data Visulization:  Plotly, Matplotlib.
- 📚 Machine Learning : Supervised and Unsupervised

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
- ► Extensive experience as a freelancer in Data Science projects. Autonomous, collaborative work and delivering efficient solutions in data analysis, modeling and visualization.
- ► Web scraping
- ► machine learning modeling
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




# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
