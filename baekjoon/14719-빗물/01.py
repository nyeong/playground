from sys import stdin
height, width = map(int, stdin.readline().split())
block_heights = list(map(int, stdin.readline().split()))

water_blocks = 0
for level in range(height):
    is_block_open = False
    maybe_water = 0
    for i, block_height in enumerate(block_heights):
        if level >= block_height:
            if is_block_open:
                maybe_water += 1
        else:
            is_block_open = True
            if maybe_water:
                water_blocks += maybe_water
                maybe_water = 0
print(water_blocks)
