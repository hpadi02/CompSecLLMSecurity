"""
llm_guard_integration.py

Bridges LLM Guard's input scanners into LangKit's whylogs metric pipeline.
Each call to scan() returns a flat dict that can be dropped directly into
why.log() and is also human-readable for dashboard display.

Authors: Rene Sanchez, Hugo Padilla
Course: Computer Security — Milestone 3
"""

from llm_guard import scan_prompt
from llm_guard.input_scanners import Anonymize, PromptInjection, Toxicity
from llm_guard.vault import Vault


# ---------------------------------------------------------------------------
# Module-level scanner setup. Models load once, on first import, not per call.
# ---------------------------------------------------------------------------
_vault = Vault()
_input_scanners = [
    Anonymize(_vault),
    PromptInjection(),
    Toxicity(),
]


def scan(prompt: str) -> dict:
    """
    Scan a prompt through the three LLM Guard input scanners and return a
    flat dict of metrics suitable for whylogs profiling and UI display.

    Returned keys:
        prompt                              — original input text
        prompt.sanitized                    — text after PII redaction
        prompt.llm_guard.injection_score    — raw PromptInjection score
        prompt.llm_guard.pii_detected       — 0.0 (clean) or 1.0 (PII found)
        prompt.llm_guard.toxicity_score     — raw Toxicity score
        prompt.llm_guard.blocked            — 0.0 (allowed) or 1.0 (blocked)
        prompt.llm_guard.reasons            — list of scanners that failed
    """
    sanitized, is_valid, scores = scan_prompt(_input_scanners, prompt)

    failed_scanners = [name for name, ok in is_valid.items() if not ok]

    return {
        "prompt":                            prompt,
        "prompt.sanitized":                  sanitized,
        "prompt.llm_guard.injection_score":  scores.get("PromptInjection", 0.0),
        "prompt.llm_guard.pii_detected":     0.0 if is_valid.get("Anonymize", True) else 1.0,
        "prompt.llm_guard.toxicity_score":   scores.get("Toxicity", 0.0),
        "prompt.llm_guard.blocked":          0.0 if all(is_valid.values()) else 1.0,
        "prompt.llm_guard.reasons":          failed_scanners,
    }