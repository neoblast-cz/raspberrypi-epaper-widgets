import time
from display.epaper import EPaperDisplay
from widgets import Widget1, Widget2  # Example widget imports

def main():
    # Initialize the e-paper display
    display = EPaperDisplay()
    display.initialize()

    # Create widget instances
    widget1 = Widget1()
    widget2 = Widget2()

    # Main loop to update widgets
    try:
        while True:
            display.clear()
            widget1.render(display)
            widget2.render(display)
            display.update()
            time.sleep(60)  # Update every 60 seconds
    except KeyboardInterrupt:
        display.cleanup()

if __name__ == "__main__":
    main()