"""Tests for signate-wandb-sync score command."""

import pytest
from click.testing import CliRunner

from signate_wandb_sync.commands.score import _parse_run_path, score


class TestParseRunPath:
    def test_full_url(self):
        url = "https://wandb.ai/entity/project/runs/abc123"
        assert _parse_run_path(url) == "entity/project/abc123"

    def test_full_url_with_query(self):
        url = "https://wandb.ai/entity/project/runs/abc123?foo=bar"
        assert _parse_run_path(url) == "entity/project/abc123"

    def test_full_url_other_host(self):
        # The sign-in / app domain can change (W&B moved hosts on 2026-09-30);
        # a run URL copied from any host must still parse.
        url = "https://wandb.example.com/entity/project/runs/abc123"
        assert _parse_run_path(url) == "entity/project/abc123"

    def test_path_format(self):
        assert _parse_run_path("entity/project/abc123") == "entity/project/abc123"

    def test_bare_id(self):
        assert _parse_run_path("abc123") == "abc123"


class TestScoreCommand:
    def test_no_metrics_fails(self):
        runner = CliRunner()
        result = runner.invoke(score, ["entity/project/abc123"])
        assert result.exit_code == 1
        assert "provide at least one" in result.output

    def test_bare_id_without_project_fails(self):
        runner = CliRunner()
        result = runner.invoke(score, ["abc123", "--score", "0.85"])
        assert result.exit_code == 1
        assert "bare ID" in result.output

    def test_invalid_metric_format_fails(self):
        runner = CliRunner()
        result = runner.invoke(score, ["entity/project/abc123", "-m", "invalid"])
        assert result.exit_code == 1
        assert "KEY=VALUE" in result.output
