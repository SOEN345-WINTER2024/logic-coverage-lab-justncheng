from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connect to the device
device = MonkeyRunner.waitForConnection()

# Dictionary mapping button names to their screen coordinates
buttons = {
    '0': (108, 385),
    '1': (10, 317),
    '2': (108, 317),
    '3': (206, 317),
    '4': (10, 248),
    '5': (108, 248),
    '6': (206, 248),
    '7': (10, 180),
    '8': (108, 180),
    '9': (206, 180),
    '*': (304, 180),
    '/': (304, 248),
    '+': (304, 385),
    '-': (304, 317),
    'C': (10, 453), # Clear button
    '=': (206, 385),
    '.': (10, 385)
}

# Function to press a button
def press_button(button):
    x, y = buttons[button]
    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.5)  # Adjust delay as needed

# Node Coverage: Press each button at least once
def node_coverage():
    for button in buttons:
        press_button(button)
        MonkeyRunner.sleep(1)  # Add delay to observe each press

# Edge Coverage: Perform basic operations
def edge_coverage():
    # Example: Performing addition
    press_button('1')
    press_button('+')
    press_button('1')
    press_button('=')
    press_button('C')  # Clear after operation

# Edge-Pairs Coverage: Sequence of operations without clearing in between
def edge_pairs_coverage():
    # Example: 1 + 1, then clear, then 2 - 1
    edge_coverage()  # Perform first operation and clear
    press_button('2')
    press_button('-')
    press_button('1')
    press_button('=')
    press_button('C')

# Running the tests
node_coverage()
edge_coverage()
edge_pairs_coverage()
