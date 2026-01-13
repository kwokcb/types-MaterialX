import MaterialX.PyMaterialXCore
import MaterialX.PyMaterialXFormat
import collections.abc
import typing
from _typeshed import Incomplete
from typing import ClassVar, overload

HW_ATTR_TRANSPARENT: str
HW_LIGHT_DATA: str
HW_PIXEL_OUTPUTS: str
HW_PRIVATE_UNIFORMS: str
HW_PUBLIC_UNIFORMS: str
HW_VERTEX_DATA: str
HW_VERTEX_INPUTS: str
PIXEL_STAGE: str
SHADER_INTERFACE_COMPLETE: ShaderInterfaceType
SHADER_INTERFACE_REDUCED: ShaderInterfaceType
SPECULAR_ENVIRONMENT_FIS: HwSpecularEnvironmentMethod
SPECULAR_ENVIRONMENT_NONE: HwSpecularEnvironmentMethod
SPECULAR_ENVIRONMENT_PREFILTER: HwSpecularEnvironmentMethod
VERTEX_STAGE: str

class ApplicationVariableHandler:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class ColorManagementSystem:
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> None"""
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> str

        Return the ColorManagementSystem name.
        """
    def loadLibrary(self, arg0: MaterialX.PyMaterialXCore.Document) -> None:
        """loadLibrary(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXCore.Document) -> None

        Load a library of implementations from the provided document, replacing any previously loaded content.
        """
    def supportsTransform(self, arg0: ColorSpaceTransform) -> bool:
        """supportsTransform(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXGenShader.ColorSpaceTransform) -> bool

        Returns whether this color management system supports a provided transform.
        """

