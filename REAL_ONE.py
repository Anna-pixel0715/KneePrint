import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# KNEEPRINT
# PAGE 1 + PAGE 2
# AESTHETIC CREAM / BEIGE / NAVY DESIGN
# ============================================================

root = tk.Tk()
root.title("KneePrint - Knee Analysis System")
root.geometry("1500x900")
root.minsize(1100, 700)
root.configure(bg="#EEE8DF")


# ============================================================
# COLOUR PALETTE
# ============================================================

CREAM = "#EEE8DF"
WHITE = "#FFFDFC"

NAVY = "#2C365A"
NAVY_DARK = "#202946"

BEIGE = "#C4BCB0"
BEIGE_LIGHT = "#D8CDBE"
BEIGE_PALE = "#E5DDD2"
BEIGE_DARK = "#AFA394"

TEXT = "#26324F"
MUTED = "#707789"

BORDER = "#D3C9BC"


# ============================================================
# GLOBAL FONT SETTINGS
# ============================================================

TITLE_FONT = ("Georgia", 46, "bold")
PAGE_TITLE_FONT = ("Georgia", 38, "bold")
WELCOME_FONT = ("Georgia", 42, "bold")
SECTION_FONT = ("Georgia", 22, "bold")
BODY_FONT = ("Georgia", 15)
SMALL_FONT = ("Arial", 10)
BUTTON_FONT = ("Arial", 12, "bold")


# ============================================================
# MAIN CANVAS
# ============================================================

canvas = tk.Canvas(
    root,
    bg=CREAM,
    highlightthickness=0
)

canvas.pack(fill="both", expand=True)


# ============================================================
# PAGE CONTROL
# ============================================================

current_page = 1


def clear_canvas():
    canvas.delete("all")


# ============================================================
# SOFT BACKGROUND DESIGN
# ============================================================

def draw_background():

    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # --------------------------------------------------------
    # LARGE SOFT CIRCLES
    # --------------------------------------------------------

    canvas.create_oval(
        -230, 190, 330, 750,
        fill="#E5DBCE",
        outline=""
    )

    canvas.create_oval(
        -300, 520, 210, 1030,
        fill="#E2D6C8",
        outline=""
    )

    canvas.create_oval(
        width - 310, -170,
        width + 250, 400,
        fill="#E6DCD0",
        outline=""
    )

    canvas.create_oval(
        width - 180, 590,
        width + 330, 1100,
        fill="#E3D7C9",
        outline=""
    )

    # --------------------------------------------------------
    # LEFT DECORATIVE CURVES
    # --------------------------------------------------------

    canvas.create_arc(
        -170, 40, 440, 730,
        start=250,
        extent=135,
        style="arc",
        outline="#C8BDAF",
        width=1
    )

    canvas.create_arc(
        -100, 110, 380, 650,
        start=250,
        extent=135,
        style="arc",
        outline="#D0C5B7",
        width=1
    )

    canvas.create_arc(
        -40, 180, 320, 570,
        start=245,
        extent=140,
        style="arc",
        outline="#D6CCC0",
        width=1
    )

    # --------------------------------------------------------
    # RIGHT DECORATIVE CURVES
    # --------------------------------------------------------

    canvas.create_arc(
        width - 410, -80,
        width + 190, 600,
        start=50,
        extent=130,
        style="arc",
        outline="#C8BDAF",
        width=1
    )

    canvas.create_arc(
        width - 340, 30,
        width + 130, 520,
        start=45,
        extent=135,
        style="arc",
        outline="#D0C5B7",
        width=1
    )

    # --------------------------------------------------------
    # DECORATIVE DOTS
    # --------------------------------------------------------

    dots = [
        (width * 0.25, 195, 8),
        (width * 0.16, 460, 5),
        (width * 0.10, 690, 8),
        (width * 0.78, 195, 8),
        (width * 0.91, 320, 5),
        (width * 0.87, 670, 8),
        (width * 0.72, 760, 5)
    ]

    for x, y, r in dots:
        canvas.create_oval(
            x-r, y-r,
            x+r, y+r,
            fill=BEIGE,
            outline=""
        )


# ============================================================
# HEADER
# ============================================================

def draw_header():

    width = canvas.winfo_width()

    canvas.create_rectangle(
        0, 0,
        width, 82,
        fill=NAVY_DARK,
        outline=""
    )

    # Logo
    canvas.create_text(
        42, 40,
        text="KneePrint",
        anchor="w",
        font=("Georgia", 26, "bold"),
        fill=WHITE
    )

    # Vertical divider
    canvas.create_line(
        258, 20,
        258, 62,
        fill="#B8B1A8",
        width=1
    )

    # Header subtitle
    canvas.create_text(
        290, 32,
        text="MENISCUS DONOR",
        anchor="w",
        font=("Arial", 10),
        fill="#DCD5CC"
    )

    canvas.create_text(
        290, 50,
        text="MATCHING SYSTEM",
        anchor="w",
        font=("Arial", 10),
        fill="#DCD5CC"
    )

    # Right text
    canvas.create_text(
        width - 40,
        40,
        text="EDUCATIONAL PROTOTYPE   •   AI-ASSISTED ANALYSIS",
        anchor="e",
        font=("Arial", 9),
        fill="#DCD5CC"
    )


# ============================================================
# PAGE PROGRESS
# ============================================================

def draw_progress(active_page):

    width = canvas.winfo_width()

    start_x = width / 2 - 170
    y = 125

    steps = [
        ("1", "Patient Profile"),
        ("2", "Knee Measurements"),
        ("3", "Knee Analysis"),
        ("4", "KneePrint"),
        ("5", "ML Matching")
    ]

    spacing = 150

    for i, (number, label) in enumerate(steps):

        x = start_x + i * spacing

        if i + 1 == active_page:
            circle_color = NAVY
            text_color = WHITE
        elif i + 1 < active_page:
            circle_color = BEIGE
            text_color = NAVY
        else:
            circle_color = "#D5CDC2"
            text_color = NAVY

        canvas.create_oval(
            x - 18,
            y - 18,
            x + 18,
            y + 18,
            fill=circle_color,
            outline=""
        )

        canvas.create_text(
            x,
            y,
            text=number,
            font=("Arial", 10, "bold"),
            fill=text_color
        )

        canvas.create_text(
            x,
            y + 43,
            text=label,
            font=("Arial", 9),
            fill=TEXT if i + 1 <= active_page else MUTED
        )

        # connector line
        if i < len(steps) - 1:

            canvas.create_line(
                x + 25,
                y,
                x + spacing - 25,
                y,
                fill="#C8BFB4",
                width=1
            )


# ============================================================
# PAGE 1 — HOME
# ============================================================

def show_home():

    global current_page
    current_page = 1

    clear_canvas()

    draw_background()
    draw_header()

    width = canvas.winfo_width()

    center_x = width / 2

    # --------------------------------------------------------
    # TOP BRAND
    # --------------------------------------------------------

    canvas.create_line(
        center_x - 32,
        132,
        center_x + 32,
        132,
        fill=BEIGE_DARK,
        width=2
    )

    canvas.create_text(
        center_x,
        185,
        text="KNEEPRINT",
        font=TITLE_FONT,
        fill=NAVY
    )

    canvas.create_text(
        center_x,
        238,
        text="AI-ASSISTED KNEE & MENISCUS ANALYSIS SYSTEM",
        font=("Arial", 12),
        fill=NAVY
    )

    canvas.create_line(
        center_x - 32,
        275,
        center_x + 32,
        275,
        fill=BEIGE_DARK,
        width=2
    )

    # --------------------------------------------------------
    # MAIN CARD
    # --------------------------------------------------------

    card_width = min(1000, width - 180)
    card_height = 500

    left = center_x - card_width / 2
    right = center_x + card_width / 2

    top = 330
    bottom = top + card_height

    # Shadow
    canvas.create_rectangle(
        left + 9,
        top + 10,
        right + 9,
        bottom + 10,
        fill="#D5CCC0",
        outline=""
    )

    # Card
    canvas.create_rectangle(
        left,
        top,
        right,
        bottom,
        fill=WHITE,
        outline="#FFFFFF",
        width=2
    )

    # Small label
    canvas.create_text(
        center_x,
        top + 52,
        text="KNEEPRINT",
        font=("Arial", 9, "bold"),
        fill=MUTED
    )

    # --------------------------------------------------------
    # WELCOME
    # --------------------------------------------------------

    canvas.create_text(
        center_x,
        top + 125,
        text="Welcome to KneePrint",
        font=WELCOME_FONT,
        fill=NAVY
    )

    # Description
    canvas.create_text(
        center_x,
        top + 195,
        text=(
            "A patient-specific bilateral knee measurement and\n"
            "machine-learning donor matching prototype."
        ),
        font=BODY_FONT,
        fill=TEXT,
        justify="center"
    )

    # --------------------------------------------------------
    # START BUTTON
    # --------------------------------------------------------

    button_width = 410
    button_height = 70

    bx1 = center_x - button_width / 2
    by1 = top + 270
    bx2 = center_x + button_width / 2
    by2 = by1 + button_height

    # White border
    canvas.create_rectangle(
        bx1 - 4,
        by1 - 4,
        bx2 + 4,
        by2 + 4,
        fill=WHITE,
        outline=WHITE
    )

    # Beige button
    canvas.create_rectangle(
        bx1,
        by1,
        bx2,
        by2,
        fill=BEIGE,
        outline=BEIGE_DARK,
        width=1,
        tags="start_button"
    )

    canvas.create_text(
        center_x - 25,
        by1 + 35,
        text="START ANALYSIS",
        font=BUTTON_FONT,
        fill=NAVY,
        tags="start_button"
    )

    canvas.create_text(
        center_x + 155,
        by1 + 34,
        text="→",
        font=("Arial", 23),
        fill=NAVY,
        tags="start_button"
    )

    # --------------------------------------------------------
    # BOTTOM DESCRIPTION
    # --------------------------------------------------------

    canvas.create_text(
        center_x,
        bottom - 62,
        text="Patient Profile   |   Bilateral Measurements   |   KneePrint   |   ML Donor Matching",
        font=("Arial", 10),
        fill=MUTED
    )

    # Footer
    canvas.create_text(
        center_x,
        bottom - 28,
        text="EDUCATIONAL SOFTWARE PROTOTYPE",
        font=("Arial", 9),
        fill=MUTED
    )


# ============================================================
# PAGE 2 — PATIENT PROFILE
# ============================================================

