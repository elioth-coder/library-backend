from .repository import Repository

class MemberRepository(Repository):
    def __init__(self):
        super().__init__('member')