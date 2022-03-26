from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        if self.categories:
            for category in self.categories:
                if category.id == category_id:
                    category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        if self.topics:
            for topic in self.topics:
                if topic.id == topic_id:
                    topic.topic = new_topic
                    topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        if self.documents:
            for doc in self.documents:
                if doc.id == document_id:
                    doc.file_name = new_file_name

    def delete_category(self, category_id):
        if self.categories:
            for cat in self.categories:
                if cat.id == category_id:
                    self.categories.remove(cat)

    def delete_topic(self, topic_id):
        if self.topics:
            for top in self.topics:
                if top.id == topic_id:
                    self.topics.remove(top)

    def delete_document(self, document_id):
        if self.documents:
            for doc in self.documents:
                if doc.id == document_id:
                    self.documents.remove(doc)

    def get_document(self, document_id):
        if self.documents:
            for doc in self.documents:
                if doc.id == document_id:
                    return doc

    def __repr__(self):
        result = []
        for doc in self.documents:
            result.append(repr(doc))
        return "\n".join(result)


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)