def show_patient_profile():

    global current_page
    current_page = 1

    clear_canvas()

    draw_background()
    draw_header()

    width = canvas.winfo_width()

    # --------------------------------------------------------
    # PAGE TITLE
    # --------------------------------------------------------

    canvas.create_text(
        100,
        175,
        text="Patient Profile",
        anchor="w",
        font=PAGE_TITLE_FONT,
        fill=NAVY
    )

    canvas.create_text(
        103,
        222,
        text="Enter the basic information required for the analysis",
        anchor="w",
        font=("Arial", 13),
        fill=MUTED
    )

    draw_progress(1)

    # --------------------------------------------------------
    # MAIN FORM CARD
    # --------------------------------------------------------

    card_left = 100
    card_top = 270
    card_right = width - 100
    card_bottom = 770

    # Shadow
    canvas.create_rectangle(
        card_left + 8,
        card_top + 9,
        card_right + 8,
        card_bottom + 9,
        fill="#D5CCC0",
        outline=""
    )

    # Card
    canvas.create_rectangle(
        card_left,
        card_top,
        card_right,
        card_bottom,
        fill=WHITE,
        outline="#FFFFFF",
        width=2
    )

    # --------------------------------------------------------
    # CARD TITLE
    # --------------------------------------------------------

    canvas.create_text(
        card_left + 40,
        card_top + 45,
        text="Patient Information",
        anchor="w",
        font=SECTION_FONT,
        fill=NAVY
    )

    canvas.create_text(
        card_left + 40,
        card_top + 78,
        text="Please enter the details below.",
        anchor="w",
        font=("Arial", 11),
        fill=MUTED
    )

    # --------------------------------------------------------
    # FORM VARIABLES
    # --------------------------------------------------------

    patient_id = tk.StringVar()
    patient_name = tk.StringVar()
    dob = tk.StringVar()
    age_var = tk.StringVar()
    age_var.set("(Age: --)")
    gender = tk.StringVar()

    # --------------------------------------------------------
    # INPUT FUNCTION
    # --------------------------------------------------------

    def create_input(label, variable, x, y, width=350):

        canvas.create_text(
            x,
            y,
            text=label,
            anchor="w",
            font=("Arial", 11, "bold"),
            fill=TEXT
        )

        entry = tk.Entry(
            root,
            textvariable=variable,
            font=("Arial", 12),
            bg="#F8F5F0",
            fg=TEXT,
            relief="flat",
            highlightthickness=1,
            highlightbackground="#D4CABE",
            highlightcolor=NAVY
        )

        canvas.create_window(
            x,
            y + 38,
            anchor="w",
            window=entry,
            width=width,
            height=42
        )

        return entry

    # --------------------------------------------------------
    # FORM LAYOUT
    # --------------------------------------------------------

    left_x = card_left + 45
    right_x = width / 2 + 35

    create_input(
        "Patient ID",
        patient_id,
        left_x,
        card_top + 125
    )

    create_input(
        "Patient Name",
        patient_name,
        right_x,
        card_top + 125
    )

    create_input(
        "Date of Birth",
    dob,
    left_x,
    card_top + 225,
    width=350
    )

    # Gender
    canvas.create_text(
        right_x,
        card_top + 225,
        text="Gender",
        anchor="w",
        font=("Arial", 11, "bold"),
        fill=TEXT
    )

    gender_box = tk.OptionMenu(
        root,
        gender,
        "Select",
        "Male",
        "Female",
        "Other"
    )

    gender_box.config(
        font=("Arial", 11),
        bg="#F8F5F0",
        fg=TEXT,
        activebackground=BEIGE,
        activeforeground=NAVY,
        relief="flat",
        highlightthickness=1,
        highlightbackground="#D4CABE"
    )

    canvas.create_window(
        right_x,
        card_top + 263,
        anchor="w",
        window=gender_box,
        width=350,
        height=42
    )

    # --------------------------------------------------------
    # INFORMATION BOX
    # --------------------------------------------------------

    info_left = card_left + 45
    info_top = card_top + 330
    info_right = card_right - 45
    info_bottom = card_top + 415

    canvas.create_rectangle(
        info_left,
        info_top,
        info_right,
        info_bottom,
        fill="#F1EBE3",
        outline="#DED5CA"
    )

    canvas.create_text(
        info_left + 20,
        info_top + 20,
        text="ⓘ",
        anchor="w",
        font=("Arial", 16, "bold"),
        fill=NAVY
    )

    canvas.create_text(
        info_left + 50,
        info_top + 23,
        text="Educational Prototype",
        anchor="w",
        font=("Arial", 11, "bold"),
        fill=NAVY
    )

    canvas.create_text(
        info_left + 50,
        info_top + 52,
        text=(
            "The information entered here is used to create the patient-specific\n"
            "bilateral measurement and donor-matching workflow."
        ),
        anchor="w",
        font=("Arial", 10),
        fill=MUTED
    )

    # --------------------------------------------------------
    # CONTINUE BUTTON
    # --------------------------------------------------------

    button_width = 240
    button_height = 55

    bx2 = card_right - 45
    bx1 = bx2 - button_width

    by2 = card_bottom - 10
    by1 = by2 - button_height

    # White border
    canvas.create_rectangle(
        bx1 - 3,
        by1 - 3,
        bx2 + 3,
        by2 + 3,
        fill=WHITE,
        outline=WHITE
    )

    # Navy button
    canvas.create_rectangle(
        bx1,
        by1,
        bx2,
        by2,
        fill=NAVY,
        outline=NAVY,
        tags="continue_button"
    )

    canvas.create_text(
        bx1 + button_width / 2 - 12,
        by1 + button_height / 2,
        text="CONTINUE",
        font=("Arial", 11, "bold"),
        fill=WHITE,
        tags="continue_button"
    )

    canvas.create_text(
        bx2 - 35,
        by1 + button_height / 2,
        text="→",
        font=("Arial", 19),
        fill=WHITE,
        tags="continue_button"
    )

    # --------------------------------------------------------
    # BACK BUTTON
    # --------------------------------------------------------

    canvas.create_text(
        card_left + 70,
        by1 + button_height / 2,
        text="←  BACK",
        font=("Arial", 10, "bold"),
        fill=NAVY,
        tags="back_button"
    )

    # --------------------------------------------------------
    # SAVE DATA
    # --------------------------------------------------------

    def continue_to_measurements():

        if not patient_id.get().strip():
            messagebox.showwarning(
                "Missing Information",
                "Please enter the Patient ID."
            )
            return

        if not patient_name.get().strip():
            messagebox.showwarning(
                "Missing Information",
                "Please enter the Patient Name."
            )
            return

        if not dob.get().strip():
            messagebox.showwarning(
                "Missing Information",
                "Please enter the Date of Birth."
            )
            return
        
        if gender.get() in ("", "Select"):
            messagebox.showwarning(
                "Missing Information",
                "Please select the Gender."
            )
            return

        # ----------------------------------------------------
        # THIS IS WHERE YOUR EXISTING KNEE MEASUREMENT PAGE
        # CAN BE CALLED.
        #
        # For now this demonstrates the navigation.
        # ----------------------------------------------------

        # Open the measurement page after the current click event
        # finishes. This prevents the canvas bindings from interfering
        # with the page transition.
        root.after(10, show_knee_measurements)

    def go_back():

        show_home()

    # --------------------------------------------------------
    # CLICK AREAS
    # --------------------------------------------------------

    def mouse_click(event):

        # Continue
        if (
            bx1 <= event.x <= bx2
            and by1 <= event.y <= by2
        ):
            continue_to_measurements()

        # Back
        elif (
            card_left + 25 <= event.x <= card_left + 130
            and by1 <= event.y <= by2
        ):
            go_back()

    canvas.bind(
        "<Button-1>",
        mouse_click
    )

    # Cursor
    def mouse_move(event):

        if (
            bx1 <= event.x <= bx2
            and by1 <= event.y <= by2
        ):
            canvas.configure(cursor="hand2")

        elif (
            card_left + 25 <= event.x <= card_left + 130
            and by1 <= event.y <= by2
        ):
            canvas.configure(cursor="hand2")

        else:
            canvas.configure(cursor="")

    canvas.bind(
        "<Motion>",
        mouse_move
    )



# ============================================================
# PAGE 3 — KNEE MEASUREMENTS
# ============================================================

# Stores the measurement values so they can be used by later pages.
measurement_values = {
    "left": {},
    "right": {}
}


def rounded_rectangle(x1, y1, x2, y2, radius=18, **kwargs):
    """Draw a rounded rectangle on the main canvas."""
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2 - radius,
        x1, y1 + radius
    ]

    # Main body
    canvas.create_polygon(points, smooth=True, **kwargs)

    # Small rectangles/circles make the rounded shape visually solid.
    fill = kwargs.get("fill", "")
    outline = kwargs.get("outline", "")
    width = kwargs.get("width", 1)

    canvas.create_rectangle(
        x1 + radius,
        y1,
        x2 - radius,
        y2,
        fill=fill,
        outline=""
    )
    canvas.create_rectangle(
        x1,
        y1 + radius,
        x2,
        y2 - radius,
        fill=fill,
        outline=""
    )

    canvas.create_oval(
        x1,
        y1,
        x1 + radius * 2,
        y1 + radius * 2,
        fill=fill,
        outline=outline,
        width=width
    )
    canvas.create_oval(
        x2 - radius * 2,
        y1,
        x2,
        y1 + radius * 2,
        fill=fill,
        outline=outline,
        width=width
    )
    canvas.create_oval(
        x1,
        y2 - radius * 2,
        x1 + radius * 2,
        y2,
        fill=fill,
        outline=outline,
        width=width
    )
    canvas.create_oval(
        x2 - radius * 2,
        y2 - radius * 2,
        x2,
        y2,
        fill=fill,
        outline=outline,
        width=width
    )


