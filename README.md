# fitness-ai-backend

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

FitAnalytics API — backend service for fitness data processing built with FastAPI.

## Features

- **Calories Calculator** — estimate calories burned based on weight, duration, and intensity
- **Heart Rate Zones** — calculate max HR and target training zones
- **BMR Calculator** — basal metabolic rate using Mifflin-St Jeor equation
- **Pydantic Validation** — strict request/response schemas
- **Auto-docs** — interactive API docs at `/docs`

## Installation

```bash
git clone https://github.com/EminSans1/fitness-ai-backend.git
cd fitness-ai-backend
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --reload
```

API available at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| POST | `/calories` | Calculate calories burned |
| POST | `/heart-rate` | Calculate heart rate zones |
| POST | `/bmr` | Calculate basal metabolic rate |

### Examples

**Calories:**

```bash
curl -X POST http://localhost:8000/calories \
  -H "Content-Type: application/json" \
  -d '{"weight": 70, "duration": 60, "intensity": 3}'
```

Response:

```json
{
  "weight": 70,
  "duration": 60,
  "intensity": 3,
  "calories_burned": 2500.0
}
```

**Heart Rate Zones:**

```bash
curl -X POST http://localhost:8000/heart-rate \
  -H "Content-Type: application/json" \
  -d '{"age": 30, "resting_hr": 65}'
```

Response:

```json
{
  "age": 30,
  "resting_hr": 65,
  "max_hr": 190,
  "target_zone_min": 114,
  "target_zone_max": 152
}
```

**BMR:**

```bash
curl -X POST http://localhost:8000/bmr \
  -H "Content-Type: application/json" \
  -d '{"weight": 80, "height": 180, "age": 25, "gender": "male"}'
```

Response:

```json
{
  "weight": 80,
  "height": 180,
  "age": 25,
  "gender": "male",
  "bmr": 1829.18
}
```

## Development

### Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install pytest httpx
```

### Tests

```bash
pytest
```

## Project Structure

```
fitness-ai-backend/
├── main.py                 # FastAPI application
├── requirements.txt        # Dependencies
├── setup.py                # Package setup
├── pyproject.toml          # Build config
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── LICENSE
├── README.md
└── .gitignore
```

## Contributing

1. Fork the repository
2. Create your branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License — see [LICENSE](LICENSE) for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) — modern Python web framework
- [Pydantic](https://docs.pydantic.dev/) — data validation
