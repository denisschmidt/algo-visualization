config = {
    # =============================================================================
    # WINDOW SETTINGS
    # =============================================================================
    "WIDTH": 800,  # window width (pixels); change to None to autoscale window size
    "HEIGHT": 800,  # window height
    "BOX_WIDTH": 26,  # iff "WIDTH" is None each row and column will be "BOX_WIDTH" pixels wide

    # =============================================================================
    # GRID SETTINGS
    # =============================================================================
    "C": 40,  # 4 <= C <= 400 and C must be even
    "R": 40,  # 4 <= R <= 400 and R must be even
    "GRID_COLOR": (150, 150, 150),
    "GRID_THICKNESS": 1,
    "SHOW_GRID": False,  # Turn grid on / off
    "UPDATE_BACKGROUND": False,  # Switches true for one frame when grid or hamcycle changes

    # =============================================================================
    # GAME SPEED SETTINGS
    # =============================================================================
    "SLEEP_TIME": 0.02,  # sleep between iterations to reduce the frame rate
    "LOCK_TIME": 0.2,  # delay between allowed input actions (seconds)

    # =============================================================================
    # HAMILTONIAN CYCLE SETTINGS
    # =============================================================================
    "SHUFFLE": True,  # shuffle the kernel windows before merging sybcycles (True = more random grid)
    "MAX_SIZE": 6,  # 6 <= MAX_SIZE <= 36 the maximum window size for the subdivided array
    "HAM_COLOR": (100, 200, 100),  # color of the ham path
    "HAM_WIDTH": 1,  # width of the hamiltonian cycle path
    "SHOW_PATH": True,
    "SHORTCUTS": True,  # Allows snake to leave the path if it is safe and efficient to do so

    # =============================================================================
    # SNAKE AND FOOD SETTINGS
    # =============================================================================
    "SNAKE_WIDTH": 0.8,  # fraction of min(col_width, row_height)
    "SNAKE_COLOR": (0, 100, 0),
    "CENTER_SNAKE": False,  # start with snake in center of map
    "SNAKE_LENGTH": 20,  # the start length of the snake minimum is 2
    "FOOD_COLOR": (175, 0, 0),
}
