from django.http import HttpResponse

# Create your views here.
import logging
logger = logging.getLogger("django")

def get_tasks(request):
    """
    func:
        Task management page search
    """
    logger.info("in get tasks...")
    return HttpResponse("OK!")