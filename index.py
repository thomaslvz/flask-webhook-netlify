from flask import Flask, request, Response, abort
from token_auth import signed



app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    #Parse event payload as string
    body_str = request.get_data(as_text=True) #see Flask's request object
    
    #Verify JWT
    if not signed(request, body_str):
        print("Error: JSON Web Token verification has failed")
        abort(403)
    
    #Execute webhook
    else:
        body_json = request.json
        print(body_json)
        return Response(status=200)