
# 🎄 Advent of Code

A collection of my Advent of Code solutions over the years.  
Each year’s folder contains Python solutions for that year’s challenges.

# 📊 Yearly Progress

| **Year** | **Stars** | **Problems** | **Progress** | **Notes** |
|:--------:|:---------:|:------------:|:-------------:|:---------:|
| [**2025**](https://github.com/lambertinialessandro/adventofcode/tree/main/2025) |  `20/24` 🌖 |  `11/12` 🧠 | █████████████████▒░░ &nbsp; 86% | Second year! 🔥 |
| [**2024**](https://github.com/lambertinialessandro/adventofcode/tree/main/2024) | `45/50` 🌕 | `25/25` 🎯 | ██████████████████▒░ &nbsp; 92% | First year! 🔥 |
| [**2023**](https://github.com/lambertinialessandro/adventofcode/tree/main/2023) | `16/50` 🌘 | `10/25` 🧠 | ██████▓░░░░░░░░░░░░░ &nbsp; 34% | Some unfinished business… |
| [**2022**](https://github.com/lambertinialessandro/adventofcode/tree/main/2022) |  `0/50` 🌑 |  `0/25` ❌ | ░░░░░░░░░░░░░░░░░░░░ &nbsp; 0% | |
| [**2021**](https://github.com/lambertinialessandro/adventofcode/tree/main/2021) |  `0/50` 🌑 |  `0/25` ❌ | ░░░░░░░░░░░░░░░░░░░░ &nbsp; 0% | |
| [**2020**](https://github.com/lambertinialessandro/adventofcode/tree/main/2020) |  `0/50` 🌑 |  `0/25` ❌ | ░░░░░░░░░░░░░░░░░░░░ &nbsp; 0% | |
| [**2019**](https://github.com/lambertinialessandro/adventofcode/tree/main/2019) |  `0/50` 🌑 |  `0/25` ❌ | ░░░░░░░░░░░░░░░░░░░░ &nbsp; 0% | |
| [**2018**](https://github.com/lambertinialessandro/adventofcode/tree/main/2018) |  `0/50` 🌑 |  `0/25` ❌ | ░░░░░░░░░░░░░░░░░░░░ &nbsp; 0% | |
| [**2017**](https://github.com/lambertinialessandro/adventofcode/tree/main/2017) |  `0/50` 🌑 |  `0/25` ❌ | ░░░░░░░░░░░░░░░░░░░░ &nbsp; 0% | |
| [**2016**](https://github.com/lambertinialessandro/adventofcode/tree/main/2016) |  `0/50` 🌑 |  `0/25` ❌ | ░░░░░░░░░░░░░░░░░░░░ &nbsp; 0% | |
| [**2015**](https://github.com/lambertinialessandro/adventofcode/tree/main/2015) |  `0/50` 🌑 |  `0/25` ❌ | ░░░░░░░░░░░░░░░░░░░░ &nbsp; 0% | |

# 🧭 About

Advent of Code is an annual set of holiday-themed programming puzzles released every December.
Each challenge helps improve problem-solving, algorithmic thinking, and coding efficiency.

This repository:
- **Organized solutions** for each year. Each year folder contains its own `README.md` detailing daily performance and notes.
- **Automation scripts** in the `commands/` folder to set up problems, download inputs, and scaffold solutions.
- **Programming language:** Python 3.12

# 🚀 Setup & Deployment

Follow these steps to get started locally:

## 1. Clone the repository

```bash
git clone https://github.com/lambertinialessandro/adventofcode.git
cd adventofcode
```

## 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/macOS
# OR
.venv\Scripts\activate      # On Windows
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure environment variables

Copy the environment template and edit your personal settings

```bash
cp .env.template .env
```

Then open `.env` in your text editor and fill in any required values

```bash
AOC_SESSION=your_session_id
USER_AGENT={project name} (Python requests; +{repository link}; {contact info})
```

> 💡 You can get your Advent of Code session cookie from your browser’s DevTools after logging in at [adventofcode.com](https://adventofcode.com).

## 5. Run automation commands (optional)

The `commands/` folder contains helper scripts for common tasks, such as fetching problem inputs automatically.

### Command-line usage:

```bash
python ./commands/start_problem.py 2024 01
```

### GUI usage:

`aoc_manager.py` provides a simple interface to run these tasks visually:

```bash
python ./aoc_manager.py
```

## 6. Run solutions

Navigate to a year’s folder and execute the solution for a given day:

```bash
cd 2024/01
python main_part_01.py
```

# 🗂️ Directory Structure

```txt
adventofcode/
├─ 2024/
│   ├─ 01/
│   ├─ ...
│   └─ README.md
├─ ...
│
├─ commands/           # Automation scripts CLI
│   └─ README.md
├─ utils/
├─ requirements.txt    # Global dependencies
├─ aoc_manager.py      # Automation scripts GUI
├─ .env.template       # Environment variable template
└─ README.md
```

# 🤝 Contributing

Contributions are welcome! You can help by:
- Improving automation scripts in the commands/ folder.
- Fixing bugs or optimizing existing solutions.

How to contribute:
1. Fork the repository.
1. Create a new branch: git checkout -b feature/my-solution
1. Make your changes.
1. Submit a pull request with a clear description of your changes.

🌕🌖🌗🌘🌑

