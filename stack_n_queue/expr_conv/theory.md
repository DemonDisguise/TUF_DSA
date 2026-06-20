# Expressions

Expressions are ways of writing arithmetic operations.

There are 3 common notations:

1. Infix
2. Prefix (Polish Notation)
3. Postfix (Reverse Polish Notation)

---

# Operators

- `*`, `/`, `+`, `-`, `^` (`**`)

---

# Priority Order

| Operator | Priority |
|-----------|-----------|
| `^` | 3 |
| `*`, `/` | 2 |
| `+`, `-` | 1 |

Associativity:

| Operator | Associativity |
|-----------|---------------|
| `^` | Right to Left |
| `*`, `/`, `+`, `-` | Left to Right |

Examples:

```text
2 ^ 3 ^ 2

= 2 ^ (3 ^ 2)
= 2 ^ 9
= 512
```

```text
10 - 5 - 2

= (10 - 5) - 2
= 3
```

---

# Infix Expression

Operator is written between operands.

Form:

```text
operand operator operand
```

Examples:

```text
A + B
```

```text
A + B * C
```

```text
(A + B) * C
```

This is the notation humans naturally use.

---

# Prefix Expression (Polish Notation)

Operator comes before operands.

Form:

```text
operator operand operand
```

Examples:

```text
+ A B
```

```text
* + A B C
```

which means:

```text
(A + B) * C
```

Another:

```text
+ A * B C
```

means:

```text
A + (B * C)
```

---

# Postfix Expression (Reverse Polish Notation)

Operator comes after operands.

Form:

```text
operand operand operator
```

Examples:

```text
A B +
```

```text
A B + C *
```

which means:

```text
(A + B) * C
```

Another:

```text
A B C * +
```

means:

```text
A + (B * C)
```

---

# Why Prefix and Postfix Exist

Infix needs:

```text
operator precedence
```

and

```text
parentheses
```

to remove ambiguity.

Example:

```text
A + B * C
```

Need precedence rules to know:

```text
A + (B * C)
```

and not:

```text
(A + B) * C
```

Prefix and Postfix remove this ambiguity.

---

# Comparison

Example:

```text
(A + B) * C
```

| Type | Expression |
|--------|------------|
| Infix | `(A + B) * C` |
| Prefix | `* + A B C` |
| Postfix | `A B + C *` |

---

# Evaluation Direction

## Infix

Humans evaluate according to:

```text
1. Parentheses
2. Precedence
3. Associativity
```

---

## Prefix

Traverse:

```text
Right → Left
```

Use a stack.

---

## Postfix

Traverse:

```text
Left → Right
```

Use a stack.

---

# Postfix Evaluation

Expression:

```text
23*54*+9-
```

Equivalent:

```text
(2 * 3) + (5 * 4) - 9
```

Process:

```text
2 → push
3 → push
* → pop 3,2 → push 6

5 → push
4 → push
* → pop 4,5 → push 20

+ → pop 20,6 → push 26

9 → push

- → pop 9,26 → push 17
```

Answer:

```text
17
```

---

# Prefix Evaluation

Expression:

```text
- + * 2 3 * 5 4 9
```

Traverse from:

```text
Right → Left
```

Answer:

```text
17
```

---

# Parentheses

Only infix requires parentheses.

Examples:

```text
(A+B)*C
```

```text
A+(B*C)
```

Prefix:

```text
* + A B C
```

No parentheses needed.

Postfix:

```text
A B + C *
```

No parentheses needed.

---

# Why Stacks Are Used

Prefix and Postfix naturally fit stack operations.

Whenever an operator appears:

```text
Pop operands
Apply operation
Push result
```

Hence most expression problems are stack problems.

---

# Important Observation

For an expression with:

```text
n operands
```

there will be:

```text
n - 1 operators
```

Example:

```text
A + B * C
```

Operands:

```text
A B C
```

Count:

```text
3
```

Operators:

```text
+ *
```

Count:

```text
2 = 3 - 1
```


# Infix(RootLR) conversions
```text
a+b*(c^d-e)^(f+g*h)-i
```
## Postfix(LRootR)
```text
abcd^e-fgh*+^*+i-
```

## Prefix(LRRoot)
```text
-+a*b^-^cde+f*ghi
```