# from fastapi import FastAPI
#
# from scan import scanner, disarm
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.post("/scan_model")
# def scan_model(model: str):
#     res = scanner(model)
#     return {"Scan result" : res}
#
#
# @app.post("/disarm_model")
# def scan_model(model: str):
#     res = disarm(model)
#     return {"Disarm result" : "The model disarmed!"}
#
# @app.post("/scan_and_disarm_model")
# def scan_model(model: str):
#     res = disarm(model)
#     return {"Scan and disarm result" : "The model disarmed!"}

#####################################################################################3
## version 2 -
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel
#
# from scan import scanner, disarm
#
# app = FastAPI()
#
# # HTML for the frontend
# html_content = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Model Scanner</title>
# </head>
# <body>
#     <h1>Model Scanner Interface</h1>
#     <input type="text" id="model_input" placeholder="Enter model name">
#     <button onclick="scanModel()">Scan Model</button>
#     <button onclick="disarmModel()">Disarm Model</button>
#     <button onclick="scanAndDisarmModel()">Scan and Disarm Model</button>
#     <p id="result"></p>
#
#     <script>
#         async function scanModel() {
#             console.log("scanModel called");  // Log when function is called
#             const modelName = document.getElementById('model_input').value;
#             console.log("Model Name: ", modelName);  // Log the model name being sent
#             const response = await fetch('/scan_model', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ model: modelName })
#             });
#             const data = await response.json();
#             document.getElementById('result').innerText = 'Scan result: ' + data.Scan_result;
#             console.log("Response Data: ", data);  // Log the response data
#         }
#
#         async function disarmModel() {
#             const modelName = document.getElementById('model_input').value;
#             const response = await fetch('/disarm_model', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ model: modelName }) // Ensure the key 'model' is used
#             });
#             const data = await response.json();
#             document.getElementById('result').innerText = 'Disarm result: ' + data.Disarm_result;
#         }
#
#         async function scanAndDisarmModel() {
#             const modelName = document.getElementById('model_input').value;
#             const response = await fetch('/scan_and_disarm_model', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ model: modelName }) // Ensure the key 'model' is used
#             });
#             const data = await response.json();
#             document.getElementById('result').innerText = 'Scan and disarm result: ' + data.Scan_and_disarm_result;
#         }
#
#     </script>
# </body>
# </html>
# """
#
# class Model(BaseModel):
#     model: str
#
# @app.get("/", response_class=HTMLResponse)
# def read_root():
#     return html_content
#
#
# @app.post("/scan_model")
# def scan_model(model_data: Model):
#     res = scanner(model_data.model)
#     return {"Scan result" : res}
#
#
# @app.post("/disarm_model")
# def disarm_model(model: str):
#     res = disarm(model)
#     return {"Disarm result" : "The model disarmed!"}
#
# @app.post("/scan_and_disarm_model")
# def scan_and_disarm_model(model: str):
#     res = disarm(model)
#     return {"Scan and disarm result" : "The model disarmed!"}
####################################################################################
# version 3  works but GUI look bad-
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel
#
# from scan import scanner, disarm
#
# app = FastAPI()
#
# # Define the Pydantic model for incoming data
# class Model(BaseModel):
#     model: str
#
# # HTML content for the frontend
# html_content = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Model Scanner</title>
# </head>
# <body>
#     <h1>Model Scanner Interface</h1>
#     <input type="text" id="model_input" placeholder="Enter model name">
#     <button onclick="scanModel()">Scan Model</button>
#     <button onclick="disarmModel()">Disarm Model</button>
#     <button onclick="scanAndDisarmModel()">Scan and Disarm Model</button>
#     <p id="result"></p>
#
#     <script>
#         async function scanModel() {
#             const modelName = document.getElementById('model_input').value;
#             const response = await fetch('/scan_model', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ model: modelName })
#             });
#             const data = await response.json();
#             document.getElementById('result').innerText = 'Scan result: ' + data.result;
#         }
#
#         async function disarmModel() {
#             const modelName = document.getElementById('model_input').value;
#             const response = await fetch('/disarm_model', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ model: modelName })
#             });
#             const data = await response.json();
#             document.getElementById('result').innerText = 'Disarm result: ' + data.result;
#         }
#
#         async function scanAndDisarmModel() {
#             const modelName = document.getElementById('model_input').value;
#             const response = await fetch('/scan_and_disarm_model', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ model: modelName })
#             });
#             const data = await response.json();
#             document.getElementById('result').innerText = 'Scan and disarm result: ' + data.result;
#         }
#     </script>
# </body>
# </html>
# """
#
# @app.get("/", response_class=HTMLResponse)
# def read_root():
#     return html_content
#
# @app.post("/scan_model")
# def scan_model(model_data: Model):
#     res = scanner(model_data.model)
#     return {"result": res}
#
# @app.post("/disarm_model")
# def disarm_model(model_data: Model):
#     res = disarm(model_data.model)
#     return {"result": "The model disarmed!"}
#
# @app.post("/scan_and_disarm_model")
# def scan_and_disarm_model(model_data: Model):
#     res = disarm(model_data.model)
#     return {"result": "The model disarmed!"}

