from cProfile import run
from workflow.workflow_comic import run_workflow_comic
from flask import Flask, session

def search_comic(request):
    comic = request.args.get('comic')
    character = request.args.get('character')
    if (comic and character):
        return {"code:":"Error, sólo buscar un objeto", "status":400}
    elif (not(comic) and not (character)):
        return {"code:":"Error, selecciona un objeto", "status":400}
    else:
        return run_workflow_comic(request)
    