import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="widgets/{id:int?}", methods=["GET"])

def GetWidgetInfo(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    method = req.method
    if method == 'GET':
        # Handle GET request
        item_id = req.route_params.get('id')
        return func.HttpResponse(f"Returning you information on item ID: {item_id}", status_code=200)
    else:
        return func.HttpResponse("This HTTP method is not supported.", status_code=405)
