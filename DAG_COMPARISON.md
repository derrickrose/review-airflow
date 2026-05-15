# RTS24 DAG Variants Comparison

## Overview

Three DAG variants have been created for the RTS24 Regulatory Reporting pipeline:

1. **`dagggbbb.py`** - Original (Full pipeline with loads)
2. **`dagggbbb1.py`** - ShortCircuit Approach (Recommended ⭐)
3. **`dagggbbb2.py`** - Mode-based Approach

---

## DAG 1: `dagggbbb1.py` - ShortCircuit Approach ⭐ RECOMMENDED

**DAG ID:** `{ENV}_LCRR_D004_RTS24_CLASSIC_1`

### How It Works:
- Uses `@task.short_circuit` decorators to conditionally skip task branches
- All tasks exist in DAG structure but are skipped based on `mode` parameter
- **Airflow-native approach** - respects Airflow best practices
- Tasks show as "SKIPPED" in UI when not executed

### Execution Modes:

#### 1. Full Pipeline (Default)
```json
{
  "trading_date": "2026-05-14"
}
```
**OR**
```json
{
  "trading_date": "2026-05-14",
  "mode": "full"
}
```
**Runs:** Extract → Loads (all segments) → Generate (all segments) → On-demand

---

#### 2. Loads Only
```json
{
  "trading_date": "2026-05-14",
  "mode": "loads_only"
}
```
**Runs:** Extract → Loads (all segments)
**Skips:** Generate, On-demand

**Use case:** Re-load data for specific date without regenerating files

---

#### 3. Generate Only
```json
{
  "trading_date": "2026-05-14",
  "mode": "generate_only"
}
```
**Runs:** Extract → Generate (all segments)
**Skips:** Loads, On-demand

**Use case:** Regenerate RTS24 files from already-loaded data

---

#### 4. On-demand Only
```json
{
  "mode": "ondemand_only"
}
```
**Runs:** On-demand workflow (query → process → generate → update → verify)
**Skips:** Extract, Loads, Generate

**Use case:** Process pending on-demand requests from database

---

### Segment Filtering (NEW ✨)

You can now filter which segments to run using the `segments` parameter:

#### Run specific segments only:
```json
{
  "trading_date": "2026-05-14",
  "mode": "full",
  "segments": ["EQU", "BLK"]
}
```
**Runs:** Extract → Loads (EQU, BLK only) → Generate (EQU, BLK only) → On-demand

#### Load only specific segments:
```json
{
  "trading_date": "2026-05-14",
  "mode": "loads_only",
  "segments": ["ETF", "WAR"]
}
```
**Runs:** Extract → Loads (ETF, WAR only)
**Skips:** Generate, On-demand, other segments

#### Generate only specific segments:
```json
{
  "trading_date": "2026-05-14",
  "mode": "generate_only",
  "segments": ["FXI"]
}
```
**Runs:** Extract → Generate (FXI only)
**Skips:** Loads, On-demand, other segments

**Valid segments:** `EQU`, `ETF`, `FXI`, `WAR`, `BLK`

**Default:** If `segments` is not specified, all 5 segments run

---

### Task Flow:

```
trading_date (always runs)
    ├─> check_loads (ShortCircuit) ─> filter_load_segments (Branch) ─> load_segment_[EQU|ETF|FXI|WAR|BLK] (30 tasks total)
    ├─> check_generate (ShortCircuit) ─> filter_generation_segments (Branch) ─> generate_[EQU|ETF|FXI|WAR|BLK]_files (5 tasks)
    └─> check_ondemand (ShortCircuit) ─> query_on_demand ─> process ─> generate ─> update ─> verify
```

### Advantages:
- ✅ **Airflow-native** - Uses standard ShortCircuitOperator and BranchOperator patterns
- ✅ **Clean UI** - Tasks show as "skipped" not "missing"
- ✅ **Clear dependencies** - Task graph visible in UI
- ✅ **Flexible** - Easy to add new modes
- ✅ **Segment filtering** - Run specific segments (EQU, BLK, etc.)
- ✅ **trigger_rule='none_failed'** on critical tasks ensures proper execution

---

## DAG 2: `dagggbbb2.py` - Mode-based Approach

**DAG ID:** `{ENV}_LCRR_D004_RTS24_CLASSIC_2`

### How It Works:
- Checks `mode` parameter at runtime
- All tasks are created and connected
- Tasks check mode internally to decide execution
- **Less Airflow-native** but simpler dependency structure

### Execution Modes:
Same as DAG 1 (full, loads_only, generate_only, ondemand_only)

### Task Flow:
```
mode = get_execution_mode()
trading_date → all_load_tasks → generation_tasks
                      └─> query_on_demand → process → generate → update → verify
```

