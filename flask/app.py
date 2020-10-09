from flask import Flask, request, render_template, redirect,send_file, make_response
# from flask import Flask, request, render_template, session, redirect,send_file, make_response
from cloudant.client import Cloudant
import pandas as pd
import matplotlib.pyplot as plt
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
from matplotlib.backends.backend_pdf import PdfPages
import pypandoc
import requests
# from flask_session import Session
# from flask.ext.session import Session
from redis import Redis
import redis
import os
import urllib.parse
from urllib.parse import parse_qsl, urljoin, urlparse



app = Flask(__name__,template_folder='templates')
# SESSION_TYPE = 'filesystem'
# app.config.from_object(__name__)
# Session(app)

# session["globaldb"]=""
# session["username"]=""
# session["password"]=""
# session=redis.from_url(os.environ['REDISCLOUD_URL'])
# url = urlparse(os.environ.get('redis://:p0LH1HMATyAmzR052x8kjoXj7Ft9Bkab@redis-11919.c232.us-east-1-2.ec2.cloud.redislabs.com:11919'))
session = redis.Redis(host="redis-11919.c232.us-east-1-2.ec2.cloud.redislabs.com", port="11919", password="p0LH1HMATyAmzR052x8kjoXj7Ft9Bkab")

def getall(param,db):
    db_username =  param['username']  
    api = param['api']
    databaseName = db
    client = Cloudant.iam(db_username,api, connect = True)
    myDatabaseDemo = client[databaseName]
    dic={}
    i=0
    for document in myDatabaseDemo:
        dic[i]=document["_id"]
        i=i+1
    return dic

def getDBdoc(param,id,db):
    db_username = param['username']  
    api = param['api'] 
    databaseName = db
    client = Cloudant.iam(db_username,api, connect = True)
    myDatabaseDemo = client[databaseName]
    db_doc = myDatabaseDemo[id]
    return  db_doc

@app.route('/wel_cust',methods=['POST'])
def wel_cust():
    logdb="customer_login"
    #     session["globaldb"]=""
    #     session["username"]=""
    #     session["password"]=""
    session.set('globaldb',"")
    session.set('username',"")
    session.set('password',"")
    #     global username
    #     session["username"] = request.form['username']
    s=request.form['username']
    session.set('username',s)
    a=request.form['password']
    session.set('password',a)
    #     global password
    #     session["password"] = request.form['password']
    pp={'username':"4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",'api':"4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6"}
    #     client = Cloudant.iam(
    #         "4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",
    #         "4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6",
    #         connect=True)
    #     my_database = client['customer_login']
    u=session.get('username')
    p=session.get('password')
    u=u.decode("utf-8")
    p=p.decode("utf-8")
    if(u=="" or p==""):
        message="Please enter both username and password"
        return render_template('cust_login.html',me=message)
    matchu=False
    matchp=False
    bleh= getall(pp,logdb)
    l=len(bleh)   
    for i in range(0,l):
        id=bleh[i]
        haha=getDBdoc(pp,id,logdb)
        matchu=False
        matchp=False
        if(haha['username']==u):
            matchu=True
            if(haha['password']==p):
                matchp=True
                x={}
    #                 global globaldb
    #                 globaldb=haha['db_name']
                hh=haha['db_name']
                session.set('globaldb',hh)
    #                 response = requests.post('https://eu-gb.functions.appdomain.cloud/api/v1/web/sanjanasr.cs18%40rvce.edu.in_dev/default/start.json', json={'db_name': globaldb,'username':username})
                break

    if(matchu==False or matchp==False):
        message="Invalid username or password"
        return render_template('cust_login.html',me=message)

    u=session.get('username')
    g=session.get('globaldb')
    u=u.decode("utf-8")
    g=g.decode("utf-8")
    return render_template('Wel_cust.html',name=u,db_name=g)

@app.route('/wel_serv',methods=['POST'])
def wel_serv():
    logdb="service_login"
    #     session["globaldb"]=""
    #     session["username"]=""
    #     session["password"]=""
