from pyatool import PYAToolkit


# real function should contains an argument named 'toolkit'
def test_b(toolkit):
    return 'i am test_b, running on {}'.format(toolkit.device_id)


# bind adb command
PYAToolkit.bind_cmd(func_name='test_a', command='shell pm list package | grep google')
# or a real function
PYAToolkit.bind_func(real_func=test_b)

# init
d = PYAToolkit('123456F')

# and call it
result = d.test_a()
# output (may be different)
# package:com.google.android.webview

# and call it too
result = d.test_b()
# i am test_b, running on 123456F

# show all functions
all_functions = d.current_function()
print(all_functions)

# use build-in function
d.hello_world()
d.show_package()
d.get_current_activity()
d.install_from(url=r'https://github.com/williamfzc/simhand2/releases/download/v0.1.2/app-debug-androidTest.apk')
