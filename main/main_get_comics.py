from multiprocessing.reduction import register
from cProfile import run
from workflow.workflow_get_comic import run_workflow_get_comic
from flask import Flask, session

def get_comic(request):
    fecha = request.args.get('fecha')
    alfabetico = request.args.get('alfabetico')
    if ( fecha and alfabetico ):
        return {"code:":400, "message":"Error, sólo puedes agregar un filtro"}
    else:
        return run_workflow_get_comic(request)