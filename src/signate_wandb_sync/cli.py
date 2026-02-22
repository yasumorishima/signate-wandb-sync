"""CLI entry point for signate-wandb-sync."""

import click

from signate_wandb_sync import __version__
from signate_wandb_sync.commands.score import score


@click.group()
@click.version_option(version=__version__)
def main():
    """Record SIGNATE competition scores to W&B.

    Typical usage:
        signate-wandb-sync score https://wandb.ai/me/my-proj/runs/abc123 --score 0.85 --rank 3
    """
    pass


main.add_command(score)
