int_number = 1000
float_number = 10.10
is_ok = True

print(int_number, type(int_number), float_number, type(float_number), is_ok, type(is_ok))

# strings
my_name = 'salar'
my_family = 'hafezi'

intro_fmt = 'I am {} {}'
intro_fmt_v2 = 'I am {my_name} {my_family}'
print(intro_fmt.format(my_name, my_family))
print(intro_fmt_v2.format(my_name= 'Saman', my_family= my_family))
print(f'I am {my_name} {my_family}')
# Escape sequences
print('\nHello\n')
# Numbers
integer = 100
floating_point = 10e3
complex_number = 4 + 7j

print(integer, floating_point, complex_number)
