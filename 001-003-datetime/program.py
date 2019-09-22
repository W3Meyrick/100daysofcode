import datetime


def print_header():
    print('--------------------------------------')
    print('       DAILY POMODORO PLANNER')
    print('--------------------------------------')
    print()


def add_task(tasks):
    if len(tasks) < 8:
        task = input("Please enter task name: ")
        tasks.append(task)
    else:
        print("Maximum tasks per day reached.")
    return tasks


def start_session(tasks, pomodoro=0):
    """
    Simple Pomodoro timer by Luke Meyrick.
    """
    task_length = datetime.timedelta(seconds=10)
    short_break = datetime.timedelta(seconds=5)
    long_break = datetime.timedelta(seconds=10)
    session_start_time = datetime.datetime.now()
    runs_completed = 0

    # Objective is to play with time and date rather than make clean and usable code.
    # Below would need refactoring in to functions or maybe create a Pomodoro class
    # as well as some kind of OS specific reminder alert.

    # Pomodoro starts
    if runs_completed == 0:
        print('Session started at {}'.format(session_start_time))

    for task in tasks:
        runs_completed += 1
        task_start_time = datetime.datetime.now()
        task_timer = task_start_time + task_length
        update_interval = task_start_time - datetime.timedelta(seconds=15)

        print('Starting Pomodoro: #{} {} at {}'.format(runs_completed, task, task_start_time))

        while (task_timer - datetime.datetime.now()) > datetime.timedelta(seconds=0):
            if (datetime.datetime.now() - update_interval) > datetime.timedelta(seconds=15):
                time_remaining = task_timer - datetime.datetime.now()
                print("Time remaining: {}".format(time_remaining))
                update_interval = datetime.datetime.now()

        if runs_completed == 4:
            print("Starting Long Break...")
            break_start_time = datetime.datetime.now()
            update_interval = break_start_time - datetime.timedelta(seconds=15)
            long_break_timer = break_start_time + long_break

            while (long_break_timer - datetime.datetime.now()) > datetime.timedelta(seconds=0):
                if (datetime.datetime.now() - update_interval) > datetime.timedelta(seconds=15):
                    time_remaining = long_break_timer - datetime.datetime.now()
                    print("Time remaining: {}".format(time_remaining))
                    update_interval = datetime.datetime.now()
        else:
            print("Starting Short Break...")
            break_start_time = datetime.datetime.now()
            update_interval = break_start_time - datetime.timedelta(seconds=15)
            short_break_timer = break_start_time + short_break

            while (short_break_timer - datetime.datetime.now()) > datetime.timedelta(seconds=0):
                if (datetime.datetime.now() - update_interval) > datetime.timedelta(seconds=15):
                    time_remaining = short_break_timer - datetime.datetime.now()
                    print("Time remaining: {}".format(time_remaining))
                    update_interval = datetime.datetime.now()

        # Pomodoro ends
        task_end_time = datetime.datetime.now()
        print('Starting Pomodoro: #{} {} at {}'.format(runs_completed, task, task_start_time))
        input("Press Enter to continue...")

    return


def main():
    print_header()

    print('What do you want to do with your task list?')

    cmd = 'EMPTY'
    tasks = 'EMPTY'

    while cmd != 'x' and cmd:
        cmd = input('[S]tart session, [A]dd task, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 's':
            start_session(tasks)
        elif cmd == 'a':
            if tasks == 'EMPTY':
                tasks = []
                add_task(tasks)
            else:
                add_task(tasks)
        elif cmd != 'x' and cmd:
            print("Sorry, unrecognised choice: '{}'.".format(cmd))


if __name__ == '__main__':
    main()
