from pydantic import BaseModel, Field
import json


class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week"
)
print('Course default model:', course_default_model)


# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)


# Инициализируем модель CourseSchema через JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)


# Если у нас есть JSON-файл, мы можем загрузить его в Pydantic-модель
with open("course.json", "r") as file:
    course_data = file.read()

course_model = CourseSchema.model_validate_json(course_data)
print(course_model)

# Но если нам нужно вернуть JSON в camelCase, то можно использовать by_alias=True
print(course_dict_model.model_dump(by_alias=True))


