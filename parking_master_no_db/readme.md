# Parking Master

A parking management system built with Flask.

## Project Structure

```
parking_master_no_db/
├── park_master/         # Virtual environment
├── app.py               # Main Flask application (assumption)
├── templates/           # Jinja2 templates (assumption)
└── static/              # Static files (CSS, JS, images) (assumption)
```

## Technologies Used

*   Python
*   Flask
*   Jinja2

## Setup and Run

1.  **Navigate to the project directory:**
    ```bash
    cd c:\Users\Harsh\Documents\Learnings\MAD\vishal_bhai_sessions\homework3\parking_master_no_db
    ```

2.  **Activate the virtual environment:**
    ```bash
    .\park_master\Scripts\activate
    ```

3.  **Run the Flask application:**
    ```bash
    flask run
    ```

4.  Open your web browser and go to `http://127.0.0.1:5000` for the user view or `http://127.0.0.1:5000/admin` for the admin view.

## Notes

*   This version uses an in-memory Python dictionary for data storage.
*   All booking data is lost when the Flask application stops or restarts.
*   There is currently no functionality to "unbook" or free a slot once it's booked, other than restarting the server.
*   Further development might involve integrating a database for persistent storage and adding unbooking features.

----

## Backend Data Handling (In-Memory Dictionary in app.py)

This version manages parking slot status using a Python dictionary named `bookings` stored in memory within `app.py`

Here's how booked and available slots are handled:

*   **Structure:**
    *   The `bookings` dictionary uses integer slot numbers (from 1 to `total_slots`, which is 9) as keys.
    *   The value associated with each key represents the booking status.
*   **Available Slot:**
    *   An available slot is represented by having `None` as the value for its corresponding slot number key in the `bookings` dictionary.
    *   Example: `bookings = {1: None, 2: {'name': 'Jane Doe', 'vehicle_id': 'DEF456'}, 3: None, ...}` (Slots 1 and 3 are available).
*   **Booked (Occupied) Slot:**
    *   When a user successfully books a slot via the `/book` route:
        *   The application checks if the requested `slot_number` exists and its current value in `bookings` is `None`.
        *   If available, the value for that `slot_number` key is updated from `None` to a new dictionary containing the booking details: `{'name': user_name, 'vehicle_id': user_vehicle_id}`.
    *   Example: `bookings[2] = {'name': 'Jane Doe', 'vehicle_id': 'DEF456'}` (Slot 2 is booked).
*   **Checking Status:**
    *   In the user view (`/`), available slots are found by iterating through `bookings.items()` and collecting keys where the value `is None`.
    *   In the admin view (`/admin`), the template checks if `bookings.get(slot_num)` returns `None` (available) or a dictionary (booked).
*   **No Unbooking:** The current logic in [`app.py`](c:\Users\Harsh\Documents\Learnings\MAD\vishal_bhai_sessions\homework3\parking_master_no_db\app.py) only handles booking. There is no route or function implemented to change a booked slot back to `None` (available).
