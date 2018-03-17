import hashlib


class SolveHash:
    def __init__(
        self,
        block_no,
        prev_block_hash,
        name,
        surname,
        title,
        phone_number,
        e_mail
    ):
        self.block_no = str(block_no)
        self.prev_block_hash = prev_block_hash
        self.name = name
        self.surname = surname
        self.title = title
        self.phone_number = phone_number
        self.e_mail = e_mail

    def solve(self):
        nonce = -1
        hash = ''
        while hash[0:4] != '0000':
            nonce = nonce + 1
            hash = self.calculate(nonce)
        return nonce, hash

    def calculate(self, nonce):
        m = hashlib.md5()
        m.update(self.block_no)
        m.update(self.prev_block_hash)
        m.update(self.name)
        m.update(self.surname)
        m.update(self.title)
        m.update(self.phone_number)
        m.update(self.e_mail)
        m.update(str(nonce))
        return m.hexdigest()
