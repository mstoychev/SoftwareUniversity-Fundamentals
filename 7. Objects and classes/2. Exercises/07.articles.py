class Article:
    def __init__(self, title: str, content: str, author: str):
        self.title = str(title)
        self.content = str(content)
        self.author = str(author)

    def edit(self, new_content: str):
        self.content = str(new_content)

    def change_author(self, new_author: str):
        self.author = str(new_author)

    def rename(self, new_title: str):
        self.title = str(new_title)

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"
