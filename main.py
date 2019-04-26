# [SOF]
#
# Information Area {Start}:
# - File(s) Information: 
# -- Central File:
# ---- main.py
# ----- File Path: 
# ------ C:\Users\Gary\lc101\web-caesar\main.py
# ----- Relative File Path: 
# ------ main.py
# -- Funtional Permanent Archive Files:
# ---- File Paths:
# ------ C:\Users\Gary\lc101\web-caesar\main_c0a1p1_tpoa2op2of5.py
# -- Additional Key Files:
# ----- File Path:
# ------ C:\Users\Gary\lc101\web-caesar\caesar.py 
# ----- Relative File Path: 
# ------ caesar.py
# ----- Flask Virtual Environment:
# ------ flask-env
# 
# - Context: 
# -- Program, Support And Organization Context:
# --- LaunchCode: LC101 January 2019 (LC101 STL JAN19)
# --- {https://learn.launchcode.org/courses/160}
# --- LaunchCode St. Louis: LaunchCode Mentor Center:
# --- launchcode.org or learnstl@launchcode.org or
# --- 314-254-0107 or 4811 Delmar Blvd, St. Louis, MO 63108
#
# - Program Support And Resources:
# -- LaunchCode Mentor Center St. Louis :: LC101 January 2019
# -- Slack Utility: htttps://lc101winter2019.slack.com
# -- TA-Team: "deep_space_orbiters"
# --- TA = "SLY237" ((KINGSLY SHEY TANYU) = TA for Kingsly's Team: "deep_space_orbiters"
# ---- (a Collaboration Innovation Progress Group)
# --- LAUNCHCODE HELP FORUM :: http://help.launchcode.org/
#
# - External Documentation And Other Resources:
# -- https://learn.launchcode.org
# -- https://docs.python.org
# -- https://stackoverflow.com
# -- https://www.w3schools.com
# -- https://www.codecademy.com
# -- https://www.khanacademy.org
# -- https://github.com/
# -- https://git-scm.comv
#
# - Assignment:
# -- LC101 StL Winter 2019: Unit # 2: Web Caesar Asssignment
# -- Assignment Information, Provided Instructions, Provided Code, Etc.:
# --- Informatioin from the Assignment:
# --- Provided Code from the Assignment:
#
# - Project Coder: 
# -- Gary Cotton  gary.cotton.codemaker.helper@gmail.com  m: 314-283-9875 
# --- Git Hub: Account Name: gary-cotton-tech-collaborator
# --- Git Hub: Account Email: gary.cottom.tech.collaborator@gmail.com
# --- Git Hub Account URL: https://github.com/gary-cotton-tech-collaborator
# --- Git Hub Assignment URL: ($ git remote add origin) https://github.com/gary-cotton-tech-collaborator/web-caesar.git
# --- $ git remote --verbose
# ---- origin  https://github.com/gary-cotton-tech-collaborator/web-caesar.git (fetch)
# ---- origin  https://github.com/gary-cotton-tech-collaborator/web-caesar.git (push)
# --- Git--Miniconda Virtuaal Environment: (hello-flask)
# 
# - Program:: Events: / Versions: / Dates: / Times:
# -- Program: Newsearch-Provelopment:
# --- Version / Date / Time:
# --- a0 /     2019-Apr-13-Saturday / ~15:00~ pm CDT
#
# --  Program: In Work: 
# --- Version / Date / Time:
# --- b0 /     2019-Qpr-14-Sunday / ~18:00 pm CDT
#
# --  Program: ==>> Partially: <<== Current, Revised, Integrated, Tested, Functional, Working!:
# --- Version   / Date                / Time:
# --- c0a0     /  2019-Apr-15-Monday / 03:46 am CDT
#
# --  Program: ==>> Fully: <<==Current, Revised, Integrated, Tested, Functional, Working!, To Be Git Integrated & Submitted:
# --- Version   / Date                / Time:
# --- c0a0     /  2019-Apr-21-Saturday / 22:52 pm CDT

# - Omniversal Notes, Thoughts, Questions, Concerns, Ideas, Reflections, Hopes, Etc.:
# -- *(2019Mar30Sat1828)* Please Note: I, Gary Cotton, would like to create an additional webpage/website that shares and expresses the mathematics of
# --  Nature, such as the area of Fractals, and how they help guide the growth and well-being of plants, and life in general.
#
# Information Area {_End_}:
#
# Code Area {Start}:
#
from flask import Flask, request
from caesar import rotate_string
#
app = Flask(__name__)
app.config['DEBUG'] = True
#
form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
<!--               height: 120px; -->
<!--               font: 16px sans-serif; --->
                font-family: sans-serif;
                font-size: 16px;
                border-radius: 10px;
            }}
            textarea {{
<!--                font: 16px sans-serif -->
                font-family: sans serif;
                font-size: 32px;
                margin: 10px 0;
                width: 540px;
                height: 120px;
<!--               width: 720px; -->
<!--               height: 540px; -->
            }}
        </style>
    </head>
    <body>    
      <!-- create your form here -->
<!--            <form action="/hello" method="POST"> -->
<!--           <form action="/encrypt" method="POST"> -->
            <form action="/" method="POST">

                <label for="rotation-spec"> Rotate by: </label>
                <input id="rotation-spec" type="text" name="rot" value="0"/>
                <br><br>
        <label> Enter Text To Encrypt:  
<!--            <textarea id="text-to-encrypt" name="text"> '<h1>' + encrypted_text_str + '</h1>' </textarea> -->
            <textarea id="text-to-encrypt" name="text" font="72px" >{0}</textarea>
        </label>
<!--               <label for="text-to-encrypt"> Enter Text To Encrypt: </label> -->
<!--                <input id="text-to-encrypt" type=textarea name="text" /> -->
<!--                <label for="submit-button"> Submit Query: </label> -->
                <input id="submit-button" type="submit" />
            </form>
    </body>
</html>
"""

###>
# form = """
# <!doctype = html>
#     <html>
#         <body>
#             <form action="/hello" method="POST">
#                 <label for="first-name"> First Name: </label>
#                 <input id="first-name" type="text" name="first_name" />
#                 <input type="submit" />
#             </form>
#         </body>
#     </html>
# """
###<
@app.route("/", methods=['GET'])
def index():
    return form.format("")
#
# @app.route("/encrypt", methods=['POST'])
@app.route("/", methods=['POST'])
#
def encrypt():
#     rotation_spec_int = int(request.form('rot'))
    rotation_spec_str = request.form['rot']
    rotation_spec_int = int(rotation_spec_str)
    text_to_encrypt_str = (request.form['text'])
#    encrypted_text_str = rotate_string(rotation_spec_int, text_to_encrypt_str)
    encrypted_text_str = rotate_string(text_to_encrypt_str, rotation_spec_int)
#
#     return '<h1>' + encrypted_text_str + '</h1>'
    return form.format(encrypted_text_str)
#
# @app.route("/hello", methods=['POST'])
# @app.route("/hello", methods=['POST', 'GET'])
# def hello():
#    first_name = request.args.get('first_name')
#     first_name = request.form['first_name']
#     return '<h1>Hello, ' + first_name + '</h1>'
#
app.run()
#
# Code Area {_End_}:
#
# [EOF]