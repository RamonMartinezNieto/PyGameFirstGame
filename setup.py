import cx_Freeze
from cx_Freeze.dist import build_exe

executable = [cx_Freeze.Executable('MainGame.py')]

cx_Freeze.setup(
    name = "SpaceInvaders(?)",
    version = "1.0",
    options = {
        "build_exe": {
            "packages": ["pygame", "random"],
            
            "include_files": ['resources/']
        },
        },
    
    descripcion = "Juego SpaceInvader para prácticar python",
    executables = executable

)