role = "organizer"
owner_id = "Marvin"
current_user_id = "Claire"
if role == "organizer" and owner_id == current_user_id:
    print("You can edit this event")
else:
    print("You cannot edit this event")