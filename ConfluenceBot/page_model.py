# Возможно, в будущем здесь появятся модели, если будем обрабатывать структуру страниц
class Page:
    def __init__(self, id, title, ancestors):
        self.id = id
        self.title = title
        self.ancestors = ancestors

    def depth(self):
        return len(self.ancestors)

    def __str__(self):
        indent = "  " * self.depth()
        return f"{indent}- {self.title} (ID: {self.id})"
