def BodyJson(req, res):
    if(req.header("Content-Type") == 'application/json' and req.body("__raw__") == None):
        return True
    return Exception('Invalid body content. BodyParser error.')

def ParamValidation(req, res):
    if(req.params("__raw__") == None):
        return True
    return Exception('Invalid url params. ParamValidation error.')