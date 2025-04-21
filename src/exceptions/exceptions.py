class AppError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class DuplicateEmailError(AppError):
    def __init__(self, email: str):
        super().__init__(f"O e-mail '{email}' já está em uso.", status_code=409)

class DatabaseError(AppError):
    def __init__(self, message="Erro ao acessar o banco de dados"):
        super().__init__(message, status_code=500)