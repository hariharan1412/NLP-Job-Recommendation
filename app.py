from flask import Flask , render_template , url_for , redirect , abort , request
from pymongo import MongoClient
import pymongo
import operator
import spacy

app = Flask(__name__)

def extract_information_from_user(text):

    key=[]
    value=[]
    nlp = spacy.load("./output/model-best/")

    doc = nlp(text)

    for ent in doc.ents:
        key.append(ent.label_)
        value.append(ent.text)

    Dict = {key[i]: value[i] for i in range(len(key))}

    SKILLS= Dict["SKILLS"].split(",")

    Dict.update(SKILLS=SKILLS)
    print(Dict["SKILLS"])
    
    return retirve_info_from_db(text)

def retirve_info_from_db(user_list):

    len_user_list = len(user_list)
    n = mydb.find( { 'skills': { '$in': user_list}} ,{'_id':0}) 

    jobs = []
    for i in n:

        job_skills = i['skills']

        match = len([k for k , val in enumerate(job_skills) if val in user_list])
        
        total_len = len(job_skills) + len_user_list 
        i['rank'] = match/total_len #RANKING COEFFICIENT
        jobs.append(i)

    return show_info(jobs)

def show_info(jobs):

    jobs.sort(key=operator.itemgetter('rank') , reverse=True) #SORTING JOBS BASED ON THE RANK SCORE
    return render_template('show_job.html' , jobs=jobs)
 

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']

    return extract_information_from_user(text)    


if __name__ == "__main__":
    
    #CONNECTING WITH MONGO DB
    connection_string = "mongodb://localhost:27017"
    client = MongoClient(connection_string)

    db = client['jobs']
    mydb = db['narkuri']
    
    #STARTING THE APPLICATION
    app.run(host="0.0.0.0" ,port=5000, debug = True)