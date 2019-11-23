#!/usr/bin/env python3
import sys
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter
import io
from contextlib import redirect_stdout

# main
def main(argv):
    import getopt
    (opts, args) = getopt.getopt(argv[1:], 'dP:o:t:O:c:s:R:Y:p:m:SCnAVM:W:L:F:')
    imagewriter = None
    caching = True
    laparams = LAParams()
    retstr = io.StringIO()
    rsrcmgr = PDFResourceManager(caching=caching)
    device = TextConverter(rsrcmgr, retstr, laparams=laparams,imagewriter=imagewriter )
    data = []
    
    for fname in args:
        with open(fname, 'rb') as fp:
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.get_pages(fp,
                         
                                          caching=caching, check_extractable=True):
                interpreter.process_page(page)
                data = retstr.getvalue()

    weird=["\xa0","\uf0da","\x0c","• ","* ","(LinkedIn)"," (LinkedIn)","\uf0a7","(Mobile)","-       ","●"]
    for i in weird:
       data=data.replace(i, "")
    
    result_list=data.split('\n')
    skills=[]
    languages=[]
    summary=[]
    certifications=[]
    contact=[]
    linkedin=[]
    experience=[]
    education=[]
    exp_dict={}
    edu_dict={}
    alld={}

    for i in result_list:
        if i=='Contact':
            value=result_list.index(i)
            while True:
                value=value+1
                contact.append(result_list[value].strip())
                
                if result_list[value] =='':
                    contact.remove(result_list[value])
                    break
        
        if i.__contains__('www.linkedin.com'):
            value=result_list.index(i)
            while True:             
                linkedin.append(result_list[value])
                value=value+1
                if result_list[value] =='':
            
                    break
            if len(linkedin)>=2:
                ln=[]
                merged=linkedin[0]+linkedin[1].strip()
                ln.append(merged)
                linkedin=ln
        
        if i=='Top Skills':
            value=result_list.index(i)
            while True:
                value=value+1
                skills.append(result_list[value])
                if result_list[value] =='':
                    skills.remove(result_list[value])
                    break
          
    
        if i.__contains__('Certifications'):
            value=result_list.index(i)
            while True:
                value=value+1
                certifications.append(result_list[value])
                if result_list[value] =='':
                    certifications.remove(result_list[value])
                    break
        
        if i.__contains__('Summary'):
            value=result_list.index(i)
            while True:
                value=value+1
                summary.append(result_list[value])
                if result_list[value] =='':
                    summary.remove(result_list[value])
                    break
        
        if i=='Languages':
            value=result_list.index(i)
            while True:
                value=value+1
                languages.append(result_list[value])
                if result_list[value] =='':
                    languages.remove(result_list[value])
                    break
          
        if i=='Experience':
            value=result_list.index(i)
            value=value+2
            while True:
                experience.append(result_list[value])
                value=value+1
                a=str(result_list[value])
                if a.__contains__('-'):
                    k=a.split('-')
               #     print('start:',k[0],'end:',k[1])
                    break
                elif result_list[value] =='':
                    break
            
            listOfExp = ["company", "position","period","place","description" ]  
            zipbObj = zip(listOfExp, experience)
            exp_dict = dict(zipbObj)
            exp_dict['startdate']=k[0]
            exp_dict['enddate']=k[1]


        
        if i=='Education':
            value=result_list.index(i)
            value=value+1
            while True:
                education.append(result_list[value])
                value=value+1
                if result_list[value] =='':
                    break
            listOfEdu = ["school", "degree" ]
            zipbObj = zip(listOfEdu, education)
            edu_dict = dict(zipbObj)

    alld['contact']=contact
    alld['skills']=skills
    alld['linkedin']=linkedin[0]
    alld['skills']=skills
    alld['certifications']=certifications
    alld['summary']=summary
    alld['languages']= languages  
    alld.update(edu_dict)
    alld.update(exp_dict)
    alld['message']= "testing" 
    alld['host']= "jobhax.com"  

    import requests
    import json
    Parsed_data = json.dumps(alld)

    print(Parsed_data)
    device.close()
    retstr.close()

#     graylog_url = "http://127.0.0.1:12201/gelf"


#     #header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
#     #payload = '{"short_message":"Hello there", "host":"example.org", "facility":"test", "_foo":"bar"}'
#    # payload=Parsed_data
#     response_code=requests.post(graylog_url, data=Parsed_data)
#     if response_code == '202':
#         print('Data was successfully sent to Graylog Server')
#     else:
#         print('Failed to sent data to Graylog Server')

#     #print(alld,'\n')
    
    return
if __name__ == '__main__': sys.exit(main(sys.argv))

