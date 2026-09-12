# Demo runbook (SIH 2026)

A clean end-to-end demo takes ~2 minutes to bring up.

## 0. Prerequisites

- Docker (for PostgreSQL + pgvector)
- Python 3.11+
- Node 18+

## 1. Database

```bash
make db          # docker compose up -d db  (Postgres on host port 5433)
```

If you already had a volume from an older build, apply migrations:

```bash
make migrate
```

## 2. Backend + sample data

```bash
make venv        # one-time: virtualenv + deps
make seed        # wipe, load 108 CPSE records, run matching, play steward decisions
make api         # http://localhost:8000  (docs at /docs)
```

`make seed` provisions two demo accounts (password `materialsetu`):
`admin@` / `steward@material-setu.gov.in`, then produces a realistic
starting state:

| | |
|---|---|
| Local material records | ~124 across 18 CPSEs, 5 sectors, ~19 Federal Supply Groups |
| Procurement history | ~430 representative PO lines (price varies by CPSE) |
| Candidate matches | ~104 cross-CPSE pairs above 0.60 (lexical + semantic) |
| Auto-approved | ~28 high-confidence identities → ~19 National Material Codes |
| Auto-rejected | 2 near-misses (bronze vs carbon-steel gate valve) |
| Left pending | ~74 for the live steward demo |
| Aggregation opportunity | ~₹80 L estimated annual saving across ~12 NMCs |

The sample master is built from **real** manufacturer designations and standard
specs (SKF 6205-2Z, FAG 22217 EK, ISO 4014 M16, API 600 gate valves, IS 7098
XLPE cable, IS 2062 E250 plate, …) recorded the way different CPSEs actually
fragment them — different codes, descriptions and units for the same item.

## 3. Dashboard

```bash
make ui          # http://localhost:5173  → landing page, then sign in
```

## 4. Suggested walk-through

Sign in as `steward@material-setu.gov.in` / `materialsetu`. Sidebar:
**Overview · Materials · Review queue · Registry · Audit trail** (admins also see
**Team & access**).

1. **Overview** — impact tiles and coverage by sector / CPSE / **Federal Supply
   Group** (the NATO Codification System's 2-digit groups) / family.
2. **Materials → Add material** — type a description (e.g.
   `Power cable 11 KV 3 core 240 sqmm aluminium XLPE armoured`) and pick a family;
   the **standardization preview** updates live:
   - normalized text
   - **class → FSC 6145 · Wire and Cable, Electrical** with the term that drove it
   - **unit → MTR metre · UN/CEFACT Rec 20** (typed `RMT`, `NOS`, `MT` … all resolve)
   - extracted attributes
3. **Run harmonization** (top-right) — jumps to the Review queue and plays the
   staged panel: standardization → attribute extraction → cross-CPSE scoring → ranking.
4. **Review queue** — open a pending card:
   - the score ring and the **explanation** — including
     `description similarity: 85% lexical, 56% semantic → 90% combined`
     (the semantic pass bridges `DGBB` ↔ `deep groove ball bearing`)
   - green chips are agreeing attributes, red chips are conflicts
   - **Approve** → a National Material Code is published live; **Reject** → recorded
5. **Guardrail** — filter to *rejected*: the bronze-body gate valve matched the
   carbon-steel ones on bore / rating / type, but the steward declined. A critical
   conflict (voltage, bore, grade) automatically cuts the score — identity
   matching is **not** substitution approval.
6. **Registry** — each National Material Code is **anchored to its FSC class**
   (`NMC-3110-00001` = an antifriction-bearing identity) and keeps every local
   code as a crosswalk; no CPSE code is overwritten. Search by NMC, FSC, CPSE or
   description.
7. **Procurement** — the pay-off. For each National Material Code bought by 2+
   CPSEs, the screen shows the **price each CPSE actually paid** for the same
   item, the spread (often 1.5–2×), and the saving if all procured at the best
   achieved rate — one aggregated tender per row. Headline saving on the tile.
8. **Audit trail** — every ingestion, classification, run and decision,
   filterable, attributed to the signed-in user.
9. **Team & access** (admin) — promote a steward to admin for full control;
   the last admin can't be demoted.

## Reset between runs

```bash
make seed        # full wipe + reload
# or, with the backend running:
make reset       # POST /admin/reset (truncate only)
```

`/admin/reset` is enabled only while `MATERIAL_SETU_DEMO=1` (the default in dev).
Set it to `0` for any non-demo deployment.
