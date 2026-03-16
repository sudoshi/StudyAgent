from __future__ import annotations

import os
from typing import Any, Dict

from ._common import with_meta

PROJECT_REPO = "https://github.com/FINNGEN/HadesExtras"
PROJECT_LABEL = "HadesExtras"


def register(mcp: object) -> None:
    @mcp.tool(name="finngen_hades_extras_catalog")
    def finngen_hades_extras_catalog() -> Dict[str, Any]:
        payload = {
            "project": "finngen_hades_extras",
            "label": PROJECT_LABEL,
            "repository": PROJECT_REPO,
            "workspace": "artifact-studio",
            "enabled": True,
            "configured": bool(
                os.getenv("FINNGEN_HADES_EXTRAS_BASE_URL")
                or os.getenv("FINNGEN_HADES_EXTRAS_COMMAND")
            ),
            "operations": [
                "render_sql",
                "diff_generated_artifacts",
                "build_hades_bundle",
                "inspect_package_manifest",
            ],
            "visualizations": [
                "sql_diff_view",
                "artifact_pipeline",
                "manifest_dependency_graph",
                "rendered_output_gallery",
            ],
        }
        return with_meta(payload, "finngen_hades_extras_catalog")

    return None