#     session.set('globaldb',"")
    session.set('username',"")
    session.set('password',"")
    #     global username
    #     session["username"] = request.form['username']
    s=request.form['username']
    session.set('username',s)
    a=request.form['password']
    session.set('password',a)
    #     global password
    #     session["password"] = request.form['password']
    pp={'username':"4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",'api':"4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6"}
    #     client = Cloudant.iam(
    #         "4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",
    #         "4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6",
    #         connect=True)
    #     my_database = client['customer_login']
    u=session.get('username')
    p=session.get('password')
    u=u.decode("utf-8")
    p=p.decode("utf-8")
    if(u=="" or p==""):
        message="Please enter both username and password"
        return render_template('serv_login.html',me=message)
    matchu=False
    matchp=False
    bleh= getall(pp,logdb)
    l=len(bleh)   
    for i in range(0,l):
        id=bleh[i]
        haha=getDBdoc(pp,id,logdb)
        matchu=False
        matchp=False
        if(haha['username']==u):
            matchu=True
            if(haha['password']==p):
                matchp=True
                x={}
    #                 global globaldb
    #                 globaldb=haha['db_name']
#                 hh=haha['db_name']
#                 session.set('globaldb',hh)
    #                 response = requests.post('https://eu-gb.functions.appdomain.cloud/api/v1/web/sanjanasr.cs18%40rvce.edu.in_dev/default/start.json', json={'db_name': globaldb,'username':username})
                break

    if(matchu==False or matchp==False):
        message="Invalid username or password"
        return render_template('serv_login.html',me=message)

    u=session.get('username')
#     g=session.get('globaldb')
    u=u.decode("utf-8")
#     g=g.decode("utf-8")
    return render_template('Wel_serv.html',name=u)

@app.route('/signout',methods=['GET','POST'])
def signout():
    if (request.form['signout_button'] == 'signout'):
#         session["globaldb"]=""
#         session["username"]=""
#         session["password"]=""
        session.set('globaldb',"")
        session.set('username',"")
        session.set('password',"")
        return render_template('cust_login.html')
@app.route('/signout2',methods=['GET','POST'])
def signout2():
    if (request.form['signout_button2'] == 'signout'):
#         session["globaldb"]=""
#         session["username"]=""
#         session["password"]=""
#         session.set('globaldb',"")
        session.set('username',"")
        session.set('password',"")
        session.set('tp_name',"")
        return render_template('trading_login.html')
@app.route('/signout3',methods=['GET','POST'])
def signout3():
    if (request.form['signout_button3'] == 'signout'):
#         session["globaldb"]=""
#         session["username"]=""
#         session["password"]=""
#         session.set('globaldb',"")
        session.set('username',"")
        session.set('password',"")
        return render_template('serv_login.html')


@app.route('/')
def home():
    return render_template('login_main.html')

@app.route('/trading_partner',methods=['GET','POST'])
def trading_partner():
    if(request.form['trading partner'] == 'Trading Partner'):
        return render_template('trading_login.html')

@app.route('/customer',methods=['GET','POST'])
def customer():
    if(request.form['customer'] == 'Customer'):
        return render_template('cust_login.html')
    
@app.route('/service',methods=['GET','POST'])
def service():
    if(request.form['service'] == 'Service Provider'):
        return render_template('serv_login.html')
    
    
@app.route('/wel_trade',methods=['POST'])
def wel_trade():
    logdb="trading_partner_login"
    #     session["globaldb"]=""
    #     session["username"]=""
    #     session["password"]=""
