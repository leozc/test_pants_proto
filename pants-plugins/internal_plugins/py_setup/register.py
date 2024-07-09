from __future__ import annotations

import os
import uuid

from pants.backend.python.util_rules.package_dists import (
    SetupKwargs,
    SetupKwargsRequest,
)
from pants.engine.rules import collect_rules, rule
from pants.engine.target import Target
from pants.engine.unions import UnionRule


class PantsSetupKwargsRequest(SetupKwargsRequest):
    @classmethod
    def is_applicable(cls, _: Target) -> bool:
        return True


sdk_folder_path = "cipherowl/databricks/sdk"


@rule
async def pants_setup_kwargs(request: PantsSetupKwargsRequest) -> SetupKwargs:
    kwargs = request.explicit_kwargs.copy()

    sha = os.environ.get("CIRCLE_SHA1", uuid.uuid4())

    if sdk_folder_path in str(request.target.address):
        overwrite_args = dict(version=kwargs["version"] + f"-{sha}")
        kwargs.update(overwrite_args)

    return SetupKwargs(kwargs, address=request.target.address)


def rules():
    return (*collect_rules(), UnionRule(SetupKwargsRequest, PantsSetupKwargsRequest))
