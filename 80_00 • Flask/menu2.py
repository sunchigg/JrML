# -*- coding: utf-8 -*-
"""
"""
from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)
app.config["SECRET_KEY"] = "d3y23udh2noidmp2o"
csv_file = "static/drink.csv"
df = pd.read_csv(csv_file)


@app.route('/menu2', methods=['POST', 'GET'])
def menu2():
    df1 = df['drink1']
    DRINK = df1.unique()
    if 'drink' in request.form:
        eid = request.form.get('drink')
        step2 = df[df['drink1'] == eid][['Drink', 'Price']]
        return render_template('menu2.html', tables=[step2.to_html(classes='data', index=False)], titles=eid, DRINK=DRINK)
    return render_template('menu2.html', DRINK=DRINK)


if __name__ == '__main__':
    app.run(debug=True)
