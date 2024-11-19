from pathlib import Path
import shutil

Path("test_dir").mkdir(exist_ok=True)

with open("test_dir/arquivo.txt", "w") as f:
    f.write("Contedo do arquivo 1")

shutil.copy("test_dir/arquivo.txt", "test_dir/arquivo2.txt")

Path("test_dir/arquivo2.txt").rename("test_dir/arquivo_renomeado.txt")

Path("test_dir/arquivo.txt").unlink()