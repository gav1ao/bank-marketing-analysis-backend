import pickle


class Pipeline:

    def __init__(self):
        self.pipeline = None

    def load_pipeline(self, path: str):
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                self.pipeline = pickle.load(file)
                return self.pipeline

        raise Exception("Formato de arquivo não suportado")