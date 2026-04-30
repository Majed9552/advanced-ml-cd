# Stage 1: Build environment and install dependencies
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
# Install dependencies for the local user to easily copy later
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.11-slim
WORKDIR /app
# Copy only the installed packages from the builder stage
COPY --from=builder /root/.local /root/.local
COPY . .
# Update PATH to include user installed packages
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000

# Start the FastAPI server
CMD ["python", "webapp/app.py"]