# 06. Docker 🐳
Topics: images, containers, Dockerfile, layers, ports, volumes, networks, Compose, registries and image hygiene.

## Starter lab
    docker --version
    docker run --rm hello-world

## Minimal Dockerfile
    FROM python:3.12-slim
    WORKDIR /app
    COPY app.py .
    CMD ["python", "app.py"]

Create a simple app.py, build the image and run it locally. Exercises: explain image vs container, use a named volume, and write a Compose file.

Do not mount sensitive host directories into containers. Review image sources and permissions.