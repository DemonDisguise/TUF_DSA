# Python Code Structure — PEP 8 Essentials

## The one meta-rule worth knowing before any specific one

PEP 8 is Python's official style guide, but it explicitly says its own
rules can be broken when following them would make code *less* readable.
The goal was never "obey the numbers" — it's "make code predictable to
anyone else who opens it." Every specific rule below exists because it
answers a real question a reader would otherwise have to guess at.

> Interview framing: if you deviate from a convention below, know *why*
> you did it. "I kept this on one line because splitting it hurt
> readability more than the line-length rule helped" is a fine answer.
> "I didn't know the rule" is not.

---

## Imports

**Order**: standard library, then third-party packages, then your own
local modules — each group separated by one blank line.
```python
import sys
from collections import deque

import numpy as np

from graphs.graph import Graph
from graphs.undirected_graph import UndirectedGraph
```
> Why grouped this way: it lets a reader instantly see "how much of this
> file's behavior depends on code I don't control" — standard library is
> stable and everywhere, third-party is a real dependency, local modules
> are the project's own code. Mixing them erases that signal.

**One import per line** for `import`, though `from X import a, b, c` on
one line is fine and common.
```python
import os
import sys
# not: import os, sys
```

**Always at the top of the file**, after the module docstring (if any),
before any other code. Not inside functions unless there's a specific
reason (avoiding a circular import, or a genuinely optional/expensive
dependency) — and if you do that, it's worth a comment saying why, since
it's the exception, not the norm.

---

## Blank Lines — the numbers people actually ask about

**Two blank lines** before and after a top-level function or class
definition.
```python
import sys


def solve(graph):
    ...


class Solution:
    ...
```
> Why two, not one: this is the visual signal for "a completely new,
> independent unit starts here" — enough whitespace that even a fast
> skim through a long file makes definitions jump out as separate
> things, not one continuous block.

**One blank line** between methods inside a class.
```python
class UndirectedGraph:
    def add_edge(self, u, v):
        ...

    def has_cycle(self):
        ...
```
> Why fewer than the top-level rule: methods are already visually grouped
> by the class's indentation — you don't need as strong a separator to
> tell them apart, since the indentation itself is doing some of that
> work already.

**Blank lines *inside* a function**, sparingly — to separate logical
sections, not after every single line.
```python
def solve(graph, start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        # ...
```
One blank line above `while queue:` here reads as "setup is done, the
real algorithm starts now" — a real signal, not decoration. Overusing
blank lines inside a function (one after every statement) has the
opposite effect: it stops meaning anything.

---

## Line Length

**79 characters**, per the original PEP 8 — though this is the single
most commonly relaxed rule in real codebases. Many teams use 99 or 120;
Black (the popular auto-formatter) defaults to 88.
> Why the original number is so short: PEP 8 was written when
> side-by-side diffs on narrow terminals were common. Most teams today
> pick a wider limit and enforce it with a formatter rather than by hand
> — the exact number matters far less than "the whole team uses the
> same one," which is why a formatter (not memorization) is the real
> modern answer to this rule.

---

## Naming Conventions — the one that actually gets checked in interviews

