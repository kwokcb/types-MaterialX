import MaterialX.PyMaterialXCore
import collections.abc
import typing
from typing import ClassVar, overload

FormatNative: Format
FormatPosix: Format
FormatWindows: Format
MATERIALX_SEARCH_PATH_ENV_VAR: str
PATH_LIST_SEPARATOR: str
TypeAbsolute: Type
TypeNetwork: Type
TypeRelative: Type

class ExceptionFileMissing(Exception): ...

class ExceptionParseError(Exception): ...

class FilePath:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXFormat.FilePath) -> None

        2. __init__(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -> None
        """
    @overload
    def __init__(self, arg0: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXFormat.FilePath) -> None

        2. __init__(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -> None
        """
    def addExtension(self, arg0: str) -> None:
        """addExtension(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -> None

        Add a file extension to the given path.
        """
    def asString(self, format: Format = ...) -> str:
        """asString(self: MaterialX.PyMaterialXFormat.FilePath, format: MaterialX.PyMaterialXFormat.Format = <Format.FormatWindows: 0>) -> str

        Return this path as a standard string with the given format.
        """
    def createDirectory(self) -> None:
        """createDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -> None

        Create a directory on the file system at the given path.
        """
    def exists(self) -> bool:
        """exists(self: MaterialX.PyMaterialXFormat.FilePath) -> bool

        Return true if the given path exists on the file system.
        """
    def getBaseName(self) -> str:
        """getBaseName(self: MaterialX.PyMaterialXFormat.FilePath) -> str

        Return the base name of the given path, with leading directory information removed.
        """
    @staticmethod
    def getCurrentPath() -> FilePath:
        """getCurrentPath() -> MaterialX.PyMaterialXFormat.FilePath

        Return the current working directory of the file system.
        """
    def getExtension(self) -> str:
        """getExtension(self: MaterialX.PyMaterialXFormat.FilePath) -> str

        Return the file extension of the given path.
        """
    def getFilesInDirectory(self, arg0: str) -> list[FilePath]:
        """getFilesInDirectory(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -> list[MaterialX.PyMaterialXFormat.FilePath]

        Return a vector of all files in the given directory with the given extension.

        If extension is empty all files are returned.
        """
    @staticmethod
    def getModulePath() -> FilePath:
        """getModulePath() -> MaterialX.PyMaterialXFormat.FilePath

        Return the directory containing the executable module.
        """
    def getNormalized(self) -> FilePath:
        """getNormalized(self: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath

        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.

        /b' and 'c/../d/../a/b' become 'a/b'.
        """
    def getParentPath(self) -> FilePath:
        """getParentPath(self: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath

        Return the parent directory of the given path, if any.

        If no parent directory is present, then the empty path is returned.
        """
    def getSubDirectories(self) -> list[FilePath]:
        """getSubDirectories(self: MaterialX.PyMaterialXFormat.FilePath) -> list[MaterialX.PyMaterialXFormat.FilePath]

        Return a vector of all directories at or beneath the given path.
        """
    def isAbsolute(self) -> bool:
        """isAbsolute(self: MaterialX.PyMaterialXFormat.FilePath) -> bool

        Return true if the given path is absolute.
        """
    def isDirectory(self) -> bool:
        """isDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -> bool

        Return true if the given path is a directory on the file system.
        """
    def isEmpty(self) -> bool:
        """isEmpty(self: MaterialX.PyMaterialXFormat.FilePath) -> bool

        Return true if the given path is empty.
        """
    def removeExtension(self) -> None:
        """removeExtension(self: MaterialX.PyMaterialXFormat.FilePath) -> None

        Remove the file extension, if any, from the given path.
        """
    def size(self) -> int:
        """size(self: MaterialX.PyMaterialXFormat.FilePath) -> int

        Return the number of strings in the path.
        """
    def __eq__(self, arg0: FilePath) -> bool:
        """__eq__(self: MaterialX.PyMaterialXFormat.FilePath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> bool"""
    def __ne__(self, arg0: FilePath) -> bool:
        """__ne__(self: MaterialX.PyMaterialXFormat.FilePath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> bool"""
    def __truediv__(self, arg0: FilePath) -> FilePath:
        """__truediv__(self: MaterialX.PyMaterialXFormat.FilePath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath"""

class FileSearchPath:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> None

        2. __init__(self: MaterialX.PyMaterialXFormat.FileSearchPath, searchPath: str, sep: str = ';') -> None
        """
    @overload
    def __init__(self, searchPath: str, sep: str = ...) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> None

        2. __init__(self: MaterialX.PyMaterialXFormat.FileSearchPath, searchPath: str, sep: str = ';') -> None
        """
    @overload
    def append(self, arg0: FilePath) -> None:
        """append(*args, **kwargs)
        Overloaded function.

        1. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        2. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        """
    @overload
    def append(self, arg0: FileSearchPath) -> None:
        """append(*args, **kwargs)
        Overloaded function.

        1. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        2. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        """
    def asString(self, sep: str = ...) -> str:
        """asString(self: MaterialX.PyMaterialXFormat.FileSearchPath, sep: str = ';') -> str

        Convert this sequence to a string using the given separator.
        """
    def clear(self) -> None:
        """clear(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> None

        Clear all paths from the sequence.
        """
    def find(self, arg0: FilePath) -> FilePath:
        """find(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath

        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.

        On success, the combined path is returned; otherwise the original filename is returned unmodified.
        """
    def isEmpty(self) -> bool:
        """isEmpty(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> bool

        Return true if the search path is empty.
        """
    def prepend(self, arg0: FilePath) -> None:
        """prepend(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Prepend the given path to the sequence.
        """
    def size(self) -> int:
        """size(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> int

        Return the number of paths in the sequence.
        """

class Format:
    __members__: ClassVar[dict] = ...  # read-only
    FormatNative: ClassVar[Format] = ...
    FormatPosix: ClassVar[Format] = ...
    FormatWindows: ClassVar[Format] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: typing.SupportsInt) -> None:
        """__init__(self: MaterialX.PyMaterialXFormat.Format, value: typing.SupportsInt) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object, /) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object, /) -> int"""
    def __index__(self) -> int:
        """__index__(self: MaterialX.PyMaterialXFormat.Format, /) -> int"""
    def __int__(self) -> int:
        """__int__(self: MaterialX.PyMaterialXFormat.Format, /) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object, /) -> bool"""
    @property
    def name(self): ...
    @property
    def value(self) -> int: ...

