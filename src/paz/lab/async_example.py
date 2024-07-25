"""
Advanced Asynchronous Programming in Python

This module demonstrates key concepts in asynchronous programming using Python's asyncio library,
including error handling, task cancellation, and performance monitoring.

Key Concepts Covered:
1. Coroutines and the Event Loop
2. Concurrent execution of multiple tasks
3. Error handling in asynchronous code
4. Task cancellation and interruption
5. Performance monitoring of asynchronous tasks

Prerequisites:
- Python 3.7+
- Understanding of basic Python concepts and general programming concepts
"""

import asyncio
import random


async def basic_async_task(task_id: int) -> float:
    """
    Simulates an asynchronous task with a random processing time.

    This function demonstrates basic concepts of asynchronous programming
    by simulating a task that takes a random amount of time to complete.
    It uses asyncio.sleep() to mimic a non-blocking operation.

    Args:
        task_id (int): An identifier for the task.

    Returns:
        float: The actual time taken to complete the task.

    Example:
        process_time = await basic_async_task(1)
    """
    # Generate a random processing time between 1 and 3 seconds
    process_time = random.uniform(1, 3)

    # Print the start message with the estimated time
    print(f"Basic task {task_id} started. Estimated time: {process_time: .2f} seconds.")

    # Simulate the task execution by "sleeping" for the generated amount of time
    # This is where a real task would perform its actual work
    await asyncio.sleep(process_time)

    # Print the completion message with the actual time taken
    print(f"Basic task {task_id} completed after {process_time: .2f} seconds.")

    # Return the actual processing time
    return process_time


async def error_prone_task(task_id, should_fail=None):
    """
    An asynchronous function that simulates an error-prone task.

    This function demonstrates error handling, random failures, and cleanup in
    asynchronous programming. It uses asyncio for asynchronous execution and
    random for introducing variability in task duration and failure probability.

    Args:
        task_id (int): An identifier for the task, used in logging.
        should_fail (bool, optional): If provided, determines whether the task
                                      should fail. If None, failure is random.

    Returns:
        str: A result message if the task completes successfully.

    Raises:
        RuntimeError: If the task is set to fail or randomly decides to fail.

    Note:
        The function always performs cleanup in the 'finally' block, regardless
        of whether the task succeeds or fails.
    """
    try:
        # Log the start of the task
        print(f"Error-prone task {task_id} started.")

        # Simulate some asynchronous work with a random duration
        # asyncio.sleep is used instead of time.sleep to allow other tasks to run
        await asyncio.sleep(random.uniform(0.5, 1.5))

        # Determine if the task should fail
        if should_fail is None:
            # If not specified, there's a 50% chance of failure
            should_fail = random.random() < 0.5

        # Simulate a failure if should_fail is True
        if should_fail:
            raise RuntimeError(f"Simulated error in task {task_id}")

        # If we reach here, the task has completed successfully
        print(f"Error-prone task {task_id} completed successfully.")
        return f"Result from task {task_id}"

    except RuntimeError as e:
        # Catch and handle the specific RuntimeError we raised
        print(f"Error in task {task_id}: {str(e)}")
        # Re-raise the exception to propagate it to the caller
        raise

    finally:
        # This block always executes, whether there was an exception or not
        # It's useful for cleanup operations that should happen in both cases
        print(f"Cleanup for task {task_id}")


async def cancellable_task(task_id, duration):
    """
    An asynchronous function that simulates a cancellable task with a specified duration.

    This function demonstrates how to create a task that can be cancelled at any point
    during its execution. It uses a loop to simulate work and checks for cancellation
    regularly. The task can finish normally if not cancelled before its duration expires.

    Args:
        task_id (int): An identifier for the task, used in logging.
        duration (float): The intended duration of the task in seconds.

    Returns:
        str: A result message if the task completes successfully.

    Raises:
        asyncio.CancelledError: If the task is cancelled during a sleep operation.

    Note:
        The function always performs cleanup in the 'finally' block, regardless
        of whether the task completes, is cancelled, or raises an exception.
    """
    try:
        # Log the start of the task with its ID and intended duration
        print(f"Cancellable task {task_id} started. Duration: {duration} seconds")

        # Get the current time to track the task's progress
        start_time = asyncio.get_event_loop().time()

        # Loop until the intended duration has passed
        while asyncio.get_event_loop().time() - start_time < duration:
            # Sleep for a short interval (0.1 seconds)
            # This allows for frequent cancellation checks
            await asyncio.sleep(0.1)

            # Check if the task has been cancelled
            if asyncio.current_task().cancelled():
                print(f"Task {task_id} was cancelled. Cleaning up...")
                # Return early if the task was cancelled
                return

        # If the loop completes without cancellation, the task finished normally
        print(f"Cancellable task {task_id} completed normally.")
        return f"Result from cancellable task {task_id}"

    except asyncio.CancelledError:
        # This block catches cancellation that occurs during the asyncio.sleep() call
        print(f"Task {task_id} was cancelled while sleeping.")
        # Re-raise the CancelledError to propagate it to the caller
        raise

    finally:
        # This block always executes, whether the task completes, is cancelled, or raises an exception
        # It's useful for cleanup operations that should happen in all cases
        print(f"Cleanup for cancellable task {task_id}")
