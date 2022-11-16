from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep

from pymongo import MongoClient
import pymongo

driver_path = "/home/hariharan/project/insta/chromedriver"
web = webdriver.Chrome(executable_path=driver_path)

skills = ['HTML','Cryptography' , 'Data structures' ,'Blockchain' ,'Cryptography' ,'Smart contracts' ,'Outlook','Netbeans','python','JAVA','Networking','DML','Rest Web Services','Windows','MS Power Point.','MS-Access','technical assistance.','SAP','UNIX','Citrix Xen Server','Web Application testing','Cyara','Linux','MICROSOFT','Nagios','Software Testing','GIT','Eclipse','Sonar Qube''C#.net','Apache','Data Modeling','Database','MySQL','Angular Js','Networking','AWS','java servlet','Jquery','Selenium','Selenium Webdriver','NoSQL','GWT','CSS','Computer','SQL Server 2010','Web Development','Internet Of Things','Windows/XP','R Studio','network engineers','Java.','MS OFFICE','Testing','CCNA','ipsec','ANDROID','HSRP','CPP','Application Designer','PowerShell','MS Word','Ms-Access', "NetBeans",'Cloud Computing','OpenShit','Web Designing','Jdeveloper','computer and firesafety','HTML','Windows and Linux','CISCO','Azure','SAS','Sql','SQL developer','Computer Networks','php','Ansible','Excel','Apache Tomcat','Ansible','Bootstrap','JavaScript','SQL','VB.net','APPLICATION SOFTWARE','Micro Services','Java Script','Eclipse IDE.','Bash','Putty','SPUFI','Agile','Hacking','bgp','Invoice','AMDP.','ASP','Artificial Intelligence','Application / Software Development','mpls','Program Management','C','MS-Access','Java' ,'Kibana','Maven','Open VZ','ASP.NET','C# .NET','AWS','java script','Hibernate','routing protocols.','cricket','Automation','MySQL','Lithium','Git','GCP','JSON','Maria-DB','Spring','Socket Programming','EJB','Nexus','Html5','PostgreSQL','Ms Word and Power Point','ASP.NET','CSS 3.0','Hyper-','Servlet','PowerPoint','JMS','multicast','Windows Services','IoT','Hardware & Networking','SAPUI5','Machine Learning','TRAINING','SQL','C++','Gephi','Go Lang','AngularJs','Object Oriented Programming','Struts','Application & Web Servers: Sciencelogic (EM7)','Java/C/C++ ','M.S. OFFICE','Billing','active directory','Big data''ASP Technical specifications creation','Confidential Record Keeping','Postman','Goal Oriented & Self Motivated','VB','Content',' SAPUI5 (Primary Skill)','Mongo DB','Market Basket Analysis','Familiar with SQL','Hospitality','Web Authoring Tools HTML 5','Reporting Tools: Vportal','Network Management','Operations','Inversion of Control','MS office','Monthly patching update activity and server owner approval / RFC follow-ups.','Ajax &JQuery','rogramming  :C/C++','problem solving','Functional Testing','Octopus','good at communication','angular','PL/SQL Developer','Windows XP','ospf','Powershell','work devotee','APACHE','Android Studio','exchange','Frontend HTML and .Net','DBMS','excellent in various sports like soccer','Predictive Modelling','KVM','JQuery.','ACCESS','Work on Windows 7','CRM','Selenium (Selenium IDE','RESOURCE PLANNING','PowerPoint Language: Fluent in verbal','STL)','good time management skills','DNS','than 1 year)','Accounts Payable-FI-A/P','java','Mac','IDE: Eclipse','JQuery','PHP','kannada','IT Literacy','SIEM','Highly Dedicated towards work','RDBMS: MySQL','MS OFFICE (MS excel','Ansys','Bid management','Corporate Communications','Wireshark','OpenStack','Front end/GUI Tools programming: Adobe Flex','team player','XML','Good communication - written and oral skills','Tally','TestNG','Team-Player','Database MySQL','Tolerant and Flexible to Different Situations','Data Driven','Building good relationship with people.','Marathi','Source Control Management: SVN','ADDITIONAL INFORMATION','wsus','C#','MATLAB','Oracle System upgrades','Mobile Applications','Page Object model','Microsoft Azure','Selenium','Design Patterns','Typewriting','Sql server 2005','Docker','MYSQL','Network Security','Database','Project management','D3js','Technical Experience: - Automation Testing (REST API','SQL Server','Bamboo','SAP UI5/Fiori','LINUX','people and environments.','SAP HANA','Scrum Ma','7','Service Virtualization)','Computer: Proficient in Windows','WAF','Git','Banking','Relay server.','Sauce Labs','5.0 (E)','Java & J2EE','PL-SQL programming','Programming  VB','NetBeans','Computer Hardware','great at taking','Sql Server','Catia V6','Editing','SQL.','good communication and listening skills.','Mobile Testing','McAfee ESM','PMP trained six sigma yellow belt',' Linux','project manager','putty',' Windows','R studio','Capable and Hardworking','Microsoft Visual Studio 2010','Ubuntu Linux','Ajax.','Html','Splunk','Framework & tools :ADF','Syslog sender','tcl','Basic Computers knowledge','ADOBE PHOTOSHOP','Css','ERP SAP R/3 in 4.7','Python','Database Management System','HttpClient','Efficient Individual and Team Player','Oracle 10g','css','Tools: RADTool','Creo parametric 2.0','Jenkins','Cisco Monitoring Tools: EM7','Android','NETWORKING','10','Sublime','Mockito','Creative Team Leadership','posting.','Operating','WinSCP','Pleasing personality','AJAX','l3vpn','Clustering','Content Migration tools Metalogix and Sharegate','Project Management','Iterative Development','SVN.','Data Structures & Algorithms','Oracle','Jackson-2','4.5','SDET','Frameworks (C#) 4.0','Cucumber','Inside Sales','Jdbc','Oracle PeopleSoft','JavaScript.','EMPLOYEE RESOURCE GROUP','jQuery','Selenium Web Driver)','DNS','.net','ASP.Net with C#','sql','CA7',' C#','Good English','VBA','running','DHCP','Domain Knowledge: E-commerce','knowledge of Active Directory','SOAP Web Services','SOAP UI','Java (Preliminary)','Tomcat','ESXi','Programming','GitLab','Windows 7','Salesforce','Positive Attitude.','Technology: Multimedia','Automation Testing','Strong Analytical and logical skills','Windows 8','Software Development Life Cycle','Database SQL Server and Oracle','Unix','JSP.','Javascript','REST','Junit','Hard working with abstract thinking.','Databases and Tools Informatica Power Center','C','DDL','Spring MVC','Sentimental Analysis','and LAN/WAN.','FlexBuilder','Middleware MVC and WCF','Java','Net beans','Tortoise SVN.','SDLC Model: -Waterfall','Oracle SQL Developer','kabbadi','Core Java','PowerShell','Mysql','MongoDB','SOAP','QMF','MS Visio','CSS','Excellent conceptual and analytical skills','Good communication skills','ABAP/4','JUnit','Flexible and high adaptability to new approaches','Smart Working.','O365','ENTERPRISE','Users / Share folders creation and permission assigning.','MS Excel','ClouStack','Jira','ORM Eclipse Link','swimming','Xpeditor','CSS3','Microsoft Office','MainView','software integration','Apache Nifi','dns','SAP ABAP','R','SQL Server','QTP','Network','Web HTML']


