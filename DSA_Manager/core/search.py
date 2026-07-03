import re


from core.models import Problem


class SearchEngine:

    @staticmethod
    def normalize(text: str) -> str:

        text = text.lower()

        text = re.sub(
            r'[^a-z0-9\s]',
            ' ',
            text
        )

        text = re.sub(
            r'\s+',
            ' ',
            text
        )

        return text.strip()

    @staticmethod
    def tokenize(text: str):

        return set(
            SearchEngine.normalize(text).split()
        )

    @staticmethod
    def get_search_text(
        problem: Problem,
        mode: str
    ) -> str:

        if mode == "title":

            return problem.title

        elif mode == "topic":

            return problem.main_topic

        elif mode == "subtopic":

            return problem.sub_topic

        elif mode == "path":

            return problem.rel_path

        return " ".join([
            problem.title,
            problem.main_topic,
            problem.sub_topic,
            problem.rel_path
        ])

    @staticmethod
    def score_problem(
        query: str,
        problem: Problem,
        mode: str = "all"
    ):

        query_tokens = SearchEngine.tokenize(query)

        searchable_text = SearchEngine.get_search_text(
            problem,
            mode
        )

        searchable_tokens = SearchEngine.tokenize(
            searchable_text
        )

        score = 0

        matched = query_tokens & searchable_tokens

        missing = query_tokens - searchable_tokens

        # perfect token match
        if len(matched) == len(query_tokens):

            score += 100

        # token score
        score += len(matched) * 15

        # penalty
        score -= len(missing) * 5

        normalized_query = SearchEngine.normalize(
            query
        )

        normalized_text = SearchEngine.normalize(
            searchable_text
        )

        # substring bonus
        if normalized_query in normalized_text:

            score += 25

        return score

    @staticmethod
    def search(
        query: str,
        problems: list[Problem],
        mode: str = "all"
    ) -> list[Problem]:

        if not query.strip():

            return sorted(
                problems,
                key=lambda p: (
                    p.main_topic.lower(),
                    p.sub_topic.lower(),
                    p.title.lower()
                )
            )

        scored = []

        for problem in problems:

            score = SearchEngine.score_problem(
                query,
                problem,
                mode
            )

            if score > 0:

                scored.append(
                    (score, problem)
                )

        scored.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return [
            item[1]
            for item in scored
        ]