class Type:
    __members__: ClassVar[dict] = ...  # read-only
    TypeAbsolute: ClassVar[Type] = ...
    TypeNetwork: ClassVar[Type] = ...
    TypeRelative: ClassVar[Type] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: typing.SupportsInt) -> None:
        """__init__(self: MaterialX.PyMaterialXFormat.Type, value: typing.SupportsInt) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object, /) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object, /) -> int"""
    def __index__(self) -> int:
        """__index__(self: MaterialX.PyMaterialXFormat.Type, /) -> int"""
    def __int__(self) -> int:
        """__int__(self: MaterialX.PyMaterialXFormat.Type, /) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object, /) -> bool"""
    @property
    def name(self): ...
    @property
    def value(self) -> int: ...

class XmlReadOptions:
    parentXIncludes: list[str]
    readComments: bool
    readNewlines: bool
    readXIncludeFunction: collections.abc.Callable[[MaterialX.PyMaterialXCore.Document, FilePath, FileSearchPath, XmlReadOptions], None]
    upgradeVersion: bool
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXFormat.XmlReadOptions) -> None"""

class XmlWriteOptions:
    elementPredicate: collections.abc.Callable[[MaterialX.PyMaterialXCore.Element], bool]
    writeXIncludeEnable: bool
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXFormat.XmlWriteOptions) -> None"""

def flattenFilenames(doc: MaterialX.PyMaterialXCore.Document, searchPath: FileSearchPath = ..., customResolver: MaterialX.PyMaterialXCore.StringResolver = ...) -> None:
    """flattenFilenames(doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000019F0059DC70>, customResolver: MaterialX.PyMaterialXCore.StringResolver = None) -> None

    Flatten all filenames in the given document, applying string resolvers at the scope of each element and removing all fileprefix attributes.

    Args:
        doc: The document to modify.
        searchPath: An optional search path for relative to absolute path conversion.
        customResolver: An optional custom resolver to apply.
    """
def getEnvironmentPath(sep: str = ...) -> FileSearchPath:
    """getEnvironmentPath(sep: str = ';') -> MaterialX.PyMaterialXFormat.FileSearchPath

    Return a FileSearchPath object from search path environment variable.
    """
def getSourceSearchPath(arg0: MaterialX.PyMaterialXCore.Document) -> FileSearchPath:
    """getSourceSearchPath(arg0: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXFormat.FileSearchPath

    Return a file search path containing the parent folder of each source URI in the given document.
    """
