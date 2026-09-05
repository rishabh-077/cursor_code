# Linked lists — nodes, `next`, and why they are not arrays

**Topic:** t10 Linked lists (foundation; t09 Queues often uses the same idea)  
**Sources (very basic):**
- [Greg — Linked Lists](https://youtu.be/dqLHTK7RuIo) — singly vs doubly, why insert/delete at **head** is O(1), Python `curr = head` loop
- [CS Dojo — Introduction to Linked Lists (#5)](https://youtu.be/WwfhLC16bis) — “boxes” connected by arrows; each box is an object with `data` + `next`
- Extra (short, interview-simple): [Gayle McDowell / HackerRank — Linked Lists](https://www.youtube.com/watch?v=njTh_OwMljA)

**Related:** [arrays.md](./arrays.md) (contiguous memory vs scattered nodes) · [hash_maps_n_sets.md](./hash_maps_n_sets.md) (buckets can be linked lists)  
**Practice (when you reach t10):** Reverse List, Merge Two Lists, Cycle detect — portal `/dsa` t10 list

---

## 1. Picture first (both videos)

**Array** (from arrays notes): one long block, indices `0, 1, 2, …`. Jump to index 5 in **O(1)**.

**Linked list:** many small boxes **scattered in memory**. Each box only knows **the next box**. No “index 5” — you **walk** from the front.

CS Dojo: visualize **boxes connected by arrows**, not one partitioned rectangle.

Greg: circles with values, arrows between them; last arrow goes to **nothing**.

```
Singly linked list:  1 → 2 → 3 → None

Memory (not contiguous):
  Node A @ 0x…a   val=1   next ──► Node B
  Node B @ 0x…b   val=2   next ──► Node C
  Node C @ 0x…c   val=3   next ──► None     ← end of list
```

- **Node** = one object: **value** (any type) + **next** (reference to another node, or `None`).
- **Head** = the **first** node. Usually that is **all** you are given (LeetCode: `head`).
- **Tail** = last node (`next is None`). You do **not** get it for free unless you store it (doubly lists often keep `head` **and** `tail`).
- Last node’s `next` is **`None`** (Python) / **`null`** (other languages) — “this is the end.”

**Chain rule:** start at `head`, follow `.next` until `None`. That is how you visit everything.

---

## 2. Why not just use a Python `list`?

| | Array / `list` | Linked list |
|--|----------------|-------------|
| Memory | **Contiguous** | Nodes **anywhere**; glued by pointers |
| Access `i`-th item | **O(1)** | **O(n)** — walk from head |
| Insert / delete **at head** | O(n) (`insert(0, x)` shifts) | **O(1)** — rewire 1–2 pointers |
| Insert / delete **in the middle** | O(n) shift | Find the spot **O(n)**, then rewire **O(1)** |
| Extra memory | Just the values | Each node also stores a pointer |

**Use a linked list when** you care about cheap insert/delete at a **known node** (especially the front), and you **don’t** need random index access.

**Use an array when** you need `a[i]` often.

Python daily code uses `list`. Linked lists show up in **interviews** and inside other structures (`deque`, hash-table chains).

---

## 3. A node is a class (Greg + CS Dojo)

CS Dojo first called it a **Box**, then rename to **Node**. Two fields:

```python
class Node:
    def __init__(self, data):
        self.data = data   # Greg often uses .val
        self.next = None   # pointer / reference to next Node
```

Greg’s version (same idea):

```python
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
```

**Pointer vs reference (Python):** you do not need C. `node.next` is just **another Node object** (or `None`). “Point to B” = `a.next = b`.

### Wiring a tiny list by hand

```python
head = SinglyNode(1)
a = SinglyNode(3)
b = SinglyNode(4)
c = SinglyNode(7)

head.next = a
a.next = b
b.next = c
# c.next is still None
# chain: 1 → 3 → 4 → 7 → None
```

Until you set `.next`, nodes are **floating** — not a list yet.

---

## 4. The #1 pattern — traverse with `curr`

Almost every linked-list problem is: **walker variable**, start at head, move with `curr = curr.next`.

```python
curr = head
while curr:                 # stops when curr becomes None
    print(curr.val)
    curr = curr.next        # one step along the chain
```

**Time: O(n)** — visit each node once. **Space: O(1)** extra (just `curr`).

Pretty print (Greg’s `display` — join with arrows):

```python
def display(head):
    curr = head
    parts = []
    while curr:
        parts.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(parts))
```

Search (also O(n) — worst case you walk the whole list):

```python
def search(head, target):
    curr = head
    while curr:
        if curr.val == target:
            return True
        curr = curr.next
    return False
```

**There are no indices.** “Position 2” means: start at head, take **one** `.next` (or two, depending how you count). You still **walk**.

---

## 5. Operations — what is actually fast?

Greg’s rule: **you only have `head`**. Anything that is **not** the first node costs a walk first.

| Operation | Time | Why |
|-----------|------|-----|
| Access / read k-th node | **O(n)** | Walk from head |
| Search for a value | **O(n)** | May scan entire list |
| Insert / delete **at head** | **O(1)** | Change `head` (and one `next`) |
| Insert / delete at position k | **O(n)** | Walk to k, then O(1) pointer change |
| Insert at **end** (no tail stored) | **O(n)** | Must find last node |
| Insert at **end** (you keep `tail`) | **O(1)** | Doubly / extra tail pointer |

### Insert at head (O(1)) — draw this

```
Before:  head → 1 → 2 → None
Want:    5 at front

1. new.next = old head     (5 → 1)
2. head = new              (head → 5)
After:   5 → 1 → 2 → None
```

```python
def insert_at_head(head, val):
    new = SinglyNode(val)
    new.next = head
    return new              # caller must keep the new head
```

### Delete at head (O(1))

```python
def delete_head(head):
    if head is None:
        return None
    return head.next        # old first node is orphaned / GC’d
```

### Insert in the middle (find then rewire)

To put **5** between **1** and **2**:

```
1. next was 2
Change to:
  1.next = 5
  5.next = 2
```

You need a pointer to **1**. Getting there from `head` is **O(n)**. The two assignments are **O(1)**.

### Delete in the middle (singly)

To remove **2** from `1 → 2 → 3`:

```
1.next = 2.next     # 1 now points at 3
```

You need the **previous** node. With **only** a pointer to **2**, a **singly** list **cannot** easily fix `1.next` — you cannot walk backwards. That is why Greg introduces **doubly** linked lists.

---

## 6. Doubly linked list (Greg)

Same chain, but **two** arrows per node: **next** and **prev**.

```
None ← 1 ⇄ 2 ⇄ 3 → None

Usually store:
  head  (front)
  tail  (back)
```

```python
class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
```

- Walk **forward** (`curr = curr.next`) or **backward** (`curr = curr.prev`).
- Head’s `prev` is `None`; tail’s `next` is `None`.
- **Insert at beginning or end** is **O(1)** if you have `head` and `tail`.
- If you already **hold a middle node**, delete can be **O(1)**: rewire neighbors  
  `node.prev.next = node.next` and `node.next.prev = node.prev`  
  (watch edges: deleting head/tail).

Greg: extra pointer per node = more memory; you buy **two-way** travel and easier deletes given a node.

Insert at beginning (O(1)) — sketch:

```python
def insert_at_beginning(head, tail, val):
    new = DoublyNode(val, next=head, prev=None)
    if head:
        head.prev = new
    else:
        tail = new          # empty list: head and tail both new
    return new, tail        # new head, same (or new) tail
```

Insert at end (O(1)) is the mirror: `new.prev = tail`, `tail.next = new`, return `(head, new)`.

---

## 7. Circular (optional, one sentence)

Last node’s `next` points **back to head** instead of `None`. Useful for round-robin. Easy to infinite-loop — always know your stop condition. Skip until t10 if this is still fuzzy.

---

## 8. Say this out loud (interview)

1. “I only have `head`. I walk with `curr`.”
2. “Insert/delete at head: O(1). Random access: O(n).”
3. “Singly: I need the **previous** node to delete the current one.”
4. “Draw arrows on paper **before** coding. Dummy / extra `prev` pointer is normal.”

---

## 9. What to study next (after these two videos)

| Resource | When |
|----------|------|
| [Abdul Bari — Linked List](https://www.youtube.com/watch?v=NobHlGUjV3g) | Same basics, more diagrams |
| Striver LL playlist (portal t10) | After you can draw insert/delete |
| [CS Dojo sample code](https://www.csdojo.io/linked) | Python/Java from video 2 |
| Portal t10 pattern | Fast & slow pointers (cycle, middle) — **after** traversal feels automatic |

**Do not start reverse / cycle problems** until the `while curr: curr = curr.next` loop is boring.

---

## 10. Quick reference

```python
# LeetCode-style node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Traverse
curr = head
while curr:
    # use curr.val
    curr = curr.next

# Insert at head
new = ListNode(x)
new.next = head
head = new
```

**Mastery (later, portal t10):** theory + draw on paper + Easy no hints (Reverse List / Merge Two Lists / Cycle).
