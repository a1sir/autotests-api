# Использование alias_generator для автоматического преобразования

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CourseSchema(BaseModel):
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str


course_data = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}

course_model = CourseSchema(**course_data)
print(course_model.model_dump(by_alias=True))
