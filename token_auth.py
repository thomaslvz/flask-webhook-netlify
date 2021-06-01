#token_auth.py

import jwt, hashlib
from os import environ

def signed(request, body):
    """
    Returns True if JWT is ok. 'body' must be a str.
    Used to check if Netlify POST request is signed.
    Decode JWT token and check if it matches with body hash.
    See https://docs.netlify.com/site-deploys/notifications/
    """
    try:        
        signature = request.headers["X-Webhook-Signature"]
        secret= environ.get('NETLIFY_FORM_HOOK_SECRET')
        token_decoded = jwt.decode(signature,
                                   secret,
                                   issuer=environ.get('NETLIFY_FORM_HOOK_ISSUER'),
                                   algorithms=environ.get('NETLIFY_FORM_HOOK_ALG'))
        return token_decoded['sha256'] == hashlib.sha256(body.encode('utf-8')).hexdigest()
    except:
        return False
