# Time Complexity README (organized by algorithms and data structures)

Purpose

- Help you quickly derive time complexity without memorizing every case.
- Emphasize dominant terms, model assumptions, and input parameters.
- Provide a checklist and patterns by algorithm family and data structure.

Core principles

- Focus on growth: Keep the highest-order term; drop constants and lower-order terms.
- Define input size precisely: n for elements/vertices, m for edges, L for string length, d for dimensions, U for value
  range, Σ for alphabet size.
- Worst, average, expected: Specify which you mean; randomness or input distribution can change bounds.
- Model matters: Random access vs sequential, integer vs comparison-based, RAM vs cache/I/O models.
- Tight bounds when possible: Prefer Θ(·); otherwise provide O(·) with a note on typical/worst behavior.
- Cost per operation × count: Break algorithm into operations with known costs and sum them.

Cost model and parameters

- Word-RAM: O(1) arithmetic on word-sized integers (often 64-bit).
- n: number of items, vertices, or length of sequence.
- m: number of edges/relations.
- L: total length across inputs (e.g., sum of string lengths).
- U/k/Σ: ranges or alphabet size for integer/string algorithms.
- h: recursion/structure height; w: frontier width; P: number of processors/threads.

By algorithms

1) Single-pass scans and searches

- Linear scan:
    - Time: Θ(n).
- Binary search (sorted array):
    - Time: Θ(log n).
- Two-pointer/sliding window:
    - Time: Typically Θ(n) if each index advances monotonically.
- Hash-based membership checks across a stream:
    - Time: Expected Θ(1) per check/insert; Θ(n) for n operations. Worst-case Θ(n) per op if adversarial hashing.

2) Divide and conquer and sorting

- Mergesort:
    - Time: Θ(n log n) comparisons and moves.
- Quicksort:
    - Expected: Θ(n log n). Worst-case: Θ(n^2) without pivot protections; mitigated by randomization/median-of-three.
- Heapsort:
    - Time: Θ(n log n).
- Build-heap:
    - Time: Θ(n) using bottom-up heapify.
- Counting sort (integers in small range):
    - Time: Θ(n + k) where k is range size.
- Radix sort (integers/strings):
    - Time: Θ(d·(n + k)) where d is number of digits/passes, k is bucket range per pass.
- Lower bound (comparison sorting):
    - Any comparison-based sort requires Ω(n log n) comparisons in worst/average case.

3) Selection and order statistics

- Quickselect (k-th element):
    - Expected: Θ(n). Worst-case: Θ(n^2).
- Median-of-medians:
    - Time: Θ(n) worst-case, larger constant than randomized quickselect.

4) Recursion, backtracking, exhaustive search

- DFS/backtracking on solution space with branching factor b and depth d:
    - Time: Θ(b^d) in the worst case; add pruning heuristics to reduce effective branching.
- Balanced binary recursion on halves (e.g., divide-and-conquer without heavy combine):
    - Master theorem T(n) = 2T(n/2) + f(n):
        - If f(n) = Θ(n): Θ(n log n).
        - If f(n) = Θ(n^c), c < 1: Θ(n).
        - Use the appropriate case based on f(n).

5) Dynamic programming

- Full table DP:
    - Time ≈ number of table cells × per-cell transition cost.
    - Typical: Θ(nm) for 2D tables with O(1) transitions.
- Sequence alignment / edit distance:
    - Θ(nm).
- Knapsack (0/1):
    - Θ(nW) where W is capacity; pseudo-polynomial.
- LIS (patience sorting method):
    - Θ(n log n).

6) Graph algorithms

- Graph traversal (BFS/DFS):
    - Adjacency list: Θ(n + m).
    - Adjacency matrix: Θ(n^2).
- Topological sort:
    - Θ(n + m).
- Connected components:
    - Θ(n + m).
- Dijkstra (non-negative weights):
    - Using binary heap: Θ((n + m) log n).
    - Using Fibonacci heap: Θ(m + n log n).
- Bellman–Ford (negative weights allowed):
    - Θ(n·m).
