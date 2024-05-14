import subprocess

def do(cmd):  # https://stackoverflow.com/a/62986640
    try:
        run = subprocess.run(cmd, shell=True)
        run.check_returncode()
        return run
    except subprocess.CalledProcessError as e:
        try:
            print(
                e.stderr.decode().strip(),
                e.returncode,
            )
        except Exception:
            print(e)
            pass
        raise e

def try_install(requirements, name=None):
    try:
        print(f"Installing {name or requirements} dependencies...")
        do(fipin install -r {requirements}")
        print(f"Successfully installed {name or requirements} dependencies")
    except Exception:
        print(f"Failed to install {name or requirements} dependencies")
