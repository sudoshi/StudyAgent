"""MCP tool registry and auto-registration."""

from __future__ import annotations

import importlib
import os
from typing import Iterable

BASE_TOOL_MODULES: list[str] = [
    "study_agent_mcp.tools.concept_set_diff",
    "study_agent_mcp.tools.cohort_lint",
    "study_agent_mcp.tools.phenotype_recommendations",
    "study_agent_mcp.tools.phenotype_improvements",
    "study_agent_mcp.tools.phenotype_intent_split",
    "study_agent_mcp.tools.phenotype_search",
    "study_agent_mcp.tools.phenotype_fetch_summary",
    "study_agent_mcp.tools.phenotype_fetch_definition",
    "study_agent_mcp.tools.phenotype_list_similar",
    "study_agent_mcp.tools.phenotype_reindex",
    "study_agent_mcp.tools.phenotype_index_status",
    "study_agent_mcp.tools.phenotype_prompt_bundle",
    "study_agent_mcp.tools.phenotype_recommendation_advice",
    "study_agent_mcp.tools.lint_prompt_bundle",
    "study_agent_mcp.tools.keeper_validation",
]

OPTIONAL_TOOL_MODULES: list[tuple[str, str]] = [
    ("FINNGEN_COHORT_OPERATIONS_ENABLED", "study_agent_mcp.tools.finngen_cohort_operations"),
    ("FINNGEN_CO2_ANALYSIS_ENABLED", "study_agent_mcp.tools.finngen_co2_analysis"),
    ("FINNGEN_HADES_EXTRAS_ENABLED", "study_agent_mcp.tools.finngen_hades_extras"),
    ("FINNGEN_ROMOPAPI_ENABLED", "study_agent_mcp.tools.finngen_romopapi"),
]


def _env_enabled(name: str) -> bool:
    value = os.getenv(name, "").strip().lower()
    return value in {"1", "true", "yes", "on"}


def iter_tool_modules() -> Iterable[str]:
    for module_name in BASE_TOOL_MODULES:
        yield module_name

    for env_name, module_name in OPTIONAL_TOOL_MODULES:
        if _env_enabled(env_name):
            yield module_name


def register_all(mcp: object) -> None:
    for module_name in iter_tool_modules():
        module = importlib.import_module(module_name)
        register = getattr(module, "register", None)
        if register is None:
            raise RuntimeError(f"Tool module {module_name} missing register(mcp)")
        register(mcp)

TOOL_MODULES = list(iter_tool_modules())


__all__ = [
    "BASE_TOOL_MODULES",
    "OPTIONAL_TOOL_MODULES",
    "TOOL_MODULES",
    "iter_tool_modules",
    "register_all",
]
