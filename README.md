# signate-wandb-sync

A CLI tool to record SIGNATE competition scores to [Weights & Biases (W&B)](https://wandb.ai/).

Companion to [signate-deploy](https://github.com/yasumorishima/signate-deploy) — together they automate the full SIGNATE experiment tracking pipeline on GitHub Actions.

## Installation

```bash
pip install signate-wandb-sync
```

## Full Pipeline

```
[GitHub Actions]
  1. Download data via SIGNATE API  (signate-deploy)
  2. Run train.py — W&B run created, metrics logged
  3. Submit to SIGNATE              (signate-deploy)
  → W&B run URL printed to Actions log

[Local]
  4. Check score on SIGNATE leaderboard
  5. signate-wandb-sync score <W&B URL> --score 0.85 --rank 3
```

### Add W&B to train.py

```python
import wandb

run = wandb.init(project="my-signate-project", config={...})

# ... training and inference ...

wandb.log({"oof_score": oof_score})
print(f"W&B run URL: {run.url}")  # visible in Actions log
wandb.finish()
```

Set `WANDB_API_KEY` as a GitHub Secret:

```yaml
- name: Train and predict
  env:
    WANDB_API_KEY: ${{ secrets.WANDB_API_KEY }}
  run: python train.py
```

## Commands

<!-- commands:start -->

### `signate-wandb-sync score`

Log SIGNATE submission scores to a W&B run.

```
signate-wandb-sync score [RUN_ID] [OPTIONS]
```

| Option | Description |
|---|---|
| `--project`, `-p` | W&B project path (entity/project). Required if RUN_ID is a bare ID. |
| `--score` | SIGNATE submission score. |
| `--rank` | Leaderboard rank. |
| `--metric`, `-m` | Additional metric (can be repeated, e.g. -m f1=0.85 -m auc=0.92). |

<!-- commands:end -->

### Examples

```bash
# Full W&B URL (recommended - copy from the Actions log)
signate-wandb-sync score https://wandb.ai/your-entity/your-project/runs/abc123     --score 0.85 --rank 3

# With additional metrics
signate-wandb-sync score https://wandb.ai/your-entity/your-project/runs/abc123     --score 0.85 --rank 3     -m fbeta=0.85 -m recall=0.91

# Bare run ID (requires --project)
signate-wandb-sync score abc123 --project your-entity/your-project --score 0.85
```

Output:

```
Updated run: my-run-name (your-entity/your-project/abc123)
  submitted = True
  signate_score = 0.85
  signate_rank = 3
```

## Windows

```bash
PYTHONUTF8=1 signate-wandb-sync score <run_id> --score 0.85
```

## Authentication

W&B: run `wandb login` beforehand, or set `WANDB_API_KEY` environment variable.

## Requirements

- Python 3.9+
- [wandb](https://pypi.org/project/wandb/)

## Related

- [signate-deploy](https://github.com/yasumorishima/signate-deploy) — Automate SIGNATE submission via GitHub Actions

## License

MIT
