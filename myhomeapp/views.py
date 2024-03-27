import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def main_page(request):
    logger.info("Main page called")
    return HttpResponse("<h1>Лучший магазин игрушек </h1>")


def about(request):
    logger.info("About page called")
    return HttpResponse("<ol>"
                        "   <li><b>Адрес:</b> Лапландия</li> "
                        "   <li><b>Тел:</b> +9999999999</li> "
                        "   <li><b>Почта:</b> ...@...com</li> "
                        "   <li><b>Режим работы:</b> круглые сутки</li>"
                        "</ol>")
