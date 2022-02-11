#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="images/IDSNlogo.png"  width="300" alt="cognitiveclass.ai logo"  />
# </center>
# 
# <h1 align=center><font size = 5>Assignment: SQL Notebook for Peer Assignment</font></h1>
# 
# Estimated time needed: **60** minutes.
# 
# ## Introduction
# 
# Using this Python notebook you will:
# 
# 1.  Understand the Spacex DataSet
# 2.  Load the dataset  into the corresponding table in a Db2 database
# 3.  Execute SQL queries to answer assignment questions
# 

# ## Overview of the DataSet
# 
# SpaceX has gained worldwide attention for a series of historic milestones.
# 
# It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010.
# SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage.
# 
# Therefore if we can determine if the first stage will land, we can determine the cost of a launch.
# 
# This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.
# 
# This dataset includes a record for each payload carried during a SpaceX mission into outer space.
# 

# ### Download the datasets
# 
# This assignment requires you to load the spacex dataset.
# 
# In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the link below to download and save the dataset (.CSV file):
# 
# <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01" target="_blank">Spacex DataSet</a>
# 

# ### Store the dataset in database table
# 
# **it is highly recommended to manually load the table using the database console LOAD tool in DB2**.
# 
# <img src = "images/spacexload.png">
# 
# Now open the Db2 console, open the LOAD tool, Select / Drag the .CSV file for the  dataset, Next create a New Table, and then follow the steps on-screen instructions to load the data. Name the new table as follows:
# 
# **SPACEXDATASET**
# 
# **Follow these steps while using old DB2 UI which is having Open Console Screen**
# 
# **Note:While loading Spacex dataset, ensure that detect datatypes is disabled. Later click on the pencil icon(edit option).**
# 
# 1.  Change the Date Format by manually typing DD-MM-YYYY and timestamp format as DD-MM-YYYY HH\:MM:SS.
# 
#     Here you should place the cursor at Date field and manually type as DD-MM-YYYY.
# 
# 2.  Change the PAYLOAD_MASS\_\_KG\_  datatype  to INTEGER.
# 
# <img src = "images/spacexload2.png">
# 

# **Changes to be considered when having DB2 instance with the new UI having Go to UI screen**
# 
# *   Refer to this insruction in this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/instructional-labs.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01">link</a> for viewing  the new  Go to UI screen.
# 
# *   Later click on **Data link(below SQL)**  in the Go to UI screen  and click on **Load Data** tab.
# 
# *   Later browse for the downloaded spacex file.
# 
# <img src="images/browsefile.png" width="800"/>
# 
# *   Once done select the schema andload the file.
# 
#  <img src="images/spacexload3.png" width="800"/>
# 

# In[1]:


get_ipython().system('pip install sqlalchemy==1.3.9')
get_ipython().system('pip install ibm_db_sa')
get_ipython().system('pip install ipython-sql')


# ### Connect to the database
# 
# Let us first load the SQL extension and establish a connection with the database
# 

# In[2]:


get_ipython().run_line_magic('load_ext', 'sql')


# **DB2 magic in case of old UI service credentials.**
# 
# In the next cell enter your db2 connection string. Recall you created Service Credentials for your Db2 instance before. From the **uri** field of your Db2 service credentials copy everything after db2:// (except the double quote at the end) and paste it in the cell below after ibm_db_sa://
# 
# <img src ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_edX/images/URI.jpg">
# 
# in the following format
# 
# **%sql ibm_db_sa://my-username:my-password\@my-hostname:my-port/my-db-name**
# 
# **DB2 magic in case of new UI service credentials.**
# 
# <img src ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/servicecredentials.png" width=600>  
# 
# *   Use the following format.
# 
# *   Add security=SSL at the end
# 
# **%sql ibm_db_sa://my-username:my-password\@my-hostname:my-port/my-db-name?security=SSL**
# 

# In[ ]:





# In[3]:


## CONNECTION:
# %sql ibm_db_sa://USER:PASSWORD@764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:32536/bludb?authSource=admin&replicaSet=replset&security=SSL


# In[4]:


# The code was removed by Watson Studio for sharing.
# TODO @hidden_cell


# ## Tasks
# 
# Now write and execute SQL queries to solve the assignment tasks.
# 
# ### Task 1
# 
# ##### Display the names of the unique launch sites  in the space mission
# 

# In[5]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT launch_site FROM SPACEXTBL;')


# ### Task 2
# 
# ##### Display 5 records where launch sites begin with the string 'CCA'
# 

# In[6]:


get_ipython().run_cell_magic('sql', '', "SELECT * FROM SPACEXTBL WHERE launch_site LIKE 'CCA%' LIMIT 5;")


# ### Task 3
# 
# ##### Display the total payload mass carried by boosters launched by NASA (CRS)
# 

