#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime, timedelta, timezone
nb_st = datetime.utcnow()
print(f"\nNotebook START time: {nb_st} UTC\n")


# In[2]:


import urllib
import subprocess
from pathlib import Path
import wget
import nbformat
from nbconvert.preprocessors import Preprocessor
from nbconvert import HTMLExporter
from traitlets.config import Config
from jinja2 import DictLoader, Template
from IPython.display import display, HTML
from bs4 import BeautifulSoup
from bs4.element import Tag as BeautufulSoaupTag


# In[3]:


get_ipython().run_line_magic('rm', '-r docs')
get_ipython().run_line_magic('mkdir', 'docs')
get_ipython().run_line_magic('cp', '-r images docs')


# In[4]:


OUTPUT_FILES_DIR = "index_files"

DOCS_DIR = Path.cwd() / "docs"

ERROR404PAGE_FILE = Path("404.html")
ERROR404PAGE_DOWNLOAD_URL = (
    "https://raw.githubusercontent.com/sentinel-1/"
    "sentinel-1.github.io/master/docs/404.html"
)


# In[5]:


def get_404error_page_download_date() -> datetime:
    return datetime.fromtimestamp(
        ERROR404PAGE_FILE.stat().st_ctime
    ).astimezone(timezone.utc)


if (not ERROR404PAGE_FILE.exists()
        or (datetime.utcnow().replace(tzinfo=timezone.utc)
            - get_404error_page_download_date()) > timedelta(days=1)):
    
    if (ERROR404PAGE_FILE.exists()):
        ERROR404PAGE_FILE.unlink()
    print('Downloading the latest "404.html" file:')
    ERROR404PAGE_FILE = Path(wget.download(ERROR404PAGE_DOWNLOAD_URL,
                                           out=str(ERROR404PAGE_FILE)))
else:
    print('The "404.html" file has been updated lately '
          f'({get_404error_page_download_date():%Y-%m-%d %H:%M:%S %Z}), '
          'skipping download.')


# In[6]:


get_ipython().run_line_magic('cp', '404.html docs')


# In[7]:


def get_nb_name(nb_filename: str) -> str:
    return nb_filename.rsplit('.', maxsplit=1)[0]



def get_git_ISO8601_Date_first_commited(nb_filename: str) -> str:
    d = subprocess.check_output(
        "git --no-pager log --diff-filter=A --follow --format=%aI --  "
        f"\"{nb_filename}\" | tail -1",
        stderr=subprocess.STDOUT,
        shell=True)
    d = datetime.fromisoformat(
        d.decode().strip()
    ).astimezone(timezone.utc).isoformat()
    return d



def get_git_ISO8601_Date_last_commited(nb_filename: str) -> str:
    d = subprocess.check_output(
        f"git --no-pager log -1 --format=%aI --  \"{nb_filename}\" ",
        stderr=subprocess.STDOUT,
        shell=True)
    d = datetime.fromisoformat(
        d.decode().strip()
    ).astimezone(timezone.utc).isoformat()
    return d


# In[8]:


notebooks = {
    "Data Collection API Lab.ipynb": {
        "#": 1,
        "week": 1,
        "topic": "Collecting the Data",
    },
    "Data Collection with Web Scraping lab.ipynb": {
        "#": 2,
        "week": 1,
        "topic": "Collecting the Data",
    },
    "EDA lab.ipynb": {
        "#": 3,
        "week": 1,
        "topic": "Data Wrangling",
    },
    "EDA with SQL lab.ipynb": {
        "#": 4,
        "week": 2,
        "topic": "Exploratory Analysis Using SQL",
    },
    "EDA with Visualization lab.ipynb": {
        "#": 5,
        "week": 2,
        "topic": "Exploratory Analysis Using Pandas and Matplotlib",
    },
    "Interactive Visual Analytics with Folium lab.ipynb": {
        "#": 6,
        "week": 3,
        "topic": "Interactive Visual Analytics and Dashboard",
    },
    "Machine Learning Prediction lab.ipynb": {
        "#": 7,
        "week": 4,
        "topic": "Predictive Analysis (Classification)",
    },
}

for nb_filename in notebooks:
    notebooks[nb_filename]["name_uri"] = urllib.parse.quote(
        get_nb_name(nb_filename)
    )


# In[9]:


