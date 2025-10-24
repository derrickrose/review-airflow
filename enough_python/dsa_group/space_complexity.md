# Space Complexity README (organized by algorithms and data structures)

Purpose

- Help you reason about space complexity without memorization.
- Teach a checklist and patterns you can apply to most algorithms and data structures.
- Emphasize peak live memory (what’s simultaneously alive), auxiliary vs total space, and output sensitivity.

Core principles

- What are you measuring? Auxiliary space (excluding input) is the common focus. If the output must exist, count it when
  comparing algorithms that produce different-sized outputs.
- Peak, not cumulative: Count the maximum simultaneously live memory during execution.
- Simultaneity vs sequence: If big structures overlap in lifetime, add them; if they’re reused sequentially, take the
  max.
- Recursion consumes stack: Depth of recursion equals stack frames. Without tail-call optimization (e.g., in Python),
  tail recursion still uses stack.
- Frontier size matters: Traversals like BFS are bounded by the maximum frontier/width.
- Output dominates: Building an answer of size n uses O(n) space even if the algorithm is otherwise in-place.
- Language/runtime overhead: Object headers, temporaries, copying semantics, and retained references can inflate peak
  memory.

By algorithms

1) Single-pass scans and searches

- Linear scan/search:
    - Space: O(1) auxiliary if you only keep a few scalars (indices, best-so-far).
    - Pitfall: Accumulating results or caching seen elements increases space (e.g., O(k) for k results, O(n) for a set
      of seen items).
- Binary search on random-access array:
    - Space: O(1) iterative; O(log n) if implemented recursively (stack depth).
- Two-pointer/sliding window:
    - Space: O(1) if windows are tracked by indices.
    - With frequency maps/sets: typically O(Σ) where Σ is alphabet/domain size, up to O(n) in worst case.

2) Divide and conquer

- Mergesort:
    - Space: O(n) auxiliary for the merge buffer in the straightforward version.
    - Optimization: In-place variants are complex and often trade time for less space.
- Quicksort:
    - Space: O(log n) expected (partition recursion depth), O(n) worst-case without pivot protections.
    - Tail recursion elimination or iterative partitioning keeps it at O(log n) expected.
- Heapsort:
    - Space: O(1) auxiliary (in-place heap).

3) Recursion, backtracking, and search

- DFS on trees/graphs (recursive):
    - Space: O(h) for trees where h is height; O(n) worst-case for skewed trees or deep graphs.
- DFS (explicit stack):
    - Space: O(h) or O(n) in the same worst cases—recursion vs explicit stack are equivalent asymptotically.
- Backtracking (e.g., N-Queens, subset generation):
    - Space: O(depth + representation of partial solution). If enumerating all solutions, output dominates.
- Balanced divide-and-conquer (e.g., binary recursion on halves):
    - Stack depth: O(log n) if subproblems shrink by a constant factor.

4) Dynamic programming

- Full table DP:
    - Space: proportional to table size (e.g., O(nm) for two dimensions).
- Space-optimized DP:
    - Often reducible to O(min dimension) by keeping only current/previous rows or columns.
- Memoization:
    - Space: O(number of distinct subproblems) for the cache.
- Path reconstruction:
    - Storing parents/pointers increases space; can sometimes be reconstructed by replaying computation at a time cost.

5) Graph algorithms

- BFS:
    - Space: Θ(w) where w is the maximum frontier size; worst-case Θ(n) for dense layers.
    - Also accounts for visited set: O(n).
- Dijkstra/Prim:
    - Space: O(n + m) for visited/parent arrays plus O(n) for the priority queue; adjacency representation dominates.
- Union-Find (Disjoint Set Union):
    - Space: O(n) for parent/rank arrays; near-constant extra for path compression bookkeeping.

6) String and sequence algorithms

- Streaming processing (e.g., single pass tokenization/counting):
    - Space: O(Σ) for small alphabets, otherwise O(n) if distinct tokens accumulate.
- Pattern matching:
    - KMP/Boyer-Moore preprocessing tables: O(m) for pattern length m.
- Concatenation/copying:
    - Beware transient peaks when creating new strings/arrays; copying can double live size briefly.

7) Probabilistic and sketching algorithms

- Bloom filter:
    - Space: O(k) bits per element with tunable false-positive rate; sublinear vs set of elements.
- HyperLogLog:
    - Space: O(1) relative to stream size (thousands of bytes) for cardinality estimates.
- Count-Min Sketch:
    - Space: O(w·d) configurable; trades accuracy for compactness.

8) Streaming and external memory

- One-pass streaming:
    - Goal is sublinear space, ideally O(1) or polylog(n); sketches and reservoir sampling achieve this.
- External memory models:
    - Analyze passes over data and block I/O; in-RAM state typically O(B) where B is block/buffer size.

9) Parallel and concurrent algorithms

- Per-thread stacks/queues:
    - Space adds across workers; a work-stealing scheduler’s deques plus task descriptors can dominate peaks.
- Batches and buffers:
    - Pipelines may accumulate stage buffers; peak equals sum of simultaneously full buffers.

By data structures

