from django.core.mail import send_mail

def send_reservation_email(to_email, reservation_code):
    subject = "Your Flight Reservation Confirmation"
    message = f"Thank you for your reservation. Your reservation code is {reservation_code}."
    send_mail(subject, message, None, [to_email])
