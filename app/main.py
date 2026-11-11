from fastapi import FastAPI

app = FastAPI(
    title="DevSecOps Hands-On API",
    description="Secure CI/CD pipeline training application",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "project": "DevSecOps Hands-On",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "devsecops-api"
    }