def show_knee_measurements():

    global current_page
    current_page = 2

    clear_canvas()
    draw_background()
    draw_header()
    draw_progress(2)

    width = canvas.winfo_width()
    height = canvas.winfo_height()
    center_x = width / 2

    # --------------------------------------------------------
    # PAGE TITLE
    # --------------------------------------------------------

    canvas.create_text(
        center_x, 255,
        text="KNEE MEASUREMENTS",
        font=("Georgia", 36, "bold"),
        fill=NAVY
    )

    canvas.create_line(
        center_x - 235, 302,
        center_x - 135, 302,
        fill=BEIGE_DARK, width=2
    )
    canvas.create_line(
        center_x + 135, 302,
        center_x + 235, 302,
        fill=BEIGE_DARK, width=2
    )
    canvas.create_text(
        center_x, 302,
        text="Enter measurements for both knees",
        font=("Arial", 13),
        fill=MUTED
    )

    # --------------------------------------------------------
    # RESPONSIVE CARD LAYOUT
    # --------------------------------------------------------

    card_top = 340
    nav_y2 = min(height - 25, 800)
    nav_y1 = nav_y2 - 58

    # Leave enough space below the final measurement row.
    card_bottom = nav_y1 - 35

    card_left = width * 0.148
    card_right = width * 0.516
    card2_left = width * 0.528
    card2_right = width * 0.900

    # Shadows
    canvas.create_rectangle(
        card_left + 7, card_top + 8,
        card_right + 7, card_bottom + 8,
        fill="#D7CEC2", outline=""
    )
    canvas.create_rectangle(
        card2_left + 7, card_top + 8,
        card2_right + 7, card_bottom + 8,
        fill="#D7CEC2", outline=""
    )

    # Cards
    rounded_rectangle(
        card_left, card_top, card_right, card_bottom,
        radius=20, fill=WHITE, outline=WHITE
    )
    rounded_rectangle(
        card2_left, card_top, card2_right, card_bottom,
        radius=20, fill=WHITE, outline=WHITE
    )

    # --------------------------------------------------------
    # CARD HEADERS
    # --------------------------------------------------------

    for x, letter, title, right_edge in [
        (card_left, "L", "LEFT KNEE", card_right),
        (card2_left, "R", "RIGHT KNEE", card2_right)
    ]:
        canvas.create_oval(
            x + 35, card_top + 20,
            x + 91, card_top + 76,
            fill=NAVY, outline=""
        )
        canvas.create_text(
            x + 63, card_top + 48,
            text=letter,
            font=("Arial", 18, "bold"), fill=WHITE
        )
        canvas.create_text(
            x + 125, card_top + 48,
            text=title,
            anchor="w",
            font=("Arial", 17, "bold"), fill=NAVY
        )
        canvas.create_text(
            right_edge - 35, card_top + 48,
            text="All measurements in mm",
            anchor="e",
            font=("Arial", 10), fill=MUTED
        )
        canvas.create_line(
            x + 28, card_top + 80,
            right_edge - 28, card_top + 80,
            fill="#EEE7DE", width=1
        )

    labels = [
        "Knee Width",
        "Knee Depth",
        "Meniscus Length",
        "Meniscus Width",
        "Meniscus Thickness"
    ]

    left_vars = {}
    right_vars = {}
    entry_widgets = []

    # The previous version used a 55 px row gap and placed the fifth
    # entry partly outside the card.  These smaller values keep every
    # Entry completely inside the card and away from the navigation.
    row_start = card_top + 112
    row_gap = 47
    entry_height = 36

    # Entry width is calculated from the available card width so it
    # cannot extend into the neighbouring card.
    card_inner_width = card_right - card_left
    entry_width = min(315, card_inner_width - 245)

    left_entry_x = card_left + 245
    right_entry_x = card2_left + 245

    def make_measurement_entry(variable, x, y):
        entry = tk.Entry(
            root,
            textvariable=variable,
            font=("Arial", 11),
            bg="#FBF8F4",
            fg=TEXT,
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#D8CDBE",
            highlightcolor=NAVY
        )

        canvas.create_window(
            x, y,
            anchor="w",
            window=entry,
            width=entry_width,
            height=entry_height
        )
        entry_widgets.append(entry)

        if variable.get() == "":
            variable.set("Enter value (mm)")
            entry.configure(fg="#8A8E97")

        def focus_in(event):
            if variable.get() == "Enter value (mm)":
                variable.set("")
                entry.configure(fg=TEXT)

        def focus_out(event):
            if not variable.get().strip():
                variable.set("Enter value (mm)")
                entry.configure(fg="#8A8E97")

        entry.bind("<FocusIn>", focus_in)
        entry.bind("<FocusOut>", focus_out)
        return entry

    for index, label in enumerate(labels):
        y = row_start + index * row_gap

        canvas.create_text(
            card_left + 40, y,
            text=label, anchor="w",
            font=("Arial", 10, "bold"), fill=TEXT
        )
        canvas.create_text(
            card2_left + 40, y,
            text=label, anchor="w",
            font=("Arial", 10, "bold"), fill=TEXT
        )

        left_vars[label] = tk.StringVar()
        right_vars[label] = tk.StringVar()

        make_measurement_entry(left_vars[label], left_entry_x, y)
        make_measurement_entry(right_vars[label], right_entry_x, y)

    # --------------------------------------------------------
    # NAVIGATION BUTTONS
    # --------------------------------------------------------

    back_x1 = card_left
    back_x2 = back_x1 + 175

    canvas.create_rectangle(
        back_x1, nav_y1, back_x2, nav_y2,
        fill=WHITE, outline=BEIGE_DARK, width=2,
        tags="measurement_back"
    )
    canvas.create_text(
        (back_x1 + back_x2) / 2, (nav_y1 + nav_y2) / 2,
        text="←  BACK",
        font=("Arial", 11, "bold"), fill=NAVY,
        tags="measurement_back"
    )

    next_width = min(475, width * 0.32)
    next_x1 = center_x - next_width / 2
    next_x2 = center_x + next_width / 2

    canvas.create_rectangle(
        next_x1 - 4, nav_y1 - 4,
        next_x2 + 4, nav_y2 + 4,
        fill=WHITE, outline=WHITE,
        tags="generate_kneeprint"
    )
    canvas.create_rectangle(
        next_x1, nav_y1, next_x2, nav_y2,
        fill=BEIGE, outline=BEIGE_DARK, width=1,
        tags="generate_kneeprint"
    )
    canvas.create_text(
        center_x - 20, (nav_y1 + nav_y2) / 2,
        text="NEXT",
        font=("Arial", 12, "bold"), fill=NAVY,
        tags="generate_kneeprint"
    )
    canvas.create_text(
        next_x2 - 35, (nav_y1 + nav_y2) / 2,
        text="→",
        font=("Arial", 24), fill=NAVY,
        tags="generate_kneeprint"
    )

    def clean_value(variable):
        value = variable.get().strip()
        return "" if value == "Enter value (mm)" else value

    def save_measurements():
        left_data = {}
        right_data = {}

        for label in labels:
            left_value = clean_value(left_vars[label])
            right_value = clean_value(right_vars[label])

            if not left_value or not right_value:
                messagebox.showwarning(
                    "Missing Measurement",
                    f"Please enter both LEFT and RIGHT values for:\n\n{label}"
                )
                return

            try:
                float(left_value)
                float(right_value)
            except ValueError:
                messagebox.showwarning(
                    "Invalid Measurement",
                    f"Please enter numeric values for:\n\n{label}"
                )
                return

            left_data[label] = left_value
            right_data[label] = right_value

        measurement_values["left"] = left_data
        measurement_values["right"] = right_data

        # Move to the next page only after all entries are validated.
        root.after(10, show_knee_analysis)

    def go_back_to_profile():
        show_patient_profile()

    def measurement_click(event):
        if next_x1 - 5 <= event.x <= next_x2 + 5 and nav_y1 - 5 <= event.y <= nav_y2 + 5:
            save_measurements()
        elif back_x1 - 5 <= event.x <= back_x2 + 5 and nav_y1 - 5 <= event.y <= nav_y2 + 5:
            go_back_to_profile()

    def measurement_motion(event):
        if (
            next_x1 - 5 <= event.x <= next_x2 + 5 and
            nav_y1 - 5 <= event.y <= nav_y2 + 5
        ) or (
            back_x1 - 5 <= event.x <= back_x2 + 5 and
            nav_y1 - 5 <= event.y <= nav_y2 + 5
        ):
            canvas.configure(cursor="hand2")
        else:
            canvas.configure(cursor="")

    canvas.bind("<Button-1>", measurement_click)
    canvas.bind("<Motion>", measurement_motion)


# ============================================================
# PAGE 3 — KNEE ANALYSIS
# ============================================================

