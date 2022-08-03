# Libraries that I need for my API
from flask import Flask, jsonify, make_response,request
import pandas as pd
import numpy as np
import csv
import json
# Initialize the API
app = Flask(__name__) 
#Endpoint 1 Just for testing 
@app.route('/')
def index():
    return jsonify({'Nothing':"Nothing"})


#Endpoint 2 Just for testing with POST method
@app.route('/data/suma', methods = ['POST']) # POST method
def suma():
    json_request = request.get_json() # This method NEEDS to have request for geting the JSON from the POST
    print(json_request)
    json_request["el"] = int(json_request["el"] + 1)
    print(json_request)
    return jsonify(json_request)


#Endpoint3 the funcional API for give a JSON to the frontend TEAM
@app.route('/data_api/graph', methods=['POST'])
def respuesta():
    json_request = request.get_json()
    regiones = json_request["regiones"]
    administracion=json_request["administracion"]
    finalidad= json_request["finalidad"]
    df=pd.read_csv("/Users/pablosanturioalonso/Desktop/Data API/src/concesiones_completo1.tsv",sep="\t")
    if len(regiones)!= 0:
        df=df[df["region_impacto"].isin(regiones)]
        df=df.iloc[0:,[-7,-5]]
        df=df.rename(columns = {'region_impacto':'name', 'importe':'value'})
        df=df.groupby(by="name").sum()
        df=df.reset_index()
        data=[]
        for i in np.arange(len(df)):
            data.append(df.iloc[i].to_dict())
        seriesType={}
        dic1={}
        dic1["name"]="Barplot"
        dic1["titulo"]="Importe gastado seguún regiones de impacto"
        dic1["tipo_uds"]= "Euros"
        dic1["graficos_disponibles"]="Barplot"
        dic1["data"]=data
        seriesType["content"]=[dic1]
        #Regiones=(ANDALUCIA, CASTILLA Y LEON, COMUNIDAD VALENCIANA, GALICIA)
        return jsonify(seriesType)
    if len(administracion)!= 0:
            df=df[df["administracion"].isin(administracion)]
            df=df.iloc[0:,[1,-5]]
            df=df.rename(columns = {'administracion':'name', 'importe':'value'})
            df=df.groupby(by="name").sum()
            df=df.reset_index()
            data=[]
            for i in np.arange(len(df)):
                data.append(df.iloc[i].to_dict())
            seriesType={}
            dic1={}
            dic1["name"]="BubbleChart"
            dic1["titulo"]="Importe gastado seguún administraciones"
            dic1["tipo_uds"]= "Euros"
            dic1["graficos_disponibles"]="BubbleChart"
            dic1["data"]=data
            seriesType["content"]=[dic1]
            return jsonify(seriesType)
            #administracion=["MADRID", "BARCELONA","VIGO","SEVILLA","VALENCIA","A CORUÑA","GIJÓN", "OVIEDO","SANTANDER","SALAMANCA","LEON"]
    if len(finalidad)!= 0:
        df=df[df["finalidad"].isin(finalidad)]
        df=df.iloc[0:,[-6]]
        count=pd.DataFrame(df["finalidad"].value_counts())
        df=pd.DataFrame()
        df["name"]=count.index
        df["value"]=count.values
        data=[]
        for i in np.arange(len(df)):
            data.append(df.iloc[i].to_dict())
        seriesType={}
        dic1={}
        dic1["name"]="Wordcloud"
        dic1["titulo"]="Cantidad de subvenciones según la finalidad"
        dic1["tipo_uds"]= "Frequencia absoluta"
        dic1["graficos_disponibles"]="Wordcloud"
        dic1["data"]=data
        seriesType["content"]=[dic1]
        #finalidad=["CULTURA","FOMENTO DEL EMPLEO","EDUCACIÓN"]
        return jsonify(seriesType)



def not_found(error):
    return "<h1> This url does not exists </h1>", 404 # This error handler executes thanks to the below code (app.register_error_handler(404, not found))


if __name__ == "__main__":
    app.register_error_handler(404, not_found) # This catches the 404 error
    app.run(debug = True, use_reloader = False)# This runs the API if # debug = True not need to reload if any changes are made
