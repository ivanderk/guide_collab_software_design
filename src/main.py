from typing import Any, TypeVar, Union, Protocol, runtime_checkable
from typing import Awaitable

Store = Any
Document = Any
ID = Any
Binary = Any
Text = str
DocumentAttrs = Any
Result = Any


@runtime_checkable
class Storage1(Protocol):
    def save(self, arg0: Store, arg1: Document) -> ID:
        pass

    def get(self, arg0: Store, arg1: ID) -> Document:
        pass


Data = Union[Text, Binary]
Stream = TypeVar('Stream')


@runtime_checkable
class Storage2(Protocol):
    def save(self, arg0: Store, arg1: Stream[Data], arg2: DocumentAttrs) -> ID:
        pass

    def get(self, arg0: Store, arg1: ID) -> Stream[Data]:
        pass

    def getAttr(self, arg0: Store, arg1: ID) -> DocumentAttrs:
        pass


@runtime_checkable
class Storage(Protocol):
    def save(self, arg0: Store, arg1: Stream[Data], arg2: DocumentAttrs) -> Awaitable[ID]:
        pass

    def get(self, arg0: Store, arg1: ID) -> Awaitable[Stream[Data]]:
        pass

    def getAttr(self, arg0: Store, arg1: ID) -> Result[DocumentAttrs]:
        pass

    def remove(self, arg0: ID) -> Result[None]:
        pass


# is equivalent to
class StrictAsyncStorage(Protocol):
    async def save(self, store: Any, data: Union[str, bytes], attrs: Any) -> ID:
        pass

    async def get(self, arg0: Store, arg1: ID) -> Stream[Data]:
        pass

    def getAttr(self, arg0: Store, arg1: ID) -> Result[DocumentAttrs]:
        pass

    def remove(self, arg0: ID) -> Result[None]:
        pass
