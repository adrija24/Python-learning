import win32com.client as wincl

shoutout = ["Aritra", "Aarav", "Saanvi", "Vivaan", "Ananya"]
speaker = wincl.Dispatch("SAPI.SpVoice")
for name in shoutout:
    speaker.Speak(f"Shoutout to {name}")
    print(f"Shoutout to {name}")
