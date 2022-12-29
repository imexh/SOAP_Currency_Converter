from flask import Flask, render_template, request
import zeep


templatesLocation = '/Users/imesh/Google Drive/SLTC/Semester 6/Software Architecture/Assignment/Assignment 2/AA1922_SA_Assignment2/CurrencyConverterWeb Client/website/Templates'
app = Flask('CurrencyConverter', template_folder= templatesLocation)

wsdl = 'http://localhost:8888/CurrencyConversionWebServiceAA1922?wsdl'
client = zeep.Client(wsdl=wsdl)
currencyList = client.service.getCurrencyList()

answer = ''

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", currencyList = currencyList, len = len(currencyList))

@app.route("/", methods=['POST'])
def currencyConvert():
    currency1 = request.form['currencyName1']
    currency2 = request.form['currencyName2']
    value1 = request.form['value1']
    answer = value1 + " " + currency1 + " => " + str(round(client.service.convert(value1, currency1, currency2),2)) + " " + currency2

    return render_template("index.html", currencyList = currencyList, len = len(currencyList), answer = answer)


if __name__ == "__main__":
    app.run(debug=True)