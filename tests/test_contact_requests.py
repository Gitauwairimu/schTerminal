from unittest import TestCase

from contact_requests import ContactRequest
from contact_requests_service import contact_request_service

def test_send_contact_request(self):
  """
  This test ensures that a user can successfully send a contact request to a teacher.
  """

  teacher_name = "John Doe"
  teacher_email = "john.doe@example.com"
  message = "This is a test contact request."

  # Create a contact request object.
  contact_request = ContactRequest(
      teacher_name=teacher_name,
      teacher_email=teacher_email,
      message=message,
  )

  # Send the contact request.
  contact_request_service.send_contact_request(contact_request)

  # Assert that the contact request was successfully sent.
  self.assertTrue(contact_request.sent)

