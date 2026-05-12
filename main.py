import pygame
from ui.button import Button
from services.flight_manager import FlightManager
from models.flight import Flight
from models.schedule import FlightSchedule

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Flight Ticket Booking Management System")

font = pygame.font.SysFont("Arial", 24)
small_font = pygame.font.SysFont("Arial", 18)

manager = FlightManager()

manager.add_flight(Flight("F001", "Vietnam Airlines", "HCM", "Ha Noi", "02:10"))
manager.add_flight(Flight("F002", "Vietjet Air", "Da Nang", "HCM", "01:20"))

manager.add_schedule(FlightSchedule("S001", "F001", "2026-06-01", "08:00", 1500000, 50))
manager.add_schedule(FlightSchedule("S002", "F002", "2026-06-02", "10:30", 900000, 30))

buttons = [
    Button(30, 80, 220, 45, "View Flights"),
    Button(30, 140, 220, 45, "View Schedules"),
    Button(30, 200, 220, 45, "Book Ticket"),
    Button(30, 260, 220, 45, "View Bookings"),
    Button(30, 320, 220, 45, "Save Data"),
]

current_screen = "home"
message = ""

running = True

while running:
    screen.fill((245, 245, 245))

    title = font.render("Flight Ticket Booking Management System", True, (0, 0, 0))
    screen.blit(title, (200, 20))

    for button in buttons:
        button.draw(screen, small_font)

    y = 90

    if current_screen == "flights":
        for flight in manager.flights:
            text = f"{flight.flight_id} - {flight.airline} - {flight.origin} to {flight.destination} - {flight.duration}"
            label = small_font.render(text, True, (0, 0, 0))
            screen.blit(label, (300, y))
            y += 30

    elif current_screen == "schedules":
        for schedule in manager.schedules:
            text = f"{schedule.schedule_id} - Flight {schedule.flight_id} - {schedule.departure_date} {schedule.departure_time} - Seats: {schedule.available_seats}"
            label = small_font.render(text, True, (0, 0, 0))
            screen.blit(label, (300, y))
            y += 30

    elif current_screen == "bookings":
        for booking in manager.bookings:
            text = f"{booking.booking_id} - {booking.customer_name} - {booking.number_of_tickets} tickets"
            label = small_font.render(text, True, (0, 0, 0))
            screen.blit(label, (300, y))
            y += 30

    elif current_screen == "message":
        label = small_font.render(message, True, (0, 120, 0))
        screen.blit(label, (300, 100))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if buttons[0].is_clicked(pos):
                current_screen = "flights"

            elif buttons[1].is_clicked(pos):
                current_screen = "schedules"

            elif buttons[2].is_clicked(pos):
                success = manager.create_booking("B001", "S001", "Test Customer", 2)

                if success:
                    message = "Booking created successfully!"
                else:
                    message = "Booking failed!"

                current_screen = "message"

            elif buttons[3].is_clicked(pos):
                current_screen = "bookings"

            elif buttons[4].is_clicked(pos):
                manager.save_data()
                message = "Data saved successfully!"
                current_screen = "message"

pygame.quit()