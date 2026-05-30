from __future__ import annotations

from datetime import date

from dailystock.config import load_settings
from dailystock.models.screening import PipelineRequest
from dailystock.pipeline import DailyStockPipeline


def test_pipeline_runs_full_sample_funnel(tmp_path) -> None:
    settings = load_settings()
    settings.app.output_dir = str(tmp_path)
    request = PipelineRequest(as_of=date(2026, 5, 29), markets=["CN", "HK"], dry_run=True)

    result = DailyStockPipeline(settings=settings).run(request)

    assert {candidate["code"] for candidate in result.final_candidates} == {"CN000001", "HK00001"}
    assert [(step.name, step.input_count, step.output_count) for step in result.steps] == [
        ("step1_fetch_meta", 0, 11),
        ("step2_hard_filters", 11, 4),
        ("step3_financial_quality", 4, 3),
        ("step4_valuation", 3, 2),
        ("step5_futu_executor", 2, 2),
    ]
    assert result.execution_plan
    assert all(plan["dry_run"] for plan in result.execution_plan)
    assert any(path.endswith("dashboard.md") for path in result.artifacts)
    assert any(path.endswith("result.json") for path in result.artifacts)

