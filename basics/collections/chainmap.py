# ChainMap
# Dict like class for creating a single view of multiple mappings
# quickly linking a number of mappings so they can be treated as a single unit. It is often faster than creating a new dictionary and running multiple update() calls

from collections import ChainMap
from typing import ChainMap

# local -> globals -> builtins
# underlying mappings are stored in a list.
# lookups search the underlying mappins successively until a key is found.
# writes, updates, deletions only operate on the first mapping.
# mapping by refernce

defaults: dict[str, int] = {"timeout": 30, "retries": 3}
user: dict[str, int] = {"timeout": 10}

config: ChainMap[str, int] = ChainMap(user, defaults)

print(config["timeout"])
print(config["retries"])

# using ChainMap class
c: ChainMap[str, int] = ChainMap()
d = c.new_child()
e = c.new_child()
e.maps[0]
e.maps[-1]
print(e.parents)

d['x'] = 1
print(d.items())
print(dict(d))

# Variant of chainmap
class DeepChainMap(ChainMap[str, str]):
    def __setitem__(self, key: str, value: str) -> None:
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return 
        self.maps[0][key] = value
    
    def __delitem__(self, key: str) -> None:
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)

d = DeepChainMap({"zebra": "black"}, {"elephant": "blue"}, {"lion": "yellow"})
d["lion"] = "orange"
d["snake"]  = "red"
del d["elephant"]
print(d)