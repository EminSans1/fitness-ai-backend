from fastapi import FastAPI


app = FastAPI()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/calories")
def calories(weight: float, intensity: int) -> dict:
    """
    Примерное количество калорий за час:
    базовые 500 ккал * интенсивность тренировки.
    """
    if intensity < 1:
        intensity = 1
    if intensity > 5:
        intensity = 5

    calories_per_hour: float = 500.0 * float(intensity)

    return {
        "weight": weight,
        "intensity": intensity,
        "calories_per_hour": calories_per_hour,
    }

