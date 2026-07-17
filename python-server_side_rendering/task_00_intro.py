#!/usr/bin/env python3
"""
generate_invitations:
Creates personalized invitation files from a template string and a list
of attendee dictionaries. Handles missing data, invalid types, and
empty inputs gracefully.

Parameters:
    template (str): The invitation template containing placeholders.
    attendees (list): A list of dictionaries with attendee data.

Returns:
    None: Output files are written to disk as output_X.txt.
"""

def generate_invitations(template, attendees):
    # --- Type Validation ---
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # --- Empty Input Handling ---
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # --- Process Each Attendee ---
    for index, attendee in enumerate(attendees, start=1):
        # Replace missing fields with "N/A"
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        # Fill template
        filled = (
            template.replace("{name}", name)
                    .replace("{event_title}", event_title)
                    .replace("{event_date}", event_date)
                    .replace("{event_location}", event_location)
        )

        # --- Write Output File ---
        filename = f"output_{index}.txt"
        with open(filename, "w") as f:
            f.write(filled)

        print(f"Generated: {filename}")
