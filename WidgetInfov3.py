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


@app.route(route="widgets", methods=["POST"])
def CreateWidget(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    method = req.method
    if method == 'POST':
        # Handle POST request
        try:
            req_body = req.get_json()
            widget_name = req_body.get('name')
            # Add logic to create the widget
            return func.HttpResponse(f"Widget '{widget_name}' created successfully.", status_code=201)
        except ValueError:
            return func.HttpResponse("Invalid input.", status_code=400)
    else:
        return func.HttpResponse("This HTTP method is not supported.", status_code=405)