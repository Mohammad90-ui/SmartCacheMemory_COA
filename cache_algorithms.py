"""
Cache Replacement Policy Simulators
====================================
Pure simulation logic for FIFO and LRU cache replacement policies.
Completely independent of the UI layer.
"""

from collections import OrderedDict
from typing import List, Optional


class SimulationStep:
    """Represents the result of processing a single memory reference."""

    __slots__ = ("address", "is_hit", "cache_state", "evicted_block")

    def __init__(
        self,
        address: int,
        is_hit: bool,
        cache_state: list,
        evicted_block: Optional[int] = None,
    ):
        self.address = address
        self.is_hit = is_hit
        self.cache_state = cache_state          # snapshot *after* this request
        self.evicted_block = evicted_block       # None when no eviction occurred

    def to_dict(self) -> dict:
        return {
            "address": self.address,
            "is_hit": self.is_hit,
            "cache_state": list(self.cache_state),
            "evicted_block": self.evicted_block,
        }


# ──────────────────────────────────────────────
#  FIFO Simulation
# ──────────────────────────────────────────────

def simulate_fifo(sequence: List[int], capacity: int) -> List[SimulationStep]:
    """
    Simulate a FIFO (First-In, First-Out) cache.

    On a miss with a full cache the **oldest-inserted** block is evicted.
    A hit does **not** change the block's insertion position.

    Parameters
    ----------
    sequence : list[int]
        Ordered memory-reference addresses.
    capacity : int
        Maximum number of blocks the cache can hold (≥ 1).

    Returns
    -------
    list[SimulationStep]
        One entry per reference in *sequence*.
    """
    cache: list = []          # maintains insertion order
    steps: List[SimulationStep] = []

    for addr in sequence:
        evicted: Optional[int] = None

        if addr in cache:
            # HIT – no change to cache order
            is_hit = True
        else:
            # MISS
            is_hit = False
            if len(cache) >= capacity:
                evicted = cache.pop(0)       # remove oldest (front)
            cache.append(addr)

        steps.append(
            SimulationStep(
                address=addr,
                is_hit=is_hit,
                cache_state=list(cache),     # snapshot copy
                evicted_block=evicted,
            )
        )

    return steps


# ──────────────────────────────────────────────
#  LRU Simulation
# ──────────────────────────────────────────────

def simulate_lru(sequence: List[int], capacity: int) -> List[SimulationStep]:
    """
    Simulate an LRU (Least Recently Used) cache.

    On a miss with a full cache the **least-recently-accessed** block is
    evicted.  A hit moves the accessed block to the *most-recent* position.

    Parameters
    ----------
    sequence : list[int]
        Ordered memory-reference addresses.
    capacity : int
        Maximum number of blocks the cache can hold (≥ 1).

    Returns
    -------
    list[SimulationStep]
        One entry per reference in *sequence*.
    """
    cache: OrderedDict = OrderedDict()   # key → True; order = recency
    steps: List[SimulationStep] = []

    for addr in sequence:
        evicted: Optional[int] = None

        if addr in cache:
            # HIT – move to most-recent end
            is_hit = True
            cache.move_to_end(addr)
        else:
            # MISS
            is_hit = False
            if len(cache) >= capacity:
                evicted, _ = cache.popitem(last=False)   # remove LRU (front)
            cache[addr] = True

        steps.append(
            SimulationStep(
                address=addr,
                is_hit=is_hit,
                cache_state=list(cache.keys()),   # snapshot copy
                evicted_block=evicted,
            )
        )

    return steps
