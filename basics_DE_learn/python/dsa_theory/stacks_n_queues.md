# Stacks & queues — LIFO vs FIFO (and why `deque` exists)

**Topic:** t08 Stacks · t09 Queues  
**Sources (very basic):**
- [Greg — Stacks and Queues](https://youtu.be/vOx3vY1w4tM) — stack = append/pop **right**; queue = append **right**, pop **left**; Python `list` vs `collections.deque`
- [CS Dojo — Stacks, Queues, and Deques](https://youtu.be/A3ZUpyrnCbM) — pancakes (LIFO) · people in a line (FIFO) · deque = both ends
- Extra (short): [Gayle / HackerRank — Stacks and Queues](https://www.youtube.com/watch?v=wjI1WNcIntg)

**Related:** [arrays.md](./arrays.md) (why `list.pop(0)` is O(n)) · [linked_list.md](./linked_list.md) (deque is like a doubly linked list under the hood)  
**Practice:** t08 **#20 Valid Parentheses** · t09 later (BFS uses a queue)

---

## 1. Two pictures (memorize these)

### Stack — **Last In, First Out (LIFO)**

CS Dojo: **pancakes on a plate**. You only add / take from the **top**. To get the pancake in the middle, you must lift the ones above it first.

Greg: same idea, drawn **left → right**. The **right end** is the “top.” You only care about that end.

```
Stack of plates / pancakes (top is last in):

        ┌───┐
        │ 4 │  ← top  (last in, first out)
        ├───┤
        │ 8 │
        ├───┤
        │ 7 │
        ├───┤
        │ 5 │  ← bottom (first in, last out)
        └───┘

Greg’s array view (top = RIGHT):

  [ 5, 7, 8, 4 ]
               ↑
              top   append here, pop here
```

**You cannot** grab the middle like `a[2]` is the *point* of a stack (you *could* with a list, but then it is not “using it as a stack”).

### Queue — **First In, First Out (FIFO)**

Greg + CS Dojo: **people in a movie line**. Person 1 arrived first → served first. Person 3 arrived last → waits. Do **not** reward the latecomer (that would be a stack).

```
Line (front is LEFT):

  front                         back
    ↓                             ↓
  [ 1 ] → [ 2 ] → [ 3 ] → [ 4 arriving ]
    ↑
  next to be served (dequeue)

Enqueue = join the **back**.
Dequeue = leave from the **front**.
```

| | Stack | Queue |
|--|-------|-------|
| Order | **LIFO** last in, first out | **FIFO** first in, first out |
| Add | **push** / `append` (top) | **enqueue** / `append` (back) |
| Remove | **pop** (top) | **dequeue** / `popleft` (front) |
| Real life | plates, undo, browser back | ticket line, printer jobs |
| Python | `list` (`append` + `pop`) | `collections.deque` |

---

## 2. Stack operations (Greg)

| Op | Meaning | Python (`list`) | Time |
|----|---------|-----------------|------|
| **push / append** | put on top | `s.append(x)` | **O(1)** amortized |
| **pop** | take top off (and return it) | `x = s.pop()` | **O(1)** |
| **peek / top** | look at top, do not remove | `s[-1]` | **O(1)** |
| **is empty** | anything there? | `if not s:` | **O(1)** |

Values can be **anything** (numbers, strings, tuples, dicts) — Greg: interviews often put more than ints.

**Never `pop()` an empty stack** — Python raises `IndexError`. Check first:

```python
s = []
s.append(5)
s.append(4)
s.append(3)     # [5, 4, 3]  top = 3

x = s.pop()     # x is 3, s is [5, 4]
top = s[-1]     # peek → 4

if s:           # is empty? False if list has items
    s.pop()
```

**Why `list` is OK for a stack:** you only touch the **end**. End insert/delete on a dynamic array is fast (see arrays notes). Linked-list stack also works (push/pop at head) — Greg still prefers `list` because it is simpler.

---

## 3. Queue operations (Greg)

Names look weird in textbooks: **enqueue** / **dequeue**. Same idea: add back, remove front.

| Op | Meaning | Python (`deque`) | Time |
|----|---------|------------------|------|
| **enqueue** | join the back | `q.append(x)` | **O(1)** |
| **dequeue** | serve the front | `q.popleft()` | **O(1)** |
| **peek front** | next to leave | `q[0]` | **O(1)** |
| **peek back** | last in line | `q[-1]` | **O(1)** |
| **is empty** | | `if not q:` | **O(1)** |

```python
from collections import deque

q = deque()
q.append(5)       # enqueue
q.append(6)
q.append(7)       # deque([5, 6, 7])  front=5  back=7

x = q.popleft()   # 5 leaves; now [6, 7]
front = q[0]      # 6
back = q[-1]      # 7
```

**Critical:** `q.pop()` with **no** `left` pops the **right** → that is a **stack**. Queue = `append` + **`popleft`**.

---

## 4. Why not `list` for a queue? (Greg)

If the queue is a Python `list`:

- Enqueue `q.append(4)` → O(1) ✓ (end)
- Dequeue `q.pop(0)` → **O(n)** ✗ — everything must **shift left** (arrays notes)

```
list as queue — BAD dequeue:

  [ 1, 2, 3, 4 ]
    ↑ remove 1  →  shift 2,3,4 left  →  O(n)
```

So in practice:

| Structure | Implement with | Why |
|-----------|----------------|-----|
| **Stack** | `list` | append + pop **same end** → both O(1) |
| **Queue** | **`deque`** (or doubly linked list) | add one end, remove the **other** → need O(1) at **both** ends |

Greg: `deque` behaves like a **doubly linked list** for this purpose — O(1) add/remove left **and** right. (CS Dojo also shows a **circular array** queue — same O(1) idea, more pointer math; you do **not** need it for LeetCode if you use `deque`.)

---

## 5. Deque = double-ended queue (both videos)

CS Dojo: a **deque** (pronounced “deck”) lets you **add and remove on either end**.

```
         popleft / appendleft          append / pop
                    ↓                       ↓
              [  …  middle  …  ]
```

| Method | End | Time |
|--------|-----|------|
| `append(x)` | right | O(1) |
| `appendleft(x)` | left | O(1) |
| `pop()` | right | O(1) |
| `popleft()` | left | O(1) |

- Use as a **queue:** `append` + `popleft`
- Use as a **stack:** `append` + `pop` (or a plain `list`)
- Later: sliding-window max, BFS — still this object

---

## 6. CS Dojo extra (optional, one pass)

**Stack with a pointer on an array:** `top = -1` means empty; push = `top += 1` then write; pop = `top -= 1`. Old cells can stay; only `top` counts.

**Queue with two pointers** on a **circular** array: `front` = next to serve, `rear` = slot after last person. When you walk off the end, wrap to index `0`. Empty when `front == rear`. Capacity is often **n − 1** in that teaching trick so empty vs full is not ambiguous.

For problems: **`deque` is enough.** Revisit circular queues if LC **Design Circular Queue** appears.

---

## 7. Where these show up (keep basic)

| Pattern | Structure | Example |
|---------|-----------|---------|
| Matching brackets | **stack** | LC **#20** Valid Parentheses — CS Dojo’s practice idea |
| Undo / call stack | stack | browser back, nested function calls |
| Simulation (ops on top) | stack | LC **#682** Baseball Game |
| Fair order / “next in line” | **queue** | printers, tasks |
| BFS / level-order | queue | graphs, trees (**t09 / later**) |

**Monotonic stack** (next greater, daily temps) = t08 **after** #20 feels automatic. Skip until then.

---

## 8. Say this out loud (interview)

1. “Stack is LIFO — I only touch the top: `append` / `pop`.”
2. “Queue is FIFO — like a line: `append` back, `popleft` front.”
3. “I do **not** use `list.pop(0)` for a queue — that’s O(n). I use `deque`.”
4. “Peek does not remove: stack `s[-1]`, queue front `q[0]`.”

---

## 9. What to study next

| Resource | When |
|----------|------|
| [Abdul Bari — Stack](https://www.youtube.com/watch?v=zwb3GmNAtFk) | more diagrams, same LIFO |
| [Abdul Bari — Queue](https://www.youtube.com/watch?v=zp6pBNbUB2U) | FIFO + circular |
| [CS Dojo — Queue intro](https://www.youtube.com/watch?v=okr-XE8yTO8) | extra queue walkthrough |
| Week 8 plan | **#20** then **#682**, **#844** |

---

## 10. Quick reference

```python
# --- Stack (list) ---
s = []
s.append(x)       # push     O(1)
x = s.pop()       # pop      O(1)  — check `if s` first
top = s[-1]       # peek     O(1)

# --- Queue (deque) ---
from collections import deque
q = deque()
q.append(x)       # enqueue  O(1)
x = q.popleft()   # dequeue  O(1)  — NOT pop()
front = q[0]
```

**Mastery:** t08 = theory + #20 no hints + one Medium (#155 / #739). t09 = theory + `deque` + later BFS.
