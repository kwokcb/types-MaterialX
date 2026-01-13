import MaterialX.PyMaterialXCore
import MaterialX.PyMaterialXGenShader

class SlangShaderGenerator(MaterialX.PyMaterialXGenShader.HwShaderGenerator):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator:
        """create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator"""
    def generate(self, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader:
        """generate(self: MaterialX.PyMaterialXGenSlang.SlangShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader

        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.
        """
    def getTarget(self) -> str:
        """getTarget(self: MaterialX.PyMaterialXGenSlang.SlangShaderGenerator) -> str

        Return a unique identifier for the target this generator is for.
        """
    def getVersion(self) -> str:
        """getVersion(self: MaterialX.PyMaterialXGenSlang.SlangShaderGenerator) -> str

        Return the version string for the Slang version this generator is for.
        """
