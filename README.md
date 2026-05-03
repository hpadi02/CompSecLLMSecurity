# LangKit + LLM Guard — Security Dashboard

Minimalistic Streamlit dashboard for the Milestone 3 integration module.
Wraps `llm_guard_integration.py` in a live UI that lets you paste a prompt,
run it through the LLM Guard scanners, and see the six whylogs-ready
metrics produced — including the redacted text and the final block decision.

## Quick start

```bash
# 1. Create and activate a virtual environment (Python 3.11)
python3.11 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate            # Windows PowerShell

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the dashboard
streamlit run dashboard.py
```

The first launch downloads several hundred MB of ML models — this only
happens once. Subsequent runs use the cached models.

The dashboard opens in your browser at http://localhost:8501.

## Files

| File                          | Purpose                                                           |
| ----------------------------- | ----------------------------------------------------------------- |
| `llm_guard_integration.py`    | The M3 integration module — wraps LLM Guard for whylogs profiling |
| `dashboard.py`                | Streamlit UI                                                      |
| `requirements.txt`            | Python dependencies                                               |

## Demo tips for class

- **Pre-warm the models before class.** Run the dashboard once and scan a
  prompt 5–10 minutes before presenting. The first scan after launch is
  slow because it downloads/loads models; subsequent scans are fast.
- **Use the sidebar examples.** They're the same prompts referenced in
  the M1, M2, and M3 demo sections of the report.
- **Strong moments to demo live:**
  - The SSN prompt — shows inline PII redaction
  - The persona-switch prompt — flagged on intent, no keywords
  - The "business hours" prompt — clears every scanner

## Authors

Rene Sanchez · Hugo Padilla
Department of Computer Science
Texas A&M University–San Antonio