# Order Tracking System

This is a simple order tracking system implemented using Python's `tkinter` library for the GUI and `playsound` library for playing notification sounds. The system allows users to add new orders, update their statuses, and view the list of all orders.

## Features

- Add new orders with details.
- Update the status of existing orders.
- Play a notification sound when an order is marked as completed.
- View all orders in a list with their current status.

## Requirements

- Python 3.x
- `tkinter` (usually comes pre-installed with Python)
- `playsound` library

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/order-tracking-system.git
    cd order-tracking-system
    ```

2. **Install the required library:**
    ```bash
    pip install playsound
    ```

## Usage

1. **Navigate to the project directory:**
    ```bash
    cd order-tracking-system
    ```

2. **Run the application:**
    ```bash
    python main.py
    ```

## Project Structure

order-tracking-system/
├── main.py # Entry point for the application
├── order_system.py # Contains Order and OrderSystem classes
├── order_app.py # Contains OrderApp class
├── notification.mp3 # Notification sound file
└── README.md # This README file
