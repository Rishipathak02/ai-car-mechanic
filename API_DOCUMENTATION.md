# API Documentation

Base URL: `http://localhost:8000`

## POST /api/chat/
Request:
```json
{"session_id":"abc","message":"My car is not starting"}
```
Response:
```json
{"session_id":"abc","reply":"..."}
```

## POST /api/upload/
Multipart form-data: `session_id`, `file`.
Accepts image, audio and video MIME types.

## POST /api/diagnosis/
```json
{"session_id":"abc","symptoms":"Car cranks but does not start; battery light is on"}
```

## POST /api/booking/
```json
{"name":"Rishi","phone":"9999999999","car_model":"Honda City 2022","issue":"Car does not start","preferred_date":"2026-09-25","preferred_time":"11:00"}
```

## GET /api/booking/{id}/
Returns a saved booking.

## GET /api/history/{session_id}/
Returns stored chat messages for a session.
