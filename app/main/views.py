# coding:utf-8

from . import main
from flask import render_template, request, redirect, url_for, session
from ..models import days


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print request.form['city']
        session['city'] = request.form['city']
        return redirect(url_for('.index'))
    return render_template('index.html')


@main.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        session['city'] = request.form['city']
    city = session['city']
    wea_list = []
    status = days.weather(city, wea_list)
    if status:
        session['msg'] = ''
        return render_template('result.html', wea_list=wea_list, city=city)
    return redirect(url_for('.fail'))

@main.route('/fail')
def fail():
    return render_template('fail.html')