- All-pairs shortest paths:
    - Floyd–Warshall: Θ(n^3).
    - Repeated Dijkstra (sparse): Θ(n·(m log n)).
- Minimum spanning tree:
    - Kruskal: Θ(m log n) (sorting edges dominates).
    - Prim: Θ(m log n) with binary heap; Θ(m + n log n) with Fibonacci heap.
- Union–Find across q operations:
    - Amortized: Θ(q α(n)) where α is inverse Ackermann (practically constant).

7) String and pattern algorithms

- Exact match:
    - KMP: Θ(n + m) (text length n, pattern length m).
    - Boyer–Moore / Horspool: Sublinear average; Θ(nm) worst-case.
- Tries:
    - Insert/search: Θ(L) where L is key length.
- Suffix array:
    - Build: Θ(n log n) typical; LCP queries: Θ(1) after RMQ preprocessing.
- Suffix automaton:
    - Build: Θ(n).
- Z-function, prefix-function:
    - Θ(n).

8) Numerical, matrix, and geometry

- Matrix multiply:
    - Naive: Θ(n^3). Strassen: ~Θ(n^2.81). Practical crossover varies.
- Graphical convex hull (2D):
    - Θ(n log n) (sorting) or Θ(n) if input is pre-sorted by x.
- Line sweep algorithms (intervals/segments):
    - Θ((n + k) log n) where k is number of events/intersections processed.

9) Streaming and external memory

- Single-pass streaming with O(1)/polylog space:
    - Aim for Θ(n) time; per-item cost O(1) or O(log n).
- External merge sort (I/O model):
    - Time dominated by I/O passes; CPU work ~ Θ(n log n). I/O complexity depends on block size and memory (not detailed
      here).

10) Probabilistic and randomized algorithms

- Randomized quicksort/quickselect:
    - Expected bounds as noted above; high-probability guarantees with median-of-three/random pivot.
- Sketches (Count-Min, HyperLogLog, Bloom filter operations):
    - Per update/query: O(1) or O(d) constant passes; total Θ(n).

11) Parallel and concurrent algorithms

- Work–span model:
    - T_P ≤ O(work/P + span), where work is total operations (sequential time) and span is critical-path length.
- Parallel map/reduce:
    - Map: Θ(n/P + overhead). Reduce (tree): span Θ(log n).
- Parallel BFS (level-synchronous):
    - Work Θ(n + m); span ≈ number of levels.

By data structures

- Arrays (static)
    - Random access: Θ(1).
    - Insert/delete at end: Θ(1).
    - Insert/delete in middle: Θ(n) due to shifting.
    - Search (unsorted): Θ(n). Search (sorted via binary search): Θ(log n).

- Dynamic arrays (vectors)
    - Append: Amortized Θ(1); occasional resize Θ(n).
    - Insert/delete at end: Amortized Θ(1). At arbitrary index: Θ(n).
    - Access by index: Θ(1).

- Linked lists (singly/doubly)
    - Insert/delete with pointer to node: Θ(1).
    - Search or kth access: Θ(n).
    - Merge two sorted lists: Θ(n).

- Hash tables (maps/sets)
    - Expected: Insert/find/delete Θ(1); worst-case Θ(n).
    - Iteration over all items: Θ(n).
    - Rehashing events: O(n) but amortized O(1) per insert.

- Binary search trees
    - Unbalanced BST: Operations Θ(h), worst-case Θ(n).
    - Balanced BSTs (AVL, Red–Black):
        - Search/insert/delete: Θ(log n).
        - Inorder traversal: Θ(n).

- Heaps (binary, d-ary)
    - Insert: Θ(log n).
    - Find-min/max: Θ(1).
    - Extract-min/max: Θ(log n).
    - Decrease-key: Θ(log n) for binary heap; O(1) amortized in Fibonacci heap.
    - Build-heap: Θ(n).

- Union–Find (Disjoint Set Union)
    - Make-set: Θ(1).
    - Find/union with path compression + union by rank:
        - Amortized Θ(α(n)) per op; practically constant.

- Tries and prefix trees
    - Insert/search: Θ(L) with L key length.
    - Memory-compressed variants (radix tree): similar time with better constants.

