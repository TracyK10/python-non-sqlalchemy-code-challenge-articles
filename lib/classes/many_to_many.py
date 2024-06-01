class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        """Title must be of type str, must be between 5 and 50 characters inclusive and should not be able to change after the article is instantiated."""
        if hasattr(self, '_title'):
            raise AttributeError("Cannot change the title after it has been set")
        if isinstance(title, str) and 5 <= len(title) <= 50:
            return self._title
        else:
            raise ValueError("Title must be a non-empty string.")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
        """author must be of type Author"""
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be of type Author.")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        """magazine must be of type Magazine"""
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be of type Magazine.")
        
class Author:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        """The name property"""
        return self._name
    
    @name.setter
    def name(self, name):
        """Name must be of type str, longer than 0 characters and should not be able to change after the author is instantiated"""
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name after it has been set")
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be an non-empty string.")

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        """Name must be of type str, must be between 2 and 16 characters inclusive, should be able to change after the magazine is instantiated."""
        if isinstance(name, str) and 2 <= len(name) <= 16:
            return self._name
        else:
            raise ValueError("Name must be between 2 and 16 characters long.")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        """Category must be of type str, longer than 0 characters and should be able to change after the magazine is instantiated"""
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be an non-empty string.")

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass