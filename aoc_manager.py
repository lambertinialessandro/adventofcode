import os
import re
import datetime
import customtkinter as ctk
from tkhtmlview import HTMLLabel
import markdown
import subprocess

# ---------------- Configuration ----------------
ctk.set_appearance_mode("dark")  # "light", "dark", "system"
ctk.set_default_color_theme("blue")

# ---------------- Utility Functions ----------------
ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

current_year = datetime.datetime.now().year
current_year = current_year if datetime.datetime.now().month == 12 else current_year - 1

DAYS = list(map(str, range(1, 25 + 1)))
STARS_PER_YEAR = 50
YEARS = sorted(list(map(str, range(2015, current_year + 1))), reverse=True)

PROGRESS_BARS = {}


def get_year_star_count(year):
    readme_path = os.path.join(year, "README.md")
    if not os.path.exists(readme_path):
        return 0
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"Stars-(\d+)%2F50", content)
    return int(match.group(1)) if match else 0


def get_total_stars(years):
    return sum(get_year_star_count(y) for y in years)


def update_progress_bars():
    for year, bar in PROGRESS_BARS.items():
        stars = get_year_star_count(year)
        bar.set(stars / STARS_PER_YEAR)


def update_total_label():
    total = get_total_stars(YEARS)
    total_label.configure(text=f"🌟 Total Stars: {total} / {len(YEARS)*STARS_PER_YEAR}")
    update_progress_bars()


def preview_output_command(command):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    output_lines = []
    for line in iter(process.stdout.readline, ""):
        clean_line = ansi_escape.sub("", line)
        output_lines.append(clean_line)

        preview_html.set_html(
            f"<pre style='color:white; font-family:monospace;'>{''.join(output_lines)}</pre>"
        )

    process.stdout.close()
    process.wait()

    final_output = "".join(output_lines)
    preview_html.set_html(
        f"<pre style='color:white; font-family:monospace;'>{final_output}</pre>"
    )


def start_problem():
    year = year_dropdown.get()
    day = int(day_dropdown.get())
    preview_output_command(
        ["python", "./commands/start_problem.py", str(year), f"{day:02d}"]
    )


def create_year_readme():
    year = year_dropdown.get()
    preview_output_command(["python", "./commands/create_year_readme.py", str(year)])
    update_total_label()
    preview_readme()


def update_year_readme():
    year = year_dropdown.get()
    preview_output_command(["python", "./commands/update_year_readme.py", str(year)])
    update_total_label()
    preview_readme()


def update_main_readme():
    preview_output_command(["python", "./update_main_readme.py"])
    update_total_label()


def preview_readme():
    year = year_dropdown.get()
    readme_path = os.path.join(year, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        html_content = markdown.markdown(
            md_content, extensions=["tables", "fenced_code"]
        )
        styled_html = f"""
        <div style="color:white; font-family: monospace; line-height:1.4;">
            {html_content}
        </div>
        """
        preview_html.set_html(styled_html)
    else:
        preview_html.set_html(
            "<p style='color:red;'>README.md not found for this year.</p>"
        )


# ---------------- GUI Setup ----------------
root = ctk.CTk()
root.title("🎄 Advent of Code Dashboard")
root.geometry("1200x700")

# ---------------- Total Stars ----------------
total_label = ctk.CTkLabel(root, text="", font=ctk.CTkFont(size=18, weight="bold"))
total_label.pack(pady=[10, 0])
update_total_label()

# ---------------- Main Frame ----------------
main_frame = ctk.CTkFrame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=[5, 10])

# ---------------- Sidebar ----------------
sidebar = ctk.CTkFrame(main_frame, width=250)
sidebar.pack(side="left", fill="y", padx=5, pady=5)

# ---------------- Top Sidebar ----------------
top_frame = ctk.CTkFrame(sidebar)
top_frame.pack(fill="x", padx=5, pady=5)

# Year Dropdown
ctk.CTkLabel(
    top_frame, text="Select Year:", font=ctk.CTkFont(size=14, weight="bold")
).pack(pady=5)
year_dropdown = ctk.CTkComboBox(top_frame, values=YEARS, width=200)
year_dropdown.set(YEARS[0])
year_dropdown.pack(pady=5)

# Day Dropdown
ctk.CTkLabel(
    top_frame, text="Select Day:", font=ctk.CTkFont(size=14, weight="bold")
).pack(pady=5)
day_dropdown = ctk.CTkComboBox(top_frame, values=DAYS, width=200)
day_dropdown.set(DAYS[0])
day_dropdown.pack(pady=[5, 25])

# ---------------- Buttons Sidebar ----------------

# Buttons
buttons = [
    ("👁 Preview Year README", preview_readme),
    ("⚡ Start Year Day Problem", start_problem),
    #("✨ Create Year README", create_year_readme),
    #("🔄 Update Year README", update_year_readme),
    #("🧭 Update Main README", update_main_readme),
]

for text, cmd in buttons:
    btn = ctk.CTkButton(sidebar, text=text, command=cmd, width=200)
    btn.pack(pady=5)

# ---------------- Year Progress Bars ----------------
scroll_frame = ctk.CTkScrollableFrame(sidebar, label_text="Year Progress")
scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)

PROGRESS_BARS = {}
for y in YEARS:
    year_frame = ctk.CTkFrame(scroll_frame)
    year_frame.pack(pady=5, fill="x")

    stars = get_year_star_count(y)
    progress = stars / STARS_PER_YEAR

    year_label = ctk.CTkLabel(year_frame, text=str(y), font=ctk.CTkFont(weight="bold"))
    year_label.pack(side="left", padx=(5, 5))

    # Right: normal text
    info_label = ctk.CTkLabel(
        year_frame, text=f"{stars}/{STARS_PER_YEAR} [{int(progress * 100)}%]"
    )
    info_label.pack(side="right")

    bar = ctk.CTkProgressBar(scroll_frame, width=200)
    bar.pack(pady=2)
    bar.set(progress)

    PROGRESS_BARS[y] = bar

# ---------------- Markdown Preview ----------------
preview_frame = ctk.CTkFrame(main_frame)
preview_frame.pack(side="right", fill="both", expand=True, padx=[0, 5], pady=5)

preview_html = HTMLLabel(
    preview_frame, html="", width=900, height=600, background="#1e1e1e"
)
preview_html.pack(fill="both", expand=True)

# ---------------- Run GUI ----------------

try:
    root.mainloop()
except:
    pass
