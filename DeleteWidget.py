import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="DeleteWidget/{id:int}", methods=["DELETE"])

def DeleteWidget(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    method = req.method
    if method == 'DELETE':
        # Handle DELETE request
        item_id = req.route_params.get('id')
        return func.HttpResponse(f"Item ID: {item_id} has been deleted.", status_code=200)
    else:
        return func.HttpResponse("This HTTP method is not supported.", status_code=405)