#     session.set('globaldb',"")
    session.set('username',"")
    session.set('password',"")
    session.set('tp_name',"")
    
    #     global username
    #     session["username"] = request.form['username']
    s=request.form['username']
    session.set('username',s)
    a=request.form['password']
    session.set('password',a)
    #     global password
    #     session["password"] = request.form['password']
    pp={'username':"4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",'api':"4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6"}
    #     client = Cloudant.iam(
    #         "4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",
    #         "4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6",
    #         connect=True)
    #     my_database = client['customer_login']
    u=session.get('username')
    p=session.get('password')
    u=u.decode("utf-8")
    p=p.decode("utf-8")
    if(u=="" or p==""):
        message="Please enter both username and password"
        return render_template('trading_login.html',me=message)
    matchu=False
    matchp=False
    bleh= getall(pp,logdb)
    l=len(bleh)   
    for i in range(0,l):
        id=bleh[i]
        haha=getDBdoc(pp,id,logdb)
        matchu=False
        matchp=False
        if(haha['username']==u):
            matchu=True
            if(haha['password']==p):
                matchp=True
                x={}
    #                 global globaldb
    #                 globaldb=haha['db_name']
#                 hh=haha['db_name']
#                 session.set('globaldb',hh)
                nn=haha['tp_name']
                session.set('tp_name',nn)
    #                 response = requests.post('https://eu-gb.functions.appdomain.cloud/api/v1/web/sanjanasr.cs18%40rvce.edu.in_dev/default/start.json', json={'db_name': globaldb,'username':username})
                break

    if(matchu==False or matchp==False):
        message="Invalid username or password"
        return render_template('trading_login.html',me=message)

    u=session.get('username')
#     g=session.get('globaldb')
    u=u.decode("utf-8")
#     g=g.decode("utf-8")
    t=session.get('tp_name')
    t=t.decode("utf-8")
    
    
#     li=[]
    
#     bleh= getall(pp,"customer_login")
#     l=len(bleh)   
#     for i in range(0,l):
#         id=bleh[i]
#         haha=getDBdoc(pp,id,"customer_login")
#         dd=haha['db_name']
#         bleh2= getall(pp,dd)
#         le=len(bleh2)   
#         for i in range(0,le):
#             id=bleh2[i]
#             haha2=getDBdoc(pp,id,dd)
#             if(haha2['tp_name']==t and haha2['filled_form']=='false'):
#                 li.append({"customer name":haha['cust_name'],"username":haha2['tp_login'],"password":haha2['tp_pass']})
#                 break
#     df2 = pd.DataFrame(li)
#     if(len(li)==0):
#         return render_template('Wel_trade.html',name=u,db_name="trade_master",tp=t,lis=li,mes="Currently there are no forms left to fill",tables=[df2.to_html(classes='data',table_id='htmltable2',index=False)])
        
    
        
            
                
    
    
    return render_template('Wel_trade.html',name=u,db_name="trade_master",tp=t)
        
    

@app.route('/back',methods=['GET','POST'])
def back():
    if (request.form['submitt_button'] == 'Go back'):
        u=session.get("username")
        g=session.get("globaldb")
        u=u.decode("utf-8")
        g=g.decode("utf-8")
        return render_template('Wel_cust.html',name=u,db_name=g)
    
    
@app.route('/back2',methods=['GET','POST'])
def back2():
    if (request.form['submitt_button5'] == 'Go back'):
        u=session.get("username")
#         g=session.get("globaldb")
        u=u.decode("utf-8")
#         g=g.decode("utf-8")
        session.set('customer_report',"")
        session.set('cust_db',"")

        return render_template('Wel_serv.html',name=u)
    
@app.route('/html_table', methods=['GET','POST'])
def html_table():
    if request.form['submit_button'] == 'Do Something':
        client = Cloudant.iam(
        "4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",
        "4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6",
        connect=True)
        g=session.get("globaldb")
        my_database = client[g]
        l=[]
        for document in my_database:
            l.append(document)
        df = pd.DataFrame(l)
        del df['_id']
        del df['_rev']
