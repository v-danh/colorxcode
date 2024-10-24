# File: colorxcode/__init__.py

try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    # Cho các phiên bản Python cũ hơn
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version("colorxcode")
except PackageNotFoundError:
    __version__ = "unknown"