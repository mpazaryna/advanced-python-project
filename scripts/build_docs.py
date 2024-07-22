import os
import sys

from sphinx.cmd.build import main as sphinx_main


def main():
    docs_source = os.path.join(os.path.dirname(__file__), "..", "docs", "source")
    docs_build = os.path.join(os.path.dirname(__file__), "..", "docs", "build")

    return sphinx_main(["-b", "html", docs_source, docs_build])


if __name__ == "__main__":
    sys.exit(main())
