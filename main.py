import requests
import json
import tkinter as tk
def apiCall(country):
    url = f"https://covid-19.dataflowkit.com/v1/{country}"
    response = requests.get(url)
    print(response)
    return response
def btnSubmitClicked():
    cty = txt_country.get()
    result = apiCall(cty)
    showDeatails(result)
def showDeatails(result):
    active = result.json()["Active Cases_text"]
    con = result.json()['Country_text']
    last_update = result.json()['Last Update']
    new_cases = result.json()['New Cases_text']
    new_deaths = result.json()['New Deaths_text']
    total_cases = result.json()['Total Cases_text']
    total_deaths = result.json()['Total Deaths_text']
    total_recovered = result.json()['Total Recovered_text']
    if(con.lower() == 'world'):
        label_result.configure(text = "Please Enter a Valid country name...")
    else:
        label_result.configure(text = "Country: "+con+'\n'+
                               "Active Cases: "+active+'\n'+
                               "New Cases: "+new_cases+'\n'+
                               "New Deaths: "+new_deaths+'\n'+
                               "Total Cases: "+total_cases+'\n'+
                               "Total Deaths: "+total_deaths+'\n'+
                               "Total Recovered: "+total_recovered+'\n\n\n'+
                               "Last Updated: "+last_update)



window = tk.Tk()
window.title("COVID-19 TRACKER")
window.geometry('350x350')
label_country = tk.Label(window, text = "Country: ")
label_country.grid(row=0,column=2)
txt_country = tk.Entry(window,width = 10)
txt_country.grid(column=3,row = 0)
btn_submit = tk.Button(window, text="Submit",command = btnSubmitClicked)
btn_submit.grid(column = 3, row =3)
label_result = tk.Label(window,text = '')
label_result.grid(column=3,row=5)
window.mainloop()