#         del df['tp_login']
#         del df['tp_pass']
        del df['form_filled']
        cols=["tp_name","VAN_or_AS2","contact_person","email_id","status"]
        df = df[cols]
        
        df['VAN_or_AS2'].value_counts().plot(kind='bar')
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("Number of VAN and AS2")
        axis.grid()
        bd=df['VAN_or_AS2'].value_counts()
        b = dict(bd)
        axis.bar(b.keys(), b.values(), width=0.2, align='edge')
        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)
        pngImageB64String = "data:image/png;base64,"
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("Project status ")
        axis.grid()
        labels=[]
        sizes=[]
        bd=df['status'].value_counts()
        b = dict(bd)
        for x, y in b.items():
            labels.append(x)
            sizes.append(y)
        patches, texts=axis.pie(sizes, labels=labels)
        axis.legend(patches, labels, loc="best")
        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)
        pngImageB64String1 = "data:image/png;base64,"
        pngImageB64String1 += base64.b64encode(pngImage.getvalue()).decode('utf8')
        return render_template('new.html',  tables=[df.to_html(classes='data',table_id='htmltable',index=False)],image=pngImageB64String, image1=pngImageB64String1)

@app.route('/html_table2', methods=['GET','POST'])
def html_table2():
    if request.form['submit_button4'] == 'Do Something':
        client = Cloudant.iam(
        "4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",
        "4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6",
        connect=True)
#         g=session.get("globaldb")
#         my_database = client[g]
        l=[]
        pp={'username':"4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",'api':"4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6"}
        u=session.get("username")
#         g=session.get("globaldb")
        u=u.decode("utf-8")
        cu=request.form['customer_name']
        if(cu==""):
            return render_template('Wel_serv.html',name=u,me="Please enter a customer name")
            
        session.set('customer_report',cu)
        c=session.get('customer_report')
        c=c.decode("utf-8")
        matchp=False
        bleh= getall(pp,"customer_login")
        le=len(bleh)   
        for i in range(0,le):
            id=bleh[i]
            haha=getDBdoc(pp,id,"customer_login")
            matchp=False
            if(haha['cust_name']==c):
                matchp=True
                
        #                 global globaldb
        #                 globaldb=haha['db_name']
                hhh=haha['db_name']
                session.set('cust_db',hhh)
        #                 response = requests.post('https://eu-gb.functions.appdomain.cloud/api/v1/web/sanjanasr.cs18%40rvce.edu.in_dev/default/start.json', json={'db_name': globaldb,'username':username})
                break
        if(matchp==False):
            return render_template('Wel_serv.html',name=u,me="No such customer")
            
        hh=session.get('cust_db')
        hh=hh.decode("utf-8")
        
        my_database = client[hh]
        for document in my_database:
            l.append(document)
        df = pd.DataFrame(l)
        del df['_id']
        del df['_rev']
#         del df['tp_login']
#         del df['tp_pass']
        del df['filled_form']
        cols=["tp_name","VAN_or_AS2","contact_person","email_id","status"]
        df = df[cols]
        
        df['VAN_or_AS2'].value_counts().plot(kind='bar')
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("Number of VAN and AS2")
        axis.grid()
        bd=df['VAN_or_AS2'].value_counts()
        b = dict(bd)
        axis.bar(b.keys(), b.values(), width=0.2, align='edge')
        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)
        pngImageB64String = "data:image/png;base64,"
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("Project status ")
        axis.grid()
        labels=[]
        sizes=[]
        bd=df['status'].value_counts()
        b = dict(bd)
        for x, y in b.items():
            labels.append(x)
            sizes.append(y)
        patches, texts=axis.pie(sizes, labels=labels)
        axis.legend(patches, labels, loc="best")
        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)
        pngImageB64String1 = "data:image/png;base64,"
        pngImageB64String1 += base64.b64encode(pngImage.getvalue()).decode('utf8')
        return render_template('new2.html',  tables=[df.to_html(classes='data',table_id='htmltable',index=False)],image=pngImageB64String, image1=pngImageB64String1,cc=c)


