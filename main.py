import os

TEXT = """They took the hill apart
and left a hole for the rain.

The rain has filled it an inch a year
and the far wall keeps count:
one pale line for every summer,
more lines than the town below has people.

The bottom stone is shells.
The sea was here first
and is not finished."""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    body = TEXT.strip() + "\n"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(body)
    print(f"{len(body.strip())} code points, {len(body.encode('utf-8'))} bytes")

if __name__ == "__main__":
    main()
