# signate-wandb-sync

A CLI tool to record SIGNATE competition scores to [Weights & Biases (W&B)](https://wandb.ai/).

## Installation

```bash
pip install signate-wandb-sync
```

## Usage

### score — Log SIGNATE scores to W&B

After submitting to SIGNATE and getting your score, record it to a W&B run:

```bash
# Full W&B URL
signate-wandb-sync score https://wandb.ai/your-entity/your-project/runs/abc123 --score 0.85 --rank 3

# With additional metrics
signate-wandb-sync score https://wandb.ai/your-entity/your-project/runs/abc123 \
    --score 0.85 --rank 3 \
    -m fbeta=0.85 -m recall=0.91

# Using bare run ID (requires --project)
signate-wandb-sync score abc123 --project your-entity/your-project --score 0.85
```

### Options

| Option | Description |
|---|---|
| `--score` | SIGNATE submission score (float) |
| `--rank` | Leaderboard rank (int) |
| `--metric KEY=VALUE` | Additional metric (repeatable) |
| `--project entity/project` | W&B project path (for bare run IDs) |

## Windows

```bash
PYTHONUTF8=1 signate-wandb-sync score <run_id> --score 0.85
```

## Authentication

W&B: run `wandb login` beforehand (or set `WANDB_API_KEY` environment variable).

## Requirements

- Python 3.9+
- [wandb](https://pypi.org/project/wandb/)

## License

MIT
