from sklearn.metrics import accuracy_score


class Evaluator:

    def evaluate_model(self,  model, X_test, Y_test):
        """ Faz uma predição e avalia o modelo.
        """
        predictions = model.predict(X_test)

        return accuracy_score(Y_test, predictions)