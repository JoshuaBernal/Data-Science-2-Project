from flask import Flask, request, jsonify, session
from flask_cors import CORS
from python_code import LogisticRegPre, KNNPre, SVMPre, LogisticRegAbove35, KNNAbove35, SVMAbove35, LogisticRegBelow35, KNNBelow35, SVMBelow35


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

    pre_logreg_predictions, pre_logreg_probability, pre_logreg_accuracy, pre_logreg_conf_matrix, pre_logreg_precision, pre_logreg_f1, pre_logreg_recall, pre_logreg_mse, pre_logreg_rmse = LogisticRegPre(age, gender, trestbps, has_history, cp)

    pre_knn_predictions, pre_knn_probability, pre_knn_accuracy, pre_knn_conf_matrix, pre_knn_precision, pre_knn_f1, pre_knn_recall, pre_knn_mse, pre_knn_rmse = KNNPre(age, gender, trestbps, has_history, cp)

    pre_svm_predictions, pre_svm_probability, pre_svm_accuracy, pre_svm_conf_matrix, pre_svm_precision, pre_svm_f1, pre_svm_recall, pre_svm_mse, pre_svm_rmse = SVMPre(age, gender, trestbps, has_history, cp)

    return jsonify({
        'pre_logreg_predictions': pre_logreg_predictions.tolist(), 
        'pre_logreg_probability': pre_logreg_probability.tolist(),
        'pre_logreg_accuracy': pre_logreg_accuracy.tolist(),
        'pre_logreg_conf_matrix': pre_logreg_conf_matrix.tolist(),
        'pre_logreg_precision': pre_logreg_precision.tolist(),
        'pre_logreg_f1': pre_logreg_f1.tolist(), 
        'pre_logreg_recall': pre_logreg_recall.tolist(), 
        'pre_logreg_mse': pre_logreg_mse.tolist(), 
        'pre_logreg_rmse': pre_logreg_rmse.tolist(),
        'pre_knn_predictions': pre_knn_predictions.tolist(), 
        'pre_knn_probability': pre_knn_probability.tolist(),
        'pre_knn_accuracy': pre_knn_accuracy.tolist(),
        'pre_knn_conf_matrix': pre_knn_conf_matrix.tolist(),
        'pre_knn_precision': pre_knn_precision.tolist(),
        'pre_knn_f1': pre_knn_f1.tolist(), 
        'pre_knn_recall': pre_knn_recall.tolist(), 
        'pre_knn_mse': pre_knn_mse.tolist(), 
        'pre_knn_rmse': pre_knn_rmse.tolist(),
        'pre_svm_predictions': pre_svm_predictions.tolist(), 
        'pre_svm_probability': pre_svm_probability.tolist(),
        'pre_svm_accuracy': pre_svm_accuracy.tolist(),
        'pre_svm_conf_matrix': pre_svm_conf_matrix.tolist(),
        'pre_svm_precision': pre_svm_precision.tolist(),
        'pre_svm_f1': pre_svm_f1.tolist(), 
        'pre_svm_recall': pre_svm_recall.tolist(), 
        'pre_svm_mse': pre_svm_mse.tolist(), 
        'pre_svm_rmse': pre_svm_rmse.tolist()
    })


