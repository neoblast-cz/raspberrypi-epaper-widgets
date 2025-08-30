import time
from display.epaper import EPaperDisplay
from widgets import ClockWidget, TextWidget  # Import the widgets you want

def main():
    # Initialize the e-paper display
    display = EPaperDisplay()
    display.initialize()

    # Create widget instances
    clock_widget = ClockWidget(x=10, y=10, time_format="%H:%M:%S")
    text_widget = TextWidget(text="you are the best", x=10, y=50)

    # Main loop to update widgets
    try:
        while True:
            display.clear()
            clock_widget.render(display)
            text_widget.render(display)
            display.update()
            time.sleep(60)  # Update every 60 seconds
    except KeyboardInterrupt:
        display.cleanup()

if __name__ == "__main__":
    main()