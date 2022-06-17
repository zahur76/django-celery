from django.shortcuts import render
from .tasks import debug_task

# Create your views here.
def index(request):
    """A view to return the home page"""

    debug_task.delay()

    context = {
    }

    return render(request, "home/index.html", context)