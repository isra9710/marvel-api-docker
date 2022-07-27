from services.get_comics import get_comics

def run_workflow_get_comic(request):
    fecha = request.args.get('fecha')
    alfabetico = request.args.get('alfabetico')
    return get_comics(fecha = fecha, alfabetico = alfabetico)