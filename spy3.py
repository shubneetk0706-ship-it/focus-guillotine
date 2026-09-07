import os
import time

# 1. Define your blacklisted application names here (keep them lowercase)
BLACKLIST = ["google chrome", "safari", "firefox"]

print("👀 Focus Guillotine is active. Stay focused on your code!")

while True:
    try:
        # Ask System Events directly for the exact, clean name of the active app
        cmd = "osascript -e 'tell application \"System Events\" to get name of first application process whose frontmost is true'"
        app_name = os.popen(cmd).read().strip().lower()
        
        # Print the text to verify it's reading the app name correctly
        if app_name:
            print(f"👉 Active App detected: '{app_name}'")
            
            # 2. If the active app matches your blacklist, drop the guillotine
            if app_name in BLACKLIST:
                print(f"\n🚨 CAUGHT DISTRACTED ON: {app_name.upper()}!")
                print("⚔️ DROPPING SOFTWARE GUILLOTINE...")
                
                # Natively force-quit the browser app instantly on Mac
                os.system(f"pkill -9 -i '{app_name}'")
                
                # Clear terminal and flash a full-screen warning message
                os.system('clear')
                print("\n" * 4)
                print("=" * 60)
                print("       THE GUILLOTINE DROPPED ON YOUR DISTRACTION!       ")
                print("=" * 60)
                print(f"       Force-closed: {app_name.upper()}")
                print("\n       Step away from the screen and get back to your IDE. ")
                print("=" * 60)
                
                time.sleep(3) # Cool-down to let the browser close completely
                    
    except Exception as e:
        pass
        
    time.sleep(1) # Monitor screen once every single second

