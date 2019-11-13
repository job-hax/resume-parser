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
    def usage():
        print ('usage: %s [-P password] [-o output] [-t text|html|xml|tag]'
               ' [-O output_dir] [-c encoding] [-s scale] [-R rotation]'
               ' [-Y normal|loose|exact] [-p pagenos] [-m maxpages]'
               ' [-S] [-C] [-n] [-A] [-V] [-M char_margin] [-L line_margin]'
               ' [-W word_margin] [-F boxes_flow] [-d] input.pdf ...' % argv[0])
        return 100
    try:
        (opts, args) = getopt.getopt(argv[1:], 'dP:o:t:O:c:s:R:Y:p:m:SCnAVM:W:L:F:')
    except getopt.GetoptError:
        return usage()
    if not args: return usage()
    # debug option
    debug = 0
    # input option
    password = b''
    pagenos = set()
    maxpages = 0
    # output option
    outfile = None
    outtype = None
    imagewriter = None
    rotation = 0
    stripcontrol = False
    layoutmode = 'normal'
    encoding = 'utf-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()
    pages_text = []
    for (k, v) in opts:
        if k == '-d': debug += 1
        elif k == '-P': password = v.encode('ascii')
        elif k == '-o': outfile = v
        elif k == '-t': outtype = v
        elif k == '-O': imagewriter = ImageWriter(v)
        elif k == '-c': encoding = v
        elif k == '-s': scale = float(v)
        elif k == '-R': rotation = int(v)
        elif k == '-Y': layoutmode = v
        elif k == '-p': pagenos.update( int(x)-1 for x in v.split(',') )
        elif k == '-m': maxpages = int(v)
        elif k == '-S': stripcontrol = True
        elif k == '-C': caching = False
        elif k == '-n': laparams = None
        elif k == '-A': laparams.all_texts = True
        elif k == '-V': laparams.detect_vertical = True
        elif k == '-M': laparams.char_margin = float(v)
        elif k == '-W': laparams.word_margin = float(v)
        elif k == '-L': laparams.line_margin = float(v)
        elif k == '-F': laparams.boxes_flow = float(v)
    #
    # PDFDocument.debug = debug
    # PDFParser.debug = debug
    # CMapDB.debug = debug
    # PDFPageInterpreter.debug = debug
    #
    retstr = io.StringIO()
    rsrcmgr = PDFResourceManager(caching=caching)
    device = TextConverter(rsrcmgr, retstr, laparams=laparams,imagewriter=imagewriter)
    data = []
    
    for fname in args:
        with open(fname, 'rb') as fp:
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.get_pages(fp, pagenos,
                                          maxpages=maxpages, password=password,
                                          caching=caching, check_extractable=True):
                interpreter.process_page(page)
                data = retstr.getvalue()
   #print(data)
    data=data.replace("\xa0", "")
    data=data.replace("\uf0da", "")
    data=data.replace("\x0c", "")
    data=data.replace("• ", "")
    data=data.replace("* ", "")
    data=data.replace("(LinkedIn)", "")
    data=data.replace(" (LinkedIn)", "")
    data=data.replace("\uf0a7", "")
    data=data.replace("(Mobile)", "")
    

    
    result_list=data.split('\n')
    # print(result_list)
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

    for i in result_list:
        if i=='Contact':
            value=result_list.index(i)
            while True:
                contact.append(result_list[value].strip())
                value=value+1
                if result_list[value] =='':
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
                skills.append(result_list[value])
                value=value+1
                if result_list[value] =='':
                    break
        if i.__contains__('Certifications'):
            value=result_list.index(i)
            while True:
                certifications.append(result_list[value])
                value=value+1
                if result_list[value] =='':
                    break
        if i.__contains__('Summary'):
            value=result_list.index(i)
            while True:
                summary.append(result_list[value])
                value=value+1
                if result_list[value] =='':
                    break
        if i=='Languages':
            value=result_list.index(i)
            while True:
                languages.append(result_list[value])
                value=value+1
                if result_list[value] =='':
                    break
        if i=='Experience':
            value=result_list.index(i)
            value=value+2
            while True:
                experience.append(result_list[value])
                value=value+1
                if result_list[value] =='':
                    break
            
            listOfExp = ["company", "position","period","place","description" ]
   
            zipbObj = zip(listOfExp, experience)
            exp_dict = dict(zipbObj)

        
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

    print(languages)
    #print(contact,'\n',linkedin,'\n',summary,'\n',skills,'\n',certifications,'\n',languages,'\n',exp_dict,'\n',edu_dict)

    #print(data.splitlines())
    device.close()
    retstr.close()
    return
if __name__ == '__main__': sys.exit(main(sys.argv))

