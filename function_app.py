import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="stephenfunction")
def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', 'World')
    lastname = req.params.get('lastname', 'no last name provided')
    nameCapital = name.upper()
    lastnameCapital = lastname.upper()
    
    response_message = f"Hello {nameCapital} {lastnameCapital}!"
    return func.HttpResponse(response_message)