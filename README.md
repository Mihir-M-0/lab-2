# Lab: Python Exercises & Version Control (TIER Protocol)

*Course:* Intro to Data & Computing  
*Session date:* **July 2, 2025 – Afternoon (4 h)**  
*Environment:* `lab_2` (conda/mamba)

---

## 1  Learning objectives

1. Write Python functions using loops, conditionals, and data structures.
2. Add unit tests with **pytest** to verify correctness.
3. Track changes with **Git** and publish to **GitHub**.
4. Produce a fully reproducible research bundle following the [TIER Protocol 4.0](https://www.projecttier.org/tier-protocol/protocol-4-0/).

---

## 2  Repository layout

| Path | Purpose |
|------|---------|
| `assignment.py` | **Your code** — implement 4 statistics utilities. |
| `test_assignment.py` | Autograder & local tests (do **not** edit). |
| `requirements.txt` | Package list used by GitHub Actions & mamba env. |
| `.github/workflows/autograding.yml` | CI workflow that runs tests on every push. |
| `environment.yml` | *Optional:* exact env export for TIER compliance. |

---

## 3  Setup ( one‑time)

Make sure you have accepted the assignemnt and you have cloned the repo locally and you can push it back to github to turn it in. 

Open a terminal and run:

### 3.1 Create isolated env
```bash
mamba create -n lab_2 python=3.11 -y
```

### 3.2 Activate it
```bash
mamba activate lab_2
```
### 3.3 Install required pkgs
```bash
mamba install --file requirements.txt -y
```
#### Why mamba? Faster dependency resolution and the environment.yml you export later will be portable across platforms.


## 4  Assignment tasks

All edits happen only in assignment.py.

| Function | Description |
|------|---------|
| `mean_loop(nums)` | Compute arithmetic mean **without** built‑in sum. |
| `median_loop(nums)` | Compute median (manual sort allowed). |
| `summary_stats(nums)` | Return {"mean": …, "median": …, "min": …, "max": …}. |
| `quantile(nums, q)` | Generic quantile (0 ≤ q ≤ 1) using linear interpolation. |


### 4.1  Implementation rules

- Accept any sequence‑like object (list, tuple, numpy.ndarray).
- Raise ValueError on empty input; raise TypeError if a non‑numeric value is found.
- Add Google‑style docstrings and type hints.

### 4.2  Run tests locally

```bash
pytest -q
```
A green check means all tests pass.

###  4.3  Commit & push
```bash
git add assignment.py
git commit -m "Finish mean_loop and median_loop"
git push origin main
```
GitHub Actions will run pytest automatically (see the Checks tab).
