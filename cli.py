import os
import subprocess
import shutil
import platform


print("Setting up a new Python project with uv and VS Code...")

# ASCII rocket art
rocket_art = """
       /\\
      /  \\
     |    |
     | MCP|
    /| [] |\\
   / |    | \\
  /  |    |  \\
 |  /|    |\\  |
 | / |____| \\ |
 |/  [ ][ ]  \\|
/    [ ][ ]    \\
|   ________   |
|  |________|  |
 \\ \\  ||||  / /
  \\_\\ |||| /_/
      ||||
     //||\\\\
    // || \\\\
   //  ||  \\\\
  /_   ||   _\\
     \\=====/
      \\===/
    \\=/
     V
"""
print(rocket_art)


# 1. Define project name and path
project_name = input("Enter your new project name: ")
project_path = os.path.join(os.getcwd(), project_name)
# 2. Create project folder
os.makedirs(project_path, exist_ok=True)

# 3. Initialize uv environment
if shutil.which("uv"):
    try:
        subprocess.run(["uv", "init"], cwd=project_path, check=True)
        print("✓ UV environment initialized")
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to initialize uv environment: {e}")
else:
    print("✗ 'uv' command not found. Please install uv first: https://github.com/astral-sh/uv")

# 4. Install dependencies (example: pandas, fastapi)
if shutil.which("uv"):
    try:
        subprocess.run(["uv", "add", "mcp[cli]"], cwd=project_path, check=True)
        print("✓ Dependencies installed")
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install dependencies: {e}")
else:
    print("✗ 'uv' command not found. Skipping dependency installation.")

# 5. Open VS Code in the project folder
if platform.system() in ["Linux", "Darwin"]:  # Unix/Mac
    if shutil.which("code"):
        try:
            subprocess.run(["code", project_path], check=True)
            print("✓ VS Code opened")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to open VS Code: {e}")
    else:
        print("✗ 'code' command not found. Please open the project manually or add VS Code to PATH.")
        print(f"Project created at: {project_path}")
else:  # Windows
    os.system(f'code "{project_path}"')
    print("✓ VS Code opened")


