class Publication:
    def __init__(self, title, authors):
        self.title = title
        self.authors = authors
        
    def get_title():
        return title
    
    def get_author():
        return authors
    
    def set_title(title):
    
    def set_author(author):


        class Book(Publication):
            def __init__(self, title, authors, number_of_pages):
                super().__init__(self, title, authors)
                self.number_of_pages = number_of_pages

            def get_number_of_pages():
                return number_of_pages
            
            
        class Magazine(Publication):
            def __init__(self, title, authors, number_of_pages, issue_number):
                super().__init__(self, title, authors, number_of_pages)
                self.issue_number = issue_number
