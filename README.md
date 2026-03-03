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

### score — Record SIGNATE score to W&B

```bash
# Full W&B URL (recommended — copy from Actions log)
signate-wandb-sync score https://wandb.ai/your-entity/your-project/runs/abc123 \
    --score 0.85 --rank 3

# With additional metrics
signate-wandb-sync score https://wandb.ai/your-entity/your-project/runs/abc123 \
    --score 0.85 --rank 3 \
    -m fbeta=0.85 -m recall=0.91

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

### Options

| Option | Description |
|---|---|
| `--score` | SIGNATE submission score (float) |
| `--rank` | Leaderboard rank (int) |
| `--metric KEY=VALUE` | Additional metric (repeatable) |
| `--project entity/project` | W&B project path (for bare run IDs) |

<!-- commands:end -->

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