- Arrays/vectors
    - Space: O(n) for n elements; contiguous.
    - Growth: Dynamic arrays over-allocate; peak during resize can be ~2n.
    - Slices/views: Can be O(1) if view semantics; otherwise copying creates extra O(k) space.

- Linked lists
    - Space: O(n) nodes with pointer overhead per node.
    - Pros: Stable insertion/deletion without shifting. Cons: Overhead and cache misses.

- Hash tables (maps/sets)
    - Space: O(n) with load factor slack (over-allocation).
    - Keys/values stored by reference or inline depending on language/runtime.
    - Memory spikes during rehash/resize.

- Trees (binary, balanced)
    - Space: O(n) nodes; height h controls recursion/stack space O(h).
    - Balanced trees: h = O(log n); skewed trees: h = O(n).

- Heaps (binary heap, d-ary heap)
    - Space: O(n).
    - Priority queue operations do not add asymptotic space; temporary swaps are O(1).

- Graph representations
    - Adjacency list: O(n + m) where n=vertices, m=edges.
    - Adjacency matrix: O(n^2), beneficial for very dense graphs or O(1) adjacency queries.

- Queues/deques/stacks
    - Space: O(k) where k is the number of items enqueued/pushed.
    - In BFS, queue size ≈ frontier width; in DFS, stack size ≈ depth.

- Bitsets and compressed structures
    - Bitset: O(n) bits vs O(n) words improves constants drastically.
    - Run-length, CSR/COO for sparse matrices reduce space to O(nz) where nz is nonzero count.

- Persistent/functional structures
    - Space: Structural sharing reduces incremental costs, but multiple live versions can raise peak memory.
    - Updates typically O(log n) extra due to path copying.

- Probabilistic structures
    - Bloom, Cuckoo filters, sketches: sublinear or near-constant space with tunable error rates.

Language/runtime considerations

- Object overhead:
    - High-level languages often store references and object headers; per-element overhead can be substantial.
- Temporaries and copies:
    - Expression evaluation can create transient objects that raise peaks; favor in-place updates and
      generators/iterators when possible.
- Retained references:
    - Slices, closures, or caches can keep large objects alive longer than intended.
- Garbage collection:
    - Deallocation is not always immediate; measure peak with realistic workloads.

Derivation checklist

1) What memory scales with input?

- Identify arrays, maps, sets, queues, recursion depth, and caches that can grow with n.

2) What is simultaneously alive at peak?

- Draw a quick timeline of phases; sum overlapping structures, max across sequential ones.

3) What is the recursion/iteration frontier?

- Depth for DFS/backtracking; width for BFS/level-order.

4) Are you counting auxiliary space or total space?

- Include output if comparing algorithms whose outputs differ in size or if output dominates memory.

5) Any language/runtime-induced peaks?

- Copies during concatenation, rehashing, resizing, or hidden temporaries.

Common pitfalls

- Counting freed memory or ignoring transient peaks during copying, rehashing, or concatenation.
- Assuming “no extra data structure” implies O(1) while recursion depth is Θ(n).
- Forgetting BFS queues can be Θ(n) in the worst case.
- Building list(...) around an iterator/generator, defeating streaming.
- Holding references (e.g., slices or caches) that prevent garbage collection.
- Overlooking load-factor slack in hash tables and resize spikes in dynamic arrays.

Quick references (typical)

- Linear scan: O(1) aux.
- Binary search (iterative): O(1) aux.
- DFS on balanced tree: O(log n) stack; worst-case O(n).
- BFS: O(n) worst-case queue + visited.
- Mergesort: O(n) aux.
- Quicksort: O(log n) expected, O(n) worst-case stack.
- Heapsort: O(1) aux.
- DP table (n×m): O(nm); often reducible to O(min(n, m)) with rolling arrays.
- Dijkstra with adjacency list: O(n + m) for structures; PQ O(n).

Practice guide

- For five classic problems (linear scan, binary search, mergesort, quicksort, BFS/DFS):
    - State the input size parameter(s).
    - List all structures that may grow with input.
    - Mark whether they overlap in lifetime.
    - Derive peak auxiliary space and one-sentence justification.
- Rewrite a solution twice:
    - Version A: straightforward with extra buffers.
    - Version B: in-place/streaming/generator-based.
    - Compare measured peaks on realistic inputs.
- For recursive algorithms:
    - Bound the maximum depth and what each frame stores; consider converting to an explicit stack if it clarifies peak
      usage.

Glossary

- Auxiliary space: Extra memory beyond the input and required output.
- Peak live memory: Maximum memory simultaneously in use at any point.
- Frontier: The set of currently active nodes/states being processed.
- Output-sensitive: Space or time depends on the size of the output.
- Amortized space: Peak across sequences of operations accounting for infrequent expansions.
- In-place: Uses O(1) or sometimes O(log n) extra memory, excluding the input and required output.

How to use this README

- Before coding: choose representations (adjacency list vs matrix, set vs bitset) with space in mind.
- During design: sketch lifetime of major structures and recursion/iteration frontier sizes.
- After coding: review for hidden peaks (copies, slices, temporaries) and consider streaming or in-place alternatives.

You don’t need to memorize values; practice deriving them with the checklist and patterns above.