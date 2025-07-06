from src.services.machine_learning.evaluator import Evaluator
from src.services.machine_learning.loader import Loader
from src.services.machine_learning.model import Model
from src.services.machine_learning.pipeline import Pipeline

loader = Loader()
model = Model()
evaluator = Evaluator()
pipeline = Pipeline()

url_x_dataset = "machine_learning/data/X_test_dataset.csv"
X = loader.load_dataset(url_x_dataset)

url_y_dataset = "machine_learning/data/y_test_dataset.csv"
y = loader.load_dataset(url_y_dataset)

ACCURACY_SCORE_TARGET = 0.8


def test_model_decistion_tree():
    model_path = "machine_learning/models/model_decision_tree.pkl"
    model_decision_tree = model.load_model(model_path)

    accuracy = evaluator.evaluate_model(model_decision_tree, X, y)
    assert accuracy > ACCURACY_SCORE_TARGET


def test_model_knn():
    model_path = "machine_learning/models/model_knn.pkl"
    model_knn = model.load_model(model_path)

    accuracy = evaluator.evaluate_model(model_knn, X, y)
    assert accuracy > ACCURACY_SCORE_TARGET


def test_model_naive_bayes():
    model_path = "machine_learning/models/model_naive_bayes.pkl"
    model_naive_bayes = model.load_model(model_path)

    accuracy = evaluator.evaluate_model(model_naive_bayes, X, y)
    assert accuracy > ACCURACY_SCORE_TARGET


def test_model_svm():
    model_path = "machine_learning/models/model_svm.pkl"
    model_svm = model.load_model(model_path)

    accuracy = evaluator.evaluate_model(model_svm, X, y)
    assert accuracy > ACCURACY_SCORE_TARGET


def test_model_with_pipeline():
    pipeline_path = "machine_learning/pipelines/modelo_bancario_pipeline.pkl"
    model_from_pipeline = pipeline.load_pipeline(pipeline_path)

    accuracy = evaluator.evaluate_model(model_from_pipeline, X, y)
    assert accuracy > ACCURACY_SCORE_TARGET
