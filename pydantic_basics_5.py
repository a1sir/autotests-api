import uuid

from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError


# Добавили модель FileSchema
class FileSchema(BaseModel):
    id: str
    url: HttpUrl  # Используем HttpUrl вместо str
    filename: str
    directory: str


# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"

# Инициализируем FileSchema c некорректным url
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())