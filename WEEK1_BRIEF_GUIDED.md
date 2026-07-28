# Week 1

Welcome aboard. This is a walkthrough. Follow it in order and you'll end the 
week with a real repository on GitHub and a chart you made from market data.

**What you'll have by Friday:**

- Python and VS Code working on your machine
- a chart of a company's share price, saved as an image, that your own code
  produced
- that code on GitHub, where you can send anyone a link to it

**A realistic expectation:** the first three steps are setup, and setup is
the least fun part of programming for everybody, forever. It's also the part
that only has to be done once. Push through it and the rest of the week is
the good bit.

---

## How to use this document

**Type the commands out rather than copying and pasting them.** It feels
slower and it isn't — typing is how you notice the parts you don't
understand, and how your fingers learn the tools. You'll also make typos,
which sounds bad but is actually the fastest way to learn to read error
messages.

**There are checkpoints.** Each one is a small thing to verify before moving
on. Don't skip them. Fixing one broken thing is easy; fixing five at once,
where you can't tell which broke first, is miserable.

**The 30-minute rule.** If you're stuck on the same thing for 30 minutes with
no progress, message your mentor on teams. The only real mistake
available to you this week is going quiet for three days.

When you ask, send these three things:

1. what you were trying to do
2. exactly what you typed
3. exactly what came back — **copy and paste the whole error**, don't
   summarise it. The useful information is usually in the last line, and
   people who read errors for a living can often spot the problem instantly.

**Error messages are not you being told off.** They're the computer trying to
help, in an unfriendly tone of voice. Read them. Most of them literally name
the problem.

---

## Part 0 — Five words you'll need (2 minutes)

You don't need to memorise these. Come back when a word confuses you.

**Terminal** — a window where you type commands instead of clicking things.
It feels archaic, and it's still what most programmers use most of the day,
because typing a command is faster and repeatable in a way clicking isn't.
Also called the command line, shell, PowerShell, or bash.

**Folder / path** — a path is a folder's address, like
`/Users/advait/projects/market-brief`. The terminal is always "sitting in"
one folder at a time, and commands act on wherever it's sitting. Being in the
wrong folder causes a huge share of beginner confusion, so we'll check it
often.

**Package** — code somebody else wrote that you can use in your own project.
We'll use `pandas` (for handling tables of data) and `matplotlib` (for
drawing charts). Nobody writes these from scratch, in the same way nobody
mines their own iron to make a hammer.

**Virtual environment (venv)** — a private box of packages belonging to one
project. Without it, everything installs into one shared pile and eventually
two projects want different versions of the same thing and both break. The
box keeps your projects from fighting.

**git and GitHub** — git records snapshots of your code over time, so you can
see what changed and go back if you break something. GitHub is a website
that stores those snapshots online. They're separate things with confusingly
similar names: git is the tool on your computer, GitHub is the place you send
things to.

---

## Step 1 — Install Python and VS Code

**Python** is the language. Get it from python.org, or:

- **Windows:** easiest route is the Microsoft Store — search "Python 3.12"
  and install. This avoids a common problem where Windows can't find Python
  afterwards.
- **Mac:** download the installer from python.org. Note that Macs come with
  an old Python already installed, which is why on a Mac you type `python3`
  rather than `python` throughout this guide.

**VS Code** is the editor — the program you write code in. Get it from
code.visualstudio.com. Once it's installed, open it and install the
**Python extension**: click the squares icon in the left sidebar, search
"Python", install the one by Microsoft. It gives you colour-coding and
underlines your mistakes before you run anything.

### Checkpoint 1

Open a terminal. In VS Code: the **Terminal** menu → **New Terminal**. A
panel appears at the bottom. That's it.

Type this and press enter:

```bash
python --version
```

You want to see something like `Python 3.12.1`. On a Mac, if that fails, try
`python3 --version`.

> **If it says "command not found" or "not recognized":** the installation
> worked but your computer doesn't know where to find it. On Windows this is
> usually solved by installing from the Microsoft Store instead. Don't spend
> 30 minutes here — this one is genuinely fiddly and not your fault. Message
> your mentor and we'll fix it together on a screen share.

Whichever of `python` or `python3` worked for you — use that one everywhere
below.

---

## Step 2 — Terminal survival kit

Three commands. This is genuinely all you need this week.

```bash
pwd
```

"Print working directory" — tells you which folder you're currently sitting
in. When something mysteriously doesn't work, run this first. On Windows
PowerShell, `pwd` works too.

```bash
ls
```

