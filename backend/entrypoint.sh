#!/bin/sh
set -eu

wait_for_service() {
    service_name="$1"
    service_host="$2"
    service_port="$3"

    echo "Waiting for ${service_name} at ${service_host}:${service_port}..."

    python - "$service_name" "$service_host" "$service_port" <<'PY'
import socket
import sys
import time

service_name, host, port = sys.argv[1], sys.argv[2], int(sys.argv[3])
timeout_at = time.time() + 60

while time.time() < timeout_at:
    try:
        with socket.create_connection((host, port), timeout=2):
            print(f"{service_name} is available.")
            raise SystemExit(0)
    except OSError:
        time.sleep(1)

print(f"Timed out waiting for {service_name} at {host}:{port}.", file=sys.stderr)
raise SystemExit(1)
PY
}

wait_for_service "PostgreSQL" "${POSTGRES_HOST:-db}" "${POSTGRES_PORT:-5432}"
wait_for_service "Redis" "${REDIS_HOST:-redis}" "${REDIS_PORT:-6379}"

python manage.py migrate --noinput

exec python manage.py runserver 0.0.0.0:8000
