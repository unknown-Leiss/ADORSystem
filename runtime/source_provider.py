

from pathlib import Path


class SourceProvider:
    """Base interface for ADORSystem source providers.

    A SourceProvider is responsible only for discovering and reading sources.
    It must not perform Runtime reconstruction.
    """

    def discover(self, query=None):
        raise NotImplementedError("SourceProvider.discover() must be implemented by subclasses")

    def read(self, source_path):
        raise NotImplementedError("SourceProvider.read() must be implemented by subclasses")


class LocalSourceProvider(SourceProvider):
    """Read sources from a local ADORLibrary / source_library directory."""

    def __init__(self, root_path):
        self.root_path = Path(root_path).expanduser().resolve()

    def discover(self, query=None):
        """Return markdown/text/json sources under the local source root.

        query is optional. When provided, it filters by filename text only.
        """
        if not self.root_path.exists():
            return {
                "status": "missing_root",
                "root_path": str(self.root_path),
                "sources": [],
                "source_count": 0,
            }

        allowed_suffixes = {".md", ".txt", ".json"}
        sources = []

        for path in self.root_path.rglob("*"):
            if not path.is_file():
                continue

            if path.suffix.lower() not in allowed_suffixes:
                continue

            if query and query.lower() not in path.name.lower():
                continue

            sources.append(
                {
                    "name": path.name,
                    "path": str(path),
                    "relative_path": str(path.relative_to(self.root_path)),
                    "suffix": path.suffix.lower(),
                    "provider": "local",
                }
            )

        return {
            "status": "ok",
            "root_path": str(self.root_path),
            "query": query,
            "sources": sources,
            "source_count": len(sources),
        }

    def read(self, source_path):
        """Read a source file and return its content with metadata."""
        path = Path(source_path).expanduser().resolve()

        if not path.exists():
            return {
                "status": "missing_source",
                "path": str(path),
                "content": None,
            }

        if not path.is_file():
            return {
                "status": "not_a_file",
                "path": str(path),
                "content": None,
            }

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = path.read_text(encoding="utf-8", errors="replace")

        return {
            "status": "ok",
            "name": path.name,
            "path": str(path),
            "suffix": path.suffix.lower(),
            "provider": "local",
            "content": content,
        }