def show_knee_analysis():

    global current_page
    current_page = 3

    clear_canvas()

    draw_background()
    draw_header()
    draw_progress(3)

    width = canvas.winfo_width()
    center_x = width / 2

    # --------------------------------------------------------
    # PAGE TITLE
    # --------------------------------------------------------

    canvas.create_text(
        center_x,
        255,
        text="KNEEPRINT ANALYSIS",
        font=("Georgia", 38, "bold"),
        fill=NAVY
    )

    canvas.create_line(
        center_x - 300,
        305,
        center_x - 220,
        305,
        fill=BEIGE_DARK,
        width=2
    )

    canvas.create_text(
        center_x,
        305,
        text="Bilateral KneePrint & Machine Learning Donor Analysis",
        font=("Arial", 14),
        fill=MUTED
    )

    canvas.create_line(
        center_x + 220,
        305,
        center_x + 300,
        305,
        fill=BEIGE_DARK,
        width=2
    )

    # --------------------------------------------------------
    # GET SAVED MEASUREMENTS
    # --------------------------------------------------------

    left_data = measurement_values.get("left", {})
    right_data = measurement_values.get("right", {})

    left_length = left_data.get("Meniscus Length", "--")
    left_width = left_data.get("Meniscus Width", "--")
    left_thickness = left_data.get("Meniscus Thickness", "--")

    right_length = right_data.get("Meniscus Length", "--")
    right_width = right_data.get("Meniscus Width", "--")
    right_thickness = right_data.get("Meniscus Thickness", "--")

    # --------------------------------------------------------
    # CARD SETTINGS
    # --------------------------------------------------------

    card_width = min(610, (width - 120) / 2)
    card_height = 330
    gap = 25

    left_card_x = center_x - card_width - gap / 2
    right_card_x = center_x + gap / 2

    card_top = 360
    card_bottom = card_top + card_height

    # --------------------------------------------------------
    # LEFT KNEE CARD
    # --------------------------------------------------------

    canvas.create_rectangle(
        left_card_x + 7,
        card_top + 8,
        left_card_x + card_width + 7,
        card_bottom + 8,
        fill="#D5CCC0",
        outline=""
    )

    rounded_rectangle(
        left_card_x,
        card_top,
        left_card_x + card_width,
        card_bottom,
        radius=20,
        fill=WHITE,
        outline=WHITE
    )

    circle_x = left_card_x + 75
    circle_y = card_top + 65

    canvas.create_oval(
        circle_x - 30,
        circle_y - 30,
        circle_x + 30,
        circle_y + 30,
        fill=NAVY,
        outline=""
    )

    canvas.create_text(
        circle_x,
        circle_y,
        text="L",
        font=("Georgia", 22, "bold"),
        fill=WHITE
    )

    canvas.create_text(
        left_card_x + 120,
        card_top + 65,
        text="LEFT KNEE",
        anchor="w",
        font=("Arial", 18, "bold"),
        fill=NAVY
    )

    canvas.create_line(
        left_card_x + 30,
        card_top + 115,
        left_card_x + card_width - 30,
        card_top + 115,
        fill="#E6DED4",
        width=1
    )

    left_rows = [
        ("Meniscus Length", left_length),
        ("Meniscus Width", left_width),
        ("Meniscus Thickness", left_thickness)
    ]

    row_y = card_top + 160

    for label, value in left_rows:

        canvas.create_text(
            left_card_x + 50,
            row_y,
            text=label,
            anchor="w",
            font=("Arial", 13, "bold"),
            fill=TEXT
        )

        value_left = left_card_x + card_width - 250
        value_right = left_card_x + card_width - 55

        canvas.create_rectangle(
            value_left,
            row_y - 23,
            value_right,
            row_y + 23,
            fill="#F8F5F0",
            outline="#D8CEC1",
            width=1
        )

        canvas.create_text(
            (value_left + value_right) / 2,
            row_y,
            text=str(value),
            font=("Arial", 13),
            fill=TEXT
        )

        canvas.create_text(
            left_card_x + card_width - 25,
            row_y,
            text="mm",
            font=("Arial", 10),
            fill=MUTED
        )

        row_y += 65

    # --------------------------------------------------------
    # RIGHT KNEE CARD
    # --------------------------------------------------------

    canvas.create_rectangle(
        right_card_x + 7,
        card_top + 8,
        right_card_x + card_width + 7,
        card_bottom + 8,
        fill="#D5CCC0",
        outline=""
    )

    rounded_rectangle(
        right_card_x,
        card_top,
        right_card_x + card_width,
        card_bottom,
        radius=20,
        fill=WHITE,
        outline=WHITE
    )

    circle_x = right_card_x + 75
    circle_y = card_top + 65

    canvas.create_oval(
        circle_x - 30,
        circle_y - 30,
        circle_x + 30,
        circle_y + 30,
        fill=NAVY,
        outline=""
    )

    canvas.create_text(
        circle_x,
        circle_y,
        text="R",
        font=("Georgia", 22, "bold"),
        fill=WHITE
    )

    canvas.create_text(
        right_card_x + 120,
        card_top + 65,
        text="RIGHT KNEE",
        anchor="w",
        font=("Arial", 18, "bold"),
        fill=NAVY
    )

    canvas.create_line(
        right_card_x + 30,
        card_top + 115,
        right_card_x + card_width - 30,
        card_top + 115,
        fill="#E6DED4",
        width=1
    )

    right_rows = [
        ("Meniscus Length", right_length),
        ("Meniscus Width", right_width),
        ("Meniscus Thickness", right_thickness)
    ]

    row_y = card_top + 160

    for label, value in right_rows:

        canvas.create_text(
            right_card_x + 50,
            row_y,
            text=label,
            anchor="w",
            font=("Arial", 13, "bold"),
            fill=TEXT
        )

        value_left = right_card_x + card_width - 250
        value_right = right_card_x + card_width - 55

        canvas.create_rectangle(
            value_left,
            row_y - 23,
            value_right,
            row_y + 23,
            fill="#F8F5F0",
            outline="#D8CEC1",
            width=1
        )

        canvas.create_text(
            (value_left + value_right) / 2,
            row_y,
            text=str(value),
            font=("Arial", 13),
            fill=TEXT
        )

        canvas.create_text(
            right_card_x + card_width - 25,
            row_y,
            text="mm",
            font=("Arial", 10),
            fill=MUTED
        )

        row_y += 65

    # --------------------------------------------------------
    # BACK BUTTON
    # --------------------------------------------------------

    back_x1 = max(80, width * 0.15)
    back_y1 = 735
    back_x2 = back_x1 + 175
    back_y2 = 795

    # Same boxed BACK style used on the Knee Measurements page
    canvas.create_rectangle(
        back_x1,
        back_y1,
        back_x2,
        back_y2,
        fill=WHITE,
        outline=BEIGE_DARK,
        width=2,
        tags="analysis_back"
    )

    canvas.create_text(
        (back_x1 + back_x2) / 2,
        (back_y1 + back_y2) / 2,
        text="←  BACK",
        font=("Arial", 11, "bold"),
        fill=NAVY,
        tags="analysis_back"
    )

    # --------------------------------------------------------
    # RUN ML DONOR ANALYSIS BUTTON
    # --------------------------------------------------------

    button_width = 530
    button_height = 68

    button_x1 = center_x - button_width / 2
    button_y1 = 735
    button_x2 = center_x + button_width / 2
    button_y2 = button_y1 + button_height

    rounded_rectangle(
        button_x1 - 4,
        button_y1 - 4,
        button_x2 + 4,
        button_y2 + 4,
        radius=16,
        fill=WHITE,
        outline=WHITE,
        width=2
    )

    rounded_rectangle(
        button_x1,
        button_y1,
        button_x2,
        button_y2,
        radius=13,
        fill=BEIGE,
        outline=BEIGE_DARK,
        width=1
    )

    canvas.create_text(
        center_x - 35,
        button_y1 + button_height / 2,
        text="RUN ML DONOR ANALYSIS",
        font=("Arial", 13, "bold"),
        fill=NAVY,
        tags="ml_analysis_button"
    )

    canvas.create_text(
        button_x2 - 45,
        button_y1 + button_height / 2,
        text="→",
        font=("Arial", 25),
        fill=NAVY,
        tags="ml_analysis_button"
    )

    # --------------------------------------------------------
    # BUTTON ACTIONS
    # --------------------------------------------------------

    def go_back():
        show_knee_measurements()

    def run_ml_analysis():
        # Open the actual ML Donor Matching page.
        show_ml_matching()

    def analysis_click(event):

        if (
            back_x1 <= event.x <= back_x2
            and back_y1 <= event.y <= back_y2
        ):
            go_back()

        elif (
            button_x1 <= event.x <= button_x2
            and button_y1 <= event.y <= button_y2
        ):
            run_ml_analysis()

    canvas.bind("<Button-1>", analysis_click)

    def analysis_motion(event):

        if (
            back_x1 <= event.x <= back_x2
            and back_y1 <= event.y <= back_y2
        ):
            canvas.configure(cursor="hand2")

        elif (
            button_x1 <= event.x <= button_x2
            and button_y1 <= event.y <= button_y2
        ):
            canvas.configure(cursor="hand2")

        else:
            canvas.configure(cursor="")

    canvas.bind("<Motion>", analysis_motion)




# ============================================================
# EXPLAINABLE ML WINDOW
# ============================================================

def show_explanation():
    """Open the Explainable ML analysis in a KneePrint-styled window."""

    window = tk.Toplevel(root)
    window.title("Explainable ML Analysis")
    window.geometry("900x780")
    window.minsize(780, 700)
    window.configure(bg=CREAM)

    # ------------------------------------------------------------
    # KneePrint-style decorative background
    # ------------------------------------------------------------
    bg = tk.Canvas(window, bg=CREAM, highlightthickness=0)
    bg.pack(fill="both", expand=True)

    def draw_explanation_background(event=None):
        bg.delete("bg")
        w = bg.winfo_width()
        h = bg.winfo_height()
        if w < 10 or h < 10:
            return

        # Soft decorative shapes used by the main application.
        bg.create_oval(-180, 100, 300, 580,
                       fill="#E5DBCE", outline="", tags="bg")
        bg.create_oval(-220, h - 270, 220, h + 180,
                       fill="#E2D6C8", outline="", tags="bg")
        bg.create_oval(w - 250, -130, w + 180, 300,
                       fill="#E6DCD0", outline="", tags="bg")
        bg.create_oval(w - 170, h - 260, w + 300, h + 210,
                       fill="#E3D7C9", outline="", tags="bg")

        # Decorative arcs.
        bg.create_arc(-140, 40, 350, 590,
                      start=250, extent=135, style="arc",
                      outline="#C8BDAF", width=1, tags="bg")
        bg.create_arc(w - 350, -80, w + 140, 520,
                      start=45, extent=135, style="arc",
                      outline="#C8BDAF", width=1, tags="bg")

        for x, y, r in [
            (w * .10, h * .30, 8),
            (w * .90, h * .22, 8),
            (w * .84, h * .78, 6),
            (w * .18, h * .80, 5),
        ]:
            bg.create_oval(x-r, y-r, x+r, y+r,
                           fill=BEIGE, outline="", tags="bg")

        # Header matching the main KneePrint application.
        bg.create_rectangle(0, 0, w, 82,
                            fill=NAVY_DARK, outline="", tags="bg")
        bg.create_text(38, 40, text="KneePrint",
                       anchor="w", font=("Georgia", 26, "bold"),
                       fill=WHITE, tags="bg")
        bg.create_line(255, 20, 255, 62,
                       fill="#B8B1A8", width=1, tags="bg")
        bg.create_text(285, 32, text="MENISCUS DONOR",
                       anchor="w", font=("Arial", 10),
                       fill="#DCD5CC", tags="bg")
        bg.create_text(285, 50, text="MATCHING SYSTEM",
                       anchor="w", font=("Arial", 10),
                       fill="#DCD5CC", tags="bg")
        bg.create_text(w - 35, 40,
                       text="EDUCATIONAL PROTOTYPE   •   AI-ASSISTED ANALYSIS",
                       anchor="e", font=("Arial", 9),
                       fill="#DCD5CC", tags="bg")

        # Page title and subtitle.
        bg.create_text(w / 2, 125, text="EXPLAINABLE ML ANALYSIS",
                       font=("Georgia", 32, "bold"), fill=NAVY, tags="bg")
        bg.create_line(w/2 - 315, 166, w/2 - 225, 166,
                       fill=BEIGE_DARK, width=2, tags="bg")
        bg.create_text(w / 2, 166,
                       text="Understanding the Random Forest donor prediction",
                       font=("Arial", 13), fill=MUTED, tags="bg")
        bg.create_line(w/2 + 225, 166, w/2 + 315, 166,
                       fill=BEIGE_DARK, width=2, tags="bg")

    bg.bind("<Configure>", draw_explanation_background)

    # ------------------------------------------------------------
    # Main white information card
    # ------------------------------------------------------------
    card = tk.Frame(window, bg=WHITE,
                    highlightbackground="#E0D6CA",
                    highlightthickness=1)
    card.place(relx=0.06, rely=0.255, relwidth=0.88, relheight=0.67)

    tk.Label(
        card,
        text="MODEL USED",
        font=("Georgia", 17, "bold"),
        fg=NAVY,
        bg=WHITE,
        anchor="w"
    ).pack(fill="x", padx=40, pady=(25, 7))

    tk.Label(
        card,
        text="Random Forest Classifier",
        font=("Arial", 14),
        fg=TEXT,
        bg=WHITE,
        anchor="w"
    ).pack(fill="x", padx=40)

    tk.Label(
        card,
        text=(
            "The model evaluates multiple knee and meniscus measurement "
            "features together to estimate donor compatibility."
        ),
        font=("Arial", 12),
        fg=TEXT,
        bg=WHITE,
        justify="left",
        wraplength=700,
        anchor="w"
    ).pack(fill="x", padx=40, pady=(8, 17))

    tk.Label(
        card,
        text="IMPORTANT FEATURES",
        font=("Georgia", 17, "bold"),
        fg=NAVY,
        bg=WHITE,
        anchor="w"
    ).pack(fill="x", padx=40, pady=(2, 7))

    tk.Label(
        card,
        text=(
            "• Meniscus Length\n"
            "• Meniscus Width\n"
            "• Meniscus Thickness\n"
            "• Length Difference\n"
            "• Width Difference\n"
            "• Thickness Difference"
        ),
        font=("Arial", 12),
        fg=TEXT,
        bg=WHITE,
        justify="left",
        anchor="w"
    ).pack(fill="x", padx=40)

    tk.Label(
        card,
        text="HOW THE MODEL WORKS",
        font=("Georgia", 17, "bold"),
        fg=NAVY,
        bg=WHITE,
        anchor="w"
    ).pack(fill="x", padx=40, pady=(17, 7))

    tk.Label(
        card,
        text=(
            "The patient's measurements are compared with donor measurements. "
            "The Random Forest uses patterns learned from the training dataset "
            "to classify predicted compatibility as High, Medium, or Low."
        ),
        font=("Arial", 12),
        fg=TEXT,
        bg=WHITE,
        justify="left",
        wraplength=700,
        anchor="w"
    ).pack(fill="x", padx=40)

    # Footer disclaimer.
    tk.Label(
        window,
        text=(
            "Educational prototype using synthetic/sample data. "
            "The result does not determine clinical transplant suitability."
        ),
        font=("Arial", 9),
        fg=MUTED,
        bg=CREAM
    ).place(relx=0.5, rely=0.935, anchor="center")

    # Separate white close button box.
    tk.Button(
        window,
        text="CLOSE",
        command=window.destroy,
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=NAVY,
        activebackground="#F5F1EB",
        activeforeground=NAVY,
        relief="flat",
        highlightbackground="#CFC4B6",
        highlightcolor="#CFC4B6",
        highlightthickness=1,
        width=14,
        pady=6,
        cursor="hand2"
    ).place(relx=0.5, rely=0.965, anchor="center")


