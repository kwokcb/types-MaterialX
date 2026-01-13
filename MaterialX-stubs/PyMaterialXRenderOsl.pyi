import MaterialX.PyMaterialXFormat
import MaterialX.PyMaterialXGenShader
import MaterialX.PyMaterialXRender
import collections.abc
import typing
import typing_extensions
from typing import ClassVar, overload

class OslRenderer(MaterialX.PyMaterialXRender.ShaderRenderer):
    OSL_CLOSURE_COLOR_STRING: ClassVar[str] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def captureImage(self, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image:
        """captureImage(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image

        Capture the current rendered output as an image.
        """
    def compileOSL(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """compileOSL(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Compile OSL code stored in a file.

        Args:
            oslFilePath: OSL file path.
        """
    @staticmethod
    def create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -> OslRenderer:
        """create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderOsl.OslRenderer

        Create an OSL renderer instance.
        """
    @overload
    def createProgram(self, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None:
        """createProgram(*args, **kwargs)
        Overloaded function.

        1. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        2. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: collections.abc.Mapping[str, str]) -> None
        """
    @overload
    def createProgram(self, arg0: collections.abc.Mapping[str, str]) -> None:
        """createProgram(*args, **kwargs)
        Overloaded function.

        1. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        2. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: collections.abc.Mapping[str, str]) -> None
        """
    def initialize(self, renderContextHandle: typing_extensions.CapsuleType = ...) -> None:
        """initialize(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, renderContextHandle: typing_extensions.CapsuleType = None) -> None

        Internal initialization required for program validation and rendering.

        An exception is thrown on failure. The exception will contain a list of initialization errors.
        """
    def render(self) -> None:
        '''render(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -> None

        Render OSL program to disk.

        This is done by using either "testshade" or "testrender". Currently only "testshade" is supported.

        Usage of both executables requires compiled source (.oso) files as input. A shader output must be set before running this test via the setOslOutputName() method to ensure that the appropriate .oso files can be located.
        '''
    def setOslCompilerExecutable(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOslCompilerExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Set the path to the OSL executable.

        Args:
            executableFilePath: Path to OSL compiler executable
        """
    def setOslIncludePath(self, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None:
        """setOslIncludePath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None

        Set the search locations for OSL include files.

        Args:
            dirPath: Include path(s) for the OSL compiler. This should include the path to stdosl.h.
        """
    def setOslOutputFilePath(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOslOutputFilePath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Set the location where compiled OSL files will reside.

        Args:
            dirPath: Path to output location
        """
    def setOslShaderName(self, arg0: str) -> None:
        """setOslShaderName(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: str) -> None

        Set the name of the shader to be used for the input XML scene file.

        Args:
            shaderName: Name of shader
        """
    def setOslShaderOutput(self, arg0: str, arg1: str) -> None:
        """setOslShaderOutput(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: str, arg1: str) -> None

        Set the OSL shader output.

        Args:
            outputName: Name of shader output
            outputType: The MaterialX type of the output
        """
    def setOslTestRenderExecutable(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        '''setOslTestRenderExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Set the path to the OSL rendering tester.

        Args:
            executableFilePath: Path to OSL "testrender" executable
        '''
    def setOslTestRenderSceneTemplateFile(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOslTestRenderSceneTemplateFile(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Set the XML scene file to use for testrender.

        This is a template file with the following tokens for replacement: shader% : which will be replaced with the name of the shader to use shader_output% : which will be replace with the name of the shader output to use templateFilePath Scene file name

        Args:
            templateFilePath: Scene file name
        """
    def setOslTestShadeExecutable(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        '''setOslTestShadeExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Set the path to the OSL shading tester.

        Args:
            executableFilePath: Path to OSL "testshade" executable
        '''
    def setOslUtilityOSOPath(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOslUtilityOSOPath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Set the search path for dependent shaders (.oso files) which are used when rendering with testrender.

        Args:
            dirPath: Path to location containing .oso files.
        """
    def setShaderParameterOverrides(self, arg0: collections.abc.Sequence[str]) -> None:
        """setShaderParameterOverrides(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: collections.abc.Sequence[str]) -> None

        Set shader parameter strings to be added to the scene XML file.

        These strings will set parameter overrides for the shader.
        """
    def useTestRender(self, arg0: bool) -> None:
        """useTestRender(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: bool) -> None

        Used to toggle to either use testrender or testshade during render validation By default testshade is used.

        Args:
            useTestRender: Indicate whether to use testrender.
        """
    def validateInputs(self) -> None:
        """validateInputs(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -> None

        Validate inputs for the compiled OSL program.

        Note: Currently no validation has been implemented.
        """
