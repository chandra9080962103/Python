#we can create our own error names.
class children_not_allowed(Exception):
    pass
class oldaged_not_allowed(Exception):
    def __init__(self, age, message):
        self.age = age
        self.messgae = message

def movie_permissions(x):
    if x <= 18:
        raise children_not_allowed ("under 18")
    if x>= 50:
        raise oldaged_not_allowed(x, "old_aged_not_allowed")
    
try:
    movie_permissions(60)
except Exception as e:
    print("sorry, you're not allowed")
    
