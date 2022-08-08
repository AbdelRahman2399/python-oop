#ImmutableDataClass(Frozen Data)

from dataclasses import dataclass, field


@dataclass(frozen = True)
class ImmutableClass:

    Value1: str = 'value 1'
    Value2: int = 0

obj = ImmutableClass()
print(obj.Value1)
obj.Value1 = 'Another Val'
print(obj.Value1)