@app.route('/download', methods=['GET','POST'])
def download():
    if request.form['submit_button'] == 'download':
        client = Cloudant.iam(
        "4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",
        "4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6",
        connect=True)
        g=session.get("globaldb")
        my_database = client[g]
        l=[]
        for document in my_database:
            l.append(document)
        df = pd.DataFrame(l)
        del df['_id']
        del df['_rev']
        cols=["tp_name","VAN_or_AS2","contact_person","email_id","status"]
        df = df[cols]
        with PdfPages('report.pdf') as pp:
            fig, (ax,ax1,ax2) =plt.subplots(3,1,figsize=(10,15))#figsize=(12,4)
            ax.set_title("Project Reports")
            ax.axis('tight')
            ax.axis('off')
            the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center',cellLoc='left',colLoc='left')
            ax1.set_title("Number of VAN and AS2")
            ax1.grid()
            bd=df['VAN_or_AS2'].value_counts()
            b = dict(bd)
            ax1.bar(b.keys(), b.values(), width=0.2, align='edge')
            ax2.set_title("Project status ")
            ax2.grid()
            labels=[]
            sizes=[]
            bd=df['status'].value_counts()
            b = dict(bd)
            for x, y in b.items():
                labels.append(x)
                sizes.append(y)
            patches, texts=ax2.pie(sizes, labels=labels)
            ax2.legend(patches, labels, loc="best")
            pp.savefig(fig, bbox_inches='tight')
            plt.close()
        path = "report.pdf"
        return send_file(path, as_attachment=True)
    
@app.route('/download2', methods=['GET','POST'])
def download2():
    if request.form['submit_button6'] == 'download':
        client = Cloudant.iam(
        "4a366964-f520-4ba2-afba-9a1b374f4277-bluemix",
        "4FpjCCjAVftwY8ZLZDSUJa_8iG14u0c0VsXPB-YEhrU6",
        connect=True)
        g=session.get("cust_db")
        c=session.get("customer_report")
        c=c.decode("utf-8")

        my_database = client[g]
        l=[]
        for document in my_database:
            l.append(document)
        df = pd.DataFrame(l)
        del df['_id']
        del df['_rev']
        cols=["tp_name","VAN_or_AS2","contact_person","email_id","status"]
        df = df[cols]
        with PdfPages('report.pdf') as pp:
            fig, (ax,ax1,ax2) =plt.subplots(3,1,figsize=(10,15))#figsize=(12,4)
            ax.set_title("Project Reports of Trading Partners of "+c)
            ax.axis('tight')
            ax.axis('off')
            the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center',cellLoc='left',colLoc='left')
            ax1.set_title("Number of VAN and AS2")
            ax1.grid()
            bd=df['VAN_or_AS2'].value_counts()
            b = dict(bd)
            ax1.bar(b.keys(), b.values(), width=0.2, align='edge')
            ax2.set_title("Project status ")
            ax2.grid()
            labels=[]
            sizes=[]
            bd=df['status'].value_counts()
            b = dict(bd)
            for x, y in b.items():
                labels.append(x)
                sizes.append(y)
            patches, texts=ax2.pie(sizes, labels=labels)
            ax2.legend(patches, labels, loc="best")
            pp.savefig(fig, bbox_inches='tight')
            plt.close()
        path = "report.pdf"
        return send_file(path, as_attachment=True)
    
@app.route('/main_page2', methods=['GET','POST'])
def main_page2():
    session.set('customer_report',"")
    session.set('cust_db',"")
    session.set('username',"")
    session.set('password',"")
    session.set('global_db',"")
    session.set('tp_name',"")
    if (request.form['signout_button12'] == 'Go to Main Login' ):
        return render_template('login_main.html')

@app.route('/main_page1', methods=['GET','POST'])
def main_page1():
    session.set('customer_report',"")
    session.set('cust_db',"")
    session.set('username',"")
    session.set('password',"")
    session.set('global_db',"")
    session.set('tp_name',"")
    if (request.form['signout_button11'] == 'Go to Main Login' ):
        return render_template('login_main.html')

@app.route('/main_page3', methods=['GET','POST'])
def main_page3():
    session.set('customer_report',"")
    session.set('cust_db',"")
    session.set('username',"")
    session.set('password',"")
    session.set('global_db',"")
    session.set('tp_name',"")
    if (request.form['signout_button13'] == 'Go to Main Login' ):
        return render_template('login_main.html')
    
    

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)