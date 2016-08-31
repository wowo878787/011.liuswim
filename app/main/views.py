#coding:utf-8

from . import main
from flask import render_template
from ..models import days


@main.route('/')
def index():
    # days.weather('北京')
    return render_template('index.html')