from django.http.response import HttpResponse
from django.shortcuts import render
import pdfplumber
import datetime
# Create your views here.
def index(request):
    # return HttpResponse("this is homepage")
    context = {
        'veriable':"this is the veriable from view",
        'veriable1':"this is the veriable1 from view"

    }
    return render(request,"index.html",context)
def about(request):
    # return HttpResponse("this is aboutpage")
    context = {
        'veriable':"this is the veriable from view",
        'veriable1':"this is the veriable1 from view"

    }
    return render(request,"About.html",context)
def Timetable(file,UserSection):
   
    linesComputing = ["LONDON METROPOLITAN UNIVERSITY"]
    linesNetworking = ["LONDON METROPOLITAN UNIVERSITY"]
    linesMultimedia = ["LONDON METROPOLITAN UNIVERSITY"]
    switch1=0
    switch2=0
    with pdfplumber.open(file) as pdf:
        pages = pdf.pages
        for page in pdf.pages:
            text = page.extract_text()
            for line in text.split('\n'):
                # lines.append(line)
                if line =="LONDON METROPOLITAN UNIVERSITY":
                    switch1 =1
                # else:
                #     break
                #     break    
                if switch1 == 1:
                    # print("switch2")
                    if line == "YEAR 3 COMPUTING TIME TABLE":
                        switch2 =1
                    elif line == "YEAR 3 NETWORKING TIME TABLE":
                        switch2 =2
                    elif line == "YEAR 3 MULTIMEDIA TIME TABLE":
                        switch2 =3

                    if switch2 ==1:
                        linesComputing.append(line)
                    elif switch2 ==2:
                        linesNetworking.append(line)
                    elif switch2 ==3:
                        linesMultimedia.append(line)
    listup=[]
    if UserSection.find("C") != -1 or UserSection.find("c") != -1:
        for i in linesComputing:
        
            
            if str(type(i.rfind(UserSection)))=="<class 'int'>":
                if i.rfind(UserSection) != -1:
                    if (i[(i.rindex(UserSection)+((len(UserSection))))]) == " " or (i[(i.rindex(UserSection)+((len(UserSection))))]) == "+":
                        listup.append(i)
    if UserSection.find("N") != -1 or UserSection.find("n") != -1:
        for i in linesNetworking:
            # print(i.find("C13"))
        
            
            if str(type(i.rfind(UserSection)))=="<class 'int'>":
                if i.rfind(UserSection) != -1:
                    if (i[(i.rindex(UserSection)+((len(UserSection))))]) == " " or (i[(i.rindex(UserSection)+((len(UserSection))))]) == "+":
                        listup.append(i)
                   
    if UserSection.find("M") != -1 or UserSection.find("m") != -1:
        for i in linesMultimedia:
            # print(i.find("C13"))
            if str(type(i.rfind(UserSection)))=="<class 'int'>":
                if i.rfind(UserSection) != -1:
                    if (i[(i.rindex(UserSection)+((len(UserSection))))]) == " " or (i[(i.rindex(UserSection)+((len(UserSection))))]) == "+":
                        listup.append(i)
    tostring = ' '.join(str(e +',') for e in listup) 
    l = len(tostring)
    tostring = tostring[:l-1]  
                 
    # return tostring
    return listup
def weekday():
    dayint = datetime.datetime.today().weekday()
    if dayint == 1:
        dayint = 'Tue'
    elif dayint == 2:
        dayint = 'Wed'
    elif dayint == 3:
        dayint = 'Thu'
    elif dayint == 4:
        dayint = 'Fri'
    elif dayint == 5:
        dayint = 'Sat'
    elif dayint == 6:
        dayint = 'Sun'
    elif dayint == 0:
        dayint = 'Mon'
        

    
    return  dayint
def todaysTimetable(data):
    today= weekday().upper()
    finalData = []
    for i in data:
        if i.find(today) != -1:
            finalData.append(i)
    return finalData
def services(request):
    # return HttpResponse("this is servicespage")
    context = {
        'veriable':"this is the veriable from view",
        'veriable1':"this is the veriable1 from view"

    }
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['document']
            sectionS = request.POST['section']
            # print(uploaded_file.name)
            # print(uploaded_file.size)
            toshow = Timetable(uploaded_file,sectionS)
            newver = todaysTimetable(toshow)
            countTodaysclass = str(len(newver))


            



            context = {
            'veriable':weekday() ,
            'veriable1':'Your total number of class for today is '+countTodaysclass,
            'veriable2':newver,
            'values':toshow}
            return render(request,"Services.html",context)
        except:
            context = {
            'veriable':"Some thing went wrong",
            'veriable1':"empty field or non pdf type data type is not exceptable."}
            return render(request,"Services.html",context)


        


    return render(request,"Services.html",context)
def Contact(request):
    # return HttpResponse("this is Contactpage")
    context = {
        'veriable':"this is the veriable from view",
        'veriable1':"this is the veriable1 from view"

    }
    return render(request,"Contact.html",context)