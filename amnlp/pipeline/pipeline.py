class Pipeline:

    def __init__(self):

        self.components = []

    def add(self, component):

        self.components.append(component)

    def run(self, text):

        data = text

        for c in self.components:

            data = c(data)

        return data