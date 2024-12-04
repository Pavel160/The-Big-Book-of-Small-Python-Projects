# 📄 README: Gullible

**Author**: Al Sweigart (al@inventwithpython.com)

## 🎮 Game Description
"Gullible" is a lighthearted joke program designed to playfully keep the user engaged in an endless loop of questioning. The program asks a simple "yes or no" question, but the humor lies in its persistence: if the user says "yes," the question is asked again, and if the user says "no," the loop ends.

This program is ideal for beginners learning Python as it demonstrates fundamental concepts like loops, conditionals, and input handling.

## 🚀 How It Works
1. The program asks:
"Do you want to know how to keep a gullible person busy for hours?"

2. User responses are interpreted flexibly:
- "Yes," "Y," or variations like "yEs" will continue the loop.
- "No," "N," or similar responses will end the loop.
- Invalid responses prompt a clarification message.

3. When the user decides to stop, the program exits with a kind farewell.

## 🖥️ How to Run
1. Save the script as gullible.py.
2. Run the script in your terminal or IDE:
bash
```
python main.py
```
## 📸 Example Output
```plaintext

Gullible, by Al Sweigart al@inventwithpython.com  

Do you want to know how to keep a gullible person busy for hours? Y/N  
> yes  
Do you want to know how to keep a gullible person busy for hours? Y/N  
> YES  
Do you want to know how to keep a gullible person busy for hours? Y/N  
> maybe  
"maybe" is not a valid yes/no response.  
Do you want to know how to keep a gullible person busy for hours? Y/N  
> no  

Thank you. Have a nice day!
```
## 💡 Key Features

- Flexible Input Handling: Accepts "yes" or "no" in various formats, ensuring user convenience.
- Humor-Focused: A fun and interactive way to entertain yourself or prank a friend.
- Beginner-Friendly: Perfect for learning basic Python concepts.

## 🛠️ Customization
You can tweak the following to personalize the program:

1. Question text: Change the question to any other amusing or repetitive query.
2. Exit message: Update the farewell to fit your desired tone.

## License
See the [LICENSE](LICENSE) file for details.