class ColorSpaceTransform:
    sourceSpace: str
    targetSpace: str
    type: Incomplete
    def __init__(self, arg0: str, arg1: str, arg2) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.ColorSpaceTransform, arg0: str, arg1: str, arg2: MaterialX_v1_39_5::TypeDesc) -> None"""

class DefaultColorManagementSystem(ColorManagementSystem):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create(arg0: str) -> DefaultColorManagementSystem:
        """create(arg0: str) -> MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem

        Create a new DefaultColorManagementSystem.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem) -> str

        Return the DefaultColorManagementSystem name.
        """

class GenContext:
    def __init__(self, arg0: ShaderGenerator) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> None"""
    def getApplicationVariableHandler(self, *args, **kwargs):
        """getApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext) -> collections.abc.Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]

        Get handler for application variables.
        """
    def getOptions(self, *args, **kwargs):
        """getOptions(self: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX_v1_39_5::GenOptions"""
    def getShaderGenerator(self) -> ShaderGenerator:
        """getShaderGenerator(self: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.ShaderGenerator

        Return shader generatior.
        """
    def getTypeDesc(self, *args, **kwargs):
        """getTypeDesc(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str) -> MaterialX_v1_39_5::TypeDesc

        Return a TypeDesc for the given type name.
        """
    def pushUserData(self, arg0: str, arg1) -> None:
        """pushUserData(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str, arg1: MaterialX_v1_39_5::GenUserData) -> None

        Add user data to the context to make it available during shader generator.
        """
    @overload
    def registerSourceCodeSearchPath(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """registerSourceCodeSearchPath(*args, **kwargs)
        Overloaded function.

        1. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        2. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        """
    @overload
    def registerSourceCodeSearchPath(self, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None:
        """registerSourceCodeSearchPath(*args, **kwargs)
        Overloaded function.

        1. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        2. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        """
    def resolveSourceFile(self, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath:
        """resolveSourceFile(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath

        Resolve a source code filename, first checking the given local path then checking any file paths registered by the user.
        """
    def setApplicationVariableHandler(self, arg0) -> None:
        """setApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: collections.abc.Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]) -> None

        Set handler for application variables.
        """

class GenOptions:
    addUpstreamDependencies: bool
    emitColorTransforms: bool
    fileTextureVerticalFlip: bool
    hwAmbientOcclusion: bool
    hwImplicitBitangents: bool
    hwMaxActiveLightSources: int
    hwNormalizeUdimTexCoords: bool
    hwShadowMap: bool
    hwSpecularEnvironmentMethod: HwSpecularEnvironmentMethod
    hwSrgbEncodeOutput: bool
    hwTransparency: bool
    hwWriteAlbedoTable: bool
    hwWriteDepthMoments: bool
    hwWriteEnvPrefilter: bool
    libraryPrefix: MaterialX.PyMaterialXFormat.FilePath
    shaderInterfaceType: ShaderInterfaceType
    targetColorSpaceOverride: str
    targetDistanceUnit: str
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.GenOptions) -> None"""

class GenUserData:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getSelf(self) -> GenUserData:
        """getSelf(self: MaterialX.PyMaterialXGenShader.GenUserData) -> MaterialX.PyMaterialXGenShader.GenUserData"""

class HwResourceBindingContext(GenUserData):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def emitDirectives(self, arg0: GenContext, arg1: ShaderStage) -> None:
        """emitDirectives(self: MaterialX.PyMaterialXGenShader.HwResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None"""
    def emitResourceBindings(self, arg0: GenContext, arg1: VariableBlock, arg2: ShaderStage) -> None:
        """emitResourceBindings(self: MaterialX.PyMaterialXGenShader.HwResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None"""

class HwShaderGenerator(ShaderGenerator):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def bindLightShader(self, arg0: typing.SupportsInt, arg1: GenContext) -> None:
        """bindLightShader(self: MaterialX.PyMaterialXCore.NodeDef, arg0: typing.SupportsInt, arg1: MaterialX.PyMaterialXGenShader.GenContext) -> None"""
    def unbindLightShader(self, arg0: GenContext) -> None:
        """unbindLightShader(self: typing.SupportsInt, arg0: MaterialX.PyMaterialXGenShader.GenContext) -> None"""
    def unbindLightShaders(self) -> None:
        """unbindLightShaders(self: MaterialX.PyMaterialXGenShader.GenContext) -> None"""

class HwSpecularEnvironmentMethod:
    __members__: ClassVar[dict] = ...  # read-only
    SPECULAR_ENVIRONMENT_FIS: ClassVar[HwSpecularEnvironmentMethod] = ...
    SPECULAR_ENVIRONMENT_NONE: ClassVar[HwSpecularEnvironmentMethod] = ...
    SPECULAR_ENVIRONMENT_PREFILTER: ClassVar[HwSpecularEnvironmentMethod] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: typing.SupportsInt) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.HwSpecularEnvironmentMethod, value: typing.SupportsInt) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object, /) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object, /) -> int"""
    def __index__(self) -> int:
        """__index__(self: MaterialX.PyMaterialXGenShader.HwSpecularEnvironmentMethod, /) -> int"""
    def __int__(self) -> int:
        """__int__(self: MaterialX.PyMaterialXGenShader.HwSpecularEnvironmentMethod, /) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object, /) -> bool"""
    @property
    def name(self): ...
    @property
    def value(self) -> int: ...

class Shader:
    def __init__(self, arg0: str, arg1) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str, arg1: MaterialX_v1_39_5::ShaderGraph) -> None"""
    def getAttribute(self, arg0: str) -> MaterialX.PyMaterialXCore.Value:
        """getAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> MaterialX.PyMaterialXCore.Value

        Return the value for a named attribute, or nullptr if no such attribute is found.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.Shader) -> str

        Return the shader name.
        """
    def getSourceCode(self, arg0: str) -> str:
        """getSourceCode(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> str

        Return the shader source code for a given shader stage.
        """
    def getStage(self, *args, **kwargs):
        """getStage(*args, **kwargs)
        Overloaded function.

        1. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: typing.SupportsInt) -> MaterialX_v1_39_5::ShaderStage

        2. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> MaterialX_v1_39_5::ShaderStage
        """
    def hasAttribute(self, arg0: str) -> bool:
        """hasAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> bool

        Return true if the shader has a given named attribute.
        """
    def hasStage(self, arg0: str) -> bool:
        """hasStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> bool

        Return if stage exists.
        """
    def numStages(self) -> int:
        """numStages(self: MaterialX.PyMaterialXGenShader.Shader) -> int

        Return the number of shader stages for this shader.
        """
    @overload
    def setAttribute(self, arg0: str) -> None:
        """setAttribute(*args, **kwargs)
        Overloaded function.

        1. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> None

        2. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None
        """
    @overload
    def setAttribute(self, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None:
        """setAttribute(*args, **kwargs)
        Overloaded function.

        1. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> None

        2. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None
        """

class ShaderGenerator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def generate(self, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2) -> Shader:
        """generate(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX_v1_39_5::GenContext) -> MaterialX.PyMaterialXGenShader.Shader

        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.
        """
    def getColorManagementSystem(self) -> ColorManagementSystem:
        """getColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> MaterialX.PyMaterialXGenShader.ColorManagementSystem

        Returns the color management system.
        """
    def getTarget(self) -> str:
        """getTarget(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> str

        Return the name of the target this generator is for.
        """
    def getTokenSubstitutions(self) -> dict[str, str]:
        """getTokenSubstitutions(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> dict[str, str]

        Return the map of token substitutions used by the generator.
        """
    def getUnitSystem(self, *args, **kwargs):
        """getUnitSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> MaterialX_v1_39_5::UnitSystem

        Returns the unit system.
        """
    def registerShaderMetadata(self, arg0: MaterialX.PyMaterialXCore.Document, arg1) -> None:
        '''registerShaderMetadata(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX_v1_39_5::GenContext) -> None

        Register metadata that should be exported to the generated shaders.

        Supported metadata includes standard UI attributes like "uiname", "uifolder", "uimin", "uimax", etc. But it is also extendable by defining custom attributes using AttributeDefs. Any AttributeDef in the given document with exportable="true" will be exported as shader metadata when found on nodes during shader generation. Derived shader generators may override this method to change the registration. Applications must explicitly call this method before shader generation to enable export of metadata.
        '''
    def registerTypeDefs(self, arg0: MaterialX.PyMaterialXCore.Document) -> None:
        """registerTypeDefs(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXCore.Document) -> None

        Register type definitions from the document.
        """
    def setColorManagementSystem(self, arg0: ColorManagementSystem) -> None:
        """setColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> None

        Sets the color management system.
        """
    def setUnitSystem(self, arg0) -> None:
        """setUnitSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX_v1_39_5::UnitSystem) -> None

        Sets the unit system.
        """

class ShaderInterfaceType:
    __members__: ClassVar[dict] = ...  # read-only
    SHADER_INTERFACE_COMPLETE: ClassVar[ShaderInterfaceType] = ...
    SHADER_INTERFACE_REDUCED: ClassVar[ShaderInterfaceType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: typing.SupportsInt) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.ShaderInterfaceType, value: typing.SupportsInt) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object, /) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object, /) -> int"""
    def __index__(self) -> int:
        """__index__(self: MaterialX.PyMaterialXGenShader.ShaderInterfaceType, /) -> int"""
    def __int__(self) -> int:
        """__int__(self: MaterialX.PyMaterialXGenShader.ShaderInterfaceType, /) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object, /) -> bool"""
    @property
    def name(self): ...
    @property
    def value(self) -> int: ...

class ShaderPort:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getColorSpace(self) -> str:
        """getColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the source color space for the value on this port.
        """
    def getFullName(self) -> str:
        """getFullName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the name of this port.
        """
    def getGeomProp(self) -> str:
        """getGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Get geomprop name.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the name of this port.
        """
    def getPath(self) -> str:
        """getPath(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the path to this port.
        """
    def getSemantic(self) -> str:
        """getSemantic(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the variable semantic of this port.
        """
    def getType(self, *args, **kwargs):
        """getType(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> MaterialX_v1_39_5::TypeDesc

        Return the data type for this port.
        """
    def getUnit(self) -> str:
        """getUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the unit type for the value on this port.
        """
    def getValue(self) -> MaterialX.PyMaterialXCore.Value:
        """getValue(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> MaterialX.PyMaterialXCore.Value

        Return the value set on this port.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the value set on this port as a string, or an empty string if there is no value.
        """
    def getVariable(self) -> str:
        """getVariable(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the variable name of this port.
        """
    def isEmitted(self) -> bool:
        """isEmitted(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> bool

        Return the emitted state of this port.
        """
    def isUniform(self) -> bool:
        """isUniform(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> bool

        Return the uniform flag on this port.
        """
    def setColorSpace(self, arg0: str) -> None:
        """setColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set a source color space for the value on this port.
        """
    def setGeomProp(self, arg0: str) -> None:
        """setGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set geomprop name if the input has a default geomprop to be assigned when it is unconnected.
        """
    def setName(self, arg0: str) -> None:
        """setName(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set the name of this port.
        """
    def setPath(self, arg0: str) -> None:
        """setPath(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set the path to this port.
        """
    def setSemantic(self, arg0: str) -> None:
        """setSemantic(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set the variable semantic of this port.
        """
    def setType(self, arg0) -> None:
        """setType(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX_v1_39_5::TypeDesc) -> None

        Set the data type for this port.
        """
    def setUnit(self, arg0: str) -> None:
        """setUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set a unit type for the value on this port.
        """
    def setValue(self, arg0: MaterialX.PyMaterialXCore.Value, arg1: bool) -> None:
        """setValue(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX.PyMaterialXCore.Value, arg1: bool) -> None

        Set a value on this port.
        """
    def setVariable(self, arg0: str) -> None:
        """setVariable(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set the variable name of this port.
        """

class ShaderPortPredicate:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class ShaderStage:
    def __init__(self, arg0: str, arg1) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str, arg1: MaterialX_v1_39_5::Syntax) -> None"""
    def getConstantBlock(self) -> VariableBlock:
        """getConstantBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> MaterialX.PyMaterialXGenShader.VariableBlock"""
    def getFunctionName(self) -> str:
        """getFunctionName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str

        Return the stage function name.
        """
    def getIncludes(self) -> set[str]:
        """getIncludes(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> set[str]

        Return a set of all include files.
        """
    def getInputBlock(self, arg0: str) -> VariableBlock:
        """getInputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock"""
    def getInputBlocks(self) -> dict[str, VariableBlock]:
        """getInputBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]

        Return a map of all input blocks.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str

        Return the stage name.
        """
    def getOutputBlock(self, arg0: str) -> VariableBlock:
        """getOutputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock"""
    def getOutputBlocks(self) -> dict[str, VariableBlock]:
        """getOutputBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]

        Return a map of all output blocks.
        """
    def getSourceCode(self) -> str:
        """getSourceCode(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str

        Return the stage source code.
        """
    def getSourceDependencies(self) -> set[str]:
        """getSourceDependencies(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> set[str]

        Return a set of all source dependencies.
        """
    def getUniformBlock(self, arg0: str) -> VariableBlock:
        """getUniformBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock"""
    def getUniformBlocks(self) -> dict[str, VariableBlock]:
        """getUniformBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]

        Return a map of all uniform blocks.
        """

class ShaderTranslator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create() -> ShaderTranslator:
        """create() -> MaterialX.PyMaterialXGenShader.ShaderTranslator"""
    def translateAllMaterials(self, arg0: MaterialX.PyMaterialXCore.Document, arg1: str) -> None:
        """translateAllMaterials(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Document, arg1: str) -> None

        Translate each material in the input document to the destination shading model.
        """
    def translateShader(self, arg0: MaterialX.PyMaterialXCore.Node, arg1: str) -> None:
        """translateShader(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Node, arg1: str) -> None

        Translate a shader node to the destination shading model.
        """

class TypeDesc:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getBaseType(self) -> int:
        """getBaseType(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int

        Return the basetype for the type.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> str

        Return the name of the type.
        """
    def getSemantic(self) -> int:
        """getSemantic(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int

        Return the semantic for the type.
        """
    def getSize(self) -> int:
        """getSize(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int

        Return the number of elements the type is composed of.

        Will return 1 for scalar types and a size greater than 1 for aggregate type. For array types 0 is returned since the number of elements is undefined until an array is instantiated.
        """
    def isAggregate(self) -> bool:
        """isAggregate(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is an aggregate type.
        """
    def isArray(self) -> bool:
        """isArray(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is an array type.
        """
    def isClosure(self) -> bool:
        """isClosure(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type represents a closure.
        """
    def isFloat2(self) -> bool:
        """isFloat2(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is an aggregate of 2 floats.
        """
    def isFloat3(self) -> bool:
        """isFloat3(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is an aggregate of 3 floats.
        """
    def isFloat4(self) -> bool:
        """isFloat4(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is an aggregate of 4 floats.
        """
    def isScalar(self) -> bool:
        """isScalar(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is a scalar type.
        """

class UnitSystem:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create(arg0: str) -> UnitSystem:
        """create(arg0: str) -> MaterialX.PyMaterialXGenShader.UnitSystem

        Create a new UnitSystem.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.UnitSystem) -> str

        Return the UnitSystem name.
        """
    def getUnitConverterRegistry(self) -> MaterialX.PyMaterialXCore.UnitConverterRegistry:
        """getUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem) -> MaterialX.PyMaterialXCore.UnitConverterRegistry

        Returns the currently assigned unit converter registry.
        """
    def loadLibrary(self, arg0: MaterialX.PyMaterialXCore.Document) -> None:
        """loadLibrary(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.Document) -> None

        assign document with unit implementations replacing any previously loaded content.
        """
    def setUnitConverterRegistry(self, arg0: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None:
        """setUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None

        Assign unit converter registry replacing any previous assignment.
        """
    def supportsTransform(self, arg0: UnitTransform) -> bool:
        """supportsTransform(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXGenShader.UnitTransform) -> bool

        Returns whether this unit system supports a provided transform.
        """

class UnitTransform:
    sourceUnit: str
    targetUnit: str
    type: TypeDesc
    unitType: TypeDesc
    def __init__(self, arg0: str, arg1: str, arg2: TypeDesc, arg3: str) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.UnitTransform, arg0: str, arg1: str, arg2: MaterialX.PyMaterialXGenShader.TypeDesc, arg3: str) -> None"""

class VariableBlock:
    def __init__(self, arg0: str, arg1: str) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: str, arg1: str) -> None"""
    def empty(self) -> bool:
        """empty(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> bool

        Return true if the block has no variables.
        """
    @overload
    def find(self, arg0: str) -> ShaderPort:
        """find(*args, **kwargs)
        Overloaded function.

        1. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: str) -> MaterialX.PyMaterialXGenShader.ShaderPort

        2. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: collections.abc.Callable[[MaterialX.PyMaterialXGenShader.ShaderPort], bool]) -> MaterialX.PyMaterialXGenShader.ShaderPort
        """
    @overload
    def find(self, arg0: collections.abc.Callable[[ShaderPort], bool]) -> ShaderPort:
        """find(*args, **kwargs)
        Overloaded function.

        1. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: str) -> MaterialX.PyMaterialXGenShader.ShaderPort

        2. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: collections.abc.Callable[[MaterialX.PyMaterialXGenShader.ShaderPort], bool]) -> MaterialX.PyMaterialXGenShader.ShaderPort
        """
    def getInstance(self) -> str:
        """getInstance(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> str

        Get the instance name of this block.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> str

        Get the name of this block.
        """
    def size(self) -> int:
        """size(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> int

        Return the number of variables in this block.
        """
    def __getitem__(self, arg0: typing.SupportsInt) -> ShaderPort:
        """__getitem__(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: typing.SupportsInt) -> MaterialX.PyMaterialXGenShader.ShaderPort

        Return the number of variables in this block.
        """
    def __len__(self) -> int:
        """__len__(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> int

        Return the number of variables in this block.
        """

def connectsToWorldSpaceNode(arg0: MaterialX.PyMaterialXCore.Output) -> MaterialX.PyMaterialXCore.Node:
    """connectsToWorldSpaceNode(arg0: MaterialX.PyMaterialXCore.Output) -> MaterialX.PyMaterialXCore.Node

    Determine whether the given output is directly connected to a node that generates world-space coordinates (e.g.

    Args:
        output: Output to check

    Returns:
        Return the node if found.
    """
def elementRequiresShading(arg0: MaterialX.PyMaterialXCore.TypedElement) -> bool:
    """elementRequiresShading(arg0: MaterialX.PyMaterialXCore.TypedElement) -> bool

    Determine if a given element requires shading / lighting for rendering.
    """
def findRenderableElements(doc: MaterialX.PyMaterialXCore.Document, includeReferencedGraphs: bool = ...) -> list[MaterialX.PyMaterialXCore.TypedElement]:
    """findRenderableElements(doc: MaterialX.PyMaterialXCore.Document, includeReferencedGraphs: bool = False) -> list[MaterialX.PyMaterialXCore.TypedElement]"""
def findRenderableMaterialNodes(arg0: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypedElement]:
    """findRenderableMaterialNodes(arg0: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypedElement]"""
def getNodeDefInput(arg0: MaterialX.PyMaterialXCore.Input, arg1: str) -> MaterialX.PyMaterialXCore.Input:
    """getNodeDefInput(arg0: MaterialX.PyMaterialXCore.Input, arg1: str) -> MaterialX.PyMaterialXCore.Input

    Given a node input, return the corresponding input within its matching nodedef.

    The optional target string can be used to guide the selection of nodedef declarations.
    """
def getUdimCoordinates(arg0: collections.abc.Sequence[str]) -> list[MaterialX.PyMaterialXCore.Vector2]:
    """getUdimCoordinates(arg0: collections.abc.Sequence[str]) -> list[MaterialX.PyMaterialXCore.Vector2]

    Compute the UDIM coordinates for a set of UDIM identifiers.

    Returns:
        List of UDIM coordinates
    """
def getUdimScaleAndOffset(arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.Vector2], arg1: MaterialX.PyMaterialXCore.Vector2, arg2: MaterialX.PyMaterialXCore.Vector2) -> None:
    """getUdimScaleAndOffset(arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.Vector2], arg1: MaterialX.PyMaterialXCore.Vector2, arg2: MaterialX.PyMaterialXCore.Vector2) -> None

    Get the UV scale and offset to transform uv coordinates from UDIM uv space to 0..1 space.
    """
def hasElementAttributes(arg0: MaterialX.PyMaterialXCore.Output, arg1: collections.abc.Sequence[str]) -> bool:
    """hasElementAttributes(arg0: MaterialX.PyMaterialXCore.Output, arg1: collections.abc.Sequence[str]) -> bool

    Returns true if there is are any value elements with a given set of attributes either on the starting node or any graph upsstream of that node.

    Args:
        output: Starting node
        attributes: Attributes to test for
    """
def isTransparentSurface(arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> bool:
    """isTransparentSurface(arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> bool

    Returns true if the given element is a surface shader with the potential of being transparent.

    This can be used by HW shader generators to determine if a shader will require transparency handling.

    Note: This function will check some common cases for how a surface shader can be transparent. It is not covering all possible cases for how transparency can be done and target applications might need to do additional checks to track transparency correctly. For example, custom surface shader nodes implemented in source code will not be tracked by this function and transparency for such nodes must be tracked separately by the target application.
    """
def mapValueToColor(arg0: MaterialX.PyMaterialXCore.Value, arg1: MaterialX.PyMaterialXCore.Color4) -> None:
    """mapValueToColor(arg0: MaterialX.PyMaterialXCore.Value, arg1: MaterialX.PyMaterialXCore.Color4) -> None

    Maps a value to a four channel color if it is of the appropriate type.

    Supported types include float, Vector2, Vector3, Vector4, and Color4. If not mapping is possible the color value is set to opaque black.
    """
def requiresImplementation(arg0: MaterialX.PyMaterialXCore.NodeDef) -> bool:
    """requiresImplementation(arg0: MaterialX.PyMaterialXCore.NodeDef) -> bool

    Return whether a nodedef requires an implementation.
    """
def tokenSubstitution(arg0: collections.abc.Mapping[str, str], arg1: str) -> None:
    """tokenSubstitution(arg0: collections.abc.Mapping[str, str], arg1: str) -> None

    Perform token substitutions on the given source string, using the given substitution map.

    Tokens are required to start with '$' and can only consist of alphanumeric characters. The full token name, including '$' and all following alphanumeric character, will be replaced by the corresponding string in the substitution map, if the token exists in the map.
    """
