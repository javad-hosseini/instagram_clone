from passlib.context import CryptContext

password_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

class Hash:

    @staticmethod
    def hashed_password(password: str) -> str:
        return password_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return password_context.verify(plain_password, hashed_password)