### Advantages:
- ✅ **Simple dependencies** - Linear flow
- ✅ **No ShortCircuit complexity** - Mode checked internally
- ✅ **Easier to understand** for non-Airflow experts

### Disadvantages:
- ❌ **Not Airflow-native** - Tasks run but exit early
- ❌ **Less clear in UI** - All tasks show as "success" even if skipped internally
- ❌ **More complex task logic** - Each task must check mode

---

## Original DAG: `dagggbbb.py`

**DAG ID:** `{ENV}_LCRR_D004_RTS24_CLASSIC`

### How It Works:
- Fixed structure: always runs all tasks
- No parameterization
- On-demand workflow integrated at the end

### Task Flow:
```
trading_date → all_load_tasks → generation_tasks → query_on_demand → process → generate → update → verify
```

**Use case:** Scheduled production runs with full pipeline

---

## Comparison Summary

| Feature | dagggbbb.py (Original) | dagggbbb1.py (ShortCircuit) ⭐ | dagggbbb2.py (Mode-based) |
|---------|------------------------|-------------------------------|---------------------------|
| **Parameterized** | ❌ No | ✅ Yes | ✅ Yes |
| **Skip loads** | ❌ No | ✅ Yes | ✅ Yes |
| **Skip generate** | ❌ No | ✅ Yes | ✅ Yes |
| **On-demand only** | ❌ No | ✅ Yes | ✅ Yes |
| **Segment filtering** | ❌ No | ✅ Yes | ❌ No |
| **Airflow-native** | ✅ Yes | ✅ Yes (ShortCircuit + Branch) | ⚠️ Partial |
| **UI Clarity** | ✅ Clear | ✅ Clear (shows skipped) | ⚠️ Less clear |
| **Dependency Logic** | ✅ Simple | ⚠️ Complex (gates) | ✅ Simple |
| **Best Practice** | ✅ Yes | ✅ Yes | ⚠️ Acceptable |
| **Production Ready** | ✅ Yes | ✅ Yes | ✅ Yes |

---

## Recommendation

**Use `dagggbbb1.py` (ShortCircuit Approach)** for:
- ✅ Production deployments
- ✅ Maximum flexibility
- ✅ Airflow best practices
- ✅ Clear UI representation

**Use `dagggbbb2.py` (Mode-based Approach)** for:
- Simpler mental model
- Teams less familiar with Airflow patterns
- When UI clarity is less important

**Use `dagggbbb.py` (Original)** for:
- Scheduled production runs
- When no parameterization is needed
- Simple, predictable pipeline

---

## Testing Examples

### Test DAG 1 (ShortCircuit):
```bash
# Full run (all segments)
airflow dags trigger DEV_LCRR_D004_RTS24_CLASSIC_1 \
  --conf '{"trading_date":"2026-05-14","mode":"full"}'

# Full run (specific segments only)
airflow dags trigger DEV_LCRR_D004_RTS24_CLASSIC_1 \
  --conf '{"trading_date":"2026-05-14","mode":"full","segments":["EQU","BLK"]}'

# Loads only
airflow dags trigger DEV_LCRR_D004_RTS24_CLASSIC_1 \
  --conf '{"trading_date":"2026-05-14","mode":"loads_only"}'

# Loads only (specific segments)
airflow dags trigger DEV_LCRR_D004_RTS24_CLASSIC_1 \
  --conf '{"trading_date":"2026-05-14","mode":"loads_only","segments":["ETF","WAR"]}'

# Generate only
airflow dags trigger DEV_LCRR_D004_RTS24_CLASSIC_1 \
  --conf '{"trading_date":"2026-05-14","mode":"generate_only"}'

# Generate only (specific segments)
airflow dags trigger DEV_LCRR_D004_RTS24_CLASSIC_1 \
  --conf '{"trading_date":"2026-05-14","mode":"generate_only","segments":["FXI"]}'

# On-demand only
airflow dags trigger DEV_LCRR_D004_RTS24_CLASSIC_1 \
  --conf '{"mode":"ondemand_only"}'
```

### Test DAG 2 (Mode-based):
```bash
# Same commands, just change DAG ID to DEV_LCRR_D004_RTS24_CLASSIC_2
```

---

## Migration Path

1. **Current:** Use `dagggbbb.py` for scheduled runs
2. **Testing:** Test `dagggbbb1.py` with different modes in dev environment
3. **Production:** Migrate to `dagggbbb1.py` when ready
4. **Retire:** Archive `dagggbbb.py` and `dagggbbb2.py` after validation

---

## Notes

- All DAGs share the same code for tasks (process, update, verify)
- Only DAG structure and flow control differs
- No changes needed to EMR jobs or Athena queries
- `dagggbbb1.py` is recommended for production use
