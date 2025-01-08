# Learning about classess in python.

class User:

    def __init__(self, user_id, username):
        """constructor. It will be executed every time when new class object is being created"""
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        # follower from different object
        user.followers += 1
        # following from self = the same object
        self.following +=1

# user_1 = User()
# user_1.id = "001"
# user_1.username = "Michael"
# print(user_1.id)

## Instead above, we will use constructor that will initilize atributes:

user_1 = User("001", "Michael")
user_2 = User("002", "Jack")
print(user_2.id)
print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)