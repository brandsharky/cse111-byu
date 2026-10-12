class ContentItem:
    def __init__(self, title, content_type, total_minutes, segments):
        self.title = title
        self.content_type = content_type
        self.total_minutes = total_minutes
        self.segments = segments


    def minutes_per_segment(self):
        return self.total_minutes / self.segments



class Livestream(ContentItem):
    def __init__(self, title, total_minutes, segments, host):
        super().__init__(title, "livestream", total_minutes, segments)
        self.host = host



class Tutorial(ContentItem):
    def __init__(self, title, total_minutes, segments, level):
        super().__init__(title, "tutorial", total_minutes, segments)
        self.level = level


    def level_up(self, amount):
        self.level += amount