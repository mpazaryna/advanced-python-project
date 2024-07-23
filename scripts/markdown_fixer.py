import difflib
import os
import re

from mdformat import text as mdformat_text


def fix_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        original_content = file.read()

    # Replace ```txt with ```bash and preserve other language specifications
    def fix_code_blocks(match):
        lang = match.group(1).strip().lower()
        if lang == "txt":
            return "```bash\n"
        elif lang:
            return match.group(0)  # Keep existing language specification
        return "```bash\n"  # Default to bash if no language is specified

    # Fix fenced code blocks
    content = re.sub(r"```(\w*)\s*\n", fix_code_blocks, original_content)

    # Fix line length using mdformat
    content = mdformat_text(content, options={"wrap": 100})

    # Remove trailing punctuation from headings
    content = re.sub(r"^(#+.*[^.:!?])[.:!?]\s*$", r"\1", content, flags=re.MULTILINE)

    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Fixed and saved changes to {file_path}")
        show_diff(original_content, content)
    else:
        print(f"No changes needed for {file_path}")


def show_diff(original, modified):
    diff = difflib.unified_diff(
        original.splitlines(keepends=True),
        modified.splitlines(keepends=True),
        lineterm="",
        n=3,  # context lines
    )
    print("".join(diff))


def main():
    for root, _, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}")
                fix_markdown_file(file_path)

    print("Markdown fixing process complete.")


if __name__ == "__main__":
    main()
