import os
import ast
from collections import defaultdict, Counter

# =========================================================
# CONFIG
# =========================================================
BASE_DIR = "."
FOLDERS = [
    "arrays",
    "strings",
    "trees",
    "graphs",
    "linked_list",
    "binary_search",
    "queues",
    "stacks",
    "backtracking"
]

OUTPUT_FILE = "README.md"

# =========================================================
# HEADER (with clone + setup instructions)
# =========================================================
HEADER = """# 🧠 LeetCode Practice

![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![pytest](https://img.shields.io/badge/tests-pytest-green.svg)
![status](https://img.shields.io/badge/status-in%20progress-yellow.svg)
![Tests](https://github.com/nanda-rampura/leetcode-practice/actions/workflows/python-tests.yml/badge.svg)

This repository contains my LeetCode practice problems implemented in Python with clean structure and unit tests.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/nanda-rampura/leetcode-practice.git
cd leetcode-practice
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate virtual environment
```bash
source venv/bin/activate   # Mac/Linux
venv\\Scripts\\activate    # Windows
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

---

"""

# =========================================================
# FOOTER
# =========================================================
FOOTER = """

---

## 🧪 Testing

Run all tests:

```bash
pytest -v
```

## 📌 Notes
- All problems include metadata (Problem / Difficulty / Pattern)
- README is auto-generated from source code
"""


# =========================================================
# METADATA EXTRACTION
# =========================================================
def parse_metadata(doc):
    data = {"problem": None, "difficulty": "Unknown", "pattern": "Unknown", "link": None}

    for line in doc.splitlines():
        line = line.strip()

        if line.startswith("Problem:"):
            data["problem"] = line.replace("Problem:", "").strip()

        elif line.startswith("Difficulty:"):
            data["difficulty"] = line.replace("Difficulty:", "").strip()

        elif line.startswith("Pattern:"):
            data["pattern"] = line.replace("Pattern:", "").strip()

        elif line.startswith("LeetCode:"):   
            data["link"] = line.replace("LeetCode:", "").strip()

    return data


def extract_metadata(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
    except Exception:
        return None

    # ✅ 1. Check module-level docstring FIRST
    module_doc = ast.get_docstring(tree)
    if module_doc:
        return parse_metadata(module_doc)

    # ✅ 2. Fallback: class-level docstring
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            doc = ast.get_docstring(node)
            if doc:
                return parse_metadata(doc)

    return None


# =========================================================
# COLLECT DATA
# =========================================================
def collect():
    grouped = defaultdict(list)
    difficulty = Counter()
    pattern = Counter()
    total = 0

    for folder in FOLDERS:
        path = os.path.join(BASE_DIR, folder)
        if not os.path.exists(path):
            continue

        for root, _, files in os.walk(path):
            for file in files:
                if not file.endswith(".py"):
                    continue

                full_path = os.path.join(root, file)

                meta = extract_metadata(full_path)
                if meta and meta["problem"]:
                    grouped[folder].append(meta)
                    difficulty[meta["difficulty"]] += 1
                    pattern[meta["pattern"]] += 1
                    total += 1

    return grouped, difficulty, pattern, total


# =========================================================
# BUILD README
# =========================================================
def build(grouped, difficulty, pattern, total):
    body = ""

    # =========================
    # Summary
    # =========================
    body += "## 📊 Summary\n\n"
    body += f"- **Total Problems:** {total}\n"
    body += f"- **Easy:** {difficulty['Easy']}\n"
    body += f"- **Medium:** {difficulty['Medium']}\n"
    body += f"- **Hard:** {difficulty['Hard']}\n\n"

    # =========================
    # Top Patterns
    # =========================
    body += "## 🔥 Top Patterns\n\n"
    for p, c in pattern.most_common(5):
        body += f"- {p} ({c})\n"

    body += "\n---\n\n"

    # =========================
    # Folder Emoji Map
    # =========================
    EMOJI = {
        "arrays": "🟢",
        "strings": "🧵",
        "trees": "🌳",
        "graphs": "🌐",
        "linked_list": "🔗",
        "binary_search": "🔍",
        "queues": "📦",
    }

    # =========================
    # Difficulty Icons
    # =========================
    difficulty_icon = {
        "Easy": "🟢",
        "Medium": "🟡",
        "Hard": "🔴",
    }

    # =========================
    # Sections
    # =========================
    for folder in FOLDERS:
        if folder not in grouped:
            continue

        emoji = EMOJI.get(folder, "📁")
        title = folder.replace("_", " ").title()

        body += f"## {emoji} {title}\n\n"

        # sort by difficulty then name
        sorted_items = sorted(
            grouped[folder],
            key=lambda x: (x["difficulty"], x["problem"])
        )

        for m in sorted_items:
            icon = difficulty_icon.get(m["difficulty"], "⚪")

            link = m.get("link")

            if link:
                body += (
                    f"- {icon} 🔗 [{m['problem']}]({link}) — "
                    f"{m['pattern']}\n"
                )
            else:
                body += (
                    f"- {icon} {m['problem']} — "
                    f"{m['pattern']}\n"
                )

        body += "\n"

    return HEADER + body + FOOTER


# =========================================================
# MAIN
# =========================================================
def main():
    grouped, difficulty, pattern, total = collect()
    content = build(grouped, difficulty, pattern, total)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README generated → {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
