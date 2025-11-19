#!/bin/bash

DAY=$(date +%d)   # Default is current day with leading zero
ACTION="t"        # Default action is tests

while [[ $# -gt 0 ]]; do
    case $1 in
        -d|--day)
            DAY="$2"
            shift 2
            ;;
        -a|--action)
            ACTION="$2"
            shift 2
            ;;
        *)
            if [[ -z "${FIRST_ARG:-}" ]]; then
                FIRST_ARG="$1"
            elif [[ -z "${SECOND_ARG:-}" ]]; then
                SECOND_ARG="$1"
            fi
            shift
            ;;
    esac
done

DAY="${FIRST_ARG:-$DAY}"
ACTION="${SECOND_ARG:-$ACTION}"

if [[ "$DAY" =~ ^[0-9]$ ]]; then
    DAY="0${DAY}"
fi

ACTION=$(echo "$ACTION" | tr '[:upper:]' '[:lower:]')

FOLDER="src/advent-of-code-2025/solutions/day${DAY}"

if [ ! -d "$FOLDER" ]; then
    echo "Error: Folder '$FOLDER' does not exist"
    exit 1
fi

if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Error: Virtual environment not found at 'venv/bin/activate'"
    exit 1
fi

cd "$FOLDER" || exit 1

case $ACTION in
    t|test|tests)
        echo "Running tests for day ${DAY}..."
        python -m tests --verbose
        ;;
    s|solution|sol)
        echo "Running solution for day ${DAY}..."
        python -m solution
        ;;
    *)
        echo "Error: Invalid action '$ACTION'. Use 't' for tests or 's' for solution"
        deactivate
        exit 1
        ;;
esac

EXIT_CODE=$?

deactivate

cd - > /dev/null

exit $EXIT_CODE
