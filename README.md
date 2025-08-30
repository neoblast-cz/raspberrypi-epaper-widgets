# Raspberry Pi E-Paper Widgets

This project is designed to display various widgets on a Waveshare 7.5-inch e-paper display using a Raspberry Pi. The application is structured to allow easy customization and extension of widgets.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Widgets](#widgets)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/raspberrypi-epaper-widgets.git
   cd raspberrypi-epaper-widgets
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Connect the e-paper display:**
   Follow the manufacturer's instructions to connect the Waveshare 7.5-inch e-paper display to your Raspberry Pi.

## Usage

To run the application, execute the following command:
```bash
python src/main.py
```

This will initialize the e-paper display and start the main loop for updating the widgets.

## Widgets

The application includes various widgets that can be displayed on the e-paper screen. You can customize or add new widgets by modifying the files in the `src/widgets` directory.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.