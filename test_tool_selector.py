import subprocess
import sys

def test_cli_help():
    try:
        result = subprocess.run([sys.executable, 'tool_selector.py', '--help'],
                               capture_output=True, text=True, check=True)
        print("CLI help command works correctly.")
        print("Output:")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"CLI help command failed with error: {e}")
        print("Output:")
        print(e.stdout)
        print("Error:")
        print(e.stderr)
        return False

def test_import():
    try:
        import tool_selector
        print("Tool selector module imports successfully.")
        return True
    except ImportError as e:
        print(f"Failed to import tool selector: {e}")
        return False

def main():
    print("Running tests for tool_selector.py...")
    import_success = test_import()
    cli_help_success = test_cli_help()

    if import_success and cli_help_success:
        print("All tests passed!")
        return 0
    else:
        print("Some tests failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())