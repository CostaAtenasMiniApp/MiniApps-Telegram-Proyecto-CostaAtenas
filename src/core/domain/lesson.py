from .module import Module

class Lesson:
    def __init__(
        self,
        id_lesson: int,
        title: str,
        content: str,
        duration: int,
        order: int,
        module: Module
    ):
        self.id_lesson = id_lesson
        self.title = title
        self.content = content
        self.duration = duration
        self.order = order
        self.module = module