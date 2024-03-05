class UserToken:
    def __init__(self, access, refresh):
        self.access = access
        self.refresh = refresh

    def to_dict(self):
        return {
            'Authorization': self.access,
            'refreshToken': self.refresh
        }
