import uuid
from pydantic import BaseModel, Field


class CourseSchema(BaseModel):
    id: str = "course-id"
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")

# Создадим объект модели без передачи параметров
course = CourseSchema()
print(course)


class CourseSchema2(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")


# Создадим несколько объектов модели
course1 = CourseSchema2()
course2 = CourseSchema2()

print(course1.id)
print(course2.id)