IBM_datascience_index_template = Template("""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python Notebooks by Sentinel-1</title>

  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="manifest" href="/site.webmanifest">

  <style type="text/css">
    ul {
      line-height: 2;
    }

  </style>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor"
        crossorigin="anonymous">
  <style>
    html,
    body {
      height: 100%;
      margin: 0;
      padding: 0;
      color: #2e2e2e;
    }

    main {
      min-height: calc(100% - 7.4rem - 3ex);
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    footer {
      height: calc(7.4rem + 3ex);
      margin: 0;
      padding: 0;
      text-align: center;
    }

  </style>
</head>

<body>
  <main>
    <div class="container">
      <div class="table-responsive rable-hover mt-5">
        <table class="table caption-top align-middle">
          <caption>
            Solutions by <a href="https://github.com/sentinel-1">Sentinel-1</a>
            for asignments of the 
            <strong>&quot;IBM Applied Data Science Capstone&quot;</strong> – the
            <strong>capstone project</strong>
            from the 
            <a href="https://www.coursera.org/professional-certificates/ibm-data-science"
               target="_blank">IBM Data Science Professional Certificate</a>
            courses
          </caption>
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Notebook</th>
              <th scope="col">Schedule</th>
              <th scope="col">Topic</th>
            </tr>
          </thead>
          <tbody>
            {% for nb_filename in notebooks.keys() %}
            <tr>
              <th scope="row"> {{notebooks[nb_filename]["#"]}} </th>
              <td>
                <a href="/IBM-Applied-Data-Science-Capstone/{{notebooks[nb_filename]["name_uri"]}}/">
                  {{nb_filename.rsplit('.', maxsplit=1)[0]}}
                </a>
              </td>
              <td> 
                <strong>Week {{notebooks[nb_filename]["week"]}}</strong> of the 
                <strong>10th course</strong>
              </td>
              <td> {{notebooks[nb_filename]["topic"]}} </td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
    </div>
  </main>
  <footer>
    <div class="container" style="display:flex; flex-direction: row; justify-content: center; align-items: center;">
      <p style="margin: 3.7em auto;"> 
        Solutions By © 2021-2022 <a href="https://github.com/sentinel-1"
        target="_blank">Sentinel-1</a>
        &nbsp;|&nbsp; Assignments and Tasks By © 2020-2021 IBM Corporation
      </p>
      <!-- ANALYTICS.LAGOGAL.COM -->
      <div id="analytics-lagogal-com-access" data-site-id="20221" style="margin: 0;padding: 0;"></div>
      <script async src="//analytics.lagogal.com/access.js"></script>
      <!-- / END OF ANALYTICS.LAGOGAL.COM -->
    </div>
  </footer>

</body>

</html>
                
""")


index_html_file = DOCS_DIR / "index.html"
print(f"*** Writing to: \"{index_html_file.relative_to(Path.cwd())}\"")
with open(index_html_file, "w", encoding='utf-8') as f:
    f.write(IBM_datascience_index_template.render(notebooks=notebooks))
print("  - Done.")


# In[10]:


class ExtractOutputPreprocessorFileDir(Preprocessor):
    """
    Add to resources the output file directory name
    for the ExtractOutputPreprocessor
    """

    def preprocess(self, nb, resources):
        output_files_dir = OUTPUT_FILES_DIR
        self.log.info('ExtractOutputPreprocessorFileDir preprocess(): '
                      f'resources["output_files_dir"] = {output_files_dir}')
        resources["output_files_dir"] = output_files_dir
        return nb, resources



class OGPPreprocessor(Preprocessor):
    """
    Add to resources for generating Open Graph Protocol (OGP) entries.
    """

    def preprocess(self, nb, resources):
        nb_filename = resources["original_nb_filename"]
        nb_name = get_nb_name(nb_filename)
        nb_topic = notebooks[nb_filename]["topic"]
        nb_name_uri = notebooks[nb_filename]["name_uri"]
        iso8610_nb_date_added = get_git_ISO8601_Date_first_commited(
            nb_filename
        )
        iso8610_nb_date_edited = get_git_ISO8601_Date_last_commited(
            nb_filename
        )

        self.log.info(
            f"""OGPPreprocessor preprocess():
            resources["nb_name"] = {nb_name}
            resources["nb_topic"] = {nb_topic}
            resources["nb_name_uri"] = {nb_name_uri}
            resources["iso8610_nb_date_added"] = {iso8610_nb_date_added}
            resources["iso8610_nb_date_edited"] = {iso8610_nb_date_edited}
            """)
        resources["nb_name"] = nb_name
        resources["nb_topic"] = nb_topic
        resources["nb_name_uri"] = nb_name_uri
        resources["iso8610_nb_date_added"] = iso8610_nb_date_added
        resources["iso8610_nb_date_edited"] = iso8610_nb_date_edited
        return nb, resources



