class Platform:
    def __init__(self, name, content_items=None):
        self.name = name
        if content_items is None:
            self.content_items = []
        else:
            self.content_items = content_items


    def publish(self, item):
        self.content_items.append(item)


    def is_published(self, item):
        return item in self.content_items


    def archive(self, item):
        self.content_items.remove(item)