from __future__ import annotations

import os

INTEGRATION_ID = "piphi-network-nuki"
INTEGRATION_NAME = "Piphi Network Nuki"
INTEGRATION_VERSION = "0.1.0"
PROJECT_KIND = "integration"
PROJECT_PRESET = "webhook-receiver"
PROJECT_DOMAIN = "cloud-api"
DEFAULT_PORT = 4226


def runtime_port() -> int:
    raw_port = os.getenv("PORT", str(DEFAULT_PORT))
    try:
        return int(raw_port)
    except ValueError:
        return DEFAULT_PORT
