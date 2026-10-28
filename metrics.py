"""
Metrics Calculation Module
===========================
Derives summary statistics from simulation results.
"""

from typing import List, Dict, Any
from cache_algorithms import SimulationStep


def calculate_metrics(steps: List[SimulationStep]) -> Dict[str, Any]:
    """
    Calculate summary metrics from a list of simulation steps.

    Parameters
    ----------
    steps : list[SimulationStep]
        The per-request results produced by a simulation function.

    Returns
    -------
    dict
        Keys: total_requests, hits, misses, hit_ratio, miss_ratio
        Ratios are floats in [0, 1].  Multiply by 100 for percentages.
    """
    total = len(steps)
    hits = sum(1 for s in steps if s.is_hit)
    misses = total - hits

    hit_ratio = hits / total if total > 0 else 0.0
    miss_ratio = misses / total if total > 0 else 0.0

    return {
        "total_requests": total,
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio,
        "miss_ratio": miss_ratio,
    }


def format_ratio(ratio: float, decimals: int = 2) -> str:
    """Return a ratio as a percentage string, e.g. '42.86%'."""
    return f"{ratio * 100:.{decimals}f}%"