Lists the files in the current folder. (Windows PowerShell: `ls` works, or
`dir`.)

```bash
cd Downloads
```

"Change directory" — moves into a folder. To go back up one level:

```bash
cd ..
```

Two things that will save you real time:

- **Tab completion.** Type `cd Down` then press Tab, and the terminal
  finishes the word for you. Use this constantly. It's faster and it can't
  typo.
- **Up arrow.** Brings back the last command you ran, so you can rerun or
  edit it instead of retyping.

### Checkpoint 2

Unzip the starter project somewhere you'll remember — Documents is fine, or
wherever you keep schoolwork. Then use `cd` to get into that folder and run
`ls`. You should see `data.py`, `chart.py`, `requirements.txt`,
`example_prices.csv` and a few others.

Now open that same folder in VS Code: **File** → **Open Folder**. Your files
appear in the left sidebar. Using VS Code's built-in terminal from now on is
easier, because it starts out already sitting in the right folder.

---

## Step 3 — Run your first line of Python

Before we touch the project, let's confirm you can write a file and run it.

In VS Code, make a new file called `hello.py` and type this:

```python
name = "Advait"
years = 16

print("Hello, " + name)
print(f"Next year you'll be {years + 1}")
```

Save it (Ctrl+S / Cmd+S), then in the terminal:

```bash
python hello.py
```

Two things happened worth naming. `name` and `years` are **variables** —
labels attached to values. And that `f"..."` is an **f-string**: anything
inside the curly brackets gets calculated and dropped into the text. We'll
use f-strings constantly.

### Checkpoint 3

You saw two lines of output, the second one saying 17.

Now break it on purpose: delete the closing bracket from the last `print` and
run it again. You'll get a `SyntaxError`. Look at what it tells you — it
names the file and the line number. Put the bracket back.

Deliberately breaking things to see what the error looks like is one of the
best habits you can build this week. It means that when something breaks by
accident, the message is already familiar.

You can delete `hello.py` now, or keep it. It served its purpose.

---

## Step 4 — Make the box and fill it

Now the virtual environment. Make sure your terminal is sitting in the
project folder (`pwd` to check), then:

```bash
python -m venv .venv
```

Nothing visible happens, which is normal. It created a hidden `.venv` folder
holding a private copy of Python for this project.

Now **activate** it:

```bash
source .venv/bin/activate      # Mac
.venv\Scripts\activate         # Windows
```

Your terminal prompt should now start with `(.venv)`. That prefix means
you're working inside the box.

> **This is the thing people forget.** Every time you open a new terminal,
> you have to activate again. If a command suddenly complains it can't find
> pandas, check whether `(.venv)` is there. It's the single most common
> cause of "but it worked yesterday".

Now install the packages we need:

```bash
pip install -r requirements.txt
```

`requirements.txt` is just a list of package names. This reads it and
downloads each one. Expect a wall of scrolling text — that's fine. Listing
dependencies in a file like this is how you let someone else set up your
project with one command, which is a small courtesy that makes projects
possible to share at all.

### Checkpoint 4

```bash
python -c "import pandas; print(pandas.__version__)"
```

A version number means the box is built and stocked. Move on.

---

## Step 5 — Look at the data before you touch it

We've included `example_prices.csv` — 90 days of daily prices. These are
**made-up numbers for practice**, not a real company; we'll switch to real
market data at the end of the week.

Make a new file, `explore.py`:

```python
from data import load_example_prices

df = load_example_prices()

print(df.head())
```

Run it with `python explore.py`. You'll see a small table: dates down the
left, and columns for open, high, low, close and volume.

That table is a **DataFrame** — pandas' way of holding data with rows and
columns, like a spreadsheet you control with code. A few things to know:

- `df.head()` shows the first five rows. Handy, because printing all 90 fills
  your screen with noise.
- The dates down the left are the **index** — the row labels rather than a
  normal column.
- `df["close"]` gets you one column: the closing price, meaning the last
  price the share traded at that day.

Add these lines and run it again:

```python
print("Number of rows:", len(df))
print("First date:", df.index[0].date())
print("Last closing price:", df["close"].iloc[-1])
print("Highest close:", df["close"].max())
```

`.iloc[-1]` means "the last one" — negative numbers count backwards from the
end, which is a Python idiom you'll see everywhere.

### Checkpoint 5

You can print the number of rows, and the highest closing price in the
period.

Then answer this for yourself, out loud or in a comment: **what does one row
of this table represent?** If you can say it in a sentence, you understand
the data, and everything after this is just drawing it.

---

## Step 6 — Your first chart