def getSubdirectories(arg0: collections.abc.Sequence[FilePath], arg1: FileSearchPath, arg2: collections.abc.Sequence[FilePath]) -> None:
    """getSubdirectories(arg0: collections.abc.Sequence[MaterialX.PyMaterialXFormat.FilePath], arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: collections.abc.Sequence[MaterialX.PyMaterialXFormat.FilePath]) -> None

    Get all subdirectories for a given set of directories and search paths.
    """
def loadDocuments(rootPath: FilePath, searchPath: FileSearchPath, skipFiles: collections.abc.Set[str], includeFiles: collections.abc.Set[str], documents: collections.abc.Sequence[MaterialX.PyMaterialXCore.Document], documentsPaths: collections.abc.Sequence[str], readOptions: XmlReadOptions = ..., errors: collections.abc.Sequence[str] = ...) -> None:
    """loadDocuments(rootPath: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, skipFiles: collections.abc.Set[str], includeFiles: collections.abc.Set[str], documents: collections.abc.Sequence[MaterialX.PyMaterialXCore.Document], documentsPaths: collections.abc.Sequence[str], readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None, errors: collections.abc.Sequence[str] = None) -> None

    Scans for all documents under a root path and returns documents which can be loaded.
    """
def loadLibraries(libraryFolders: collections.abc.Sequence[FilePath], searchPath: FileSearchPath, doc: MaterialX.PyMaterialXCore.Document, excludeFiles: collections.abc.Set[str] = ..., readOptions: XmlReadOptions = ...) -> set[str]:
    """loadLibraries(libraryFolders: collections.abc.Sequence[MaterialX.PyMaterialXFormat.FilePath], searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, doc: MaterialX.PyMaterialXCore.Document, excludeFiles: collections.abc.Set[str] = set(), readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> set[str]

    Load all MaterialX files within the given library folders into a document, using the given search path to locate the folders on the file system.
    """
def loadLibrary(file: FilePath, doc: MaterialX.PyMaterialXCore.Document, searchPath: FileSearchPath = ..., readOptions: XmlReadOptions = ...) -> None:
    """loadLibrary(file: MaterialX.PyMaterialXFormat.FilePath, doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000019F0059DF30>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

    Load a given MaterialX library into a document.
    """
def prependXInclude(arg0: MaterialX.PyMaterialXCore.Document, arg1: FilePath) -> None:
    """prependXInclude(arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FilePath) -> None"""
def readFile(arg0: FilePath) -> str:
    """readFile(arg0: MaterialX.PyMaterialXFormat.FilePath) -> str

    Read the given file and return a string containing its contents; if the read is not successful, then the empty string is returned.
    """
def readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: FilePath, searchPath: FileSearchPath = ..., readOptions: XmlReadOptions = ...) -> None:
    """readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000019F7F7DD030>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

    Read a Document as XML from the given filename.

    Args:
        doc: The Document into which data is read.
        filename: The filename from which data is read. This argument can be supplied either as a FilePath or a standard string.
        searchPath: An optional sequence of file paths that will be applied in order when searching for the given file and its includes. This argument can be supplied either as a FileSearchPath, or as a standard string with paths separated by the PATH_SEPARATOR character.
        readOptions: An optional pointer to an XmlReadOptions object. If provided, then the given options will affect the behavior of the read function. Defaults to a null pointer.
    """
def readFromXmlString(doc: MaterialX.PyMaterialXCore.Document, str: str, searchPath: FileSearchPath = ..., readOptions: XmlReadOptions = ...) -> None:
    """readFromXmlString(doc: MaterialX.PyMaterialXCore.Document, str: str, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000019F0059E6F0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

    Read a Document as XML from the given string.

    Args:
        doc: The Document into which data is read.
        str: The string from which data is read.
        searchPath: An optional sequence of file paths that will be applied in order when searching for the given file and its includes. This argument can be supplied either as a FileSearchPath, or as a standard string with paths separated by the PATH_SEPARATOR character.
        readOptions: An optional pointer to an XmlReadOptions object. If provided, then the given options will affect the behavior of the read function. Defaults to a null pointer.
    """
def writeToXmlFile(doc: MaterialX.PyMaterialXCore.Document, filename: FilePath, writeOptions: XmlWriteOptions = ...) -> None:
    """writeToXmlFile(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, writeOptions: MaterialX.PyMaterialXFormat.XmlWriteOptions = None) -> None"""
def writeToXmlString(doc: MaterialX.PyMaterialXCore.Document, writeOptions: XmlWriteOptions = ...) -> str:
    """writeToXmlString(doc: MaterialX.PyMaterialXCore.Document, writeOptions: MaterialX.PyMaterialXFormat.XmlWriteOptions = None) -> str"""