# ============================================================
# WHAT-IF ML SIMULATION WINDOW
# ============================================================

def show_what_if():
    """Open the What-If ML simulation in a KneePrint-styled separate window."""

    window = tk.Toplevel(root)
    window.title("What-If ML Simulation")
    window.geometry("900x780")
    window.minsize(780, 700)
    window.configure(bg=CREAM)

    # ------------------------------------------------------------
    # KneePrint-style background
    # ------------------------------------------------------------
    bg = tk.Canvas(window, bg=CREAM, highlightthickness=0)
    bg.pack(fill="both", expand=True)

    def draw_simulation_background(event=None):
        bg.delete("bg")
        w = bg.winfo_width()
        h = bg.winfo_height()
        if w < 10 or h < 10:
            return

        # Soft circles / curves matching the main application.
        bg.create_oval(-180, 100, 300, 580,
                       fill="#E5DBCE", outline="", tags="bg")
        bg.create_oval(-220, h - 270, 220, h + 180,
                       fill="#E2D6C8", outline="", tags="bg")
        bg.create_oval(w - 250, -130, w + 180, 300,
                       fill="#E6DCD0", outline="", tags="bg")
        bg.create_oval(w - 170, h - 260, w + 300, h + 210,
                       fill="#E3D7C9", outline="", tags="bg")

        bg.create_arc(-140, 40, 350, 590,
                      start=250, extent=135, style="arc",
                      outline="#C8BDAF", width=1, tags="bg")
        bg.create_arc(w - 350, -80, w + 140, 520,
                      start=45, extent=135, style="arc",
                      outline="#C8BDAF", width=1, tags="bg")

        for x, y, r in [
            (w * .10, h * .30, 8),
            (w * .90, h * .22, 8),
            (w * .84, h * .78, 6),
            (w * .18, h * .80, 5),
        ]:
            bg.create_oval(x-r, y-r, x+r, y+r,
                           fill=BEIGE, outline="", tags="bg")

        # Header.
        bg.create_rectangle(0, 0, w, 82,
                            fill=NAVY_DARK, outline="", tags="bg")
        bg.create_text(38, 40, text="KneePrint",
                       anchor="w", font=("Georgia", 26, "bold"),
                       fill=WHITE, tags="bg")
        bg.create_line(255, 20, 255, 62,
                       fill="#B8B1A8", width=1, tags="bg")
        bg.create_text(285, 32, text="MENISCUS DONOR",
                       anchor="w", font=("Arial", 10),
                       fill="#DCD5CC", tags="bg")
        bg.create_text(285, 50, text="MATCHING SYSTEM",
                       anchor="w", font=("Arial", 10),
                       fill="#DCD5CC", tags="bg")
        bg.create_text(w - 35, 40,
                       text="EDUCATIONAL PROTOTYPE   •   AI-ASSISTED ANALYSIS",
                       anchor="e", font=("Arial", 9),
                       fill="#DCD5CC", tags="bg")

        # Page title.
        bg.create_text(w / 2, 125, text="WHAT-IF ML SIMULATION",
                       font=("Georgia", 32, "bold"), fill=NAVY, tags="bg")
        bg.create_line(w/2 - 310, 166, w/2 - 220, 166,
                       fill=BEIGE_DARK, width=2, tags="bg")
        bg.create_text(w / 2, 166,
                       text="Modify donor measurements and observe the ML prediction",
                       font=("Arial", 13), fill=MUTED, tags="bg")
        bg.create_line(w/2 + 220, 166, w/2 + 310, 166,
                       fill=BEIGE_DARK, width=2, tags="bg")

    bg.bind("<Configure>", draw_simulation_background)

    # Main white card. It is placed above the decorative canvas.
    card = tk.Frame(window, bg=WHITE,
                    highlightbackground="#E0D6CA",
                    highlightthickness=1)
    card.place(relx=0.06, rely=0.25, relwidth=0.88, relheight=0.65)

    tk.Label(
        card,
        text="TEST DONOR MEASUREMENTS",
        font=("Georgia", 18, "bold"),
        fg=NAVY,
        bg=WHITE
    ).pack(anchor="w", padx=55, pady=(28, 15))

    input_frame = tk.Frame(card, bg=WHITE)
    input_frame.pack(anchor="w", padx=55)

    labels = [
        "Donor Length (mm)",
        "Donor Width (mm)",
        "Donor Thickness (mm)"
    ]
    defaults = ["42", "28", "8"]
    entries = []

    for row, (label_text, default_value) in enumerate(zip(labels, defaults)):
        tk.Label(
            input_frame,
            text=label_text,
            font=("Arial", 13),
            bg=WHITE,
            fg=TEXT
        ).grid(row=row, column=0, sticky="w", pady=8)

        entry = tk.Entry(
            input_frame,
            font=("Arial", 13),
            width=22,
            relief="flat",
            bg="#FAF8F4",
            fg=TEXT,
            highlightthickness=1,
            highlightbackground=BORDER,
            highlightcolor=NAVY
        )
        entry.insert(0, default_value)
        entry.grid(row=row, column=1, padx=45, pady=8)
        entries.append(entry)

    tk.Label(
        card,
        text="SIMULATION RESULT",
        font=("Georgia", 17, "bold"),
        fg=NAVY,
        bg=WHITE
    ).pack(anchor="w", padx=55, pady=(17, 8))

    result_label = tk.Label(
        card,
        text="Enter donor measurements and run the simulation.",
        font=("Arial", 13),
        fg=TEXT,
        bg=WHITE,
        justify="left",
        anchor="w"
    )
    result_label.pack(anchor="w", padx=55)

    def get_patient_measurements():
        data = measurement_values.get("right", {})
        if not data:
            data = measurement_values.get("left", {})
        return data

    def run_simulation():
        try:
            donor_length = float(entries[0].get().strip())
            donor_width = float(entries[1].get().strip())
            donor_thickness = float(entries[2].get().strip())

            patient = get_patient_measurements()
            patient_length = float(patient.get("Meniscus Length"))
            patient_width = float(patient.get("Meniscus Width"))
            patient_thickness = float(patient.get("Meniscus Thickness"))

            from ML_Model.ml_model import KneeMLModel
            model = KneeMLModel()
            prediction = model.predict_compatibility(
                patient_length,
                patient_width,
                patient_thickness,
                donor_length,
                donor_width,
                donor_thickness
            )

            compatibility = prediction["Compatibility"]
            confidence = prediction["Confidence"] * 100

            result_label.config(
                text=(
                    f"Patient: {patient_length:g} × {patient_width:g} × "
                    f"{patient_thickness:g} mm\n\n"
                    f"Test Donor: {donor_length:g} × {donor_width:g} × "
                    f"{donor_thickness:g} mm\n\n"
                    f"Predicted Compatibility: {compatibility}\n"
                    f"Model Confidence: {confidence:.2f}%"
                )
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numerical measurements.",
                parent=window
            )
        except (TypeError, KeyError):
            messagebox.showwarning(
                "Missing Patient Data",
                "Please complete the knee measurements before using What-If Simulation.",
                parent=window
            )
        except Exception as error:
            messagebox.showerror(
                "Simulation Error",
                "Could not run the ML simulation.\n\n" + str(error),
                parent=window
            )

    tk.Button(
        card,
        text="RUN ML SIMULATION",
        command=run_simulation,
        font=("Arial", 12, "bold"),
        bg=NAVY_DARK,
        fg=WHITE,
        activebackground=NAVY,
        activeforeground=WHITE,
        relief="flat",
        width=22,
        pady=9,
        cursor="hand2"
    ).pack(anchor="w", padx=55, pady=(16, 8))

    tk.Label(
        window,
        text=(
            "What-If Simulation changes only the test donor values; "
            "the trained Random Forest model remains unchanged."
        ),
        font=("Arial", 9),
        fg=MUTED,
        bg=CREAM
    ).place(relx=0.5, rely=0.915, anchor="center")

    tk.Button(
        window,
        text="CLOSE",
        command=window.destroy,
        font=("Arial", 11, "bold"),
        bg=BEIGE,
        fg=NAVY,
        activebackground=BEIGE_DARK,
        activeforeground=NAVY,
        relief="flat",
        width=14,
        pady=6,
        cursor="hand2"
    ).place(relx=0.5, rely=0.955, anchor="center")


# ============================================================
# GENERATE REPORT WINDOW
# ============================================================