c = Config()
c.HTMLExporter.preprocessors = [
    'nbconvert.preprocessors.ClearMetadataPreprocessor',
    ExtractOutputPreprocessorFileDir,
    'nbconvert.preprocessors.ExtractOutputPreprocessor',
    OGPPreprocessor
]

dl = DictLoader({'OGP_classic':
"""
{%- extends 'classic/index.html.j2' -%}
{%- block html_head -%}

{#  OGP attributes for shareability #}
<meta property="og:url"          content="https://sentinel-1.github.io/IBM-Applied-Data-Science-Capstone/{{resources.nb_name_uri}}/" />
<meta property="og:type"         content="article" />
<meta property="og:title"        content="IBM Applied Data Science Capstone: {{resources.nb_name}}" />
<meta property="og:description"  content="{{resources.nb_topic}}" />
<meta property="og:image"        content="https://raw.githubusercontent.com/sentinel-1/IBM-Applied-Data-Science-Capstone/master/images/IDSNlogo.png" />
<meta property="og:image:alt"    content="cognitiveclass.ai logo" />
<meta property="og:image:type"   content="image/png" />
<meta property="og:image:width"  content="800" />
<meta property="og:image:height" content="800" />

<meta property="article:published_time" content="{{ resources.iso8610_nb_date_added }}" />
<meta property="article:modified_time"  content="{{ resources.iso8610_nb_date_edited }}" />
<meta property="article:publisher"      content="https://sentinel-1.github.io" />
<meta property="article:author"         content="https://github.com/sentinel-1" />
<meta property="article:section"        content="datascience" />
<meta property="article:tag"            content="datascience" />
<meta property="article:tag"            content="Python" />
<meta property="article:tag"            content="data" />
<meta property="article:tag"            content="analytics" />
<meta property="article:tag"            content="datavisualization" />
<meta property="article:tag"            content="visualization" />
<meta property="article:tag"            content="ibmdatascience" />
<meta property="article:tag"            content="deeplearning" />
<meta property="article:tag"            content="bigdata" />
<meta property="article:tag"            content="datamining" />
<meta property="article:tag"            content="github" />
<meta property="article:tag"            content="pythonprogramming" />
<meta property="article:tag"            content="jupyternotebooks" />


{{ super() }}

{%- endblock html_head -%}


{% block body_header %}
<body>

<div class="container">
  <nav class="navbar navbar-default">
    <div class="container-fluid">
      <ul class="nav nav-pills  navbar-left">
        <li role="presentation">
          <a href="/">
            <svg xmlns="http://www.w3.org/2000/svg"
                 viewBox="0 0 576 512" width="1em">
              <path 
                fill="#999999"
d="M 288,0 574,288 511,288 511,511 352,511 352,352 223,352 223,511 62,511 64,288 0,288 Z"
              />
            </svg> Home
          </a>
        </li>
      </ul>
      <ul class="nav nav-pills  navbar-right">
        <li role="presentation" class="active">
          <a href="/IBM-Applied-Data-Science-Capstone/{{resources.nb_name_uri}}/">🇬🇧 English </a>
        </li>
        <li role="presentation">
          <a href="/IBM-Applied-Data-Science-Capstone/{{resources.nb_name_uri}}/ka/">🇬🇪 ქართული</a>
        </li>
      </ul>
    </div>
  </nav>
</div>


<div class="container">
  <div class="row">
    <div class="alert alert-danger small" role="alert">
        <strong>DISCLAIMER:</strong> Please be aware, that
        <u>this notebook contains solutions for the Capstone Project</u> from the 
        <a href="https://www.coursera.org/professional-certificates/ibm-data-science"
           class="alert-link" target="_blank"
           >IBM Data Science Professional Certificate</a> 
        courses. Originally I have shared it to my GitHub repository
        <a href="https://github.com/sentinel-1/IBM-Applied-Data-Science-Capstone"
           class="alert-link"  target="_blank"
           >IBM-Applied-Data-Science-Capstone</a>
        as part of the required "share to GitHub" exercises of the 10th course
        from the said courses. The 10th course is where the sharing to GitHub comes into play,
        but until that, during the courses 1 to 9, students are not required or encouraged to share solutions
        of those courses, thus I am NOT sharing any of my solutions from any of the 1-9 courses,
        but only the relevant solutions from the 10th course – which are supposed to be shared
        in the first place.
        Nevertheless, if you are going to complete all the assignments from the 10th course (including 
        shared ones) independently, then you may prefer not to see in advance solutions provided below.
    </div>
  </div>
</div>


  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">    
{% endblock body_header %}

{% block body_footer %}
    </div>
  </div>
  <footer>
    <div class="container"
         style="display:flex; flex-direction: row; justify-content: center; align-items: center;">
      <p style="margin: 3.7em auto;"> 
        Solutions By © 2021-2022 <a href="https://github.com/sentinel-1" target="_blank">Sentinel-1</a>
         &nbsp;|&nbsp; Assignments and Tasks By © 2020-2021 IBM Corporation
      </p>
      <!-- ANALYTICS.LAGOGAL.COM -->
      <div id="analytics-lagogal-com-access" data-site-id="20221"
           style="margin: 0;padding: 0;"></div>
      <script async src="//analytics.lagogal.com/access.js"></script>
      <!-- / END OF ANALYTICS.LAGOGAL.COM -->
     </div>
  </footer>
</body>
{% endblock body_footer %}  
"""})



