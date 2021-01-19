from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
   return "Hello World!"

@server.route("/<project_id>/documents/<doc_id>", methods=['GET', 'PUT'])
def docx_upload(project_id, doc_id):
   # 1. save file to s3, 
   # 2. save meta to mysql, link to file
   pass

@server.route("/<project_id>/documents", methods=['GET'])
def list_docs_in_project(project_id):
   pass

if __name__ == "__main__":
   server.run(host='0.0.0.0')