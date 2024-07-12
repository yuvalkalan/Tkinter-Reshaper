# Tkinter-Reshaper
String reshaper for Tkinter using RTL language 

## Usage
This script transforms Right-to-Left (RTL) language strings or mixed strings to be displayed correctly in a Tkinter GUI.
It ensures that RTL text is rendered in the correct order and formatting within a Tkinter application.

```python
import reshaper
import tkitner as tk
...
...
root = tk.Tk()
text = 'שלום HI מה נשמע?'
text = reshaper.hebrew_reshaper(text)
label = tk.Label(root, text=text)
label.pack(fill=tk.BOTH)
root.mainloop()
```
