from helpers.TerminalColors import tcolors

def EnableCors(req, res):
    res.cors('*')
    return True

def BodyJson(req, res):
    if(req.body("__raw__") == None):
        return True
    return Exception('Invalid body content. BodyParser error.')

def ParamValidation(req, res):
    if(req.params("__raw__") == None):
        return True
    return Exception('Invalid url params. ParamValidation error.')

def RequestLog(req, res):
    if(req.method == None or req.path == None or req.http_version == None):
        print(tcolors.ERROR + '[CORRUPTED HEADER]'+ tcolors.ENDC + ' -> ' +
                tcolors.BOLD + '{}:{}'.format(req.addr, req.port) + tcolors.ENDC)
    else:
        print(tcolors.method_color(req.method) + '[' + req.method + ']'+ tcolors.ENDC + ' ' +
                tcolors.BOLD + req.path + tcolors.ENDC + ' [FROM] ' + tcolors.BOLD + '{}:{}'.format(req.addr, req.port) + tcolors.ENDC)
    return True
