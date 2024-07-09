# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_requirements(
    module_mapping={
        "strawberry-graphql": ["strawberry"],
        "beautifulsoup4": ["bs4"],
        "python-gnupg": ["gnupg"],
        "node-semver": ["nodesemver"],
    },
)

__dependents_rules__(
    (  # Only the explorer server may depend on these libraries
        (
            "[fastapi]",
            "[starlette]",
            "[strawberry-graphql]",
            "[uvicorn]",
        ),
        "pants-plugins/pants_explorer/server/**",
        "!*",
    ),
    # Free for all on the rest
    ("*", "*"),
)

python_requirements (
        name="delta-spark",
        source="ds-requirement.txt",
        resolve="python-ds",
)