- Segment trees and Fenwick (BIT)
    - Point update and range query:
        - Segment tree: Θ(log n) per op.
        - Fenwick tree: Θ(log n) per op.
    - Build:
        - Segment tree: Θ(n).

- Graph representations
    - Adjacency list:
        - Iterate neighbors: Θ(degree).
        - Traversal: Θ(n + m).
    - Adjacency matrix:
        - Check edge: Θ(1).
        - Traversal: Θ(n^2).

- Bitsets and boolean arrays
    - Set/test/clear: Θ(1).
    - Bulk operations (AND/OR/XOR):
        - Θ(n / word_size) using word-level operations; often vectorizable.

Amortized analysis patterns

- Dynamic array growth by doubling: Append is amortized Θ(1).
- Hash table with load factor control: Insert amortized Θ(1), occasional Θ(n) rehash.
- Union–Find with path compression: Near-constant amortized operations.
- Incremental algorithms with rare rebuilds (e.g., maintaining buckets): Distribute rebuild cost over many cheap ops.

Derivation checklist

1) Define the input parameters

- Which variables grow? n, m, L, U, Σ, d, w, h.

2) Count dominant loops/recursions

- How many iterations/calls? What is the per-iteration cost?

3) Use known bounds

- Sorting lower bounds, traversal Θ(n + m), heap ops Θ(log n), hash ops expected Θ(1).

4) Consider best/average/worst

- State clearly which case you analyze and whether randomness is used.

5) Validate with structure properties

- Tree height, frontier size, degree distribution, partition balance.

6) Account for amortization

- Are there occasional expensive operations masked by many cheap ones?

7) Mind the model

- Comparison vs integer sorting, adjacency list vs matrix, cache/I/O effects if relevant.

Common pitfalls

- Ignoring input representation differences (matrix vs list).
- Quoting average-case hash table times without noting adversarial worst-case.
- Assuming “two nested loops → Θ(n^2)” without checking shrinking ranges or amortization.
- Forgetting sort cost when an algorithm starts by sorting.
- Treating recursion as Θ(depth) without multiplying by per-level work or branching factor.
- Double-counting work that can be charged once (amortized analysis).

Quick references (typical)

- Linear scan: Θ(n).
- Binary search: Θ(log n).
- BFS/DFS: Θ(n + m).
- Dijkstra (binary heap): Θ((n + m) log n).
- Kruskal MST: Θ(m log n).
- Topological sort: Θ(n + m).
- Mergesort/Heapsort: Θ(n log n).
- Quicksort: Expected Θ(n log n), worst Θ(n^2).
- Counting/Radix sort: Θ(n + k)/Θ(d·(n + k)).
- KMP: Θ(n + m).
- Build-heap: Θ(n).
- Union–Find ops: Amortized Θ(α(n)).
- Segment tree ops: Θ(log n).
- LIS (patience): Θ(n log n).

Practice guide

- For each algorithm, write:
    - Input parameters and representation.
    - Main loops/recursions and per-iteration cost.
    - Case analysis (best/average/worst, expected).
    - Final bound with one-sentence justification.
- Compare two approaches:
    - Version A sorts first; Version B uses a heap or hash. Derive and contrast Θ(n log n) vs Θ(n) or Θ(n log k).
- Validate with small empirical checks:
    - Plot n vs runtime; confirm slope matches predicted n, n log n, or n^2 growth.

Glossary

- Big-O: Upper bound up to constants.
- Big-Ω: Lower bound up to constants.
- Big-Θ: Tight bound (both upper and lower).
- Amortized time: Average per operation over a sequence, smoothing costly spikes.
- Expected time: Average over algorithm’s random choices or input distribution.
- Work/span: Total operations vs critical path in parallel algorithms.

How to use this README

- Before coding: choose data structures that match desired per-op time (hash vs tree, heap vs sort).
- During design: identify dominant loops and whether preprocessing (sorting, indexing) amortizes over many queries.
- After coding: check for hidden sorts, repeated scans, or avoidable quadratic patterns; consider amortization and
  randomized pivots/ordering when safe.