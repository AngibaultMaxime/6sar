from cx_Freeze import setup, Executable

icon_path = "piece-de-monnaie.ico"

setup(
    name = "6sar",
    version = "0.2",
    description = "Encryption et Decryption Cesar",
    executables = [Executable("main.py", icon = icon_path)]
)