html_exporter = HTMLExporter(extra_loaders=[dl],
                             template_file='OGP_classic',
                             template_name='classic',
                             config=c)


# In[11]:


for nb_filename in notebooks.keys():
    print(f"\n\n*** Processing: \"{nb_filename}\"")
    nb_name = get_nb_name(nb_filename)
    nb_docs_dir = DOCS_DIR / nb_name
    (nb_docs_dir / OUTPUT_FILES_DIR).mkdir(parents=True)
    
    with open(nb_filename) as nb_f:
        nb_text = nb_f.read()
    nb_node = nbformat.reads(nb_text, as_version=4)
    (nb_body, nb_resources) = html_exporter.from_notebook_node(
        nb_node,
        resources={'original_nb_filename': nb_filename},
    )
    
    print(f" ** Processing static files extracted from outputs (if any):")
    static_file = None
    
    for static_file in nb_resources['outputs'].keys():
        print(f"  - \"{static_file}\"")
        with open(nb_docs_dir / static_file, 'wb') as f:
            f.write(nb_resources['outputs'][static_file])
            
    if static_file is None:
        print("  - No static file has been extracted from outputs.")
        
    print(f" ** Correcting original markdown static image sources:")
    nb_soup = BeautifulSoup(nb_body)

    for img in nb_soup.find_all("img"):
        if img.attrs["src"].startswith("images/"):
            print(f'  - "{img.attrs["src"]}"')
            img.attrs["src"] = "../" + img.attrs["src"]
    
    print(" ** Adding OGP tags for the "
          f"original notebook author(s) found in the notebook:")
    authors_start_cell = (
        nb_soup.find(id="Authors") or nb_soup.find(id="Author(s)")
    ).find_parent(class_="cell")
    authors_end_cell = (
        nb_soup.find(id="Change-Log") or nb_soup.find(id="Change-log")
    ).find_parent(class_="cell")
    detected_authors = {}
    
    while authors_start_cell != authors_end_cell:
        
        if isinstance(authors_start_cell, BeautufulSoaupTag):
            
            for a in authors_start_cell.find_all("a"):
                author_name = a.text.strip()
                
                if (not author_name in detected_authors
                        and len(author_name.split()) > 1):
                    url = urllib.parse.urlparse(
                        a.attrs['href']
                    )._replace(fragment="", query="").geturl()
                    
                    if len(url) > 0:
                        detected_authors[author_name] = url
                        print(f"  - [{author_name}]({url})")
        authors_start_cell = authors_start_cell.next_element
    author_sentinel_1 = nb_soup.find(property="article:author")

    for author_profile in detected_authors.values():
        next_author = nb_soup.new_tag("meta",
                                      content=author_profile,
                                      property="article:author")
        author_sentinel_1.insert_before(next_author)
    
    print(" ** Writing HTML:")
    nb_output_html_file = nb_docs_dir / "index.html"
    print(f'  - "{nb_output_html_file.relative_to(Path.cwd())}"')
    with open(nb_output_html_file, "w", encoding='utf-8') as f:
        f.write(str(nb_soup.prettify()))
    print(" ** done.\n")


# In[12]:


print(f"\n ** Total Elapsed time: {datetime.utcnow() - nb_st} ** \n")
print(f"Notebook END time: {datetime.utcnow()} UTC\n")

