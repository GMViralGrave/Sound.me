import keyboard
import pyautogui
import time

hotkeys_enabled = True
video_count = 0  
decline_count = 0  

def click_button(button_coords):
    pyautogui.click(button_coords)

def approve_action():
    approve_coords = (1298, 1353)
    click_button(approve_coords)

def decline_action():
    decline_coords = (1700, 1353) 
    click_button(decline_coords)

def bullet_point_action():
    bullet_point_coords = (918, 882)
    click_button(bullet_point_coords)

def scroll_to_top():
    pyautogui.press('home')

def scroll_to_bottom():
    pyautogui.press('end')

def click_text_box():
    text_box_coords = (1086, 1631)
    click_button(text_box_coords)

def click_confirm():
    confirm_coords = (1119, 1873) 
    click_button(confirm_coords)

def click_play():
    play_coords = (530, 1518)  
    click_button(play_coords)  

def click_monday():
    play_coords = (2678, 1269) 
    click_button(play_coords)

def disable_hotkeys():
    global hotkeys_enabled
    hotkeys_enabled = False

def enable_hotkeys():
    global hotkeys_enabled
    hotkeys_enabled = True

def update_counts():
    print(f"({video_count} Videos / {decline_count} Declines)")

def reset_counts():
    global video_count, decline_count
    video_count = 0
    decline_count = 0
    print("Counts have been reset.")

def main():
    global video_count, decline_count  

    while True:
        
        if keyboard.is_pressed('esc'):
            print("Program Exited.")
            break  

        if keyboard.is_pressed('left') or keyboard.is_pressed('right') or keyboard.is_pressed('up') or keyboard.is_pressed('down'):
            time.sleep(0.1)  
            continue

        if keyboard.is_pressed('3'):  
            disable_hotkeys()
            time.sleep(0.2)  

        elif keyboard.is_pressed('='):  
            enable_hotkeys()
            time.sleep(0.2) 

        if keyboard.is_pressed('4'):
            reset_counts()
            time.sleep(0.2)

        if hotkeys_enabled:
            if keyboard.is_pressed('1'):
                video_count += 1  
                print("Approved")
                scroll_to_top()
                time.sleep(0.5)
                approve_action()
                time.sleep(0.5)
                update_counts() 
                time.sleep(0.5)

            elif keyboard.is_pressed('2'): 
                decline_count += 1
                video_count += 1
                print("Declined")
                scroll_to_top()
                time.sleep(0.5)
                decline_action()
                time.sleep(0.5)
                bullet_point_action()
                time.sleep(0.5)
                scroll_to_bottom()
                time.sleep(0.5)
                click_text_box()
                time.sleep(0.5)
                update_counts() 

            elif keyboard.is_pressed('`'):
                click_play()
                time.sleep(0.2)

            elif keyboard.is_pressed('-'):
                click_monday()  
                time.sleep(0.2)  

        elif keyboard.is_pressed('-'):
            click_monday()
            time.sleep(0.2)

        time.sleep(0.1) 

if __name__ == "__main__":
    print("Time to get to work.")
    main()
