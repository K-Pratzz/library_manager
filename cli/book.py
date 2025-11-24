#Name : Kumari Pratibha
#Roll no : 2501010123
#B.Tech CSE Core "A"
class Book:
    def _init_(self, title, author, status="available"):
        self.title = title
        self.author = author
        self.status = status

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "status": self.status
        }
