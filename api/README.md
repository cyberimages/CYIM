# CyberGenerateOS API

The CyberGenerateOS API provides endpoints for generating art and music, checking server status, and managing models. It is built with FastAPI and designed for seamless integration with external systems.

## Endpoints

### Art Generation
- **POST** `/api/v1/art/`: Generate artwork based on a prompt.

### Music Generation
- **POST** `/api/v1/music/`: Generate music tracks based on a prompt and duration.

### Server Status
- **GET** `/api/v1/status/`: Retrieve the current server status.

## Installation

1. Navigate to the `api/` folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