def generate_report():
    """Create and display the separate styled KneePrint analysis report.
       Only the report window is handled here; the rest of the application
       remains unchanged.
    """
    try:
        # --------------------------------------------------------
        # EXISTING MEASUREMENTS / ML RESULTS
        # --------------------------------------------------------
        left_data = measurement_values.get("left", {})
        right_data = measurement_values.get("right", {})
        data = right_data if right_data else left_data

        length = float(data.get("Meniscus Length"))
        mwidth = float(data.get("Meniscus Width"))
        thickness = float(data.get("Meniscus Thickness"))

        from ML_Model.ml_donor_matching import MLDonorMatcher

        patient_meniscus = {
            "Meniscus Length": length,
            "Meniscus Width": mwidth,
            "Meniscus Thickness": thickness
        }
        matches = MLDonorMatcher(patient_meniscus).get_top_matches(4)

        # --------------------------------------------------------
        # SAVE THE EXISTING TEXT REPORT
        # --------------------------------------------------------
        report_folder = os.path.join(PROJECT_ROOT, "Analysis_Report")
        os.makedirs(report_folder, exist_ok=True)
        report_path = os.path.join(report_folder, "kneeprint_report.txt")

        def value_text(source, key):
            value = source.get(key, "--")
            return str(value)

        report_lines = [
            "KNEEPRINT ANALYSIS REPORT",
            "=" * 55,
            "",
            "EDUCATIONAL PROTOTYPE - AI-ASSISTED ANALYSIS",
            "",
            "PATIENT MEASUREMENT PROFILE",
            "-" * 55,
            "Affected/Analyzed Knee: Right",
            "",
            "LEFT KNEE MEASUREMENTS",
            f"Knee Width          : {value_text(left_data, 'Knee Width')} mm",
            f"Knee Depth          : {value_text(left_data, 'Knee Depth')} mm",
            f"Meniscus Length     : {value_text(left_data, 'Meniscus Length')} mm",
            f"Meniscus Width      : {value_text(left_data, 'Meniscus Width')} mm",
            f"Meniscus Thickness  : {value_text(left_data, 'Meniscus Thickness')} mm",
            "",
            "RIGHT KNEE MEASUREMENTS",
            f"Knee Width          : {value_text(right_data, 'Knee Width')} mm",
            f"Knee Depth          : {value_text(right_data, 'Knee Depth')} mm",
            f"Meniscus Length     : {value_text(right_data, 'Meniscus Length')} mm",
            f"Meniscus Width      : {value_text(right_data, 'Meniscus Width')} mm",
            f"Meniscus Thickness  : {value_text(right_data, 'Meniscus Thickness')} mm",
            "",
            "ML MODEL",
            "-" * 55,
            "Random Forest Classifier",
            "",
            "TOP ML DONOR MATCHES",
            "-" * 55,
        ]

        for i, donor in enumerate(matches, 1):
            try:
                confidence = float(donor.get("Confidence", 0)) * 100
                confidence_text = f"{confidence:.2f}%"
            except Exception:
                confidence_text = "--"
            report_lines.extend([
                f"{i}. Donor ID: {donor.get('Donor_ID', '--')}",
                f"   Side: {donor.get('Side', '--')}",
                f"   Meniscus Type: {donor.get('Meniscus_Type', '--')}",
                f"   Dimensions: {donor.get('Length_mm', '--')} x {donor.get('Width_mm', '--')} x {donor.get('Thickness_mm', '--')} mm",
                f"   Compatibility: {donor.get('Compatibility', '--')}",
                f"   Confidence: {confidence_text}",
                ""
            ])

        report_lines.extend([
            "KNEEPRINT VISUALIZATION",
            "-" * 55,
            "The KneePrint diagrams are measurement-derived visual representations.",
            "They are separate from the Random Forest donor matching.",
            "",
            "DISCLAIMER",
            "-" * 55,
            "This is an educational prototype using synthetic/sample data.",
            "It does not determine clinical transplant suitability.",
        ])

        with open(report_path, "w", encoding="utf-8") as file:
            file.write("\n".join(report_lines))

        # --------------------------------------------------------
        # REPORT WINDOW — STYLED LIKE THE REFERENCE DESIGN
        # --------------------------------------------------------
        window = tk.Toplevel(root)
        window.title("KneePrint - Analysis Report")
        window.geometry("1500x900")
        window.minsize(1200, 760)
        window.configure(bg=CREAM)

        # ---------- HEADER ----------
        header = tk.Frame(window, bg=NAVY_DARK, height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="KneePrint", bg=NAVY_DARK, fg=WHITE,
            font=("Georgia", 28, "bold")
        ).pack(side="left", padx=(45, 25))

        tk.Frame(header, bg="#B8B1A8", width=1, height=45).pack(side="left", pady=18)

        tk.Label(
            header,
            text="MENISCUS DONOR\nMATCHING SYSTEM",
            bg=NAVY_DARK, fg="#DCD5CC",
            font=("Arial", 10), justify="left"
        ).pack(side="left", padx=25)

        tk.Label(
            header,
            text="EDUCATIONAL PROTOTYPE   •   AI-ASSISTED ANALYSIS",
            bg=NAVY_DARK, fg="#DCD5CC",
            font=("Arial", 9)
        ).pack(side="right", padx=45)

        # ---------- SCROLLABLE REPORT BODY ----------
        body_canvas = tk.Canvas(window, bg=CREAM, highlightthickness=0)
        scrollbar = tk.Scrollbar(window, orient="vertical", command=body_canvas.yview)
        body_canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        body_canvas.pack(side="left", fill="both", expand=True)

        content = tk.Frame(body_canvas, bg=CREAM)
        body_window = body_canvas.create_window((0, 0), window=content, anchor="nw")

        def resize_content(event=None):
            body_canvas.configure(scrollregion=body_canvas.bbox("all"))
            body_canvas.itemconfigure(body_window, width=body_canvas.winfo_width())

        content.bind("<Configure>", resize_content)
        body_canvas.bind("<Configure>", resize_content)

        # ---------- TITLE ----------
        tk.Label(
            content,
            text="KNEEPRINT ANALYSIS REPORT",
            bg=CREAM, fg=NAVY,
            font=("Georgia", 31, "bold")
        ).pack(pady=(20, 0))

        title_line = tk.Frame(content, bg=CREAM)
        title_line.pack(pady=(3, 5))
        tk.Frame(title_line, bg=BEIGE_DARK, width=95, height=2).pack(side="left", padx=12)
        tk.Label(
            title_line, text="Generated ML Donor Analysis",
            bg=CREAM, fg=NAVY, font=("Arial", 12)
        ).pack(side="left")
        tk.Frame(title_line, bg=BEIGE_DARK, width=95, height=2).pack(side="left", padx=12)

        # ---------- DECORATIVE BACKGROUND ----------
        # This stays lightweight and uses only Tkinter.
        deco = tk.Canvas(content, height=1, bg=CREAM, highlightthickness=0)
        deco.pack(fill="x")

        # ---------- KNEEPRINT CARDS ----------
        visual_frame = tk.Frame(content, bg=CREAM)
        visual_frame.pack(fill="x", padx=75, pady=(8, 16))

        def make_visual(parent, title, measurements):
            card = tk.Frame(
                parent, bg=WHITE,
                highlightbackground="#E0D6CA", highlightthickness=1
            )

            title_row = tk.Frame(card, bg=WHITE)
            title_row.pack(fill="x", padx=28, pady=(14, 0))
            tk.Label(
                title_row, text=title, bg=WHITE, fg=NAVY,
                font=("Georgia", 16, "bold")
            ).pack(side="left")

            main = tk.Frame(card, bg=WHITE)
            main.pack(fill="both", expand=True, padx=22, pady=(2, 15))

            drawing = tk.Canvas(
                main, width=390, height=255,
                bg=WHITE, highlightthickness=0
            )
            drawing.pack(side="left", fill="both", expand=True)

            info = tk.Frame(main, bg="#F5F0E8")
            info.pack(side="right", padx=(8, 0), pady=25, ipadx=16, ipady=12)

            tk.Label(
                info, text=f"Length:   {value_text(measurements, 'Meniscus Length')} mm",
                bg="#F5F0E8", fg=NAVY, font=("Arial", 12)
            ).pack(anchor="w", padx=8, pady=5)
            tk.Label(
                info, text=f"Width:    {value_text(measurements, 'Meniscus Width')} mm",
                bg="#F5F0E8", fg=NAVY, font=("Arial", 12)
            ).pack(anchor="w", padx=8, pady=5)
            tk.Label(
                info, text=f"Thickness: {value_text(measurements, 'Meniscus Thickness')} mm",
                bg="#F5F0E8", fg=NAVY, font=("Arial", 12)
            ).pack(anchor="w", padx=8, pady=5)

            tk.Frame(info, bg=BEIGE_DARK, height=1, width=180).pack(padx=8, pady=(8, 3))
            tk.Label(
                info, text=title, bg="#F5F0E8", fg=NAVY,
                font=("Georgia", 11, "bold")
            ).pack(pady=(3, 0))

            def draw_kneeprint():
                drawing.delete("all")
                w = drawing.winfo_width()
                h = drawing.winfo_height()
                if w < 100:
                    return

                cx = min(w * 0.48, 190)
                cy = h / 2

                try:
                    lval = float(measurements.get("Meniscus Length", 42))
                except Exception:
                    lval = 42
                try:
                    wval = float(measurements.get("Meniscus Width", 28))
                except Exception:
                    wval = 28

                # Fingerprint-like measurement-derived arcs.
                scale_x = max(0.78, min(1.22, lval / 42.0))
                scale_y = max(0.78, min(1.22, wval / 28.0))
                arc_w = 235 * scale_x
                arc_h = 125 * scale_y

                # Upper and lower curved lines.
                for i in range(9):
                    inset = i * 8
                    drawing.create_arc(
                        cx - arc_w/2 + inset, cy - arc_h/2 + i*1.5,
                        cx + arc_w/2 - inset, cy + 35,
                        start=205, extent=130,
                        style="arc", outline=NAVY, width=1
                    )

                for i in range(11):
                    inset = i * 8
                    drawing.create_arc(
                        cx - arc_w/2 + inset, cy - 5,
                        cx + arc_w/2 - inset, cy + arc_h/2 + i*1.8,
                        start=25, extent=130,
                        style="arc", outline=NAVY, width=1
                    )

                # Outer measurement form.
                drawing.create_oval(
                    cx - 42*scale_x, cy - 88*scale_y,
                    cx + 42*scale_x, cy + 88*scale_y,
                    outline=NAVY, width=3
                )
                drawing.create_oval(
                    cx - 23*scale_x, cy - 48*scale_y,
                    cx + 23*scale_x, cy + 48*scale_y,
                    outline="#71809A", width=2
                )

                # Four measurement points.
                pts = [
                    (cx, cy-101*scale_y),
                    (cx-66*scale_x, cy),
                    (cx+66*scale_x, cy),
                    (cx, cy+101*scale_y)
                ]
                for px, py in pts:
                    drawing.create_oval(px-4, py-4, px+4, py+4, fill=NAVY, outline="")

            drawing.bind("<Configure>", lambda e: draw_kneeprint())
            card.after(40, draw_kneeprint)
            return card

        left_card = make_visual(visual_frame, "LEFT KNEEPRINT", left_data)
        left_card.pack(side="left", fill="both", expand=True, padx=(0, 8))

        right_card = make_visual(visual_frame, "RIGHT KNEEPRINT", right_data)
        right_card.pack(side="left", fill="both", expand=True, padx=(8, 0))

        # ---------- INFORMATION GRID ----------
        grid = tk.Frame(content, bg=WHITE, highlightbackground="#E0D6CA", highlightthickness=1)
        grid.pack(fill="x", padx=75, pady=(0, 15))

        def section_title(parent, text, width=None):
            row = tk.Frame(parent, bg=WHITE)
            row.pack(fill="x", padx=18, pady=(13, 7))
            icon = tk.Canvas(row, width=34, height=34, bg=WHITE, highlightthickness=0)
            icon.pack(side="left")
            icon.create_oval(3, 3, 31, 31, fill="#F5F0E8", outline=BEIGE_DARK)
            icon.create_text(17, 17, text="•", fill=NAVY, font=("Arial", 16, "bold"))
            tk.Label(
                row, text=text, bg=WHITE, fg=NAVY,
                font=("Georgia", 14, "bold")
            ).pack(side="left", padx=10)
            return row

        # Left: analyzed knee profile
        profile = tk.Frame(grid, bg=WHITE)
        profile.pack(side="left", fill="both", expand=True, padx=(18, 8), pady=12)
        section_title(profile, "AFFECTED KNEE MENISCUS PROFILE")

        profile_table = tk.Frame(profile, bg="#F7F3ED")
        profile_table.pack(fill="x", padx=4)

        profile_rows = [
            ("Knee Width", value_text(data, "Knee Width")),
            ("Knee Depth", value_text(data, "Knee Depth")),
            ("Meniscus Length", value_text(data, "Meniscus Length")),
            ("Meniscus Width", value_text(data, "Meniscus Width")),
            ("Meniscus Thickness", value_text(data, "Meniscus Thickness")),
        ]
        for label, val in profile_rows:
            row = tk.Frame(profile_table, bg="#F7F3ED")
            row.pack(fill="x")
            tk.Label(row, text=label, bg="#F7F3ED", fg=TEXT, font=("Arial", 10), width=22, anchor="w").pack(side="left", padx=10, pady=4)
            tk.Label(row, text=f"{val} mm", bg="#F7F3ED", fg=NAVY, font=("Arial", 10), anchor="e").pack(side="right", padx=12)

        # Right: bilateral comparison
        comparison = tk.Frame(grid, bg=WHITE)
        comparison.pack(side="left", fill="both", expand=True, padx=(8, 18), pady=12)
        section_title(comparison, "BILATERAL KNEE COMPARISON")

        comp_table = tk.Frame(comparison, bg="#F7F3ED")
        comp_table.pack(fill="x", padx=4)

        heads = tk.Frame(comp_table, bg="#EFE8DD")
        heads.pack(fill="x")
        for text_, width_ in [("Measurement", 21), ("Left Knee (mm)", 14), ("Right Knee (mm)", 14)]:
            tk.Label(heads, text=text_, bg="#EFE8DD", fg=NAVY, font=("Arial", 9, "bold"), width=width_).pack(side="left", pady=5)

        for key in ["Knee Width", "Knee Depth", "Meniscus Length", "Meniscus Width", "Meniscus Thickness"]:
            row = tk.Frame(comp_table, bg=WHITE)
            row.pack(fill="x")
            tk.Label(row, text=key, bg=WHITE, fg=TEXT, font=("Arial", 9), width=21, anchor="w").pack(side="left", padx=7, pady=3)
            tk.Label(row, text=value_text(left_data, key), bg=WHITE, fg=NAVY, font=("Arial", 9), width=14).pack(side="left", pady=3)
            tk.Label(row, text=value_text(right_data, key), bg=WHITE, fg=NAVY, font=("Arial", 9), width=14).pack(side="left", pady=3)

        # ---------- ML RESULTS + SUMMARY ----------
        lower = tk.Frame(content, bg=CREAM)
        lower.pack(fill="x", padx=75, pady=(0, 18))

        ml_card = tk.Frame(lower, bg=WHITE, highlightbackground="#E0D6CA", highlightthickness=1)
        ml_card.pack(side="left", fill="both", expand=True, padx=(0, 8))
        section_title(ml_card, "ML DONOR MATCHING RESULTS")

        table = tk.Frame(ml_card, bg=WHITE)
        table.pack(fill="x", padx=18, pady=(0, 16))

        headers = [("#", 5), ("Donor ID", 12), ("Compatibility", 16), ("Confidence", 13)]
        for htext, hwidth in headers:
            tk.Label(table, text=htext, bg="#EFE8DD", fg=NAVY, font=("Arial", 9, "bold"), width=hwidth).grid(row=0, column=headers.index((htext,hwidth)), sticky="nsew", pady=1)

        for i, donor in enumerate(matches, 1):
            try:
                conf = f"{float(donor.get('Confidence', 0))*100:.2f}%"
            except Exception:
                conf = "--"
            comp = str(donor.get("Compatibility", "--"))
            comp_bg = "#E9F0E5" if comp == "High" else ("#F4EEDC" if comp == "Medium" else "#F8E1E1")
            comp_fg = "#3D6543" if comp == "High" else ("#856A28" if comp == "Medium" else "#B23B3B")

            tk.Label(table, text=str(i), bg=WHITE, fg=TEXT, font=("Arial", 9), width=5).grid(row=i, column=0, pady=3)
            tk.Label(table, text=str(donor.get("Donor_ID", "--")), bg=WHITE, fg=NAVY, font=("Arial", 9), width=12).grid(row=i, column=1, pady=3)
            tk.Label(table, text=comp, bg=comp_bg, fg=comp_fg, font=("Arial", 9, "bold"), width=16).grid(row=i, column=2, pady=3)
            tk.Label(table, text=conf, bg=WHITE, fg=NAVY, font=("Arial", 9), width=13).grid(row=i, column=3, pady=3)

        summary_card = tk.Frame(lower, bg=WHITE, highlightbackground="#E0D6CA", highlightthickness=1)
        summary_card.pack(side="left", fill="both", expand=True, padx=(8, 0))
        section_title(summary_card, "ANALYSIS SUMMARY")

        summary_text = (
            "The Random Forest model compares the patient's meniscus "
            "measurements with donor measurements to predict compatibility. "
            "The top 4 donor candidates are shown with their predicted "
            "compatibility and model confidence scores.\n\n"
            "The KneePrint visuals above are a separate measurement-derived "
            "representation and are not used as biometric identification."
        )
        tk.Label(
            summary_card, text=summary_text,
            bg="#F7F3ED", fg=TEXT,
            font=("Arial", 10), justify="left", wraplength=570,
            padx=20, pady=15
        ).pack(fill="both", expand=True, padx=18, pady=(0, 18))

        tk.Label(
            content,
            text="Educational prototype using synthetic/sample data. The result does not determine clinical transplant suitability.",
            bg=CREAM, fg=MUTED, font=("Arial", 9)
        ).pack(pady=(0, 8))

        # ---------- BOTTOM BUTTONS ----------
        bottom = tk.Frame(window, bg=CREAM, height=68)
        bottom.pack(fill="x", side="bottom")
        bottom.pack_propagate(False)

        def save_report():
            try:
                with open(report_path, "w", encoding="utf-8") as file:
                    file.write("\n".join(report_lines))
                messagebox.showinfo("Report Saved", f"Report saved successfully:\n\n{report_path}", parent=window)
            except Exception as error:
                messagebox.showerror("Save Error", str(error), parent=window)

        # Center the two buttons inside the bottom bar.
        # Do not calculate padding from winfo_width() here because the
        # window may still report a very small width during creation,
        # which can produce a negative Tkinter padding value.
        button_row = tk.Frame(bottom, bg=CREAM)
        button_row.pack(pady=10)

        tk.Button(
            button_row, text="▣  SAVE REPORT", command=save_report,
            font=("Arial", 11, "bold"), bg=NAVY_DARK, fg=WHITE,
            activebackground=NAVY, activeforeground=WHITE,
            relief="flat", width=25, pady=10, cursor="hand2"
        ).pack(side="left", padx=6)

        tk.Button(
            button_row, text="×  CLOSE", command=window.destroy,
            font=("Arial", 11, "bold"), bg="#D6CCC0", fg=NAVY,
            activebackground="#C8BDAF", activeforeground=NAVY,
            relief="flat", width=25, pady=10, cursor="hand2"
        ).pack(side="left", padx=6)

        window.transient(root)
        window.grab_set()
        body_canvas.yview_moveto(0)

    except (ValueError, TypeError):
        messagebox.showwarning(
            "Missing Measurements",
            "Please complete the knee measurements before generating the report."
        )
    except Exception as error:
        messagebox.showerror(
            "Report Error",
            "Could not generate the report.\n\n" + str(error)
        )


