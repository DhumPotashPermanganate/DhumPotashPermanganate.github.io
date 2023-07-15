import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander

#test

# Set page title
st.set_page_config(page_title="Arijeet Dasgupta", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 Arijeet Dasgupta';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_utown = Image.open("images/utown.jpg")
img_lh = Image.open("images/lh.jpg")
img_ifg = Image.open("images/ifg.jpg")
#Assets for competitions
img_lit = Image.open("images/legalease.jpg")
img_lifehack2 = Image.open("images/lifehack2.jpg")
img_lifehack = Image.open("images/lifehack.jpg")
img_he4d = Image.open("images/he4d.jpg")
img_ecc = Image.open("images/ecc.jpg")
img_shopee = Image.open("images/shopee.png")
img_sbcc = Image.open("images/sbcc.png")
img_runes = Image.open("images/runes.png")
# Assets for education
img_sji = Image.open("images/sji.jpg")
img_tpjc = Image.open("images/tpjc.jpg")
img_fiem = Image.open("images/fiem.jpg")
img_poc = Image.open("images/poc.jpg")
img_gmss = Image.open("images/gmss.jpg")
img_sjij = Image.open("images/sjij.jpg")
img_dsa = Image.open("images/dsa.jpg")
# Assets for Certification
img_aws = Image.open("images/aws.png")
img_ud1 = Image.open("images/ud1.jpg")
img_ud2 = Image.open("images/ud2.jpg")
img_ud3 = Image.open("images/ud3.jpg")
img_ud4 = Image.open("images/ud4.jpg")
img_ud5 = Image.open("images/ud5.jpg")
img_ud6 = Image.open("images/ud6.jpg")
img_ud7 = Image.open("images/ud7.jpg")
img_np1 = Image.open("images/nptel1.png")
img_np2 = Image.open("images/nptel2.png")
img_np3 = Image.open("images/nptel3.png")
# Assets for experiences
img_mm = Image.open("images/mm.png")
img_iasg = Image.open("images/iasg.jpg")
img_epam = Image.open("images/epam.png")
img_yll = Image.open("images/yll.jpg")
img_saf = Image.open("images/saf.jpg")
img_cognizant = Image.open("images/cognizant.png")
# Assets for projects
image_names_projects = ["ecom", "chatgpt", "videogames", "health", 
                         "biopics", "anime", "word2vec", "cellphone", 
                         "spotify", "map", "gephi", "fob", "get", "ttdb",
                         "blockchain"]
images_projects = [Image.open(f"images/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_projects]
# Assets for volunteering
image_names_vol = ["sdslogo", "sportslogo", "gdsclogo", "csclogo", 
                         "nussulogo", "sklogo", "simlogo", "tpjclogo", 
                         "sjilogo", "nuspc"]
images_vol = [Image.open(f"images/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_vol]
# Assets for blog
img_qb = Image.open("images/qb.jpg")
img_mayans = Image.open("images/mayans.jpg")
img_outlier = Image.open("images/outlier.png")
img_dac = Image.open("images/dac.png")
img_raffles = Image.open("images/raffles.jpg")
img_covid = Image.open("images/covid.jpg")
img_gender = Image.open("images/gender.jpg")
img_hci = Image.open("images/hci.jpg")
img_wordcloud = Image.open("images/wordcloud.jpg")
img_taste = Image.open("images/taste.jpg")
img_measles = Image.open("images/measles.jpeg")
img_bmsaew = Image.open("images/bmsaew.png")
img_dac1 = Image.open("images/dac1.png")
img_dac2 = Image.open("images/dac2.png")
# Assets for gallery
# 2005
img_2005_1 = Image.open("gallery/2005_1.jpg")
img_2005_2 = Image.open("gallery/2005_2.jpg")
# 2006
img_2006_1 = Image.open("gallery/2006_1.jpg")
# 2008
img_2008_1 = Image.open("gallery/2008_1.jpg")
# 2009
img_2009_1 = Image.open("gallery/2009_1.jpg")
# 2011
image_dict = {}
num_images = 4
for i in range(1, num_images + 1):
    image_key = f"img_2011_{i}"
    image_path = f"gallery/2011_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
# 2012 
image_dict = {}
num_images = 7
for i in range(1, num_images + 1):
    image_key = f"img_2012_{i}"
    image_path = f"gallery/2012_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
# 2013
image_dict = {}
num_images = 11
for i in range(1, num_images + 1):
    image_key = f"img_2013_{i}"
    image_path = f"gallery/2013_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
# 2014
image_dict = {}
num_images = 13
for i in range(1, num_images + 1):
    image_key = f"img_2014_{i}"
    image_path = f"gallery/2014_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
# 2015
image_dict = {}
num_images = 48
for i in range(1, num_images + 1):
    image_key = f"img_2015_{i}"
    image_path = f"gallery/2015_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
# 2016
image_dict = {}
num_images = 25
for i in range(1, num_images + 1):
    image_key = f"img_2016_{i}"
    image_path = f"gallery/2016_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
# 2017
image_dict = {}
num_images = 4
for i in range(1, num_images + 1):
    image_key = f"img_2017_{i}"
    image_path = f"gallery/2017_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
# 2018
image_dict = {}
num_images = 16
for i in range(1, num_images + 1):
    image_key = f"img_2018_{i}"
    image_path = f"gallery/2018_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
# 2019
image_dict = {}
num_images = 20
for i in range(1, num_images + 1):
    image_key = f"img_2019_{i}"
    image_path = f"gallery/2019_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
#2020
image_dict = {}
num_images = 3
for i in range(1, num_images + 1):
    image_key = f"img_2020_{i}"
    image_path = f"gallery/2020_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
#2021
image_dict = {}
num_images = 14
for i in range(1, num_images + 1):
    image_key = f"img_2021_{i}"
    image_path = f"gallery/2021_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
#2022
image_dict = {}
num_images = 19
for i in range(1, num_images + 1):
    image_key = f"img_2022_{i}"
    image_path = f"gallery/2022_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
#2023
image_dict = {}
num_images = 11
for i in range(1, num_images + 1):
    image_key = f"img_2023_{i}"
    image_path = f"gallery/2023_{i}.jpg"
    image_dict[image_key] = Image.open(image_path)
#img_lottie_animation = Image.open("images/lottie_animation.gif")
# Assets for contact
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

img_linkedin = Image.open("images/linkedin.png")
img_github = Image.open("images/github.png")
img_email = Image.open("images/email.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "youtube": "https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png",
                "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                "wordpress": "https://img.icons8.com/ios-filled/100/ff8c00/wordpress--v1.png",
                "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')   


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_lh, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "Arijeet Dasgupta", 
                        ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Competitions", "Blog", "Gallery", "Resume", "Contact"],
                         icons=['person fill', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'pencil square', 'image', 'paperclip', 'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f5f5dc"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )
    youtube_url = "https://www.youtube.com/@harrychangjr"
    linkedin_url = "https://www.linkedin.com/in/harrychangjr/"
    github_url = "https://github.com/harrychangjr"
    wordpress_url = "https://antcabbage.wordpress.com"
    email_url = "mailto:harrychang.work@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, Youtube=youtube_url, LinkedIn=linkedin_url, GitHub=github_url, Wordpress=wordpress_url, Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Arijeet Dasgupta")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Aspiring Data Engineer/Cloud Architect")
            st.write("👋🏻 Hi, I'm Arijeet! I am a Data Engineer currently working at Cognizant Technology Solutions. I have just began my tech journey as an IT professional and am constantly looking for opportunites to grow and learn.")
            st.write("💼 As a data engineer, my work is crucial in enabling organizations to harness the power of data. I design and build the infrastructure that allows for efficient and reliable data processing, storage, and retrieval. By creating robust data pipelines, I ensure that data flows seamlessly from various sources, undergoes necessary transformations, and is made available to data scientists, analysts, and decision-makers in a timely manner. In essence, my role as a data engineer is vital for unlocking the true potential of data and driving success in a data-driven world.")
            st.write("🏋🏻 In addition, I like to play and watch sports (Football, the most), play video games (mostly FIFA). I like to visit several eateries as I always appreciate some good food. !")
            st.write("👨🏼‍💻 Academic interests: Data Analysis, Cloud Architecture, Machine Learning, Big Data")
            st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, Data Engineer, Cloud Architect")
            st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/1n4TQxDkn98Tu5i2--aNKbK-JvP7xGcDe/view?usp=drive_link)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_utown)
# elif choose == "Site Overview":
#     #overview.createPage()
#     st.header("Site Overview")
#     st.markdown("""
#     Initally creating this as a portfolio website in the form of an extended resume, I came to discover the uniqueness of Streamlit as compared to typical front-end frameworks such as Angular and Bootstrap. Even though Streamlit is primarily used as a web application for dashboarding, its extensive features make it more aesthetically appealing to explore with as compared to alternatives such as Plotly and Shiny.
#
#     With the convenience of using Python as a beginner-friendly programming language, I have now decided to evolve this personal project into a time capsule - documenting key moments and achievements that I have attained since commencing my formal education at 6 years old.
#
#     """)
#     with st.container():
#             col1, col2, col3 = st.columns((1,3,1))
#             with col1:
#                 st.empty()
#             with col2:
#                 st.video("https://youtu.be/1QlgizeKg44")
#             with col3:
#                 st.empty()
#     st.markdown("""
#     *For an optimal experience, do browse this site on desktop!*
#
#     Updated May 1, 2023
#     """)
# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_cognizant)
        with text_column:
            st.subheader("Programmer Analyst, [Cognizant](https://www.cognizant.com/us/en)")
            st.write("*September 2022 - (Ongoing)*")
            st.markdown("""
            - Getting trained as an Azure Data Engineer (Stack: PySpark, SparkSQL, Azure)
            - Trained and completed AWS Solutions Architect Associate SAA-C02

            `Python` `mySQL` `Apache Spark` `Azure` `AWS` `Hadoop`
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_mm)
        with text_column:
            st.subheader("Coding Instructor, [MarksMaster](https://marksmaster.business.site/)")
            st.write("*September 2020 - (Ongoing)*")
            st.markdown("""
            -  Curate several courses for different programming languages which includes several libraries of Python. Apart from that, C#, Java and C as well.
            -  Conduct 1:1 classes for programming bootcamps for students eager to start programming. Conducts group sessions as well. 
            -  Helps in creating solutions and projects to different problem statements.
            
            `Python` `Java` `C` `C++` `C#` `Arduino` `Scratch` 
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_epam)
        with text_column:
            st.subheader("Apprentice Trainee, [EPAM Systems](https://www.epam.com/)")
            st.write("*August 2020 - August 2021*")
            st.markdown("""
                - Trained in Java and Spring framework, enabling efficient and scalable development of robust and enterprise-level applications.
                - Trained in using Git and Maven for version control and dependency management, ensuring seamless collaboration and streamlined project development.
                - Trained in JUnit testing, ensuring code quality and reliability through comprehensive unit testing and test-driven development practices.
                
                `Java`, `Spring`, `GIT`, `Maven`, `Junit Testing`
            """)

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    txt3("Programming Languages", "`Python`, `SQL`, `Java`, `C#`, `C++`")
    txt3("Data Visualization", "`matplotlib`, `seaborn`, `Plotly`, `Dash`")
    txt3("Database Systems", "`MySQL`, `PostgreSQL`, `SQLite`, `NoSQL`")
    txt3("Cloud Platforms", "`Google Cloud Platform`, `Amazon Web Services`, `Azure`")
    txt3("Natural Language Processing", "`NLTK`")
    txt3("Version Control", "`Git`")
    txt3("Data Engineering", "`Spark`")
    txt3("Data Science Techniques", "`Regression`, `Clustering`, `Random Forest`, `Decison Trees`, `Sentiment Analysis`")
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`")
    txt3("Automation Library", "`Selenium`")
    txt3("Testing", "`JUnit`, `Nunit`, `Selenium`")
    txt3("Design and Front-end Development", "`HTML`, `CSS`, `Streamlit`, `Wordpress`")

# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    selected_options = ["Summary", "Certifications"
                        ]
    selected = st.selectbox("Which section would you like to read?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Summary":
        st.subheader("Summary")
        st.write("*Summary of education from primary school till university*")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_fiem)
            with text_column:
                st.subheader("Bachelor of Technology [Information Technology](https://futureeducation.in/b-tech/), [West Bengal University of Technology](https://makautwb.ac.in/) (2018-2022)")
                st.write("Relevant Coursework: Data Structures and Algorithms, Computer Organisation, IT Workshop, Python Lab, Discrete Mathematics, Automata Theory, Computer Architecture, Software Engineering, Compiler Design, Operating Systems, Distributed Systems, Data Warehousing and Data mining, Research Methodology")
                st.write("Final CGPA: 9.02")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_poc)
            with text_column:
                st.subheader("AISSCE, Class 12, [Kendriya Vidyalaya, Ballygunge](https://baligunge.kvs.ac.in/) (2016-2018)")
                st.write("Coursework: Physics, Chemistry, Computer Science, Mathematics, English")
                st.write("Final Marks: 76.4")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_tpjc)
            with text_column:
                st.subheader("AISSE, Class 10 - [Kendriya Vidyalaya, Ballygunge](https://baligunge.kvs.ac.in/) (2006 - 2016)")
                st.write("Coursework: English, Hindi, Science, Mathematics, Social Studies")
                st.write("Final CGPA: 9.6")

    elif selected == "Certifications":
        st.subheader("Certifications")
        st.write("*Summary of all the certifications done till date*")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_aws)
            with text_column:
                st.subheader(
                    "AWS Certified Solutions Architect Associate SAA-C02")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_np1)
            with text_column:
                st.subheader(
                    "NPTEL Joy of Computing using Python")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_np2)
            with text_column:
                st.subheader(
                    "NPTEL An Introduction to Programming through C++")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_np3)
            with text_column:
                st.subheader(
                    "NPTEL Enhanching Soft Skills and Personality")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_ud1)
            with text_column:
                st.subheader(
                    "Data Anaylysis with Pandas and Python")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_ud2)
            with text_column:
                st.subheader(
                    "Data Visualisation using Python for Beginners")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_ud3)
            with text_column:
                st.subheader(
                    "Complete course on Data Visualisation, MatPlotLib and Python")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_ud4)
            with text_column:
                st.subheader(
                    "Interactive Python Dashboards with PlotLy and Dash")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_ud5)
            with text_column:
                st.subheader(
                    "Python for Beginners: Learn Python Programming")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_ud6)
            with text_column:
                st.subheader(
                    "Python for Programmers")
        with st.container():
            image_column, text_column = st.columns((1, 2.5))
            with image_column:
                st.image(img_ud7)
            with text_column:
                st.subheader(
                    "The Complete SQL Bootcamp 2022: Go from Zero to Hero")




elif choose == "Projects":
    # Create section for Projects
    #st.write("---")
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Blockchain Social Media Webscraper")
            st.write("*Project for US-based stealth startup, Bitmetrix.ai (in progress)*")
            st.markdown("""
            - Utilised snscrape to scrape tweets from top blockchain websites such as CoinGecko and CoinMarketCap
            - Built webscraper using BeautifulSoup4 to scrape content from fintech news websites such as https://blockchain.news
            """)
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/blockchain-webscraping",)
        with image_column:
            st.image(images_projects[14])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Enhanced TikTok Analytics Dashboard")
            st.write("*Self-initiated project*")
            st.markdown("""
            - Provided options to plot Tiktok user overview data using 3D lineplots, 3D scatterplots, 3D surfaceplots and radar chart from Plotly
            - Filtered number of hashtags per Tiktok video to investigate relationship between hashtag count and other variables: views, comments, likes and shares
            - Performed hashtag analysis using Word2Vec to calculate cosine similarity scores and deduce correlation with average performance scores of each hashtag
            """)
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            mention(label="Streamlit App", icon="streamlit", url="https://huggingface.co/spaces/harrychangjr/tiktok_analytics",)
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/tiktok-analytics",)
        with image_column:
            st.image(images_projects[13])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Creating Sales Volume Prediction Model with Regression Methods")
            st.write("*Self-initiated project based on e-commerce case study*")
            st.markdown("""
            - Conducted exploratory data analysis (EDA) to identify relationships between variables using correlation heatmaps and histograms
            - Trained and compared multiple regression, random forest and XGBoost to build optimal model for sales volume prediction
            - Performed randomized search with cross-validation to increase performance of random forest regressor and reduce MSE
            """)
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/sales-prediction",)
        with image_column:
            st.image(images_projects[0])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Optimising Article Quality with ChatGPT and NLP")
            st.write("*Self-initiated project using past articles written for module SP1541: Exploring Science Communication in Popular Science in Academic Year 2020/21 Semester 1*")
            st.markdown("""
            - Preliminary analysis - comparing word counts, readability scores and sentiment (compound) scores of all 6 article variants using NLTK and Textstat
            - Generated word clouds to highlight frequently used words in each article variant
            - Identified top 10 most commonly used words between variants of the same article to assess suitability of ChatGPT in enhancing article quality
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/sp1541-nlp)")
            mention(label="Streamlit App", icon="streamlit", url="https://sp1541-nlp.streamlit.app",)
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/sp1541-nlp",)
        with image_column:
            st.image(images_projects[1])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Statistical Learning: Analysis on Video Game Sales")
            st.write("*Completed project within 48 hours for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2*")
            #st.write("Methods performed on [Kaggle dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings):")
            st.markdown("""
            - Utilised multiple regression to investigate impact of publishers on global sales by regression coefficient, including performing one-hot encoding on 'Publisher' categorical variable
            - Compared performances of multiple linear regression, random forest and XGBoost to predict global sales using critic scores and user scores from Metacritic
            - Trained linear mixed-effects model to investigate impact of publishers, platform and genres in global sales
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/st4248-termpaper) | [Term Paper](https://github.com/harrychangjr/st4248-termpaper/blob/main/ST4248%20Term%20Paper%20(A0201825N)%20v5.pdf)")
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/st4248-termpaper",)
        with image_column:
            st.image(images_projects[2])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Statistical Learning: Nourish Your Body with Data")
            st.write("*Completed group project for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2*")
            st.markdown("""
            - Adapted [previous project](https://drive.google.com/file/d/10ZOdQ8Q7UnevXxODAQs1YOstNSsiKh7G/view?usp=sharing) from DSA3101: Data Science in Practice, with the usage of statistical learning methods instead
            - Performed random forest classification and clustering methods to identify different consumer segments of grocery shoppers in supermarkets
            - Built recommendation system using matrix factorisation to recommend healthier food alternatives for grocery shoppers from different backgrounds
            """)
            #st.write("[Final Report](https://drive.google.com/file/d/1YuYxSTuDstSvyUa-bn782sLE5kCfbyH8/view?usp=sharing) | [Pitch Deck](https://www.canva.com/design/DAFeSnJeqgM/uXpz0kw8e7If4T1PG2tpaQ/view?utm_content=DAFeSnJeqgM&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Product Demo](https://www.youtube.com/watch?v=XMlt-kfdC7g)")
            mention(label="Final Report", icon="📄", url="https://drive.google.com/file/d/1YuYxSTuDstSvyUa-bn782sLE5kCfbyH8/view?usp=sharing",)
        with image_column:
            st.image(images_projects[3])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data Science Project on Biopics Dataset from Kaggle")
            st.write("*Self-initiated project using various machine learning methods on [biopics dataset](https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-biopics-dataset)*")
            st.markdown("""
            - Ran regression models to predict box office revenue (linear regression, random forest, support vector machines)
            - Used k-means clustering with principal components analysis to identify similar types of movies
            - Built content-based recommendation system using cosine similarity to recommend similar movies based on input title
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/biopics) | [RPubs](https://rpubs.com/harrychangjr/biopics)")
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/biopics",)
        with image_column:
            st.image(images_projects[4])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Optimisation for Large-Scale Data-Driven Inference: Anime Recommendation System")
            st.write("*Completed assignment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2*")
            st.markdown("""
            - Built recommendation system using various non-factor models, including content-based collaborative filtering and clustering
            - Utilised matrix factorisation (single value decomposition) to optimise performance of recommendation system with lower test MSE
            - Provided optional recommendations to further optimise performance e.g scraping additional data, using deep learning methods
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/dsa4212) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%202%20Group%2039%20Report.pdf)")
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/dsa4212",)
        with image_column:
            st.image(images_projects[5])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Optimisation for Large-Scale Data-Driven Inference: Word Embedding")
            st.write("*Completed assigmment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2*")
            st.markdown("""
            - Trained Word2Vec model on 20 Newsgroups dataset from scikit-learn package in Python, which provides a number of similar words based on input word
            - Evaluated usefulness of model by applying model to text classification (46% accuracy) and sentiment analysis (86.4% accuracy)
            """)
            #st.write("[Github Code](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039.ipynb) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039%20Report.pdf)")
            mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039.ipynb",)
        with image_column:
            st.image(images_projects[6])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data-Driven Marketing: Exploration of cellphone billing and subscriber data")
            st.write("*Self-initiated project based on past assignment from module BT4211: Data-Driven Marketing*")
            st.markdown("""
            - Performed preliminary churn analysis, customer segmentation and descriptive analysis to understand more about dataset
            - Trained logit and probit models, as well as providing model estimations for duration models
            - Utilised random forest classifier to predict customer churn
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/cellphone-billing) | [RPubs](https://rpubs.com/harrychangjr/cellphone)")
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/cellphone-billing",)
        with image_column:
            st.image(images_projects[7])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data Visualization: Analysis on Spotify Dataset from [tidytuesday](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-21)")
            st.write("*Completed group project for module DSA2101: Essential Data Analytics Tools: Data Visualization in Academic Year 2021/22 Semester 2*")
            st.markdown("""
            - Investigated variables that differentiates songs of different genres, which could be useful in designing recommendation systems
            - Explored how do the four seasons affect number of songs produced in each period
            - Visualizations used: ridgeline faceted density plot, boxplot, line chart, faceted donut chart
            """)
            #st.write("[Github Code](https://github.com/harrychangjr/dsa2101/blob/main/DSA2101_Group%20B.Rmd) | [RPubs](https://rpubs.com/harrychangjr/dsa2101-groupb)")
            mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/dsa2101/blob/main/DSA2101_Group%20B.Rmd",)
        with image_column:
            st.image(images_projects[8])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Computers and the Humanities: Chloropleths using Google Sheets and Folium in Python")
            st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
            st.markdown("""
            - Visualized the total number of performances of A Doll's House by country, using a chloropleth from Google Sheets
            - Drafted scatterplots and boxplots using seaborn to investigate relationship between number of events per country and number of years these plays have been performed
            - Created chloropleth using Folium in Google Colab to compare total performance counts in China, categorised by province
            """)
            #st.write("[Google Sheets](https://docs.google.com/spreadsheets/d/1NBlGM7Sjcybbpl1Esa55qLRJw-Seti1LhC93EhV_68w/edit?usp=sharing) | [Google Colab](https://colab.research.google.com/drive/1RHqtb5XC7PkJDpNEb-BY3tO-8mI2j32E?usp=sharing)")
            mention(label="Google Drive", icon="🗂️", url="https://drive.google.com/drive/folders/1Iva0oLZim6zJlAndoSzR63pUq4NCznim?usp=share_link",)
        with image_column:
            st.image(images_projects[9])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Computers and the Humanities: Network Analysis on Harry Potter Film Database")
            st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
            st.markdown("""
            - Utilised custom Python file based on NetworkX and Glob to create networks using Harry Potter film database
            - Drafted visualizations using matplotlib and seaborn to compare densities and weighted degree values of nodes from generated networks
            - Customised network visualization using Gephi to investigate relationship between various Harry Potter film directors
            """)
            #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N_GET1030_Tutorial_4.ipynb)")
            mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/get1030/blob/main/A0201825N_GET1030_Tutorial_4.ipynb",)
        with image_column:
            st.image(images_projects[10])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Computers and the Humanities: Text Processing and Analysis on Song Lyrics")
            st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
            st.markdown("""
            - Utilised custom Python file based on NetworkX and Glob to create networks using Harry Potter film database
            - Drafted visualizations using matplotlib and seaborn to compare proportions of nouns and verbs between different songs
            - Analysed type/token ratios of songs from both albums to evaluate which album produced better quality songs based on words used
            """)
            #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb)")
            mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb",)
        with image_column:
            st.image(images_projects[11])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Computers and the Humanities: Spotify in the Covid-19 Era")
            st.write("*Completed group project for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
            st.markdown("""
            - Compiled and scraped Spotify data from [Spotify](https://www.spotifycharts.com), [Kaggle](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks), and [OWID](https://ourworldindata.org/coronavirus/country/singapore) to analyse top songs played in Singapore during Covid-19
            - Drafted Tableau dashboard to showcase correlation between various features of top songs, including tempo, acousticness and popularity
            - Embedded 30-second snippet of featured song on dashboard for increased interactiveness
            """)
            #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb)")
            mention(label="Final Report", icon="📄", url="https://github.com/harrychangjr/get1030/blob/main/GET1030%20Final%20Project.pdf",)
        with image_column:
            st.image(images_projects[12])
    
elif choose == "Competitions":
    # Create section for Competitions
    #st.write("---")
    st.header("Competitions")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_lit)
            #st.empty()
        with text_column:
            st.subheader("[SMU-LIT Hackathon 2023](https://www.smulit.org/hackathon-2023/) - Hosted by [SMU Legal-in-Tech Club](https://smulit.org)")
            st.write("Built LegalEase with OpenAI - a Streamlit-based web application empowering lawyers in hybrid working environments with optimal task scheduling.")
            #st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/legalease",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_lifehack2)
            #st.empty()
        with text_column:
            st.subheader("[NUS LifeHack 2023](https://lifehack-website.web.app//) - Hosted by [NUS Students' Computing Club](https://nuscomputing.com/)")
            st.write("Awarded Top 15 Finalist out of 141 team submissions")
            st.write("Built and integrated PassionPassport with ChatGPT - a Streamlit-based web application that recommends travel locations based on one’s hobbies.")
            #st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
            mention(label="Github Repo", icon="github", url="https://github.com/BrendanCheong/lifehack-2023",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_lifehack)
        with text_column:
            st.subheader("[NUS LifeHack 2022](https://lifehack-2022.vercel.app/) - Hosted by [NUS Students' Computing Club](https://nuscomputing.com/)")
            st.write("Awarded Theme Best - Safety and Overall 2nd Place out of 117 team submissions")
            st.write("Ideated and developed Drive Woke! - a Flutter-based mobile application that aims to keep drivers awake by simulating conversations")
            #st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
            mention(label="Github Repo", icon="github", url="https://github.com/yuechen2001/LifeHack2022",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_he4d)
        with text_column:
            st.subheader("NUS Fintech Month Hackathon 2021 - Hosted by [NUS Fintech Society](https://fintechsociety.comp.nus.edu.sg/)")
            st.write("Awarded Overall 2nd Place")
            st.write("Ideated a multi-pronged approach using blockchain and machine learning methods to improve fraud detection amongst complex entities in a digital or hybrid (digital and manual) operating environment")
            #st.write("[Pitch Deck](https://www.linkedin.com/feed/update/urn:li:ugcPost:6761489595420037120/)")
            mention(label="Pitch Deck", icon="🪧", url="https://www.linkedin.com/feed/update/urn:li:ugcPost:6761489595420037120/)",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_ecc)
        with text_column:
            st.subheader("NUS Economics Case Competition - Hosted by [NUS Economics Society](https://www.nuseconsoc.com/)")
            st.write("Performed financial modelling and market research to suggest methods for brick-and-mortar retailers to compete against e-commerce stores")
            #st.write("[Report](https://drive.google.com/drive/u/4/folders/1NfsRr1P3xAkuJq3HEJ9LQU1uCo6TZIFK)")
            mention(label="Report", icon="📄", url="https://drive.google.com/drive/u/4/folders/1NfsRr1P3xAkuJq3HEJ9LQU1uCo6TZIFK",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_shopee)
        with text_column:
            st.subheader("[Shopee Product and Design Challenge 2021](https://careers.shopee.sg/event-detail/396)")
            st.write("Redesigned user interface of Shopee mobile app using Figma to reduce clutter and increase user utilization of in-app rewards")
            #st.write("[Figma Prototype](https://www.figma.com/proto/3UXT29N1RgVGDUlSBeWcPN/UI-Prototype-1?node-id=18-3&viewport=-675%2C231%2C0.32458001375198364&scaling=scale-down) | [Pitch Deck](https://drive.google.com/file/d/12qnveB-SMjG_gF_gwNj3Nr-JsKeyKd6g/view)")
            mention(label="Figma", icon="📱", url="https://www.figma.com/proto/3UXT29N1RgVGDUlSBeWcPN/UI-Prototype-1?node-id=18-3&viewport=-675%2C231%2C0.32458001375198364&scaling=scale-down",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_sbcc)
        with text_column:
            st.subheader("Singapore Business Case Competition 2020 - Hosted by [NTU Business Solutions Club](https://clubs.ntu.edu.sg/businesssolutions/)")
            st.write("Proposed solutions to help increase competitiveness of BreadTalk after performing market research and analysis on the F&B industry")
            #st.write("[Pitch Deck](https://drive.google.com/file/d/1kLgbBVuth4KvfhjaK00n30xlr4bmn-iM/view)")
            mention(label="Pitch Deck", icon="🪧", url="https://drive.google.com/file/d/1kLgbBVuth4KvfhjaK00n30xlr4bmn-iM/view",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_runes)
        with text_column:
            st.subheader("Contest 2.2 Beautiful Runes - CS1010S Programming Methodology")
            st.write("Awarded 1st Place for 2D Runes category out of over 600 students enrolled in the module for Academic Year 2020/21 Semester 1")
            st.write("2D pixel art created using Pillow (PIL) Library in Python")
            #st.write("[Github Repo](https://github.com/harrychangjr/runes)")
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/runes",)

elif choose == "Blog":
    st.header("Blog")
    selected_options = ["Overview", "Article & Essay List",
    #"“It’s not pink, it’s salmon” – Why I returned to my previous start-up for FREE", 
                        "Mayans MC – Season 5 Detailed Preview",
                        "Finding success as an outlier (Extracted Using Wordpress REST API)",
                        ]
    selected = st.selectbox("Which section or write-up would you like to read?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Overview":
        st.subheader("Overview")
        st.markdown("""
        I must admit - I hated reading books as a kid, and in turn, I disliked writing essays or expressing my thoughts as well. However, throughout my time in university, I have gradually picked up the essence of writing, to the extent of making use of it as a destressor from my technical modules.

        Although my writing skills were novice at best when I was a freshman, I eventually got better at it (in my opinion), even to the extent of writing content articles as a regular hobby! It is indeed an asset to pick up as many skills as possible when still young, as you never know when you may need to utilise a particular skill whenever necessary.

        In this section, you will be able to read some of my finest write-ups from my university experiences, based on topics varying from science to politics. For those looking forward to a good read, enjoy!
        """)

    elif selected == "Article & Essay List":
        st.subheader("Article & Essay List")
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_mayans)
            with text_column:
                st.subheader("Mayans MC - Season 5 Detailed Preview")
                st.write("*May 13, 2023* | [*Article*](https://antcabbage.wordpress.com/2023/05/13/mayans-mc-season-5-detailed-preview/)")
                st.write("A preview of the fifth and final season Mayans MC, along with its similarities with Sons of Anarchy")
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_outlier)
            with text_column:
                st.subheader("Finding success as an outlier")
                st.write("*April 12, 2023* | [*Article*](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
                st.write("A personal reflection of my tumultous undergraduate journey so far - and how I finally found my resolve")
                #st.write("[Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")       
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_raffles)
            with text_column:
                st.subheader("Essays for Final Test - GES1037: A History of Singapore in Ten Objects")
                st.write("*April 29, 2022* | [*Essays*](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Take%20Home%20Test.pdf)")
                st.markdown("""
                Essays written within 24-hour window in Academic Year 2021/22 Semester 2:
                - Q4: Should the statue of Sir Stamford Raffles disappear for good?
                - Q6: Should the Women's Charter replace one of the existing ten objects in the module? 
                """)       

    elif selected == "Mayans MC – Season 5 Detailed Preview":
        with st.echo(code_location="below"):
            import streamlit as st
            import requests
            from bs4 import BeautifulSoup

            def arrange_images_side_by_side(html_content):
                soup = BeautifulSoup(html_content, "html.parser")
                images = soup.find_all("img")

                i = 0
                while i < len(images) - 1:
                    current_image = images[i]
                    next_image = images[i + 1]

                    current_figure = current_image.find_parent("figure")
                    next_figure = next_image.find_parent("figure")

                    # Check if the next image is an immediate sibling
                    if current_figure and next_figure and current_figure.find_next_sibling() == next_figure:
                        container = soup.new_tag("div", style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center;")
                        current_figure.wrap(container)
                        next_figure.wrap(container)

                        # Set the same height for both images and add a little margin for better centering
                        current_image['style'] = "height: 400px; margin: auto;"
                        next_image['style'] = "height: 400px; margin: auto;"

                        # Update the images list
                        images = soup.find_all("img")
                    i += 1

                return str(soup)

            def get_post_by_id(url, post_id):
                site_url = url.replace("https://", "").replace("http://", "")
                response = requests.get(f"https://public-api.wordpress.com/wp/v2/sites/{site_url}/posts/{post_id}?_embed")
                response.raise_for_status()
                return response.json()

            url = "https://antcabbage.wordpress.com"
            post_id = 83
            post = get_post_by_id(url, post_id)

            post_title = post["title"]["rendered"]
            post_content = post["content"]["rendered"]
            soup = BeautifulSoup(post_content, "html.parser")
            clean_post_content = soup.get_text()
            st.subheader(post_title)
            st.write("May 13, 2023 | [Article](https://antcabbage.wordpress.com/2023/05/13/mayans-mc-season-5-detailed-preview/)")
            st.write("*The content of this article was extracted using `requests` and `BeautifulSoup`, along with the Worpress REST API. Thus, there may be some formatting and alignment issues, especially for the images and/or video featured. A code block will also be shown at the bottom of this article to demonstrate how the REST API was used with the respective libraries to extract the content from the Wordpress site*")
            modified_content = arrange_images_side_by_side(post_content)
            st.markdown(modified_content, unsafe_allow_html=True)
    elif selected == "Finding success as an outlier (Extracted Using Wordpress REST API)":
        with st.echo(code_location="below"):
            import streamlit as st
            import requests
            from bs4 import BeautifulSoup

            def arrange_images_side_by_side(html_content):
                soup = BeautifulSoup(html_content, "html.parser")
                images = soup.find_all("img")

                i = 0
                while i < len(images) - 1:
                    current_image = images[i]
                    next_image = images[i + 1]

                    current_figure = current_image.find_parent("figure")
                    next_figure = next_image.find_parent("figure")

                    # Check if the next image is an immediate sibling
                    if current_figure and next_figure and current_figure.find_next_sibling() == next_figure:
                        container = soup.new_tag("div", style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center;")
                        current_figure.wrap(container)
                        next_figure.wrap(container)

                        # Set the same height for both images and add a little margin for better centering
                        current_image['style'] = "height: 400px; margin: auto;"
                        next_image['style'] = "height: 400px; margin: auto;"

                        # Update the images list
                        images = soup.find_all("img")
                    i += 1

                return str(soup)

            def get_post_by_id(url, post_id):
                site_url = url.replace("https://", "").replace("http://", "")
                response = requests.get(f"https://public-api.wordpress.com/wp/v2/sites/{site_url}/posts/{post_id}?_embed")
                response.raise_for_status()
                return response.json()

            url = "https://antcabbage.wordpress.com"
            post_id = 72
            post = get_post_by_id(url, post_id)

            post_title = post["title"]["rendered"]
            post_content = post["content"]["rendered"]
            soup = BeautifulSoup(post_content, "html.parser")
            clean_post_content = soup.get_text()
            st.subheader(post_title)
            st.write("April 12, 2023 | [Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
            st.write("*The content of this article was extracted using `requests` and `BeautifulSoup`, along with the Worpress REST API. Thus, there may be some formatting and alignment issues, especially for the images and/or video featured. A code block will also be shown at the bottom of this article to demonstrate how the REST API was used with the respective libraries to extract the content from the Wordpress site*")
            modified_content = arrange_images_side_by_side(post_content)
            st.markdown(modified_content, unsafe_allow_html=True)
        
        

elif choose == "Gallery":
    st.header("Gallery")
    st.subheader("Some of my highlights throughout my educational years!")
    selected_options = ["Overview", "Images"]
    selected = st.selectbox("Which year would you like to explore?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Overview":
        st.subheader("Overview")
        st.markdown("""
        > "Photos are always the greatest gifts, because the memories from them will remain forever."
        
        My sister said this to me when I was in primary school. Having an immature and materialistic mindset back then, I was disappointed when I did not receive a present from her back then.

        The quote that she shared that day - was something that I failed to appreciate only until recently. Over the course of these past few years, I have made many memories - both good and bad - which I will fondly remember.

        Thus, this section is a compilation of highlights from my educational years, starting from primary school (7 years old), until the recent day (*in progress*). These images are not only meant to remind myself of the good times that I once had with long lost friends who I hardly keep in touch with nowadays due to our busy schedules, but also serve to show potential viewers a glimpse of what my life was like beyond academics.

        In particular, I hope to be able to refer to this time and time again, especially upon graduating from university and when I formally commence my full-time career.

        To those viewing my website and this section in particular, enjoy the pictures!

        *Note: Photos filed under each year are not necessarily posted in any particular order, as I may have forgotten the exact dates of some photos that were taken.*
        """)
    elif selected == "Images":
        st.subheader("Images")
        st.write("*Baby steps*")
        # Load the images
        num_images = 2
        images_2005 = [Image.open(f"gallery/2005_{i}.jpg") for i in range(1, num_images + 1)]

        # Display the images in a grid
        num_columns = 2
        num_rows = num_images // num_columns

        for row in range(num_rows):
            # Create a row of columns
            columns = st.columns(num_columns)
    
            # Display the images in the columns
            for col in range(num_columns):
                index = row * num_columns + col
                with columns[col]:
                    st.image(images_2005[index], use_column_width=True)


elif choose == "Resume":   
    resume_url = "https://drive.google.com/file/d/1n4TQxDkn98Tu5i2--aNKbK-JvP7xGcDe/view?usp=drive_link"
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume (2 pages)**"), unsafe_allow_html=True)
    show_pdf("Arijeet Dasgupta Resume2024.pdf")
    with open("Arijeet Dasgupta Resume2024.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume (2 pages)",
            data=file,
            file_name="Arijeet Dasgupta Resume2024.pdf",
            mime="application/pdf"
        )

elif choose == "Contact":
# Create section for Contact
    #st.write("---")
    st.header("Contact")
    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    with st.container():
        text_column, mid, image_column = st.columns((1,0.2,0.5))
        with text_column:
            st.write("Let's connect! You may either reach out to me at harrychang.work@gmail.com or use the form below!")
            #with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
                #st.write('Please help us improve!')
                #Name=st.text_input(label='Your Name',
                                    #max_chars=100, type="default") #Collect user feedback
                #Email=st.text_input(label='Your Email', 
                                    #max_chars=100,type="default") #Collect user feedback
                #Message=st.text_input(label='Your Message',
                                        #max_chars=500, type="default") #Collect user feedback
                #submitted = st.form_submit_button('Submit')
                #if submitted:
                    #st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
            def create_database_and_table():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS contacts
                            (name TEXT, email TEXT, message TEXT)''')
                conn.commit()
                conn.close()
            create_database_and_table()

            st.subheader("Contact Form")
            if "name" not in st.session_state:
                st.session_state["name"] = ""
            if "email" not in st.session_state:
                st.session_state["email"] = ""
            if "message" not in st.session_state:
                st.session_state["message"] = ""
            st.session_state["name"] = st.text_input("Name", st.session_state["name"])
            st.session_state["email"] = st.text_input("Email", st.session_state["email"])
            st.session_state["message"] = st.text_area("Message", st.session_state["message"])


            column1, column2= st.columns([1,5])
            if column1.button("Submit"):
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                        (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
                conn.commit()
                conn.close()
                st.success("Your message has been sent!")
                # Clear the input fields
                st.session_state["name"] = ""
                st.session_state["email"] = ""
                st.session_state["message"] = ""
            def fetch_all_contacts():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("SELECT * FROM contacts")
                rows = c.fetchall()
                conn.close()
                return rows
            
            if "show_contacts" not in st.session_state:
                st.session_state["show_contacts"] = False
            if column2.button("View Submitted Forms"):
                st.session_state["show_contacts"] = not st.session_state["show_contacts"]
            
            if st.session_state["show_contacts"]:
                all_contacts = fetch_all_contacts()
                if len(all_contacts) > 0:
                    table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
                    table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
                    markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
                    st.markdown(markdown_table)
                else:
                    st.write("No contacts found.")


            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/harrychangjr/"
            github_url = "https://github.com/harrychangjr"
            email_url = "mailto:harrychang.work@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
            #st.write("© 2023 Arijeet Dasgupta")
            #st.write("[LinkedIn](https://linkedin.com/in/harrychangjr) | [Github](https://github.com/harrychangjr) | [Linktree](https://linktr.ee/harrychangjr)")
        with mid:
            st.empty()
        with image_column:
            st.image(img_ifg)
st.markdown("*Copyright © 2023 Arijeet Dasgupta*")

