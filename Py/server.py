from flask import Flask, request, jsonify, session
from flask_cors import CORS
from python_code import LogisticRegPre, KNNPre, SVMPre, LogisticRegAbove35, KNNAbove35, SVMAbove35


app = Flask(__name__)
app.secret_key = "balls"
CORS(app, origins="*")


@app.route("/Preliminary", methods=["POST"])
def preliminary_predict():
    data = request.get_json(force=True)
    age = data["age"]
    gender = data["gender"]
    trestbps = data["trestbps"]
    has_history = data["has_history"]
    cp = data["cp"]

    session['preliminary_inputs'] = {
        'age': age,
        'gender': gender,
        'trestbps': trestbps,
        'has_history': has_history,
        'cp': cp
    }

    logreg_predictions, logreg_probability, logreg_accuracy, logreg_conf_matrix, logreg_precision, logreg_f1, logreg_recall, logreg_mse, logreg_rmse = LogisticRegPre(age, gender, trestbps, has_history, cp)

    knn_predictions, knn_probability, knn_accuracy, knn_conf_matrix, knn_precision, knn_f1, knn_recall, knn_mse, knn_rmse = KNNPre(age, gender, trestbps, has_history, cp)

    svm_predictions, svm_probability, svm_accuracy, svm_conf_matrix, svm_precision, svm_f1, svm_recall, svm_mse, svm_rmse = SVMPre(age, gender, trestbps, has_history, cp)

    return jsonify({
        'logreg_predictions': logreg_predictions.tolist(), 
        'logreg_probability': logreg_probability.tolist(),
        'logreg_accuracy': logreg_accuracy.tolist(),
        'logreg_conf_matrix': logreg_conf_matrix.tolist(),
        'logreg_precision': logreg_precision.tolist(),
        'logreg_f1': logreg_f1.tolist(), 
        'logreg_recall': logreg_recall.tolist(), 
        'logreg_mse': logreg_mse.tolist(), 
        'logreg_rmse': logreg_rmse.tolist(),
        'knn_predictions': knn_predictions.tolist(), 
        'knn_probability': knn_probability.tolist(),
        'knn_accuracy': knn_accuracy.tolist(),
        'knn_conf_matrix': knn_conf_matrix.tolist(),
        'knn_precision': knn_precision.tolist(),
        'knn_f1': knn_f1.tolist(), 
        'knn_recall': knn_recall.tolist(), 
        'knn_mse': knn_mse.tolist(), 
        'knn_rmse': knn_rmse.tolist(),
        'svm_predictions': svm_predictions.tolist(), 
        'svm_probability': svm_probability.tolist(),
        'svm_accuracy': svm_accuracy.tolist(),
        'svm_conf_matrix': svm_conf_matrix.tolist(),
        'svm_precision': svm_precision.tolist(),
        'svm_f1': svm_f1.tolist(), 
        'svm_recall': svm_recall.tolist(), 
        'svm_mse': svm_mse.tolist(), 
        'svm_rmse': svm_rmse.tolist()
    })

@app.route("/Above35", methods=["POST"])
def above35_predict():
    data = request.get_json(force=True)
    chol = data["chol"]
    fbs = data["fbs"]
    restecg = data["restecg"]
    thalach = data["thalach"]
    thal = data["thal"]

    preliminary_inputs = session.get('preliminary_inputs', {})
    
    # Check if preliminary inputs are available
    if not preliminary_inputs:
        return jsonify({'error': 'Preliminary inputs not found. Please complete the first step.'})

    # Combine preliminary and additional inputs for Above35 prediction
    combined_inputs = {**preliminary_inputs, 'chol': chol, 'fbs': fbs, 'restecg': restecg, 'thalach': thalach, 'thal': thal}



    logreg_predictions, logreg_probability, logreg_accuracy, logreg_conf_matrix, logreg_precision, logreg_f1, logreg_recall, logreg_mse, logreg_rmse = LogisticRegAbove35(combined_inputs)

    knn_predictions, knn_probability, knn_accuracy, knn_conf_matrix, knn_precision, knn_f1, knn_recall, knn_mse, knn_rmse = KNNAbove35(combined_inputs)

    svm_predictions, svm_probability, svm_accuracy, svm_conf_matrix, svm_precision, svm_f1, svm_recall, svm_mse, svm_rmse = SVMAbove35(combined_inputs)

    return jsonify({
        'logreg_predictions': logreg_predictions.tolist(), 
        'logreg_probability': logreg_probability.tolist(),
        'logreg_accuracy': logreg_accuracy.tolist(),
        'logreg_conf_matrix': logreg_conf_matrix.tolist(),
        'logreg_precision': logreg_precision.tolist(),
        'logreg_f1': logreg_f1.tolist(), 
        'logreg_recall': logreg_recall.tolist(), 
        'logreg_mse': logreg_mse.tolist(), 
        'logreg_rmse': logreg_rmse.tolist(),
        'knn_predictions': knn_predictions.tolist(), 
        'knn_probability': knn_probability.tolist(),
        'knn_accuracy': knn_accuracy.tolist(),
        'knn_conf_matrix': knn_conf_matrix.tolist(),
        'knn_precision': knn_precision.tolist(),
        'knn_f1': knn_f1.tolist(), 
        'knn_recall': knn_recall.tolist(), 
        'knn_mse': knn_mse.tolist(), 
        'knn_rmse': knn_rmse.tolist(),
        'svm_predictions': svm_predictions.tolist(), 
        'svm_probability': svm_probability.tolist(),
        'svm_accuracy': svm_accuracy.tolist(),
        'svm_conf_matrix': svm_conf_matrix.tolist(),
        'svm_precision': svm_precision.tolist(),
        'svm_f1': svm_f1.tolist(), 
        'svm_recall': svm_recall.tolist(), 
        'svm_mse': svm_mse.tolist(), 
        'svm_rmse': svm_rmse.tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)