# ============================================================
# PAGE 5 — ML DONOR MATCHING
# ============================================================

def show_ml_matching():
    global current_page
    current_page = 5
    clear_canvas()
    draw_background()
    draw_header()

    # Reference design uses KneePrint as the active visual step.
    draw_progress(4)

    width = canvas.winfo_width()
    center_x = width / 2

    # TITLE
    canvas.create_text(center_x, 255, text="ML DONOR MATCHING",
                       font=("Georgia", 38, "bold"), fill=NAVY)
    canvas.create_line(center_x-285,305,center_x-205,305,fill=BEIGE_DARK,width=2)
    canvas.create_text(center_x,305,text="Random Forest Compatibility Prediction",
                       font=("Arial",14),fill=MUTED)
    canvas.create_line(center_x+205,305,center_x+285,305,fill=BEIGE_DARK,width=2)

    # PATIENT / ANALYZED KNEE
    data = measurement_values.get("right", {})
    length = data.get("Meniscus Length", "--")
    mwidth = data.get("Meniscus Width", "--")
    thickness = data.get("Meniscus Thickness", "--")

    ix1, ix2, iy1, iy2 = center_x-425, center_x+425, 330, 410
    canvas.create_rectangle(ix1+6,iy1+7,ix2+6,iy2+7,fill="#D5CCC0",outline="")
    rounded_rectangle(ix1,iy1,ix2,iy2,radius=18,fill=WHITE,outline=WHITE)

    # Small knee icon
    kx, ky = ix1+95, (iy1+iy2)/2
    canvas.create_oval(kx-28,ky-28,kx+28,ky+28,fill="#F5F1EA",outline="#D8CDBE",width=2)
    canvas.create_line(kx-7,ky-18,kx-7,ky-2,kx-14,ky+10,kx-8,ky+21,fill=NAVY,width=4,smooth=True)
    canvas.create_line(kx+7,ky-18,kx+7,ky-2,kx+14,ky+10,kx+8,ky+21,fill=NAVY,width=4,smooth=True)
    canvas.create_text(kx+60,iy1+28,text="Analyzed Knee: Right",anchor="w",font=("Arial",13),fill=TEXT)
    canvas.create_text(kx+60,iy1+57,text=f"Length: {length} mm    |    Width: {mwidth} mm    |    Thickness: {thickness} mm",anchor="w",font=("Arial",11),fill=TEXT)

    # REAL RANDOM FOREST MATCHING
    try:
        from ML_Model.ml_donor_matching import MLDonorMatcher
        patient_meniscus={"Meniscus Length":float(length),"Meniscus Width":float(mwidth),"Meniscus Thickness":float(thickness)}
        matches=MLDonorMatcher(patient_meniscus).get_top_matches(4)
    except Exception as error:
        messagebox.showerror("ML Matching Error", "The Random Forest donor matching could not be loaded.\n\n" + str(error))
        return

    # MATCHES CARD
    # Keep the card compact so the navigation buttons remain fully visible.
    # The canvas height must be read locally; using an undefined/global
    # height here can make the bottom controls disappear.
    height = canvas.winfo_height()
    x1,x2,y1,y2=110,width-110,420,min(700, height-145)
    canvas.create_rectangle(x1+7,y1+8,x2+7,y2+8,fill="#D5CCC0",outline="")
    rounded_rectangle(x1,y1,x2,y2,radius=20,fill=WHITE,outline=WHITE)
    canvas.create_text(x1+30,y1+30,text="TOP ML DONOR MATCHES",anchor="w",font=("Arial",16,"bold"),fill=NAVY)

    mx1,mx2,my1,my2=x2-245,x2-25,y1+16,y1+46
    rounded_rectangle(mx1,my1,mx2,my2,radius=10,fill="#F1EBE3",outline="#E0D6CA")
    canvas.create_text((mx1+mx2)/2,(my1+my2)/2,text="Based on Random Forest Classifier",font=("Arial",8,"bold"),fill=TEXT)

    left,right=x1+25,x2-25
    hy1,hy2=y1+60,y1+96
    canvas.create_rectangle(left,hy1,right,hy2,fill="#F1EBE3",outline="")
    uw=right-left
    cols=[left+uw*.035,left+uw*.18,left+uw*.43,left+uw*.65,left+uw*.89]
    for pos,label in zip(cols,["#","Donor ID","Compatibility","Confidence","View Details"]):
        canvas.create_text(pos,(hy1+hy2)/2,text=label,font=("Arial",10,"bold"),fill=TEXT)

    detail_areas=[]
    row=hy2+18
    for i,donor in enumerate(matches[:4],1):
        did=donor.get("Donor_ID","--")
        comp=donor.get("Compatibility","--")
        try: conf=f"{float(donor.get('Confidence',0))*100:.2f}%"
        except: conf="--"
        if comp=="High": fill,textc="#DCE8D8","#345A3C"
        elif comp=="Medium": fill,textc="#E9DFCE","#75602E"
        else: fill,textc="#F4D8D2","#963D32"

        canvas.create_rectangle(left,row-22,right,row+22,fill=WHITE,outline="#F0EBE4")
        canvas.create_text(cols[0],row,text=str(i),font=("Arial",10),fill=TEXT)
        canvas.create_text(cols[1],row,text=str(did),font=("Arial",11,"bold"),fill=NAVY)
        rounded_rectangle(cols[2]-45,row-16,cols[2]+45,row+16,radius=14,fill=fill,outline=fill)
        canvas.create_text(cols[2],row,text=str(comp),font=("Arial",9,"bold"),fill=textc)
        canvas.create_text(cols[3],row,text=conf,font=("Arial",10),fill=TEXT)
        dx1,dx2=cols[4]-78,cols[4]+78
        rounded_rectangle(dx1,row-17,dx2,row+17,radius=10,fill=WHITE,outline="#D8CDBE",tags="donor_detail")
        canvas.create_text(cols[4],row,text="View Details",font=("Arial",9,"bold"),fill=TEXT,tags="donor_detail")
        detail_areas.append((dx1,dx2,row-20,row+20,donor))
        row+=42

    # --------------------------------------------------------
    # BOTTOM ACTION BUTTONS
    # --------------------------------------------------------
    # Use Canvas tag bindings instead of relying only on coordinate
    # checks. This makes the buttons work even when Windows DPI scaling
    # changes the physical size of the window.

    # Always reserve a dedicated bottom strip for the four navigation/action
    # controls. This keeps them visible even when the window is resized.
    # Raise the bottom controls so every action remains fully visible.
    button_y2 = height - 70
    button_y1 = button_y2 - 58

    margin = 120
    gap = 18
    usable = width - 2 * margin
    back_w = 170
    action_w = (usable - back_w - (3 * gap)) / 3

    back = (margin, margin + back_w)
    explain = (back[1] + gap, back[1] + gap + action_w)
    whatif = (explain[1] + gap, explain[1] + gap + action_w)
    report = (whatif[1] + gap, width - margin)

    rounded_rectangle(
        back[0], button_y1, back[1], button_y2,
        radius=25, fill=WHITE, outline=BEIGE_DARK, width=2,
        tags="ml_back_btn"
    )
    canvas.create_text(
        (back[0] + back[1]) / 2,
        (button_y1 + button_y2) / 2,
        text="←  BACK",
        font=("Arial", 11, "bold"), fill=NAVY,
        tags="ml_back_btn"
    )

    rounded_rectangle(
        explain[0], button_y1, explain[1], button_y2,
        radius=12, fill=BEIGE, outline=BEIGE,
        tags="explain_ml_btn"
    )
    canvas.create_text(
        (explain[0] + explain[1]) / 2,
        (button_y1 + button_y2) / 2,
        text="EXPLAIN ML RESULT",
        font=("Arial", 10, "bold"), fill=NAVY,
        tags="explain_ml_btn"
    )

    rounded_rectangle(
        whatif[0], button_y1, whatif[1], button_y2,
        radius=12, fill=BEIGE, outline=BEIGE,
        tags="what_if_btn"
    )
    canvas.create_text(
        (whatif[0] + whatif[1]) / 2,
        (button_y1 + button_y2) / 2,
        text="WHAT-IF SIMULATION",
        font=("Arial", 10, "bold"), fill=NAVY,
        tags="what_if_btn"
    )

    rounded_rectangle(
        report[0], button_y1, report[1], button_y2,
        radius=12, fill=NAVY_DARK, outline=NAVY_DARK,
        tags="report_btn"
    )
    canvas.create_text(
        (report[0] + report[1]) / 2 - 10,
        (button_y1 + button_y2) / 2,
        text="GENERATE REPORT",
        font=("Arial", 10, "bold"), fill=WHITE,
        tags="report_btn"
    )
    canvas.create_text(
        report[1] - 25,
        (button_y1 + button_y2) / 2,
        text="→",
        font=("Arial", 18, "bold"), fill=WHITE,
        tags="report_btn"
    )

    def view_details(donor):
        try:
            confidence = f"{float(donor.get('Confidence', 0)) * 100:.2f}%"
        except Exception:
            confidence = "--"

        messagebox.showinfo(
            f"Donor {donor.get('Donor_ID', '--')} Details",
            f"Donor ID: {donor.get('Donor_ID', '--')}\n"
            f"Side: {donor.get('Side', '--')}\n"
            f"Meniscus Type: {donor.get('Meniscus_Type', '--')}\n\n"
            f"Length: {donor.get('Length_mm', '--')} mm\n"
            f"Width: {donor.get('Width_mm', '--')} mm\n"
            f"Thickness: {donor.get('Thickness_mm', '--')} mm\n\n"
            f"Compatibility: {donor.get('Compatibility', '--')}\n"
            f"Confidence: {confidence}"
        )

    def explain_action():
        show_explanation()

    def what_if_action():
        show_what_if()

    def report_action():
        generate_report()

    # Direct button bindings — these are much more reliable than the
    # previous single canvas coordinate binding.
    canvas.tag_bind("ml_back_btn", "<Button-1>", lambda e: show_knee_analysis())
    canvas.tag_bind("explain_ml_btn", "<Button-1>", lambda e: explain_action())
    canvas.tag_bind("what_if_btn", "<Button-1>", lambda e: what_if_action())
    canvas.tag_bind("report_btn", "<Button-1>", lambda e: report_action())

    for tag in ("ml_back_btn", "explain_ml_btn", "what_if_btn", "report_btn"):
        canvas.tag_bind(tag, "<Enter>", lambda e: canvas.configure(cursor="hand2"))
        canvas.tag_bind(tag, "<Leave>", lambda e: canvas.configure(cursor=""))

    # Donor detail areas still use the canvas-level handler.
    def detail_click(event):
        for a, b, c, d, donor in detail_areas:
            if a <= event.x <= b and c <= event.y <= d:
                view_details(donor)
                return

    canvas.tag_bind("donor_detail", "<Button-1>", lambda e: None)
    canvas.bind("<Button-1>", detail_click)

    canvas.create_text(
        center_x,
        min(height - 12, 825),
        text=(
            "Educational prototype using synthetic/sample data. "
            "It does not determine clinical transplant suitability."
        ),
        font=("Arial", 9), fill=MUTED
    )

# ============================================================
# HOME BUTTON CLICK
# ============================================================

def home_click(event):

    width = canvas.winfo_width()

    center_x = width / 2

    button_width = 410

    bx1 = center_x - button_width / 2
    bx2 = center_x + button_width / 2

    by1 = 330 + 270
    by2 = by1 + 70

    if (
        bx1 <= event.x <= bx2
        and by1 <= event.y <= by2
    ):
        show_patient_profile()


# ============================================================
# INITIAL HOME CLICK BINDING
# ============================================================

def page1_click(event):

    if current_page == 1:
        home_click(event)


canvas.bind(
    "<Button-1>",
    page1_click
)


# ============================================================
# RESIZE
# ============================================================

def resize(event):

    if event.widget == canvas:

        if current_page == 1:
            show_home()

        elif current_page == 2:
            show_knee_measurements()

        elif current_page == 3:
            show_knee_analysis()

        elif current_page == 5:
            show_ml_matching()


# Don't bind resize directly because recreating Entry widgets
# repeatedly during resizing can cause problems.
# Initial drawing is performed after the window appears.


# ============================================================
# INITIAL DISPLAY
# ============================================================

root.after(
    100,
    show_home
)

# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()
    

