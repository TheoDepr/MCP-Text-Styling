# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml ./
COPY server.py ./
COPY styles/ ./styles/

# Install uv for faster dependency management
RUN pip install uv

# Install dependencies using uv
RUN uv pip install --system -r pyproject.toml

# Expose port for MCP server (if needed for HTTP transport)
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash mcpuser && \
    chown -R mcpuser:mcpuser /app
USER mcpuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import server; print('Server module loads successfully')" || exit 1

# Default command to run the server
CMD ["python", "server.py"]