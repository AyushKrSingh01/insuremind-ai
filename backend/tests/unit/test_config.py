
from app.core.config import Settings, get_settings


def test_default_settings():
    settings = Settings(_env_file=None)

    assert settings.app_name == "InsureMind AI"
    assert settings.app_version == "0.1.0"
    assert settings.app_env == "development"
    assert settings.debug is True
    assert settings.log_level == "INFO"


def test_environment_variable_override(monkeypatch):
    monkeypatch.setenv("APP_NAME", "InsureMind Test")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    settings = Settings(_env_file=None)

    assert settings.app_name == "InsureMind Test"
    assert settings.debug is False
    assert settings.log_level == "DEBUG"


def test_settings_are_cached():
    get_settings.cache_clear()

    first = get_settings()
    second = get_settings()

    assert first is second

    get_settings.cache_clear()
