def route_source(character_context):
    print("\n=== Source Routing Runtime ===")
    print("Source Routing Ready")

    if character_context is None:
        character_context = {}

    priority_order = [
        "identity",
        "behavior",
        "recognition",
        "verification",
        "reconstruction",
    ]

    routed_sources = []
    missing_sources = []

    for layer_name in priority_order:
        source = character_context.get(layer_name)

        if not source:
            missing_sources.append(layer_name)
            continue

        routed_sources.append(
            {
                "layer": layer_name,
                "source": source,
                "priority": priority_order.index(layer_name) + 1,
                "status": "available",
            }
        )

    source_routing = {
        "character_context": character_context,
        "priority_order": priority_order,
        "routed_sources": routed_sources,
        "missing_sources": missing_sources,
        "routing_status": "provisional",
        "purpose": "Route available character sources before meaning extraction",
    }

    return source_routingß