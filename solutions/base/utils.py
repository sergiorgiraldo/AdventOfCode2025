from queue import SimpleQueue
from typing import Callable, Dict, Iterable, TypeVar

V = TypeVar("V")


def shortest_paths(
    s: V,
    get_neighbors: Callable[[V], Iterable[V]],
    dist_max: int = -1,
    stop_condition: Callable[[Dict[V, int]], bool] = lambda _: False,
) -> Dict[V, int]:
    """
    Compute length of shortest path from source `s` to every other node visitable from `s`.
    If `t` is provided, stop after reaching node `t`.
    If `dist_max` is provided, only find paths of length <= dist_max.
    """
    q: SimpleQueue[V] = SimpleQueue()
    q.put(s)
    dists = {s: 0}
    while not q.empty():
        v = q.get()
        for w in get_neighbors(v):
            if w not in dists:
                dists[w] = dists[v] + 1
                if stop_condition(dists):
                    return dists
                if dist_max < 0 or dists[w] < dist_max:
                    q.put(w)
    return dists


def shortest_path(s: V, t: V, get_neighbors: Callable[[V], Iterable[V]]) -> int:
    """
    Compute length of shortest path from source `s` to target `t`.
    """
    dists = shortest_paths(s, get_neighbors, stop_condition=lambda dists: t in dists)
    if t in dists:
        return dists[t]

    raise RuntimeError(f"{t} is not reachable from {s}")
