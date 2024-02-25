from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)

def index(request):
    logger.info('Главная')
    html = """
    <html>
    <head>
    <title>Главная страница</title>
    </head>
    <body>
    <h1>Привет!</h1>
    <p>Главная страница.</p>
    </body>
    </html>
    """
    return HttpResponse(html)

def about(request):
    logger.info('О себе')
    html = """
    <html>
    <head>
    <title>О себе</title>
    </head>
    <body>
    <h1>О себе</h1>
    <p>Что-то интересное обо мне.</p>
    </body>
    </html>
    """
    return HttpResponse(html)