connection_string = "mongodb://localhost:27017"

client = MongoClient(connection_string)

def do():
    ex = []
    wrong = []
    
    db = client['jobs']
    db.create_collection('narkuri')
    print("Database created........")

    t = 0
    for search in skills:
        try:
            print("index:" ,t)
            t+=1
            search_title = search
            url = "https://www.naukri.com/" + search_title + "-jobs?k=" + search_title
            print(url)
            web.get(url)

            sleep(1)

            html = web.page_source
            soup = BeautifulSoup(html)

            data = []

            TITLE         = soup.find_all("a", {"class": "title"})
            EXPERIENCE    = soup.find_all("li", {"class": "experience"}) 
            SALARY        = soup.find_all("li", {"class": "salary"})
            LOCATION      = soup.find_all("li", {"class": "location"})
            SKILLS        = soup.find_all("ul", {"class": "has-description"})   

            for i in range(20):
                
                x = {
                    'title'     : TITLE[i].text,
                    'url'       : TITLE[i].get('href'),
                    'experience': EXPERIENCE[i].text,
                    'salary'    : SALARY[i].text,
                    'location'  : (LOCATION[i].text).split(', '),
                    'skills'    : [j.text for j in SKILLS[i]],
                    'search_type'      : search_title
                }

                data.append(x)
            
            db = client['jobs']
            mydb = db['narkuri']

            x = mydb.insert_many(data)

        except Exception as e:
            ex.append(e)
            wrong.append((search , url))

do()