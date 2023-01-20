from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_data_columns_names', methods=['GET'])
def get_data_columns_names():
    response = jsonify({
        'Columns': util.get_data_columns()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict', methods=['GET', 'POST'])
def predict_home_KTAS():
    Saturation =  float(request.form['Saturation'])
    Sexm = int(request.form['Sexm'])
    Injuryy = int(request.form['Injuryy'])
    Mental = request.form['Mental']
    Painy = int(request.form['Painy'])
    KTAS_RN = request.form['KTAS_RN']
    Error_group = request.form['Error_group']
    New_Age = request.form['New_Age']
    New_SBP = request.form['New_SBP']
    New_DBP = request.form['New_DBP']
    New_HR = request.form['New_HR']
    New_RR = request.form['New_RR']
    New_BT = request.form['New_BT']
    New_NRS_pain = request.form['New_NRS_pain']
    Saturation = round((Saturation - 98)/5,3)
    KTAS_expert  = (util.get_estimated_KTAS(Saturation,Sexm,Injuryy,Mental,Painy,KTAS_RN,Error_group,New_Age,New_SBP,New_DBP,New_HR,New_RR,New_BT,New_NRS_pain))
    estimated_Disposition = util.get_estimated_Disposition(Saturation,Sexm,Injuryy,Mental,Painy,KTAS_RN,KTAS_expert,Error_group,New_Age,New_SBP,New_DBP,New_HR,New_RR,New_BT,New_NRS_pain)
    
    response = jsonify({
        'estimated_KTAS': KTAS_expert ,
        'estimated_Disposition': estimated_Disposition,
        'Saturation':Saturation
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()