import webbrowser
class Movie():
    def __init__(self,title,story,wiki_page,trailer):
        self.title=title
        self.storyline=story
        self.wiki=wiki_page
        self.trailer=trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)
        
