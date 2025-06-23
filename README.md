# 🐍 Snake Game in Python using Tkinter

A simple yet classic implementation of the **Snake Game** using Python's `tkinter` library for GUI. This project demonstrates basic GUI development, object-oriented programming, and game loop logic.

---

## 🎮 Game Features

- Grid-based snake movement
- Randomized food generation
- Increasing score counter
- Collision detection (walls and self)
- Game Over screen
- Arrow key controls
- Window auto-centering

---

## 📦 Requirements

- Python 3.x
- Tkinter (included by default with most Python distributions)

No external libraries are needed.

---

## 🚀 How to Run

1. **Clone this repository** or copy the code into a `.py` file (e.g., `snake_game.py`).
2. **Run the script** using your terminal or preferred Python IDE:
   ```bash
   python snake_game.py
   ```

The game window will appear in the center of your screen. Use arrow keys to control the snake.

---

## 🎮 Controls

- ⬆️ Up Arrow – Move Up  
- ⬇️ Down Arrow – Move Down  
- ⬅️ Left Arrow – Move Left  
- ➡️ Right Arrow – Move Right  

*Note: The snake cannot reverse direction directly (e.g., from left to right).*

---

## 📐 Game Configuration

- `GAME_WIDTH`: Width of the game canvas
- `GAME_HEIGHT`: Height of the game canvas
- `SPACE_SIZE`: Size of each grid cell (snake/food)
- `SPEED`: Lower = faster game loop
- `BODY_PARTS`: Initial length of the snake
- `SNAKE_COLOR` / `FOOD_COLOR` / `BACKGROUND_COLOR`: UI customization

You can modify these constants at the top of the file to tweak the gameplay.

---

## 🧠 Code Structure

- `Snake` class – Manages snake's body and initialization
- `Food` class – Handles random food generation
- `next_turn()` – Main game loop updating positions, detecting food, and redrawing
- `change_direction()` – Captures and applies user input
- `check_collisions()` – Detects wall and self collisions
- `game_over()` – Displays Game Over message and halts game loop

---

## 🛠️ Future Improvements

- Add difficulty levels
- Add high-score tracking
- Add snake growth animation
- Add sound effects
- Convert to `.exe` using tools like `pyinstaller`

---

## 🧱 Packaging to .exe (Optional)

To create a standalone `.exe` file:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed snake_game.py
```

The executable will be located in the `dist/` folder.

