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

    final_logreg_predictions, final_logreg_probability, final_logreg_accuracy, final_logreg_conf_matrix, final_logreg_precision, final_logreg_f1, final_logreg_recall, final_logreg_mse, final_logreg_rmse = LogisticRegAbove35(age, gender, trestbps, has_history, cp, chol, fbs, restecg, thalach, thal)

    final_knn_predictions, final_knn_probability, final_knn_accuracy, final_knn_conf_matrix, final_knn_precision, final_knn_f1, final_knn_recall, final_knn_mse, final_knn_rmse = KNNAbove35(age, gender, trestbps, has_history, cp, chol, fbs, restecg, thalach, thal)

    final_svm_predictions, final_svm_probability, final_svm_accuracy, final_svm_conf_matrix, final_svm_precision, final_svm_f1, final_svm_recall, final_svm_mse, final_svm_rmse = SVMAbove35(age, gender, trestbps, has_history, cp, chol, fbs, restecg, thalach, thal)

    return jsonify({
        'final_logreg_predictions': final_logreg_predictions.tolist(), 
        'final_logreg_probability': final_logreg_probability.tolist(),
        'final_logreg_accuracy': final_logreg_accuracy.tolist(),
        'final_logreg_conf_matrix': final_logreg_conf_matrix.tolist(),
        'final_logreg_precision': final_logreg_precision.tolist(),
        'final_logreg_f1': final_logreg_f1.tolist(), 
        'final_logreg_recall': final_logreg_recall.tolist(), 
        'final_logreg_mse': final_logreg_mse.tolist(), 
        'final_logreg_rmse': final_logreg_rmse.tolist(),
        'final_knn_predictions': final_knn_predictions.tolist(), 
        'final_knn_probability': final_knn_probability.tolist(),
        'final_knn_accuracy': final_knn_accuracy.tolist(),
        'final_knn_conf_matrix': final_knn_conf_matrix.tolist(),
        'final_knn_precision': final_knn_precision.tolist(),
        'final_knn_f1': final_knn_f1.tolist(), 
        'final_knn_recall': final_knn_recall.tolist(), 
        'final_knn_mse': final_knn_mse.tolist(), 
        'final_knn_rmse': final_knn_rmse.tolist(),
        'final_svm_predictions': final_svm_predictions.tolist(), 
        'final_svm_probability': final_svm_probability.tolist(),
        'final_svm_accuracy': final_svm_accuracy.tolist(),
        'final_svm_conf_matrix': final_svm_conf_matrix.tolist(),
        'final_svm_precision': final_svm_precision.tolist(),
        'final_svm_f1': final_svm_f1.tolist(), 
        'final_svm_recall': final_svm_recall.tolist(), 
        'final_svm_mse': final_svm_mse.tolist(), 
        'final_svm_rmse': final_svm_rmse.tolist()
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

    final_logreg_predictions, final_logreg_probability, final_logreg_accuracy, final_logreg_conf_matrix, final_logreg_precision, final_logreg_f1, final_logreg_recall, final_logreg_mse, final_logreg_rmse = LogisticRegBelow35(age, gender, trestbps, has_history, cp, chol, fbs, restecg)

    final_knn_predictions, final_knn_probability, final_knn_accuracy, final_knn_conf_matrix, final_knn_precision, final_knn_f1, final_knn_recall, final_knn_mse, final_knn_rmse = KNNBelow35(age, gender, trestbps, has_history, cp, chol, fbs, restecg)

    final_svm_predictions, final_svm_probability, final_svm_accuracy, final_svm_conf_matrix, final_svm_precision, final_svm_f1, final_svm_recall, final_svm_mse, final_svm_rmse = SVMBelow35(age, gender, trestbps, has_history, cp, chol, fbs, restecg)

    return jsonify({
        'final_logreg_predictions': final_logreg_predictions.tolist(), 
        'final_logreg_probability': final_logreg_probability.tolist(),
        'final_logreg_accuracy': final_logreg_accuracy.tolist(),
        'final_logreg_conf_matrix': final_logreg_conf_matrix.tolist(),
        'final_logreg_precision': final_logreg_precision.tolist(),
        'final_logreg_f1': final_logreg_f1.tolist(), 
        'final_logreg_recall': final_logreg_recall.tolist(), 
        'final_logreg_mse': final_logreg_mse.tolist(), 
        'final_logreg_rmse': final_logreg_rmse.tolist(),
        'final_knn_predictions': final_knn_predictions.tolist(), 
        'final_knn_probability': final_knn_probability.tolist(),
        'final_knn_accuracy': final_knn_accuracy.tolist(),
        'final_knn_conf_matrix': final_knn_conf_matrix.tolist(),
        'final_knn_precision': final_knn_precision.tolist(),
        'final_knn_f1': final_knn_f1.tolist(), 
        'final_knn_recall': final_knn_recall.tolist(), 
        'final_knn_mse': final_knn_mse.tolist(), 
        'final_knn_rmse': final_knn_rmse.tolist(),
        'final_svm_predictions': final_svm_predictions.tolist(), 
        'final_svm_probability': final_svm_probability.tolist(),
        'final_svm_accuracy': final_svm_accuracy.tolist(),
        'final_svm_conf_matrix': final_svm_conf_matrix.tolist(),
        'final_svm_precision': final_svm_precision.tolist(),
        'final_svm_f1': final_svm_f1.tolist(), 
        'final_svm_recall': final_svm_recall.tolist(), 
        'final_svm_mse': final_svm_mse.tolist(), 
        'final_svm_rmse': final_svm_rmse.tolist()
        })


if __name__ == "__main__":
    app.run(debug=True)
