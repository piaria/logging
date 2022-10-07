from django.http import HttpResponse

# Create your views here.
import logging


def get_tasks(request):
    """
    func:
        Task management page search
    """
    logging.info("We've got the tasks")
    return HttpResponse("OK!")
