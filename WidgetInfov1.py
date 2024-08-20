import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="GetWidgetInfo", methods=["GET", "PUT"])

def GetWidgetInfo(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    method = req.method

    if method == 'GET':
        # Handle GET request
        return func.HttpResponse("This function was triggered by a GET request", status_code=200)
    elif method == 'PUT':
        # Handle PUT request
        return func.HttpResponse("This function was triggered by a PUT request", status_code=200)
    else:
        return func.HttpResponse("This HTTP method is not supported.", status_code=405)
