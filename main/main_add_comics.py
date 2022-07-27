from multiprocessing.reduction import register
from cProfile import run
from workflow.workflow_add_comic import run_workflow_add_comic
from flask import Flask, session

def add_comic(request):
    id_comic = request.args.get('id_comic')
    if (not(id_comic)):
        return {"code:":"Error, agrega un id de comic valido", "status":400}
    else:
        return run_workflow_add_comic(request)
    