# In[7]:


get_ipython().run_cell_magic('sql', '', 'SELECT sum(payload_mass__kg_) AS "Total payload mass (NASA (CRS))" FROM SPACEXTBL WHERE customer = \'NASA (CRS)\';')


# ### Task 4
# 
# ##### Display average payload mass carried by booster version F9 v1.1
# 

# In[8]:


get_ipython().run_cell_magic('sql', '', 'SELECT AVG(payload_mass__kg_) AS "Average payload mass (booster version F9 v1.1)" FROM SPACEXTBL WHERE booster_version LIKE \'F9 v1.1%\';')


# ### Task 5
# 
# ##### List the date when the first successful landing outcome in ground pad was acheived.
# 
# *Hint:Use min function*
# 

# In[9]:


get_ipython().run_cell_magic('sql', '', 'SELECT min(DATE) AS "First successful landing outcome in ground pad" FROM SPACEXTBL WHERE landing__outcome = \'Success (ground pad)\';')


# ### Task 6
# 
# ##### List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000
# 

# In[10]:


get_ipython().run_cell_magic('sql', '', "SELECT booster_version FROM SPACEXTBL WHERE landing__outcome = 'Success (drone ship)' AND payload_mass__kg_ BETWEEN 4000 AND 6000;")


# ### Task 7
# 
# ##### List the total number of successful and failure mission outcomes
# 

# In[11]:


get_ipython().run_cell_magic('sql', '', 'SELECT \'Success\' AS "Outcome", count(*) AS "Count" FROM SPACEXTBL WHERE landing__outcome LIKE \'Success%\'\nUNION ALL\nSELECT \'Failure\' AS "Outcome", count(*) AS "Count" FROM SPACEXTBL WHERE landing__outcome NOT LIKE \'Success%\'\nUNION ALL\nSELECT \'(All)\' AS "Outcome", count(*) AS "Count" FROM SPACEXTBL;')


# ### Task 8
# 
# ##### List the   names of the booster_versions which have carried the maximum payload mass. Use a subquery
# 

# In[12]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT booster_version\nFROM SPACEXTBL\nWHERE payload_mass__kg_ = (\n    SELECT max(payload_mass__kg_)\n    FROM SPACEXTBL\n)')


# ### Task 9
# 
# ##### List the failed landing_outcomes in drone ship, their booster versions, and launch site names for in year 2015
# 

# In[13]:


get_ipython().run_cell_magic('sql', '', "\nSELECT booster_version, launch_site,landing__outcome\nFROM SPACEXTBL\nWHERE landing__outcome = 'Failure (drone ship)'\n  AND EXTRACT(YEAR FROM DATE) = 2015")


# ### Task 10
# 
# ##### Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order
# 

# In[14]:


get_ipython().run_cell_magic('sql', '', '\nSELECT landing__outcome, COUNT(*) AS "Count"\nFROM SPACEXTBL\nWHERE DATE BETWEEN \'2010-06-04\' and \'2017-03-20\'\nGROUP BY landing__outcome\nORDER BY Count DESC\n;')


# ### Reference Links
# 
# *   <a href ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20String%20Patterns%20-%20Sorting%20-%20Grouping/instructional-labs.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01&origin=www.coursera.org">Hands-on Lab : String Patterns, Sorting and Grouping</a>
# 
# *   <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Built-in%20functions%20/Hands-on_Lab__Built-in_Functions.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01&origin=www.coursera.org">Hands-on Lab: Built-in functions</a>
# 
# *   <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sub-queries%20and%20Nested%20SELECTs%20/instructional-labs.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01&origin=www.coursera.org">Hands-on Lab : Sub-queries and Nested SELECT Statements</a>
# 
# *   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-3-SQLmagic.ipynb?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01">Hands-on Tutorial: Accessing Databases with SQL magic</a>
# 
# *   <a href= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-4-Analyzing.ipynb?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01">Hands-on Lab: Analyzing a real World Data Set</a>
# 

# ## Author(s)
# 
# <h4> Lakshmi Holla </h4>
# 

# ## Other Contributors
# 
# <h4> Rav Ahuja </h4>
# 

# ## Change log
# 
# | Date       | Version | Changed by    | Change Description        |
# | ---------- | ------- | ------------- | ------------------------- |
# | 2021-10-12 | 0.4     | Lakshmi Holla | Changed markdown          |
# | 2021-08-24 | 0.3     | Lakshmi Holla | Added library update      |
# | 2021-07-09 | 0.2     | Lakshmi Holla | Changes made in magic sql |
# | 2021-05-20 | 0.1     | Lakshmi Holla | Created Initial Version   |
# 

# ## <h3 align="center"> © IBM Corporation 2021. All rights reserved. <h3/>
# 