#####################################################################33
## version 4 - good GUI
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel
#
# from scan import scanner, disarm
#
# app = FastAPI()
#
# class Model(BaseModel):
#     model: str
#
# html_content = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Model Scanner</title>
#     <style>
#         body, html {
#             height: 100%;
#             margin: 0;
#             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#             background-color: #f4f4f9;
#             display: flex;
#             justify-content: center;
#             align-items: center;
#         }
#         .container {
#             background: white;
#             padding: 40px;
#             border-radius: 10px;
#             box-shadow: 0 4px 16px rgba(0,0,0,0.2);
#             width: 50%; /* Adjust width here to control the size of the form */
#             max-width: 600px; /* Ensures the form doesn't get too wide on larger screens */
#             display: flex;
#             flex-direction: column;
#             align-items: stretch;
#         }
#         input, button {
#             padding: 15px;
#             margin-top: 10px;
#             border-radius: 5px;
#             border: 1px solid #ccc;
#             width: 100%;
#             box-sizing: border-box; /* Ensures padding doesn't affect width */
#         }
#         button {
#             background-color: #007BFF;
#             color: white;
#             cursor: pointer;
#             transition: background-color 0.3s;
#         }
#         button:hover {
#             background-color: #0056b3;
#         }
#         p {
#             color: #333;
#             background-color: #e2e3e5;
#             padding: 15px;
#             border-radius: 5px;
#             text-align: center;
#             margin-top: 10px;
#         }
#     </style>
# </head>
# <body>
#     <div class="container">
#         <h1>Model Scanner Interface</h1>
#         <input type="text" id="model_input" placeholder="Enter model name">
#         <button onclick="scanModel()">Scan Model</button>
#         <button onclick="disarmModel()">Disarm Model</button>
#         <button onclick="scanAndDisarmModel()">Scan and Disarm Model</button>
#         <p id="result">Results will appear here</p>
#     </div>
#
#     <script>
#         async function scanModel() {
#             const modelName = document.getElementById('model_input').value;
#             const response = await fetch('/scan_model', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ model: modelName })
#             });
#             const data = await response.json();
#             document.getElementById('result').innerText = 'Scan result: ' + data.result;
#         }
#
#         async function disarmModel() {
#             const modelName = document.getElementById('model_input').value;
#             const response = await fetch('/disarm_model', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ model: modelName })
#             });
#             const data = await response.json();
#             document.getElementById('result').innerText = 'Disarm result: ' + data.result;
#         }
#
#         async function scanAndDisarmModel() {
#             const modelName = document.getElementById('model_input').value;
#             const response = await fetch('/scan_and_disarm_model', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ model: modelName })
#             });
#             const data = await response.json();
#             document.getElementById('result').innerText = 'Scan and disarm result: ' + data.result;
#         }
#     </script>
# </body>
# </html>
# """
#
#
# @app.get("/", response_class=HTMLResponse)
# def read_root():
#     return html_content
#
# @app.post("/scan_model")
# def scan_model(model_data: Model):
#     res = scanner(model_data.model)
#     return {"result": res}
#
# @app.post("/disarm_model")
# def disarm_model(model_data: Model):
#     res = disarm(model_data.model)
#     return {"result": "The model disarmed!"}
#
# @app.post("/scan_and_disarm_model")
# def scan_and_disarm_model(model_data: Model):
#     res = disarm(model_data.model)
#     return {"result": "The model disarmed!"}

