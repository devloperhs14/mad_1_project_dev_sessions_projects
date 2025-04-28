# filepath: app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

total_slots = 9
bookings = {}
for i in range(1, total_slots + 1):
    bookings[i] = None

@app.route('/')
def user_view():
    available_slots = [slot for slot, details in bookings.items() if details is None]
    lot_id = 1
    return render_template('user.html',
                           available_slots=available_slots,
                           lot_id=lot_id,
                           total_slots=total_slots
                           )

@app.route('/book', methods=['POST'])
def book_slot():
    try:
        slot_number = int(request.form['slot_id'])
        name = request.form['name']
        vehicle_id = request.form['vehicle_no']

        if name and vehicle_id and slot_number in bookings and bookings[slot_number] is None:
            bookings[slot_number] = {'name': name, 'vehicle_id': vehicle_id}
            print(f"Booking successful: Slot {slot_number} for {name}")
        else:
            print(f"Booking failed for slot {slot_number}. Already booked or invalid input.")
            pass

    except (ValueError, KeyError) as e:
         print(f"Booking failed due to invalid form data: {e}")
         pass

    return redirect(url_for('user_view'))

@app.route('/admin')
def admin_view():
    return render_template('admin.html', bookings=bookings, total_slots=total_slots)


if __name__ == '__main__':
    app.run(debug=True)