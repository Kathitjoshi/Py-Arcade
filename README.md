# Retro Game Engine 🎮

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/retro-game-engine)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-black.svg)](https://github.com/psf/black)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/yourusername/retro-game-engine/graphs/commit-activity)

A collection of classic arcade-style games built with Python and Pygame, featuring a retro Game Boy-inspired aesthetic with a 160x144 pixel resolution scaled up for modern displays.

## 🎯 Features

- **Four Classic Games**: Racer, Brick Breaker, Pong, and Maze Runner
- **Three Difficulty Levels**: Easy, Medium, and Hard for each game
- **Retro Aesthetic**: Game Boy-inspired 160x144 resolution with 3x scaling
- **Simple Controls**: Keyboard-based controls for all games
- **Score Tracking**: Keep track of your performance in each game
- **Game Selection Menu**: Easy-to-use interface for switching between games

## 🎮 Games Included

### 🏎️ Racer
Navigate your car through oncoming traffic! Use left and right arrow keys to dodge red cars and rack up points.

**Controls**: 
- `←` / `→` Arrow keys to move left/right

### 🧱 Brick Breaker
Classic brick-breaking action! Control the paddle to keep the ball in play and destroy all the bricks.

**Controls**: 
- `←` / `→` Arrow keys to move paddle

### 🏓 Pong
Take on the computer in this timeless classic! First to 15 points wins.

**Controls**: 
- `↑` / `↓` Arrow keys to move paddle

### 🏃 Maze Runner
Navigate through increasingly complex mazes to reach the green exit!

**Controls**: 
- `↑` / `↓` / `←` / `→` Arrow keys to move

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Pygame 2.0 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/retro-game-engine.git
cd retro-game-engine
```

2. Install required dependencies:
```bash
pip install pygame
```

3. Run the game:
```bash
python game_engine.py
```

## 🎯 How to Play

1. Run the game to see the main menu
2. Press number keys to select a game:
   - `1` - Racer
   - `2` - Brick Breaker
   - `3` - Pong
   - `4` - Maze Runner
3. Use letter keys to change difficulty:
   - `E` - Easy
   - `M` - Medium
   - `H` - Hard
4. Each game will display its own instructions when started

## 🛠️ Technical Details

- **Resolution**: 160x144 pixels (Game Boy resolution) scaled 3x to 480x432
- **Frame Rate**: 60 FPS
- **Color Palette**: Classic retro colors (white, black, green, red, blue, etc.)
- **Architecture**: Modular design with separate functions for each game

## 📁 Project Structure

```
retro-game-engine/
│
├── game_engine.py          # Main game engine and all game implementations
├── README.md              # This file
└── LICENSE               # MIT License (optional)
```

## 🎨 Customization

The game engine is designed to be easily customizable:

- **Colors**: Modify the color constants at the top of the file
- **Difficulty**: Adjust speed and spawn rates in each game function
- **Resolution**: Change `SCREEN_WIDTH`, `SCREEN_HEIGHT`, and `SCALE` constants
- **Controls**: Modify key bindings in each game's event handling

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

- Add new games to the engine
- Improve existing game mechanics
- Add sound effects and music
- Implement high score saving
- Create additional difficulty levels
- Improve the user interface

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📋 Roadmap

- [ ] Add sound effects and background music
- [ ] Implement high score persistence
- [ ] Add more games (Snake, Tetris, Space Invaders)
- [ ] Create sprite-based graphics
- [ ] Add gamepad controller support
- [ ] Implement pause functionality
- [ ] Add animation effects

## 🐛 Known Issues

- None currently reported

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic Game Boy games
- Built with the excellent [Pygame](https://www.pygame.org/) library
- Thanks to the retro gaming community for inspiration

## 📊 Stats

![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/retro-game-engine)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/yourusername/retro-game-engine)
![Lines of code](https://img.shields.io/tokei/lines/github/yourusername/retro-game-engine)

---

**Enjoy the games! 🎮** If you like this project, please give it a ⭐ star on GitHub!