The interesting bit. Open `chart.py` — it has TODO comments in it, and we're
going to work through them together. Here's the whole thing, explained piece
by piece.

The top of the file already has this:

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
```

That middle line tells matplotlib "don't try to open a window, just save
image files". It prevents a class of confusing errors depending on your
setup.

Change the import line to use the example data for now:

```python
from data import load_example_prices
```

And inside `main()`, replace the `get_daily_prices(...)` line with:

```python
df = load_example_prices()
```

Now, the four lines that make a chart. Type them in where the TODOs are:

```python
fig, ax = plt.subplots(figsize=(10, 5))
```

This makes a blank chart, 10 inches by 5. You get two things back: `fig` is
the whole image, `ax` is the area inside the axes where data gets drawn. You
mostly talk to `ax`.

```python
ax.plot(df.index, df["close"], label="Example Co.")
```

Draw a line. X values are the dates (the index), Y values are the closing
prices. The `label` is what shows up in the legend.

```python
ax.set_title("Example Co. — closing price")
ax.set_ylabel("Price (USD)")
ax.legend()
```

Title, y-axis label, and legend. **Never skip these.** An unlabelled chart is
not a chart — it's a squiggle. If you showed it to someone in a meeting the
first question would be "what am I looking at", and you'd have wasted
everyone's time.

```python
fig.savefig("output/my_first_chart.png", bbox_inches="tight", dpi=150)
```

Save it. `bbox_inches="tight"` trims the excess white border, `dpi=150` makes
it sharp enough to actually look at.

Run it:

```bash
python chart.py
```

### Checkpoint 6

Open `output/my_first_chart.png` — click it in the VS Code sidebar. There's
your chart. **You made that.** From a file of numbers, with code you typed.

> **If you get `ModuleNotFoundError: No module named 'data'`:** your terminal
> isn't sitting in the project folder. Run `pwd` and `cd` to the right place.
> Python looks for `data.py` next to the file you're running.
>
> **If you get `FileNotFoundError` mentioning `output`:** the folder is
> missing. `mkdir output` will fix it.

---

## Step 7 — Make it yours

Now stop following instructions and start poking at it. Change one thing at
a time and rerun. If something breaks, you know exactly what caused it.

- change the title to something you'd rather it said
- make the line a different colour: add `color="darkgreen"` inside
  `ax.plot(...)`
- add a grid: `ax.grid(True, alpha=0.3)` — try changing that 0.3
- chart only the last 30 days: `df = df.tail(30)` before you plot
- change the figure size and see what happens to the shape

Try at least three. This step matters more than it looks: reading code
teaches you a little, changing code and seeing what moves teaches you a lot.

**Then a thinking question, no code required.** Look at your y-axis — it
probably starts somewhere around 180 rather than at 0. Try adding
`ax.set_ylim(0, 220)` and compare the two charts side by side. Same data,
very different impression of how dramatic the movement was.

Which one is more honest? There's a real answer, and it depends on what
you're trying to show — but the important realisation is that a chart is
never neutral. Whoever drew it made choices. Bring your answer to the Friday
call; it's the kind of thing people argue about professionally.

---

## Step 8 — Put it on GitHub

Your code currently exists in one place, on one laptop. Let's fix that.

**First, a warning that matters.** The project uses an API key — a password
for the data service. It lives in a file called `.env`, and `.env` must never
go to GitHub. Leaked keys are one of the most common real-world security
mistakes, and they're embarrassing at every level of seniority. The starter
project already lists `.env` in `.gitignore`, which tells git to ignore it,
but you should verify rather than trust. We'll do that in a moment.

Set up git if you never have (it'll be part of your commits forever, so use
your real details):

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Then, in the project folder:

```bash
git init
git status
```

`git status` is the command you'll run most. It shows what's changed and
what's about to be saved.

**Read that output carefully now.** You should see `chart.py`, `explore.py`
and others listed. You should **not** see `.env`. If you do see `.env`, stop
and tell your mentor before doing anything else.

```bash
git add .
git commit -m "Week 1: my first chart from price data"
```

`git add .` stages everything ("these are the changes I mean"), and `commit`
saves the snapshot with a message describing it. Write messages for a human —
a future you, wondering what on earth you were doing.

Now make an account on github.com if you don't have one, create a new **empty**
repository (don't let it add a README — you already have one), and follow the
"push an existing repository" commands it shows you. Two lines, roughly:

```bash
git remote add origin <the URL GitHub gives you>
git push -u origin main
```

Refresh the page. Your code is on the internet.

Finally, open `README.md` and replace the placeholder text with your own
words — what this does, how to set it up, how to run it. Add your chart with:

```markdown
![My first chart](output/my_first_chart.png)
```

Then commit and push again:

```bash
git add .
git commit -m "Add README"
git push
```

### Checkpoint 8

Your repository page shows your code, your README, and your chart. You can
send that link to somebody. That's the deliverable for the week.

---

## Step 9 — Swap in real market data

Everything so far used practice numbers. Time for the real thing.

Your mentor will give you an API key for Alpha Vantage, a service that
provides live share prices. Do this:

1. Find the file `.env.example`, make a copy of it, name the copy `.env`
2. Paste the key in, replacing `paste_the_key_here`
3. In the terminal, run: `python data.py`

You should see five rows of actual Apple share prices, from today's real
market. Try `python data.py MSFT` too.

Now go back to `chart.py` and switch the data source:

```python
from data import get_daily_prices
...
df = get_daily_prices("AAPL", days=90)
```

Run it. **That's a chart of a real company's real share price, and you built
the thing that made it.**

Notice how little you had to change — one import, one line. That's because
both functions hand back a DataFrame with the same shape, so everything built
on top of one works on the other. That idea is worth filing away: it's a big
part of how larger programs are kept from turning into spaghetti.

Commit and push your change.

> One reminder: `git status` before you push, every time. `.env` should never
> appear.

---

## If you still have time

Optional, in rough order of difficulty. **You are not expected to reach
these** — finishing Step 9 is a complete, successful week. Pick whatever
looks fun.

**A. Choose the company from the command line.** Make `python chart.py MSFT`
work, instead of editing the file each time. Look up `sys.argv`. Make sure
plain `python chart.py` still works rather than crashing.

**B. Add a second company.** Plot two lines with a legend. You'll hit
something annoying: if one share costs $200 and the other $30, the cheap one
is squashed flat at the bottom and the chart is useless. Don't look anything
up yet — just think about what you actually want to compare. (Hint if you
want it: we care how much each one *moved*, not what it costs.)

**C. Read `data.py` and write down five questions.** Anything you don't
understand counts, including small things like "what does `orient="index"`
mean". Put them in a file called `questions.md`.

This one is the most useful thing on the list, and it needs no new skills. In
Week 2 you're going to write your own version of that file from scratch, so
these questions are your head start — and they tell your mentor exactly what
to explain first.

---

## Before the Friday call

Write three or four sentences in your README:

- what you got working
- what took longest, or annoyed you most
- one thing you're now curious about

The middle one is not a complaint box — it's genuinely useful information.
If setup ate two days, that's worth knowing, and it isn't a reflection on you.

Then on the call, just run it and let us watch the chart appear. Not a
progress report. A demo.

---

## Appendix — When things go wrong

| What you see | What it usually means |
|---|---|
| `command not found: python` | Try `python3`. If neither works, Python isn't on your PATH — ask for help, this one is fiddly. |
| `ModuleNotFoundError: No module named 'pandas'` | The venv isn't active (no `(.venv)` in your prompt), or `pip install -r requirements.txt` hasn't been run. |
| `ModuleNotFoundError: No module named 'data'` | Your terminal is in the wrong folder. `pwd`, then `cd` to the project. |
| `FileNotFoundError: output/...` | The `output` folder doesn't exist. `mkdir output`. |
| `SyntaxError` | A typo — missing bracket, quote, or colon. The line number in the message is where to look, though the real cause is sometimes the line *above*. |
| `IndentationError` | Python cares about leading spaces. Keep it consistent; let VS Code handle it. |
| `KeyError: 'close'` | You asked for a column that isn't there. `print(df.columns)` to see the real names — watch for capitals. |
| `No API key found` | You made `.env` but it's empty, misnamed (`.env.txt` is a classic on Windows), or in the wrong folder. |
| It worked yesterday and doesn't today | 90% of the time: new terminal, forgot to activate the venv. |

**A note on AI assistants.** You're welcome to use ChatGPT or Claude, and in
Week 3 we'll be building with LLMs ourselves — they're part of the job now.
One rule: **don't submit code you can't explain.** These models can solve
this entire week in about a minute, and if you let them, you'll arrive at
Week 4 with a project you can't debug and nothing to show for the month.

Asking "explain what `.iloc[-1]` does" or "why is my venv not activating" is
an excellent use of them. Asking "write chart.py for me" and pasting the
answer in is how you waste your own summer. Your mentor will ask you to talk
through your code — not as a trap, just because explaining it is the part
where the learning gets locked in.
