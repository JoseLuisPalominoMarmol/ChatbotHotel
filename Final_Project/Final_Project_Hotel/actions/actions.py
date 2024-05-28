from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ValidateBookRoomForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_book_room_form"

    def validate_room_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `room_type` value."""
        allowed_room_types = ["individual", "doble", "suite"]
        if slot_value.lower() not in allowed_room_types:
            dispatcher.utter_message(text=f"Solo ofrecemos habitaciones individuales, dobles, y suites.")
            return {"room_type": None}
        dispatcher.utter_message(text=f"OK! Quieres una habitación {slot_value}.")
        return {"room_type": slot_value}

    def validate_check_in_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `check_in_date` value."""
        # Example of date validation, you might need a date parser
        if not self.is_valid_date(slot_value):
            dispatcher.utter_message(text=f"La fecha de entrada no es válida. Por favor, proporcione una fecha en formato DD/MM/YYYY.")
            return {"check_in_date": None}
        dispatcher.utter_message(text=f"Perfecto! Tenemos disponiblidad para tu entrada el {slot_value}.")
        return {"check_in_date": slot_value}

    def validate_check_out_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `check_out_date` value."""
        # Example of date validation, you might need a date parser
        if not self.is_valid_date(slot_value):
            dispatcher.utter_message(text=f"La fecha de salida no es válida. Por favor, proporcione una fecha en formato DD/MM/YYYY.")
            return {"check_out_date": None}
        dispatcher.utter_message(text=f"Estupendo! Hemos fijado tu salida para el {slot_value}.")
        return {"check_out_date": slot_value}

    def validate_number_of_guests(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `number_of_guests` value."""
        try:
            guests = int(slot_value)
            if guests < 1 or guests > 10:  # Assuming the room cannot accommodate more than 10 people
                raise ValueError
            dispatcher.utter_message(text=f"Perfecto! Confirmo disponibilidad para {slot_value} personas.") 
            return {"number_of_guests": slot_value}
        except ValueError:
            dispatcher.utter_message(text=f"Por favor, ingrese un número válido de huéspedes (1-10).")
            return {"number_of_guests": None}

    def validate_customer_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `customer_email` value."""
        if "@" not in slot_value or "." not in slot_value:  # Basic validation for email
            dispatcher.utter_message(text=f"La dirección de correo electrónico no parece válida. Asegúrese de incluir un '@' y un '.'.")
            return {"customer_email": None}
        dispatcher.utter_message(text=f"Perfecto! El email {slot_value} ha sido validado.")
        return {"customer_email": slot_value}

    def is_valid_date(self, date_str):
        # You can implement a more robust date validation logic here
        from datetime import datetime
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
