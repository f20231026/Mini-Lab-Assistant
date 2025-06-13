import tkinter as tk
from tkinter import messagebox
import winsound
from playsound import playsound

def calculate_molarity():
   
 mass=float(entry_mass.get())
 molar_mass=float(entry_molar_mass.get())
 volume_molarity=float(entry_volume_molarity.get())
 molarity=mass/(molar_mass*volume_molarity)
 result_molarity.config(text=f"Molarity:{molarity:.3f} mol/L")

def calculate_dilution():
   
 molarity1=float(entry_molarity1.get())
 molarity2=float(entry_molarity2.get())
 volume1=float(entry_volume1.get())
 volume2=(molarity1*volume1)/(molarity2)
 result_dilution.config(text=f"Final volume:{volume2:.3f} L")

    

 
 
 
window=tk.Tk()
window.title('mini lab assistant')
window.geometry('400x400')

tk.Label(window,text='your lil molarity calculator').pack()

tk.Label(window, text="Mass (g):").pack()
entry_mass = tk.Entry(window)
entry_mass.pack()

tk.Label(window, text="Molarity1(g):").pack()
entry_molarity1= tk.Entry(window)
entry_molarity1.pack()

tk.Label(window, text="Molarity2(g):").pack()
entry_molarity2= tk.Entry(window)
entry_molarity2.pack()



tk.Label(window, text="Molar Mass (g/mol):").pack()
entry_molar_mass = tk.Entry(window)
entry_molar_mass.pack()

tk.Label(window, text="Volume molarity (L):").pack()
entry_volume_molarity = tk.Entry(window)
entry_volume_molarity.pack()

tk.Label(window, text="Volume1 (L):").pack()
entry_volume1 = tk.Entry(window)
entry_volume1.pack()

tk.Button(window,text='calculate molarity',command=calculate_molarity).pack(pady=5)

tk.Button(window,text='calculate dilution',command=calculate_dilution).pack(pady=5)

result_molarity=tk.Label(window,text='molarity:')
result_molarity.pack()


result_dilution=tk.Label(window,text='final volume :')
result_dilution.pack()


root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x150")

# Step 2: Create a variable to store the time (in seconds)
time_left = 10 # You can change this to any value

# Step 3: Create a label to display the time
timer_label = tk.Label(root, text="", font=("Helvetica", 30))
timer_label.pack(pady=20)

# Step 4: Define the countdown function
def countdown():
    global time_left
    if time_left > 0:
        # Step 4a: Calculate minutes and seconds
        minutes = time_left // 60
        seconds = time_left % 60

        # Step 4b: Update the label with formatted time
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

        

        # Step 4d: Call this function again after 1000 ms (1 second)
        root.after(1000, countdown)
        time_left -= 1
    else:
        # Step 5: Show final message when time is up
        timer_label.config(text="Time's up!")
        playsound("alarm.mp3")

# Step 6: Create a Start button to begin countdown
start_button = tk.Button(root, text="Start Timer", command=countdown)
start_button.pack()

# Step 7: Run the GUI loop
root.mainloop()









