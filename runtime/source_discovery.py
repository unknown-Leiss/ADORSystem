

from source_provider import LocalSourceProvider


class SourceDiscovery:
    """Discover candidate sources required for Runtime Bootstrap."""

    def __init__(self, source_root):
        self.provider = LocalSourceProvider(source_root)

    def discover(self, query=None):
        """Discover candidate sources.

        This stage only identifies available sources.
        It does not read or interpret them.
        """
        result = self.provider.discover(query=query)

        return {
            "status": result["status"],
            "query": query,
            "source_count": result.get("source_count", 0),
            "sources": result.get("sources", []),
            "provider": "local",
            "next_stage": "Source Routing",
        }


if __name__ == "__main__":
    SOURCE_ROOT = "source_library"

    discovery = SourceDiscovery(SOURCE_ROOT)
    result = discovery.discover()

    print("=== Source Discovery ===")
    print(f"Status : {result['status']}")
    print(f"Sources: {result['source_count']}")

    for source in result["sources"]:
        print(f" - {source['relative_path']}")