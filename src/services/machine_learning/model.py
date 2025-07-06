import pickle


class Model:

    def __init__(self):
        self.model = None

    def load_model(self, path: str):
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                self.model = pickle.load(file)
                return self.model

        raise Exception("Formato de arquivo não suportado")

    def predictor(self, X_input):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        if self.model is None:
            raise Exception("Model not loaded")

        diagnosis = self.model.predict(X_input)
        return diagnosis
