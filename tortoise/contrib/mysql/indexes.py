from typing import Optional

from pypika_tortoise.terms import Term

from tortoise.indexes import Index


class FullTextIndex(Index):
    INDEX_TYPE = "FULLTEXT"

    def __init__(
        self,
        *expressions: Term,
        fields: Optional[tuple[str, ...]] = None,
        name: Optional[str] = None,
        parser_name: Optional[str] = None,
    ) -> None:
        super().__init__(*expressions, fields=fields, name=name)
        if parser_name:
            self.extra = f" WITH PARSER {parser_name}"


class SpatialIndex(Index):
    INDEX_TYPE = "SPATIAL"
