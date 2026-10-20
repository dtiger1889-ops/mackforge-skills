---
name: plain
description: >-
  Re-explains dense or jargon-heavy text in plain English while preserving
  its substance. Use for /plain, plain English please, de-jargon this, or
  unpack that. Targets the previous assistant message unless a passage
  or file is specified. Picture mode, only when asked (/plain show, or
  "show me" about an answer), re-explains with the smallest plain-text
  picture. Does not add new analysis or recommendations.
---

# Plain English

Re-express the target so a reader can understand it without decoding
project shorthand. Preserve the meaning and necessary detail.

## Procedure

1. Use the previous assistant message unless the user specifies another
   passage. Ask only if the intended target is unclear.
2. Resolve unfamiliar codes, abbreviations, and project terms from the
   relevant glossary, notes, or source files. Do not guess. If a meaning
   cannot be found, say that plainly.
3. Unpack compressed clauses into ordinary sentences. Define unavoidable
   technical terms at first use.
4. Keep all substantive claims, qualifications, and consequences. This is
   a translation, not a shortened summary.
5. Lead with the point and use connected paragraphs or a simple list.
   Introduce no new shorthand, opinions, or next steps.

An explanation may need more words than the original. Use them where they
make the meaning clearer, without adding process narration.

## Picture mode

Use this only on `/plain show` or when the user says "show me" about an
answer; otherwise stay in prose.

1. Resolve every code first (step 2). Labels inside a picture are words
   too, so an unexplained code in a tree node fails like it would in a
   sentence.
2. Pick the smallest picture that makes the point, usually one:
   - steps or logic: pseudocode in plain words, numbered or indented
   - what runs what, in order: an indented call tree
   - how parts or files are arranged and who owns what: a shallow
     component or file tree
   - what changes: a `diff` block of the tree or list (`-` removed,
     `+` added) when the shape already exists; the whole thing when most
     of it is new
3. Put one or two plain sentences before each picture saying what it
   shows. Keep only the parts that answer the point.
4. Use a fenced block of plain ASCII (`|--`, `` `-- ``, indentation), with
   lines under about 60 characters so a narrow terminal does not wrap them.
5. Do not use Mermaid in a terminal session, where it prints as raw text,
   and do not write an HTML file. If plain text cannot carry the picture
   (a screen layout, a dense comparison), say so and suggest a rendered
   diagram instead.
6. Everything above still holds: what the picture cannot hold goes in
   plain sentences under it, so no substance is lost, and no new
   shorthand or analysis comes in.

## Attribution

Picture mode is adapted from humanlayer's
[show-me](https://github.com/humanlayer/skills) skill, MIT.
