from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class Problem:

    title: str
    filename: str
    extension: str

    abs_path: str
    rel_path: str

    main_topic: str
    sub_topic: str

    last_modified: float

    def to_dict(self) -> Dict:

        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict):

        return cls(**data)