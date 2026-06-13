from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(
    title="FitAnalytics API",
    description="Backend service for fitness data processing and analysis",
    version="1.0.0",
)


class CaloriesRequest(BaseModel):
    weight: float = Field(..., gt=0, description="Body weight in kg")
    duration: float = Field(..., gt=0, description="Workout duration in minutes")
    intensity: int = Field(..., ge=1, le=5, description="Intensity level 1-5")


class CaloriesResponse(BaseModel):
    weight: float
    duration: float
    intensity: int
    calories_burned: float


class HeartRateRequest(BaseModel):
    age: int = Field(..., gt=0, le=120)
    resting_hr: int = Field(..., gt=0, le=200)


class HeartRateResponse(BaseModel):
    age: int
    resting_hr: int
    max_hr: int
    target_zone_min: int
    target_zone_max: int


class BMRRequest(BaseModel):
    weight: float = Field(..., gt=0)
    height: float = Field(..., gt=0)
    age: int = Field(..., gt=0, le=120)
    gender: str = Field(..., pattern="^(male|female)$")


class BMRResponse(BaseModel):
    weight: float
    height: float
    age: int
    gender: str
    bmr: float


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/calories", response_model=CaloriesResponse)
def calculate_calories(req: CaloriesRequest) -> CaloriesResponse:
    base_rate = 500.0
    calories_per_hour = base_rate * req.intensity
    calories_burned = (calories_per_hour / 60) * req.duration

    return CaloriesResponse(
        weight=req.weight,
        duration=req.duration,
        intensity=req.intensity,
        calories_burned=round(calories_burned, 2),
    )


@app.post("/heart-rate", response_model=HeartRateResponse)
def calculate_heart_rate(req: HeartRateRequest) -> HeartRateResponse:
    max_hr = 220 - req.age
    target_min = int(max_hr * 0.6)
    target_max = int(max_hr * 0.8)

    return HeartRateResponse(
        age=req.age,
        resting_hr=req.resting_hr,
        max_hr=max_hr,
        target_zone_min=target_min,
        target_zone_max=target_max,
    )


@app.post("/bmr", response_model=BMRResponse)
def calculate_bmr(req: BMRRequest) -> BMRResponse:
    if req.gender == "male":
        bmr = 88.362 + (13.397 * req.weight) + (4.799 * req.height) - (5.677 * req.age)
    else:
        bmr = 447.593 + (9.247 * req.weight) + (3.098 * req.height) - (4.330 * req.age)

    return BMRResponse(
        weight=req.weight,
        height=req.height,
        age=req.age,
        gender=req.gender,
        bmr=round(bmr, 2),
    )