# #################################################################3
# ## version 5 Browe file from files & poor GUI:
#
# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import HTMLResponse
# from scan import scanner, disarm
# import os
#
# app = FastAPI()
#
# # # Directory to save uploaded files
# # UPLOAD_DIRECTORY = "/home/aviya/Desktop/FastAPI"
# #
# # if not os.path.exists(UPLOAD_DIRECTORY):
# #     os.makedirs(UPLOAD_DIRECTORY)
#
# # HTML for the frontend
# html_content = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Model Scanner</title>
# </head>
# <body>
#     <h1>CDR - Model Scanner</h1>
#     <input type="file" id="model_file" accept=".pkl, .pickle, .hdf5, .h5, .dill">
#     <button onclick="scanModel()">Scan Model</button>
#     <button onclick="disarmModel()">Disarm Model</button>
#     <button onclick="scanAndDisarmModel()">Scan and Disarm Model</button>
#     <p id="result"></p>
#
#     <script>
#         async function scanModel() {
#             const file = document.getElementById('model_file').files[0];
#             const formData = new FormData();
#             formData.append('file', file);
#
#             const response = await fetch('/scan_model', {
#                 method: 'POST',
#                 body: formData
#             });
#             const data = await response.json();
#
#              // Convert the JSON object to a string and display it with formatting
#             document.getElementById('result').innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
#
#         }
#
#         async function disarmModel() {
#             const file = document.getElementById('model_file').files[0];
#             const formData = new FormData();
#             formData.append('file', file);
#
#             const response = await fetch('/disarm_model', {
#                 method: 'POST',
#                 body: formData
#             });
#             const data = await response.json();
#             document.getElementById('result').innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
#         }
#
#         async function scanAndDisarmModel() {
#             const file = document.getElementById('model_file').files[0];
#             const formData = new FormData();
#             formData.append('file', file);
#
#             const response = await fetch('/scan_and_disarm_model', {
#                 method: 'POST',
#                 body: formData
#             });
#             const data = await response.json();
#             document.getElementById('result').innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
#         }
#     </script>
# </body>
# </html>
# """
#
# @app.get("/", response_class=HTMLResponse)
# def read_root():
#     return html_content
#
# @app.post("/scan_model")
# async def scan_model(file: UploadFile = File(...)):
#     file_path = file.filename
#     res = scanner(file_path)  # Pass file path instead of data
#     return {"Scan result": res}
#     # return res
#
# @app.post("/disarm_model")
# async def disarm_model(file: UploadFile = File(...)):
#     file_path = file.filename
#     res = disarm(file_path)  # Pass file path instead of data
#     return {"Scan and disarm result": f"Scan: {res}, The file disarm successfuly ! (⌐■_■) "}
#
#
# @app.post("/scan_and_disarm_model")
# async def scan_and_disarm_model(file: UploadFile = File(...)):
#     file_path = file.filename
#     disarm_res = disarm(file_path)
#     return {"Scan and disarm result": f"Scan: {disarm_res}, Disarm: The model disarmed!"}


#################################################################3
## version 6 Browse file from files & good GUI:

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from scan import scanner, disarm
import os

app = FastAPI()

# HTML for the frontend
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Model Scanner</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 20px;
            background-color: #f4f4f9;
            color: #333;
        }
        h1 {
            color: #5a5a5a;
        }
        input[type="file"] {
            margin: 10px 0;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 10px 5px;
            cursor: pointer;
            border-radius: 5px;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        pre {
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        #result {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>CDR - Model Scanner</h1>
    <input type="file" id="model_file" accept=".pkl, .pickle, .hdf5, .h5, .dill">
    <button onclick="scanModel()">Scan Model</button>
    <button onclick="disarmModel()">Disarm Model</button>
    <button onclick="scanAndDisarmModel()">Scan and Disarm Model</button>
    <p id="result"></p>

    <script>
        async function scanModel() {
            const file = document.getElementById('model_file').files[0];
            const formData = new FormData();
            formData.append('file', file);

            const response = await fetch('/scan_model', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();

             // Convert the JSON object to a string and display it with formatting
            document.getElementById('result').innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';

        }

        async function disarmModel() {
            const file = document.getElementById('model_file').files[0];
            const formData = new FormData();
            formData.append('file', file);

            const response = await fetch('/disarm_model', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            document.getElementById('result').innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
        }

        async function scanAndDisarmModel() {
            const file = document.getElementById('model_file').files[0];
            const formData = new FormData();
            formData.append('file', file);

            const response = await fetch('/scan_and_disarm_model', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            document.getElementById('result').innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
        }
    </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def read_root():
    return html_content


@app.post("/scan_model")
async def scan_model(file: UploadFile = File(...)):
    file_path = file.filename
    res = scanner(file_path)  # Pass file path instead of data
    return {"Scan result": res}
    # return res


@app.post("/disarm_model")
async def disarm_model(file: UploadFile = File(...)):
    file_path = file.filename
    res = disarm(file_path)  # Pass file path instead of data
    return {"Scan and disarm result": f"Scan: {res}, The file disarm successfuly ! (⌐■_■) "}

    
@app.post("/scan_and_disarm_model")
async def scan_and_disarm_model(file: UploadFile = File(...)):
    file_path = file.filename
    disarm_res = disarm(file_path)
    return {"Scan and disarm result": f"Scan: {disarm_res}, Disarm: The model disarmed!"}
