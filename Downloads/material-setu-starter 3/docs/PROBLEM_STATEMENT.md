# Problem Statement

**AI-Driven Standardization and Harmonization of Material Codes Across CPSEs**

Project: **Material Setu** — *One Nation. One Material Identity.*

---

## Background

Central Public Sector Enterprises (CPSEs) across Oil & Gas, Power, Steel, Mining
and Heavy Engineering independently procure and stock thousands of materials that
are identical or functionally equivalent. Because every enterprise maintains its
own material master, the *same* physical item ends up with:

- different material codes,
- inconsistent, free-text descriptions,
- varying specification formats,
- non-standard units of measurement, and
- incompatible classification hierarchies.

The downstream cost is significant — bloated and duplicated material masters,
inability to recognise equivalent items, fragmented spend data, excess safety
stock held separately by each CPSE, and missed opportunities for pooled /
collaborative procurement and inter-unit stock transfer.

## Problem

There is currently no intelligent, scalable mechanism to **detect equivalence,
reconcile descriptions, and assign a single trusted identity** to a material that
exists under many local codes across CPSEs — while still preserving each
enterprise's existing codes for operational continuity.

## Proposed Solution

An **AI-powered National Unified Material Master Framework** that ingests material
data from multiple CPSEs and:

1. **Standardizes** descriptions, units, dimensions and attributes into a common,
   machine-readable form.
2. **Extracts key engineering attributes** (series, size, rating, grade, closure,
   voltage, pressure class, …) from unstructured descriptions using
   **family-aware templates**.
3. **Identifies likely duplicates / equivalents** with a hybrid of lexical
   similarity, attribute matching and (roadmap) semantic embeddings — attaching a
   plain-language **explanation to every match**.
4. **Routes candidates to a human steward** for approve / reject review — AI
   proposes, a human decides.
5. **Publishes an approved identity as a National Material Code (NMC)**, keeping a
   full crosswalk back to every local code.
6. **Records an immutable audit trail** of who did what, when and why.

## What Makes This Approach Unique

| # | Differentiator | Why it matters |
|---|----------------|----------------|
| 1 | **Explainable-by-default matching** | Every candidate carries its rationale (`same series 6205`, `same closure zz`, `description similarity 91%`) so a steward decides in seconds instead of re-investigating each pair. |
| 2 | **Engineering-safety guardrail** | When a *critical* attribute conflicts (voltage, pressure rating, material grade, bore) the score is deliberately cut — preventing "looks similar, is actually different" errors. Identity matching is explicitly **not** substitution approval. |
| 3 | **Non-destructive harmonization** | Local CPSE codes are never overwritten. The NMC sits *above* them as a crosswalk, so existing ERP / procurement systems keep working unchanged. |
| 4 | **Human-in-the-loop steward queue** | No identity is published without review — adoptable in a trust-sensitive, multi-organisation setting. |
| 5 | **Family-aware attribute templates** | Bearings, cables, valves, fasteners, pipes, motors and plates each get their own attribute schema and critical-key set (bore snapped to a standard DN ladder, inch↔mm reconciled, UOM canonicalised), so precision improves per family instead of a one-size-fits-all model. |
| 6 | **ERP-agnostic incremental ingestion** | A CSV / API adapter layer lets a CPSE onboard without a system migration. |
| 7 | **Auditable end to end** | Ingestion, matching runs and every steward decision are written to an append-only audit log. |

## Expected Outcomes

- A searchable National Material Registry with NMC ↔ local-code crosswalks.
- Measurable reduction in duplicate master records and description inconsistency.
- Consolidated, comparable spend data across CPSEs enabling collaborative
  procurement and inter-unit material transfer.
- Lower aggregate inventory through visibility of equivalent stock held elsewhere.
- An auditable, standards-aligned harmonization process.

## Scope Boundaries (MVP)

- Matching produces **identity** candidates, not engineering substitution
  clearance.
- Semantic (Sentence-BERT / pgvector) matching is stubbed for the next milestone;
  the MVP ships lexical + family-aware attribute + manufacturer-part matching with
  a critical-conflict guardrail.
- Authentication / RBAC is a planned milestone; the MVP assumes a trusted
  steward and records every action in an append-only audit log.

## Reference demo

`scripts/seed.py` loads a 108-record master spanning 18 CPSEs across all five
sectors, runs matching, and plays a set of steward decisions — yielding published
National Material Codes, a rejected near-miss, and a live pending queue. See
[`DEMO.md`](DEMO.md).
