"""Aqueduct ETL Mapping Workbench catalog tool."""

from __future__ import annotations

import os
from typing import Any, Dict


def register(mcp: object) -> None:
    @mcp.tool(name="etl_mapping_workbench_catalog")  # type: ignore[attr-defined]
    def etl_mapping_workbench_catalog() -> Dict[str, Any]:
        """Return Aqueduct ETL Mapping Workbench service descriptor."""
        payload = {
            "project": "etl_mapping_workbench",
            "label": "Aqueduct",
            "repository": None,
            "workspace": "etl-workbench",
            "enabled": True,
            "configured": bool(os.getenv("ETL_MAPPING_WORKBENCH_ENABLED")),
            "operations": [
                "list_vocabularies",
                "preview_lookup",
                "generate_lookups",
            ],
            "visualizations": ["sql_preview"],
        }
        return payload

    return None
