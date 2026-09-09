from __future__ import annotations

from typing import Any

ENDPOINTS = {
    "health": "/health",
    "diagnostics": "/diagnostics",
    "discover": "/discover",
    "entities": "/entities",
    "state": "/state",
    "config": "/config",
    "config_sync": "/config/sync",
    "deconfigure": "/deconfigure",
    "ui_config": "/ui-config",
    "events": "/events",
    "command": "/command",
}

REQUIRED_ENDPOINTS = ["health", "entities", "command", "config", "ui_config"]

CAPABILITIES: dict[str, dict[str, Any]] = {
    "connected": {"kind": "sensor", "unit": "bool"},
    "refresh": {"kind": "action"},
}

COMMANDS: dict[str, dict[str, Any]] = {
    "refresh": {
        "description": "Refresh the integration state.",
        "timeout_ms": 5000,
    },
}

CONFIG_SCHEMA: dict[str, Any] = {
    "schema": {
        "title": "PiPhi Network Nuki Setup",
        "type": "object",
        "required": ["host"],
        "properties": {
    "host": {
        "type": "string",
        "title": "API Host",
        "default": "api.nuki.io"
    },
    "alias": {
        "type": "string",
        "title": "Account Name"
    },
    "api_token": {
        "type": "string",
        "title": "API Token",
        "format": "password",
        "writeOnly": True
    },
    "webhook_secret": {
        "type": "string",
        "title": "Webhook Secret",
        "format": "password",
        "writeOnly": True
    },
    "transport": {
        "type": "string",
        "title": "Transport",
        "enum": [
            "web",
            "mqtt",
            "matter"
        ],
        "default": "web"
    },
    "actions_enabled": {
        "type": "boolean",
        "title": "Enable Lock Actions",
        "default": False
    },
    "allowed_lock_ids": {
        "type": "array",
        "title": "Allowed Lock IDs",
        "items": {
            "type": "string"
        },
        "default": []
    }
},
    },
    "uiSchema": {
        "host": {"placeholder": "api.nuki.io"},
        "alias": {"placeholder": "Nuki Access Device"},
    },
}

FALLBACK_ENTITY: dict[str, Any] = {
    "id": "nuki-access-device",
    "name": "Nuki Access Device",
    "device_id": "nuki-access-device",
    "entity_type": "smart_lock",
    "capabilities": ["connected", "refresh"],
    "available_commands": [
        {"id": "refresh", "label": "Refresh", "kind": "action"},
    ],
    "dashboard": {
        "allowed_widgets": [
    "access-control-card",
    "battery-fleet-card",
    "tile",
    "button"
],
        "default_widget": "access-control-card",
    },
}
