# flask_6_api_management

## Setting up and testing the Flask Endpoint
1. Install the Azure Functions Core Tools using [this link](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=macos%2Cbash%2Cazure-cli&pivots=python-mode-decorators) .
2. Go the VS Code and install the following extensions:
+ `Azure Functions`
+ `Azure Account`
+ `Azure Storage`
3. Click on the `Azure` icon on the left side of the VS Code and under `Resources` sign in to your Azure account.
4. Go to `Workspaces` and click on `Create Function` under the `Azure Functions` icon. Choose a folder. Then, choose the following options:
+ `Python`
+ The version of Python interpreter you have
+ Provide a name for the function
+ `HTTP trigger`
+ `Anonymous`
5. Once the function is created, go to the `function_app.py` file and replace the code your code.
6. Go back to the `Azure` icon, under `Resources`, click on `Function App` and `Create New Function Appin Azure`. Choose a name for the function app and choose the following options:
+ `Python`
+ Your resource group
+ `East US`
+ `Consumption`
+ Your storage account
+ Create new Application Insights or skip
7. Once the function app is created, under `Workspace`, click on `Deploy to Function App...` and choose the function app you just created.
8. Login to [Azure portal](https://portal.azure.com/#home) . and under the function app, click on `Functions` and then click on the function you just created. Click on the URL.
9. You can test the endpoint using by entering `/api/` after the URL and then followed by the name of the function and the parameters. For example, the URL for my function is `https://stephen-app.azurewebsites.net/api/stephenfunction?name=stephen&lastname=hu`.

## API documentation
1. Create a new file `app.py` and modify the code using the following format:
``` 
from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: World
    responses:
      200:
        description: A greeting message
    """
    name = request.args.get('name', 'World')
    name = name.upper()
    return f'Hello {name}!'

@app.route('/hello', methods=['POST'])
def hello_post():
    """
    This endpoint returns a greeting message based on the name provided in the JSON body.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          required:
            - name
          properties:
            name:
              type: string
              default: World
    responses:
      200:
        description: A greeting message
      400:
        description: Invalid JSON
    """
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    name = data.get('name', 'World')
    name = name.upper()
    return jsonify({'message': f'Hello {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
```
2. Run the file locally and go to `http://localhost:5000/apidocs/` to see the documentation.


