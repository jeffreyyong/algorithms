def contains_cycle(first_node):

    # start both runners at tbe beginning
    slow_runner = first_node
    fast_runner = first_node

    # until we hit the end fo the list
    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        # case: fast_runner is about to "lap" slow runner
        if fast_runner is slow_runner:
            return True


    # case: fast_runner hits the end of the list
    return False