@app.route("/Above35", methods=["POST"])
def above35_predict():
    data = request.get_json(force=True)
    age = data["age"]
    gender = data["gender"]
    trestbps = data["trestbps"]
    has_history = data["has_history"]
    cp = data["cp"]
    chol = data["chol"]
    fbs = data["fbs"]
    restecg = data["restecg"]
    thalach = data["thalach"]
    thal = data["thal"]

    above_logreg_predictions, above_logreg_probability, above_logreg_accuracy, above_logreg_conf_matrix, above_logreg_precision, above_logreg_f1, above_logreg_recall, above_logreg_mse, above_logreg_rmse = LogisticRegAbove35(age, gender, trestbps, has_history, cp, chol, fbs, restecg, thalach, thal)

    above_knn_predictions, above_knn_probability, above_knn_accuracy, above_knn_conf_matrix, above_knn_precision, above_knn_f1, above_knn_recall, above_knn_mse, above_knn_rmse = KNNAbove35(age, gender, trestbps, has_history, cp, chol, fbs, restecg, thalach, thal)

    above_svm_predictions, above_svm_probability, above_svm_accuracy, above_svm_conf_matrix, above_svm_precision, above_svm_f1, above_svm_recall, above_svm_mse, above_svm_rmse = SVMAbove35(age, gender, trestbps, has_history, cp, chol, fbs, restecg, thalach, thal)

    return jsonify({
        'above_logreg_predictions': above_logreg_predictions.tolist(), 
        'above_logreg_probability': above_logreg_probability.tolist(),
        'above_logreg_accuracy': above_logreg_accuracy.tolist(),
        'above_logreg_conf_matrix': above_logreg_conf_matrix.tolist(),
        'above_logreg_precision': above_logreg_precision.tolist(),
        'above_logreg_f1': above_logreg_f1.tolist(), 
        'above_logreg_recall': above_logreg_recall.tolist(), 
        'above_logreg_mse': above_logreg_mse.tolist(), 
        'above_logreg_rmse': above_logreg_rmse.tolist(),
        'above_knn_predictions': above_knn_predictions.tolist(), 
        'above_knn_probability': above_knn_probability.tolist(),
        'above_knn_accuracy': above_knn_accuracy.tolist(),
        'above_knn_conf_matrix': above_knn_conf_matrix.tolist(),
        'above_knn_precision': above_knn_precision.tolist(),
        'above_knn_f1': above_knn_f1.tolist(), 
        'above_knn_recall': above_knn_recall.tolist(), 
        'above_knn_mse': above_knn_mse.tolist(), 
        'above_knn_rmse': above_knn_rmse.tolist(),
        'above_svm_predictions': above_svm_predictions.tolist(), 
        'above_svm_probability': above_svm_probability.tolist(),
        'above_svm_accuracy': above_svm_accuracy.tolist(),
        'above_svm_conf_matrix': above_svm_conf_matrix.tolist(),
        'above_svm_precision': above_svm_precision.tolist(),
        'above_svm_f1': above_svm_f1.tolist(), 
        'above_svm_recall': above_svm_recall.tolist(), 
        'above_svm_mse': above_svm_mse.tolist(), 
        'above_svm_rmse': above_svm_rmse.tolist()
    })


@app.route("/Below35", methods=["POST"])
def below35_predict():
    data = request.get_json(force=True)
    age = data["age"]
    gender = data["gender"]
    trestbps = data["trestbps"]
    has_history = data["has_history"]
    cp = data["cp"]
    chol = data["chol"]
    fbs = data["fbs"]
    restecg = data["restecg"]

    below_logreg_predictions, below_logreg_probability, below_logreg_accuracy, below_logreg_conf_matrix, below_logreg_precision, below_logreg_f1, below_logreg_recall, below_logreg_mse, below_logreg_rmse = LogisticRegBelow35(age, gender, trestbps, has_history, cp, chol, fbs, restecg)

    below_knn_predictions, below_knn_probability, below_knn_accuracy, below_knn_conf_matrix, below_knn_precision, below_knn_f1, below_knn_recall, below_knn_mse, below_knn_rmse = KNNBelow35(age, gender, trestbps, has_history, cp, chol, fbs, restecg)

    below_svm_predictions, below_svm_probability, below_svm_accuracy, below_svm_conf_matrix, below_svm_precision, below_svm_f1, below_svm_recall, below_svm_mse, below_svm_rmse = SVMBelow35(age, gender, trestbps, has_history, cp, chol, fbs, restecg)

    return jsonify({
        'below_logreg_predictions': below_logreg_predictions.tolist(), 
        'below_logreg_probability': below_logreg_probability.tolist(),
        'below_logreg_accuracy': below_logreg_accuracy.tolist(),
        'below_logreg_conf_matrix': below_logreg_conf_matrix.tolist(),
        'below_logreg_precision': below_logreg_precision.tolist(),
        'below_logreg_f1': below_logreg_f1.tolist(), 
        'below_logreg_recall': below_logreg_recall.tolist(), 
        'below_logreg_mse': below_logreg_mse.tolist(), 
        'below_logreg_rmse': below_logreg_rmse.tolist(),
        'below_knn_predictions': below_knn_predictions.tolist(), 
        'below_knn_probability': below_knn_probability.tolist(),
        'below_knn_accuracy': below_knn_accuracy.tolist(),
        'below_knn_conf_matrix': below_knn_conf_matrix.tolist(),
        'below_knn_precision': below_knn_precision.tolist(),
        'below_knn_f1': below_knn_f1.tolist(), 
        'below_knn_recall': below_knn_recall.tolist(), 
        'below_knn_mse': below_knn_mse.tolist(), 
        'below_knn_rmse': below_knn_rmse.tolist(),
        'below_svm_predictions': below_svm_predictions.tolist(), 
        'below_svm_probability': below_svm_probability.tolist(),
        'below_svm_accuracy': below_svm_accuracy.tolist(),
        'below_svm_conf_matrix': below_svm_conf_matrix.tolist(),
        'below_svm_precision': below_svm_precision.tolist(),
        'below_svm_f1': below_svm_f1.tolist(), 
        'below_svm_recall': below_svm_recall.tolist(), 
        'below_svm_mse': below_svm_mse.tolist(), 
        'below_svm_rmse': below_svm_rmse.tolist()
    })


if __name__ == "__main__":
    app.run(debug=True)
