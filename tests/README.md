# Test Structure

This directory contains the refactored test suite organized by functionality and modules.

## Directory Structure

```
tests/
├── conftest.py                    # Shared pytest fixtures
├── unit/                          # Unit tests
│   ├── asyncio/                   # Tests for asyncio functionality
│   │   ├── test_async_violation.py           # AsyncViolation model tests
│   │   ├── test_async_check_result.py        # AsyncCheckResult model tests
│   │   ├── test_async_definition_collector.py # AsyncDefinitionCollector tests
│   │   ├── test_async_function_analyzer.py   # AsyncFunctionAnalyzer tests
│   │   └── test_async_checker.py             # AsyncChecker main class tests
│   └── cli/                       # Tests for CLI functionality
│       └── test_check_await_cli.py           # CLI command tests
└── integration/                   # Integration tests
    └── test_async_checker_integration.py     # End-to-end integration tests
```

## Test Categories

### Unit Tests

#### AsyncIO Module Tests (`tests/unit/asyncio/`)

- **test_async_violation.py**: Tests for the `AsyncViolation` Pydantic model
  - Validation of required fields
  - Type checking for line/column numbers
  - Invalid violation type handling

- **test_async_check_result.py**: Tests for the `AsyncCheckResult` model
  - Auto-computation of violation counts and pass status
  - Serialization capabilities
  - Validation constraints

- **test_async_definition_collector.py**: Tests for collecting async definitions
  - Async function detection
  - Async method detection in classes
  - Import tracking (modules and functions)
  - Known asyncio function recognition

- **test_async_function_analyzer.py**: Tests for analyzing function calls
  - Missing await detection in async functions
  - Missing asyncio handling in sync functions
  - Coroutine return tracking
  - Complex expression analysis
  - asyncio.gather context handling

- **test_async_checker.py**: Tests for the main checker class
  - File checking with and without violations
  - Directory checking with exclusions
  - Syntax error handling
  - Different violation types

#### CLI Module Tests (`tests/unit/cli/`)

- **test_check_await_cli.py**: Tests for the command-line interface
  - Human-readable output format
  - JSON output format
  - File and directory checking
  - Exclusion patterns
  - Error handling

### Integration Tests (`tests/integration/`)

- **test_async_checker_integration.py**: End-to-end testing scenarios
  - Real-world code patterns (FastAPI-like)
  - Complex asyncio usage patterns
  - Class-based async patterns
  - Nested data structures with coroutines
  - Full project structure testing
  - Type annotation integration

## Test Naming Convention

Tests are now named by functionality rather than line numbers:

- `test_detect_missing_await_in_async_function()` instead of `test_line_225_226()`
- `test_complex_coroutine_expressions()` instead of `test_line_502_505()`
- `test_json_output_format()` instead of `test_cli_json_validation()`

## Running Tests

```bash
# Run all tests
pytest tests/

# Run only unit tests
pytest tests/unit/

# Run only integration tests
pytest tests/integration/

# Run tests for a specific module
pytest tests/unit/asyncio/

# Run tests for CLI
pytest tests/unit/cli/

# Run with coverage
pytest tests/ --cov=kairix_devtools
```

## Test Fixtures

The `conftest.py` file provides shared fixtures:

- `temp_python_file`: Creates temporary Python files for testing
- `temp_directory`: Creates temporary directories for testing

These fixtures automatically handle cleanup after tests complete.
