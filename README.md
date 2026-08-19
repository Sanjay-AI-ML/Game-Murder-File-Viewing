# 🕵️ Murder File Viewing Game (Python)

An immersive Python-based detective game where players explore files, decode evidence, and uncover clues to solve a murder mystery. This project demonstrates practical file handling, menu-driven interfaces, and narrative game design.

---

## 🎮 What You're Doing

You are a detective investigating a murder. The crime scene has left behind evidence scattered across different files:
- **Admin files** — Case records, witness statements
- **Player evidence** — Clues, decoded messages, suspicious documents
- **Decoded data** — BMP images and extracted binary evidence

Your mission: **Explore the files, decode clues, and solve the mystery!**

---

## 🚀 Quick Start

### Requirements
- Python 3.8+
- No external dependencies (built-in libraries only)

### Installation & Run

```bash
# Clone the repo
git clone https://github.com/Sanjay-AI-ML/Game-Murder-File-Viewing.git
cd Game-Murder-File-Viewing

# Run the game
python main.py
```

The game starts immediately with a welcome message and command prompt.

---

## 🎯 Gameplay

### Core Mechanics
1. **Explore Files** — Use commands to open and read different files
2. **Gather Clues** — Each file contains hints about the murder
3. **Decode Evidence** — Extract and decode messages from files
4. **Progress** — Advance through stages as you uncover secrets
5. **Solve the Mystery** — Combine all clues to identify the killer

### Command System

| Command | Purpose | Example |
|---------|---------|---------|
| `list` | View available files | `list` |
| `open <file>` | Read file contents | `open witness_statement.txt` |
| `decode <file>` | Decode binary/encrypted file | `decode evidence.bmp` |
| `check <person>` | Verify suspect alibi | `check alice` |
| `accuse <person>` | Make your final accusation | `accuse bob` |
| `help` | Show all commands | `help` |
| `exit` | Quit game | `exit` |

### Example Gameplay Session
```
>> list
Available files:
  - witness_statement.txt
  - crime_scene_notes.txt
  - suspect_alibis.txt
  - encoded_evidence.bmp

>> open witness_statement.txt
[WITNESS ACCOUNT]
"I saw someone in a red jacket near the scene at 11 PM..."

>> decode encoded_evidence.bmp
[DECODING...]
Hidden message found: "Meeting at midnight behind the warehouse"

>> accuse suspect_name
[CHECKING...]
Correct! You've solved the mystery!
```

---

## 📁 Project Structure

```
Game-Murder-File-Viewing/
├── main.py                    # Entry point and game loop
├── stage_manager.py           # Game progression and file management
├── functions.py               # Helper functions for decoding/opening files
├── decoding_functions.py      # Image/binary decoding logic
├── manage_admin.py            # Admin file operations
├── Admin_files/               # Case files (witness records, timelines)
├── Player/                    # Player-discovered evidence
├── Files/                     # Game data (suspects, clues, messages)
└── README.md                  # This file
```

---

## 🧠 Code Architecture

### Main Game Loop (`main.py`)
```python
while True:
    user_input = input(">> ").strip().casefold()
    command = parse_command(user_input)
    
    if command in commands:
        result = execute_command(command)
        print(result)
        update_game_stage()
    else:
        suggest_close_match(command)
```

### Game Progression
- **Stage 1** — Tutorial and initial file access
- **Stage 2** — Suspect investigation phase
- **Stage 3** — Decoder/evidence analysis phase
- **Stage 4** — Final accusation

Each command you use unlocks new information and progresses the story.

### File Handling Techniques Demonstrated
- **Read file contents** — `open()`, `.read()`, parsing text
- **Decode binary data** — Extract hidden messages from images
- **Stage persistence** — Save progress to continue later
- **Dynamic file listing** — Show available clues based on progress

---

## 🔑 Key Features

### 1. File-Based Storytelling
- Evidence scattered across real files
- Realistic detective work simulation
- Multiple file types (txt, bmp, json)

### 2. Progressive Disclosure
- Information revealed as you solve puzzles
- Branching narrative based on choices
- Multiple endings possible

### 3. Intelligent Command Parser
- Typo suggestions ("Did you mean 'accuse'?")
- Case-insensitive input handling
- Argument validation

