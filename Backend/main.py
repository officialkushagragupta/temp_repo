"""Backend server initialization."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Root endpoint."""
    return {"message": "Backend API is running", "version": "1.0.0"}


@app.get("/api/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


def start_backend():
    """Start the backend server."""
    print("Backend server started on http://localhost:8000")