# Resume Parser

- Linkedin Resume Parser developed in Python3.


## Quickstart
Step-by-step walkthrough of how to use Resume-Parser.

### Prerequisities

1. Install python3 on your [OS](https://realpython.com/installing-python/):

2. Install the dependencies:
```
 pip3 install -r requirements.txt
 ```

### Run as a command

```
python3 cmd/parser.py sample/linkedin_resume.pdf
```
Output:
```
{'contact': ['+444', 'mammadovshahr2332@students.', 'itu.edu'], 'skills': ['Telecommunications', 'Wireless', 'Transmission'], 'linkedin': 'www.linkedin.com/in/sakom', 'certifications': ['Amazon Web Services: Design and', 'Implement Systems', 'DevOps Foundations: Continuous', 'Delivery/Continuous Integration', 'Cert Prep: AWS Certified Solutions', 'Architect - Associate', 'IT Security Career Paths and', 'Certifications', 'Amazon Web Services: Design and', 'Implement Systems', 'DevOps Foundations: Continuous', 'Delivery/Continuous Integration', 'Cert Prep: AWS Certified Solutions', 'Architect - Associate', 'IT Security Career Paths and', 'Certifications'], 'summary': ['There is nothing more truly artistic than to love people!'], 'languages': ['English (Full Professional)', 'Azerbaijani (Native or Bilingual)', 'Turkish (Native or Bilingual)'], 'school': 'Télécom ParisTech', 'degree': 'France: MSc,IT Security and Communications·(2015-2017)', 'company': 'OpenGov Inc.', 'position': 'DevOps', 'startdate': 'September 2018', 'enddate': 'Present'}
```

### Run as a Django REST API

1. Start server located in root directory:
```
./start.sh
```

2. Send a HTTP POST request with below parameters in a [Postman](https://www.getpostman.com/downloads/):

![Alt text](img/postman.jpg?raw=true "Postman Parameters")


3. OR Query using CURL from command line:
```
curl -X POST --header "Content-Type:multipart/form-data" --form "resume=@sample/linkedin_resume.pdf"  http://127.0.0.1:8002/api/parser/
```
Output:
```
{
    "contact": [
        "iboXXXX@gmail.com"
    ],
    "skills": [
        "Microsoft Excel",
        "English",
        "Microsoft Office"
    ],
    "linkedin": "www.linkedin.com/in/ibrahim-mammadov-647a4535",
    "certifications": [
        "Power Drive Level 2 Electronic",
        "course",
        "Offshore survival training(BOSIET)",
        "Autronica Fire & Gas system ,",
        "AutroSafe 4 product"
    ],
    "summary": [
        "Experienced Automation Control Engineer with a demonstrated",
        "history of working in the oil & energy industry. Skilled in",
        "Petroleum, Electrical Wiring, English, Electrical Engineering, and",
        "Troubleshooting. Strong engineering professional with a Master's",
        "Degree focused in Automation industrial process from Azerbaijan",
        "Technological University. "
    ],
    "languages": [],
    "school": "Azerbaijan Technological University",
    "degree": "Master's Degree,Automation industrial process·(2010-2012)",
    "company": "Maersk Drilling",
    "position": "Rig Electronic Technician",
    "startdate": "July 2018",
    "enddate": "Present"
}
```

Development is still ongoing.
