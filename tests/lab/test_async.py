import asyncio

import pytest

from paz.lab.async_example import basic_async_task, cancellable_task, error_prone_task


@pytest.mark.asyncio
async def test_basic_async_task(capsys):
    """
    Unit test for the basic_async_task function.

    This test verifies that the basic_async_task function:
    1. Returns a result within the expected time range (1 to 3 seconds).
    2. Prints the correct start and completion messages.
    3. Includes the correct estimated time in the output.

    The test uses pytest's asyncio marker to handle the asynchronous nature of the function,
    and the capsys fixture to capture and examine the function's console output.

    Args:
        capsys (pytest.CaptureFixture): Pytest fixture for capturing stdout and stderr.

    Raises:
        AssertionError: If any of the test conditions are not met.

    Note:
        This test assumes that the basic_async_task function is imported from 'your_module'.
    """
    # Execute the asynchronous function and capture its result
    result = await basic_async_task(0)

    # Capture the console output generated during the function execution
    captured = capsys.readouterr()

    # Assert that the returned result is within the expected range (1 to 3 seconds)
    assert 1 <= result <= 3, f"Expected result between 1 and 3, but got {result}"

    # Assert that the start message is present in the captured output
    assert "Basic task 0 started" in captured.out, "Start message not found in output"

    # Assert that the completion message is present in the captured output
    assert (
        "Basic task 0 completed" in captured.out
    ), "Completion message not found in output"

    # Assert that the estimated time (which should match the result) is present in the output
    assert (
        f"Estimated time: {result: .2f} seconds" in captured.out
    ), "Estimated time not found or incorrect in output"

    # Note: We don't need to assert the exact completion time in the output,
    # as it's acceptable for it to differ slightly from the returned result due to
    # potential minor discrepancies in timing and string formatting.


@pytest.mark.asyncio
async def test_error_prone_task_success(capsys):
    """
    Test the successful execution of the error_prone_task function.

    This test case verifies that the error_prone_task function behaves correctly
    when it's set to succeed. It checks the return value, ensures proper logging,
    and confirms that cleanup operations are performed.

    The test uses pytest's asyncio marker to handle asynchronous testing and
    the capsys fixture to capture stdout for verification of logged messages.

    Args:
        capsys: A pytest fixture that captures writes to sys.stdout and sys.stderr.

    Raises:
        AssertionError: If any of the test assertions fail.
    """
    # Call the error_prone_task with should_fail=False to ensure it succeeds
    # We use 'await' here because error_prone_task is an async function
    result = await error_prone_task(0, should_fail=False)

    # Capture the output that was printed to stdout during the function execution
    captured = capsys.readouterr()

    # Assert that the result is a string (as expected from a successful task)
    assert isinstance(result, str), "Result should be a string"

    # Check if the result matches the expected output format
    assert result == "Result from task 0", "Unexpected result string"

    # Verify that the task start was logged correctly
    assert "Error-prone task 0 started" in captured.out, "Task start not logged"

    # Confirm that the successful completion was logged
    assert (
        "Error-prone task 0 completed successfully" in captured.out
    ), "Successful completion not logged"

    # Ensure that the cleanup operation was logged, which should happen regardless of success or failure
    assert "Cleanup for task 0" in captured.out, "Cleanup operation not logged"


@pytest.mark.asyncio
async def test_error_prone_task_failure(capsys):
    """
    Test the failure scenario of the error_prone_task function.

    This test case verifies that the error_prone_task function behaves correctly
    when it's set to fail. It checks that the correct exception is raised,
    ensures proper error logging, and confirms that cleanup operations are
    performed even in the case of an error.

    The test uses pytest's asyncio marker to handle asynchronous testing,
    the capsys fixture to capture stdout for verification of logged messages,
    and pytest.raises to check for the expected exception.

    Args:
        capsys: A pytest fixture that captures writes to sys.stdout and sys.stderr.

    Raises:
        AssertionError: If any of the test assertions fail.
    """
    # Use pytest.raises as a context manager to catch the expected exception
    # This also allows us to check the exception message
    with pytest.raises(RuntimeError, match="Simulated error in task 0"):
        # Call error_prone_task with should_fail=True to force an error
        # We use 'await' here because error_prone_task is an async function
        await error_prone_task(0, should_fail=True)

    # Capture the output that was printed to stdout during the function execution
    captured = capsys.readouterr()

    # Verify that the task start was logged correctly
    assert "Error-prone task 0 started" in captured.out, "Task start not logged"

    # Confirm that the error was logged properly
    assert (
        "Error in task 0: Simulated error in task 0" in captured.out
    ), "Error not logged correctly"

    # Ensure that the cleanup operation was logged, which should happen regardless of success or failure
    assert "Cleanup for task 0" in captured.out, "Cleanup operation not logged"


@pytest.mark.asyncio
async def test_cancellable_task_completion(capsys):
    """
    Test the successful completion of the cancellable_task function.

    This test verifies that the cancellable_task function behaves correctly
    when allowed to complete without cancellation. It checks the return value
    and ensures proper logging of task start, completion, and cleanup.

    Args:
        capsys: A pytest fixture that captures writes to sys.stdout and sys.stderr.

    Raises:
        AssertionError: If any of the test assertions fail.
    """
    # Call the cancellable_task with a short duration to ensure quick completion
    result = await cancellable_task(0, 0.5)

    # Capture the output that was printed to stdout during the function execution
    captured = capsys.readouterr()

    # Check if the result matches the expected output format
    assert result == "Result from cancellable task 0", "Unexpected result string"

    # Verify that the task start was logged correctly
    assert "Cancellable task 0 started" in captured.out, "Task start not logged"

    # Confirm that the successful completion was logged
    assert (
        "Cancellable task 0 completed normally" in captured.out
    ), "Normal completion not logged"

    # Ensure that the cleanup operation was logged
    assert (
        "Cleanup for cancellable task 0" in captured.out
    ), "Cleanup operation not logged"


@pytest.mark.asyncio
async def test_cancellable_task_cancellation(capsys):
    """
    Test the cancellation behavior of the cancellable_task function.

    This test verifies that the cancellable_task function responds correctly
    to cancellation. It creates a task, allows it to run briefly, then cancels it.
    The test checks for proper exception raising and logging of task start,
    cancellation, and cleanup.

    Args:
        capsys: A pytest fixture that captures writes to sys.stdout and sys.stderr.

    Raises:
        AssertionError: If any of the test assertions fail.
    """
    # Create a task that will run for 2 seconds (if not cancelled)
    task = asyncio.create_task(cancellable_task(0, 2))

    # Allow the task to run for a short time
    await asyncio.sleep(0.5)

    # Cancel the task
    task.cancel()

    # Attempt to await the cancelled task, expecting a CancelledError
    with pytest.raises(asyncio.CancelledError):
        await task

    # Capture the output that was printed to stdout during the function execution
    captured = capsys.readouterr()

    # Verify that the task start was logged correctly
    assert "Cancellable task 0 started" in captured.out, "Task start not logged"

    # Confirm that the cancellation was logged
    assert "Task 0 was cancelled" in captured.out, "Task cancellation not logged"

    # Ensure that the cleanup operation was logged, even after cancellation
    assert (
        "Cleanup for cancellable task 0" in captured.out
    ), "Cleanup operation not logged"
