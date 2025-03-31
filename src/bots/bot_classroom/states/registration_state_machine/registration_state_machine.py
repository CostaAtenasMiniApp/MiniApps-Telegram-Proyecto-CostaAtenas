from .name_state import NameState

class RegistrationStateMachine:
    def __init__(self):
        self.state = None  # Estado inicial de la máquina

    def start(self, update, context):
        # Inicia el proceso de registro con el estado NameState
        self.state = NameState(self)
        self.state.handle(update, context)

    def transition_to(self, new_state):
        # Cambia al siguiente estado
        self.state = new_state
