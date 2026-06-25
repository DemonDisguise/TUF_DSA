import os
import re

from typing import List

from core.models import Problem


SUPPORTED_EXTENSIONS = {
    ".py",
    ".cpp",
    ".c",
    ".java",
    ".js",
    ".ts"
}

IGNORE_FOLDERS = {
    "DSA_Manager",
    ".git",
    "node_modules",
    "__pycache__",
    "venv",
    "build",
    "dist",
    ".vscode",
    ".idea",
    "cache"
}


class Scanner:

    def __init__(self, root_dir: str):

        self.root_dir = os.path.abspath(root_dir)

    def extract_title(self, filepath: str) -> str:

        try:

            with open(
                filepath,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    clean_line = re.sub(
                        r'^(#|//|/\*|\*|"""|\'\'\')+\s*',
                        '',
                        line
                    )

                    clean_line = re.sub(
                        r'(\*/|"""|\'\'\')$',
                        '',
                        clean_line
                    ).strip()

                    if clean_line:

                        return clean_line

        except Exception:

            pass

        return os.path.basename(filepath)

    def extract_topics(self, rel_path: str):

        parts = rel_path.split(os.sep)

        if len(parts) >= 3:

            return parts[0], parts[1]

        if len(parts) == 2:

            return parts[0], "General"

        return "Root", "General"

    def scan(self) -> List[Problem]:

        problems = []

        for root, dirs, files in os.walk(self.root_dir):

            dirs[:] = [
                d for d in dirs
                if d not in IGNORE_FOLDERS
                and not d.startswith(".")
            ]

            for filename in files:

                ext = os.path.splitext(filename)[1].lower()

                if ext not in SUPPORTED_EXTENSIONS:
                    continue

                abs_path = os.path.join(root, filename)

                rel_path = os.path.relpath(
                    abs_path,
                    self.root_dir
                )

                title = self.extract_title(abs_path)

                main_topic, sub_topic = self.extract_topics(
                    rel_path
                )

                modified = os.path.getmtime(abs_path)

                problems.append(
                    Problem(
                        title=title,
                        filename=filename,
                        extension=ext,
                        abs_path=abs_path,
                        rel_path=rel_path,
                        main_topic=main_topic,
                        sub_topic=sub_topic,
                        last_modified=modified
                    )
                )

        return problems