| What | Convention | Example |
|---|---|---|
| Variables, functions, methods | `snake_case` | `has_cycle`, `node_count` |
| Classes | `PascalCase` | `UndirectedGraph`, `TreeNode` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_DEPTH = 1000` |
| "Private" (convention, not enforced) | leading underscore | `_advance`, `_UnionFind` |
| "Really don't touch this" (name-mangled) | leading double underscore | `__internal_state` |

> Why Python's "private" is a convention, not a lock: unlike some
> languages, a single leading underscore doesn't actually prevent access
> — `obj._advance()` still works from outside the class. It's a
> documented signal ("this isn't part of the public interface, don't
> rely on it staying the same") that other developers are expected to
> respect, not something the language enforces. Double-underscore names
> (`__x`) do get name-mangled (`_ClassName__x`) specifically to avoid
> accidental collisions in subclasses, which is a real mechanism — but
> it's about avoiding accidental naming clashes, not about security or
> true privacy.

**One deliberate exception worth knowing**: dunder methods (`__init__`,
`__repr__`, `__eq__`) — double underscore on *both* sides is a completely
different thing from a leading double underscore alone. These are
Python's own hook names for operator overloading and special behavior
(`__repr__` is what `repr()` calls, `__eq__` is what `==` calls) — not a
privacy convention at all. Never invent your own dunder-style name for
a regular method; that space is reserved for Python's own protocol hooks.

---

## Whitespace Inside Lines

**No space** immediately inside parentheses, brackets, or braces.
```python
foo(a, b)          # not foo( a, b )
my_list[1]         # not my_list[ 1 ]
```

**No space** before a comma, colon, or semicolon; **one space** after.
```python
def foo(a, b):     # not def foo(a , b) or def foo(a,b)
```

**Exactly one space** around most binary operators (`=`, `==`, `+`, `and`,
`in`, etc.), but **no space** around `=` for keyword arguments or default
values.
```python
x = 1 + 2                    # spaces around = and +
def foo(x, y=10):            # NO space around = here — it's a default value
result = foo(x, y=20)        # NO space here either — it's a keyword argument
```
> Why keyword/default `=` is the exception: PEP 8 treats it as binding
> the parameter name to its value tightly, more like a single unit than
> two things being compared or assigned at the top level — visually
> distinct from `x = 1`, which is a full assignment statement.

---

## Docstrings and Comments

**Docstrings** (`"""..."""`) describe *what* a function/class does and
its contract — go directly under the `def`/`class` line, are accessible
via `help()` and `.__doc__`, and are the standard place for type/behavior
documentation a caller needs.
```python
def has_cycle(self) -> bool:
    """DFS with parent-tracking, checked across every component."""
    ...
```

**Comments** (`#`) explain *why*, not *what* — the code already says what
it does; a comment earns its place by adding something the code alone
doesn't communicate.
```python
# Diagonal entries are SKIPPED -- LeetCode's convention treats them as
# formal ("a node trivially connects to itself"), never a real edge.
for j in range(i + 1, n):
    ...
```
> Why "explain why, not what" matters, concretely: `i += 1  # increment i`
> is worse than no comment at all — it adds visual noise without adding
> information, since the code already says that. A comment justifying a
> non-obvious choice (why the diagonal is skipped, why a stale heap entry
> gets ignored, why `nonlocal` is needed here) is the kind that actually
> helps a future reader, because it answers a question the code's
> structure alone can't.

---

## Type Hints — not strictly PEP 8 (that's PEP 484), but expected in
## most interview and professional contexts now

```python
def solve(graph: UndirectedGraph, start: int) -> list[int]:
    ...
```
Current convention (Python 3.10+, per everything covered in this
conversation's binary tree/BST work): `list[int]` not `List[int]`,
`X | None` not `Optional[X]`. Hint parameters with the loosest type that
still describes what the function needs; hint return values with the
most specific type you can guarantee.

---

## What Actually Gets Checked in an Interview

Realistically, an interviewer is almost never counting your blank lines.
What they *do* notice:

- **Consistent naming** — not mixing `camelCase` and `snake_case` in the
  same solution.
- **No dead/commented-out code** left in your submission.
- **Meaningful variable names** — `left_height`/`right_height`, not `a`/`b`,
  especially in anything beyond a five-line function.
- **A docstring or comment on non-obvious logic** — exactly the "why, not
  what" distinction above. If your interviewer has to ask "why does this
  check `d > dist[node]`," that's a signal you could have pre-empted with
  one line.
- **Whether you use a formatter's defaults without fighting them** — most
  companies run Black, `ruff format`, or similar automatically; showing
  you're not precious about manual spacing (letting the tool handle line
  length, quote style, etc.) reads as someone who's worked on a real team
  before.