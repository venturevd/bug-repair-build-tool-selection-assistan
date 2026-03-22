import argparse

def main():
    parser = argparse.ArgumentParser(description='Tool-Selection Assistant')
    parser.add_argument('--task', type=str, required=True, help='Description of the task')
    parser.add_argument('--tools', type=str, nargs='+', help='List of available tools')
    args = parser.parse_args()

    print(f"Task: {args.task}")
    print("Available tools:")
    for tool in args.tools:
        print(f"- {tool}")

if __name__ == "__main__":
    main()