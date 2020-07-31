from flask import Flask, render_template
from markdown2 import markdown

from functions.data_processors import per_date, per_contact, per_sector, errors
from functions.graph_builder import create_plot


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/output_1/')
def first_output_home():
    return render_template('first.html')


@app.route('/output_1/contact/')
def first_output_contact():
    contacts = per_contact()
    names =[]
    values = []
    for value, name in contacts:
        names.append(name)
        values.append(value)
    contact_bar = create_plot(names, values, "Valor total vendido por contato")

    return render_template('specific.html', contacts=contact_bar)


@app.route('/output_1/month/')
def first_output_month():
    date = per_date()
    months = []
    values = []
    for value, month in date:
        months.append(month)
        values.append(value)
    month_bar = create_plot(months, values, 'Valor total vendido por mês')
    return render_template('specific.html', contacts=month_bar)


@app.route('/output_2/')
def second_output():
    sectors = per_sector()
    previous_month = ['']
    return render_template('second.html', sectors=sectors, previous_month=previous_month)


@app.route('/readme/')
def show_readme():
    with open('templates/custom.md', 'r', encoding='utf-8') as f:
        content = f.read()
        content_converted = markdown(content)
    return render_template('readme.html', content=content_converted)


@app.route('/errors/')
def get_errors():
    error = errors()
    return render_template('error.html', erros=error)


if __name__ == '__main__':
    app.run(debug=True)

