from __future__ import annotations

import json

from piphi_network_nuki.schemas import DeviceConfig
from piphi_network_nuki.state import _split_config, make_entry


def test_tokens_are_kept_out_of_persisted_and_serialized_config() -> None:
    config = DeviceConfig(id="nuki-test", api_token="token-secret", webhook_secret="hook-secret")

    public, secrets = _split_config(config)
    entry = make_entry(config)

    assert {"api_token", "webhook_secret"}.isdisjoint(public)
    assert secrets == {"api_token": "token-secret", "webhook_secret": "hook-secret"}
    serialized = json.dumps(entry)
    assert "token-secret" not in serialized
    assert "hook-secret" not in serialized
