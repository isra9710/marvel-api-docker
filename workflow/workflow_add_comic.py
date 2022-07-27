from services.add_comics import add_comic

def run_workflow_add_comic(request):
    id_comic = request.args.get('id_comic')
    return add_comic(id_comic=id_comic)