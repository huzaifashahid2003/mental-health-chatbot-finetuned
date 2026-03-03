# ── Base image ────────────────────────────────────────────
# Python 3.11 slim keeps the image small and is CPU-compatible
FROM python:3.11-slim

# ── Working directory inside the container ────────────────
WORKDIR /app

# ── Copy dependency file first (layer-caching optimisation)
COPY requirements.txt .

# ── Install Python dependencies ───────────────────────────
RUN pip install --no-cache-dir -r requirements.txt

# ── Copy the rest of the project ─────────────────────────
COPY . .

# ── Expose Streamlit default port ────────────────────────
EXPOSE 8501

# ── Health check (optional but useful) ───────────────────
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# ── Start the Streamlit app ───────────────────────────────
CMD ["streamlit", "run", "app/streamlit_app.py", \
     "--server.port=8501", "--server.address=0.0.0.0"]
