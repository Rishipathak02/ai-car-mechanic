CAR_WORDS = {
    "car", "engine", "battery", "brake", "brakes",
    "tyre", "tire", "wheel", "clutch", "gear",
    "oil", "coolant", "radiator", "starter", "alternator",
    "ac", "a/c", "air", "conditioning",
    "headlight", "bonnet", "dashboard", "vehicle",
    "diesel", "petrol", "fuel", "steering", "suspension",
    "overheating", "overheat", "puncture", "mechanic",
    "service", "mileage", "transmission", "exhaust",
    "engine", "horn", "wiper", "windscreen", "windshield",
    "door", "window", "mirror", "seatbelt", "airbag"
}


def is_car_related(text: str) -> bool:
    text = text.lower().replace("/", " ")
    words = set(text.split())

    return bool(words & CAR_WORDS)


def rule_based_reply(message: str) -> str | None:

    text = message.lower()

    if not is_car_related(text):
        return (
            "I can help only with car and mechanical problems. "
            "Please describe your vehicle issue."
        )

    # Engine starting problem
    if (
        "not starting" in text
        or "won't start" in text
        or "wont start" in text
        or "cannot start" in text
        or "can't start" in text
    ):
        return (
            "I can help diagnose this. Does the car make a clicking "
            "sound, crank normally, or stay completely silent when "
            "you try to start it?"
        )

    # Overheating
    if "overheat" in text or "overheating" in text:
        return (
            "Please avoid driving if the temperature is very high. "
            "Is the coolant level low, and do you see steam or a "
            "coolant leak?"
        )

    # Brake
    if "brake" in text or "brakes" in text:
        return (
            "For a brake issue, safety comes first. Are you hearing "
            "grinding or squealing, feeling vibration, or noticing "
            "reduced braking performance?"
        )

    # AC
    if (
        "ac" in text
        or "air conditioning" in text
        or "air conditioner" in text
    ):
        return (
            "For the AC issue, is the airflow weak or is the air "
            "flowing normally but not getting cold? Also, does the "
            "AC problem happen all the time or only sometimes?"
        )

    # Battery
    if "battery" in text:
        return (
            "Is the battery completely dead, or does the car crank "
            "slowly? Do you see any battery warning light on the dashboard?"
        )

    # Tyre
    if "tyre" in text or "tire" in text or "puncture" in text:
        return (
            "Is the tyre losing air slowly or going flat quickly? "
            "Have you noticed any nail, cut, or visible damage?"
        )

    # Engine noise
    if "engine" in text and (
        "noise" in text
        or "sound" in text
        or "noisy" in text
    ):
        return (
            "What type of engine noise do you hear—clicking, "
            "knocking, rattling, whining, or grinding? Does it "
            "happen during starting, acceleration, or idling?"
        )

    # Oil leak
    if "oil" in text and (
        "leak" in text
        or "leaking" in text
    ):
        return (
            "Is the oil leak happening while the car is parked, "
            "and have you noticed an oil warning light or an oil "
            "spot under the vehicle?"
        )

    # Mileage
    if "mileage" in text:
        return (
            "Has the mileage dropped suddenly or gradually? "
            "Also tell me whether the car has reduced power, "
            "rough idling, or any dashboard warning light."
        )

    # Steering
    if "steering" in text:
        return (
            "Is the steering becoming hard to turn, vibrating, "
            "or pulling the car to one side? Please avoid driving "
            "if steering control is significantly affected."
        )

    # General car problem
    return (
        "Please tell me the car model/year, the exact symptom, "
        "when it started, and any dashboard warning light or "
        "unusual sound."
    )

