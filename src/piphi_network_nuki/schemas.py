from __future__ import annotations

from pydantic import Field
from piphi_runtime_kit_python import RuntimeConfig


class DeviceConfig(RuntimeConfig):
    host: str = "api.nuki.io"
    alias: str | None = None
    api_token: str | None = None
    webhook_secret: str | None = None
    transport: str = "web"
    actions_enabled: bool = False
    allowed_lock_ids: list[str] = Field(default_factory=list)
