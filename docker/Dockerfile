# ================== Compiler ==================
FROM python:3.13-slim AS compiler

ENV PYTHONUNBUFFERED 1

RUN python -m venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt ./requirements.txt

RUN pip install -Ur requirements.txt

# ================== Runner ==================
FROM python:3.13-slim AS runner

WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ../ .

CMD ["bash"]
