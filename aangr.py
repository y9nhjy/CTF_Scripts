import sys
import angr
p = angr.Project('d3rc4')
st = p.factory.entry_state(
    add_options = { angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
                    angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS}
)
sm = p.factory.simulation_manager(st)


def is_successful(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return 'right'.encode() in stdout_output


def should_abort(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return 'sorry'.encode() in stdout_output


# sm.explore(find=0x402498, avoid=0x402491)
sm.explore(find=is_successful, avoid=should_abort)

if sm.found:
    solution_state = sm.found[0]
    print(solution_state.posix.dumps(sys.stdin.fileno()).decode())
else:
    raise Exception('Could not find the solution')


# print(sm.found[0].posix.dumps(0))
# print(sm.found[0].posix.dumps(sys.stdin.fileno()).decode())