### 4. Stage Management
- Game saves your progress automatically
- Commands have stage-based availability
- Prevents sequence-breaking

### 5. Immersive Atmosphere
- Narrative-style output
- Rich crime scene descriptions
- Dramatic reveals at key moments

---

## 🧩 Technologies & Concepts

| Concept | Implementation |
|---------|---------------|
| **File I/O** | `open()`, `.read()`, `.write()` for persistent data |
| **String Processing** | Parsing commands, extracting clues from text |
| **Image Decoding** | BMP file analysis, binary message extraction |
| **State Management** | Tracking game progress, unlocked clues |
| **User Interface** | Menu-driven console with error handling |
| **Narrative Design** | Branching dialogue and progressive reveals |

---

## 🎮 Example Walkthroughs

### Walkthrough 1: Quick Solution
```
1. list                          → See all available files
2. open witness_statement.txt    → Get alibi info
3. open crime_scene_notes.txt    → Find motive
4. decode hidden_message.bmp     → Discover the meeting location
5. check all_suspects            → Verify alibis
6. accuse guilty_party           → Solve the mystery!
```

### Walkthrough 2: Deep Investigation
```
1. list                          → Explore systematically
2. open admin_record.txt         → Background on suspects
3. open timeline.txt             → Build event sequence
4. decode evidence.bmp           → Extract key clue
5. open secondary_evidence.txt   → Connect the dots
6. check suspect_1               → Rule out innocent
7. check suspect_2               → Rule out innocent
8. accuse final_suspect          → Guilty party found!
```

---

## 🔧 Customization Ideas

### Add New Suspects
Modify `files/suspects.json`:
```json
{
  "suspects": [
    {"name": "Alice", "motive": "Inheritance", "alibi": "At home"},
    {"name": "Bob", "motive": "Revenge", "alibi": "Theater visit"}
  ]
}
```

### Create New Evidence Files
Add `.txt` or `.bmp` files to `Player/` and update the manifest to make them discoverable.

### Extend the Story
Edit narrative strings in `stage_manager.py` to add flavor text and descriptions.

### Add Difficulty Levels
- **Easy** — All clues visible, clear suspects
- **Medium** — Some clues hidden, multiple suspects
- **Hard** — Cryptic clues, red herrings, decryption required

---

## 📖 Educational Value

This project teaches:
- ✅ **File Handling** — Open, read, write operations with real data
- ✅ **Parsing** — Extract meaningful information from text
- ✅ **State Management** — Track game progress and player choices
- ✅ **Binary Data** — Work with image files and encoded messages
- ✅ **User Interface Design** — Build responsive, user-friendly CLI
- ✅ **Narrative Design** — Create branching, immersive experiences
- ✅ **Modular Code** — Separate concerns (game logic, file ops, UI)

---

## 🐛 Troubleshooting

### "FileNotFoundError" error
- Ensure all files in `Admin_files/`, `Player/`, and `Files/` exist
- Check file paths are correct (case-sensitive on Linux/Mac)
- Try running from the correct directory

### Game crashes on `decode` command
- Verify BMP files are valid images
- Check that decoding functions match file format
- Ensure `decoded_bmp.py` doesn't have syntax errors

### Commands not recognized
- Check spelling (game is case-insensitive but spelling must be correct)
- Try `help` to see all available commands
- Use quoted arguments for filenames with spaces

### Progress not saving
- Ensure you have write permissions in the directory
- Check that `stage_manager.py` can access save files
- Try running as administrator

---

## 🚀 Future Enhancements

- 🎨 **GUI Version** — Tkinter or PyQt interface with file browser
- 🎭 **Multiple Scenarios** — Different murders to solve
- ⏱️ **Time Pressure** — Solve mystery within time limit
- 🏆 **Scoring System** — Points for each clue found
- 🌐 **Network Multiplayer** — Cooperative detective mode
- 🎙️ **Voice Acting** — Audio files with suspect interviews
- 📊 **Progress Tracking** — Statistics on clues found, time spent

---

## 📄 License

MIT — Free to use, modify, and share with attribution.

---

## 👤 Author

Built by [@Sanjay-AI-ML](https://github.com/Sanjay-AI-ML)

Questions? Found a clue I missed? Open an issue on GitHub!

**Happy investigating!** 🔍🕵️
