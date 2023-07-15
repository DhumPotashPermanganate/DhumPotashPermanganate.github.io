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
img_exh = Image.open('images/exhibit.jpg')
img_byju = Image.open('images/byju.jpg')
img_quiz = Image.open('images/quiz.jpg')
# Assets for education
img_fiem = Image.open("images/fiem.jpg")
img_kvb = Image.open("images/kvb.jpg")
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
img_epam = Image.open("images/epam.png")
img_cognizant = Image.open("images/cognizant.png")
# Assets for projects
vid_tf0 = open('images/tensorflow.mp4', 'rb')
vid_tf1 = vid_tf0.read()
img_fifa = Image.open('images/fifa.jpeg')
img_blind = Image.open('images/blind.jpg')



# Assets for blog

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
img_contact = Image.open('images/contact.jpg')
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
    youtube_url = ""
    linkedin_url = "https://www.linkedin.com/in/arijeet-dasgupta/"
    github_url = "https://github.com/DhumPotashPermanganate/"
    wordpress_url = ""
    email_url = "mailto:arigofficial71@gmail.com"
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
                st.image(img_kvb)
            with text_column:
                st.subheader("AISSCE, Class 12, [Kendriya Vidyalaya, Ballygunge](https://baligunge.kvs.ac.in/) (2016-2018)")
                st.write("Coursework: Physics, Chemistry, Computer Science, Mathematics, English")
                st.write("Final Marks: 76.4")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_kvb)
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
            st.subheader("Hand Gesture Recognition Model using TensorFlow")
            st.write("*Final Year Project for University*")
            st.markdown("""
            - Used TensorFlow SSD 320x320 model to create our own hand gesture recognition model.
            - The data used by it was completely made by us using pcitures of all the team members
            - Gave excellent results in limited surroundings, given that the dataset we created was of 200 images
            - Almost 90% and above accuracy in most of the cases
            """)
        with image_column:
            st.video(vid_tf1)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("FIFA Web Scraper and Analytical tool")
            st.write("*Self-initiated project*")
            st.markdown("""
            - Used Selenium Webdriver to scrape the data from internet of FIFA players and store them as csv
            - Used pandas, numpy and matplotlib to analyse different players of different metrics to compare them
            """)
        with image_column:
            st.image(img_fifa)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Blind Cap")
            st.write("*Project for Exhibit'19, Intra-college project competetion*")
            st.markdown("""
            - Conducted exploratory data analysis (EDA) to identify relationships between variables using correlation heatmaps and histograms
            - Trained and compared multiple regression, random forest and XGBoost to build optimal model for sales volume prediction
            - Performed randomized search with cross-validation to increase performance of random forest regressor and reduce MSE
            """)
        with image_column:
            st.image(img_blind)

    
elif choose == "Competitions":
    # Create section for Competitions
    #st.write("---")
    st.header("Competitions")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_exh)
        with text_column:
            st.subheader("Exhibit-19 (Future Institute of Engineering and Management")
            st.write("Third Position")
            st.markdown("""
                - Made blind cap using Arduino and light sensor
                - Can be used by blind people, the cap beeps and the frequency of beep increase as some object comes nearby to the person wearing the cap
                - Secured 3rd Prize in the the Competition
            """)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_quiz)
            #st.empty()
        with text_column:
            st.subheader("Yantra 2019 (Future Institute of Engineering and Management")
            st.write("First Position")
            st.markdown("""
                - Won intra-college technical quiz competition
                - Comprised of three rounds, cleared all them while sustaining the top position
            """)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_byju)
            #st.empty()
        with text_column:
            st.subheader("Byjus Think and Learn Challenge 2015")
            st.write("Cleared the first round beating students from more than 20 schools")
            st.markdown("""
                - Cleared the first round which comprised of more than 1000 students from several school of Kolkata
                - Quiz competition based on Science and Aptitude knowledge
                - Participated in the second round, but lost out
            """)


elif choose == "Blog":
    st.header("Blog")
    selected_options = ["Overview", "Option1",
                        "Option2",
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

    elif selected == "Option1":
        st.subheader("Option1")

    elif selected == "Option2":
        st.subheader("Option2")
        
        

elif choose == "Gallery":
    st.header("Gallery")
    st.subheader("Some of my highlights throughout my educational years!")
    selected_options = ["Overview", "Images"]
    selected = st.selectbox("Which year would you like to explore?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Overview":
        st.subheader("Overview")
        st.markdown("""""")


    elif selected == "Images":
        st.subheader("Images")
        # st.write("*Baby steps*")
        # # Load the images
        # num_images = 2
        # images_2005 = [Image.open(f"gallery/2005_{i}.jpg") for i in range(1, num_images + 1)]
        #
        # # Display the images in a grid
        # num_columns = 2
        # num_rows = num_images // num_columns
        #
        # for row in range(num_rows):
        #     # Create a row of columns
        #     columns = st.columns(num_columns)
        #
        #     # Display the images in the columns
        #     for col in range(num_columns):
        #         index = row * num_columns + col
        #         with columns[col]:
        #             st.image(images_2005[index], use_column_width=True)


elif choose == "Resume":   
    resume_url = "https://drive.google.com/file/d/1rrBqTveitMKHJ-VFrHVCAGwOJNL9rngd/view?usp=sharing"
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
            st.write("Let's connect! You may either reach out to me at arigofficial71@gmail.com or use the form below!")

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
            linkedin_url = "https://www.linkedin.com/in/arijeet-dasgupta/"
            github_url = "https://github.com/DhumPotashPermanganate/"
            email_url = "mailto:arigofficial71@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
        with mid:
            st.empty()
        with image_column:
            st.image(img_contact)
st.markdown("*Copyright © 2023 Arijeet Dasgupta*")

