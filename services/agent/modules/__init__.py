"""Module registry: auto-discover and register feature modules."""

import importlib
import pkgutil


def register_all(app, deps, features_cfg: dict) -> list:
    """Import every module in this package and call its register() if present.

    Returns the list of enabled module names (for /api/manifest).
    """
    enabled = []
    for _, name, _ in pkgutil.iter_modules(__path__):
        mod = importlib.import_module(f".{name}", __package__)
        cfg = features_cfg.get(name, {})
        if isinstance(cfg, dict) and cfg.get("enable", True) is False:
            continue
        if hasattr(mod, "register"):
            mod.register(app, deps, cfg)
            enabled.append(name)
    return enabled
