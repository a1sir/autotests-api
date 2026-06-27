from pydantic import BaseModel

class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str
    first_name: str
    middle_name: str

class ShortUserSchema(BaseModel):
    id: str
    email: str

class FullUserSchema(ShortUserSchema):
    last_name: str
    first_name: str
    middle_name: str

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: str

class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema
    estimated_time: str
    created_by_user: UserSchema

class GetCourseResponseSchema(BaseModel):
    course: CourseSchema

class ExtendedUserSchema(ShortUserSchema):
    last_name: str
    first_name: str
    middle_name: str
