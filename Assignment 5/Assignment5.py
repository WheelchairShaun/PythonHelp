# Diamond

# Top half loop
for topRows in range(1, 30):
    
    # Left padding
    for whiteSpace in range(30 - topRows, 1, -1):
        print(' ', end = '')
    
    # stars
    for stars in range(1, topRows + 1):
        print('*', end = ' ')

    # End each row
    print()

# Bottom half loop
for bottomRows in range(0, 30, 1):
    
    # Padding
    for space in range(0 , 1 + bottomRows):
        print(' ', end='')

    # Stars
    for stars in range(1, 29 - bottomRows):
        print('*', end = ' ')

    # End each row
    print()

print()
