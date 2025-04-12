class State:
    def __init__(self, machine):
        self.machine = machine

    def handle(self, update, context):
        raise NotImplementedError("Debe implementar el método handle.")
