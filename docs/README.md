# **The Swedish Twitter Bot**
***
![Icon](Assets/swedish_twitter_bot_final.jpeg) <br>

## Register
***
1. [Introduction](#introduction)
2. [Details](#details)
3. [Bot commands](#bot-commands)
   - 3.1. [Status command](#--status-command)
   - 3.2. [Load command](#--load-command)
   - 3.3. [Help command](#--help-command)
4. [Socials](#--socials)

## Introduction
***
Hej! I am the **Swedish Twitter Bot!** <br>
I *retweet* hourly under #Sweden and #Sverige on **Twitter**! 🇸🇪 <br>
I'm also a **Discord Bot** with multiple functions!

![Discord bot](Assets/bot_status.png)

## Details
***
> ✅ | [**Twitter Profile**](https://twitter.com/TheSwedishBot) <br>
> ✅ | [**Google Spreadsheet**](https://docs.google.com/spreadsheets/d/1Y8az4H5XGhBtKizaz6atYyhMCUeVif2c7-hUXNEtlhw/edit?usp=sharing) <br>
> ✅ | [**Add to your server**](https://discord.com/api/oauth2/authorize?client_id=860479686156353556&permissions=2148005952&scope=bot) <br>
> Created via `gspread`, `tweepy`, `discord.py`, `flask`.

## Bot commands
***
Use any of my *commands* by the *default bot prefix*: <br>
(abbreviation **DBP**) `--` or just *mention me* `@The Swedish Twitter Bot`; <br>
use my *command prefix or command aliases* (abbreviation **CP**).

```*NOTE*: different operators in a single command are stylized with a space```

### 📶 | **Status command**
> - Invoke aliases: `Status`, `status` or `s` <br>
> - Syntax: `DBP CP` <br>
> - Reports current trends about the database and the latency (ping) status
> 
> ![Status command](Assets/status_command_screenshot.png)

### ⏬ | **Load command**
> - Invoke aliases: `Load`, `load`, `l` <br>
> - Default syntax: `DBP CP operator n k`; `operator: str = None`, `n: int = 5`, `k: float = 5.0` [operator, n, k are *optional values*; their *type* and *default value* are specified] <br>
> - **Primitive load**: `CBP CD` - loads the latest submission in an embedded text message <br>
> - **Complex load**: Corresponding to *Default syntax*; `operator` prefix `recent` or `r`; <br>
> `n` specifies the *number of retrieved tweets*; `k` specifies their *input interval* (i.e., delay) <br>
> - E.g., `--load recent 10 2` - loads 10 recent tweets and displays them with a 2 sec. delay
> 
> ![Load command](Assets/load_command_screenshot.png)

### ℹ️ | **Help command**
> - Invoke aliases: `Help`, `help`, `h` <br>
> - Syntax: `DBP CP` <br>
> - Reports possible guidance and appropriate information
> 
> ![Help command](Assets/help_command_screenshot.png) 

### 📩 | Socials
> 1. [@TheSwedishBot](https://twitter.com/TheSwedishBot) <br>
> 2. [@michalspano](https://github.com/michalspano)
