class User: 
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


#following is who im following

user_1 = User("001", "Isaac")
user_2 = User("002","Rhi")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)



#attribute is a variable that is associated with an object